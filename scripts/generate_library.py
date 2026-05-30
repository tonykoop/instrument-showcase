#!/usr/bin/env python3
"""Generate the Heifer Zephyr Studio Explorers Library.

Walks the GitHub workspace, finds every instrument repo that has an
explorer.html (built) or a capstone-manifest.json (ready for one), pulls
status / Wolfram state / CAD readiness / family / acoustic class for each,
and emits two files in instrument-showcase/:

  data/library-manifest.json    machine-readable inventory
  site/library.html             brand-disciplined library page with
                                family / status / Wolfram / CAD filters

CAD readiness:
  inline-glb    cad/*.glb exists and is <= 5 MB  (would be inlined by generate_explorer.py)
  external-glb  cad/*.glb exists but > 5 MB
  gltf          only cad/<sub>/*.gltf exists (multi-file glTF)
  none          no CAD assets

Wolfram state (per wolfram-cloud-sync INTEGRATION-CONTRACT.md):
  live         data-permission = Public-Execute and cloud_url present
  owner-only   data-permission = Private (uploaded, not published)
  pending      no entry / blank URL with no permission flag
  diagnostic   data-permission = failed or missing

Usage:
  python3 generate_library.py                      # default paths
  python3 generate_library.py --workspace PATH     # repo root
  python3 generate_library.py --output-html PATH   # override site/library.html
  python3 generate_library.py --output-data PATH   # override data/library-manifest.json
"""

from __future__ import annotations

import argparse
import json
import sys
import html as _html
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SHOWCASE_DIR = SCRIPT_DIR.parent
# Post-2026-05-25 reorg: showcase lives at <workspace>/instruments/_meta/instrument-showcase
# so the GitHub workspace root is three parents up from SHOWCASE_DIR.
DEFAULT_WORKSPACE = SHOWCASE_DIR.parent.parent.parent
INSTRUMENT_FAMILY_DIRS = ("strings", "woodwind", "brass", "percussion", "idiophones")
INLINE_GLB_THRESHOLD = 5 * 1024 * 1024

# --------------------------------------------------------------------------
# slug -> (family, acoustic_class) lookup.
# family is the broad bucket: wind / string / drum / idiophone / hybrid
# acoustic_class is the governing model bucket the instrument actually uses
# --------------------------------------------------------------------------

FAMILY_MAP: dict[str, tuple[str, str]] = {
    # WIND - duct / rim-blown
    "andean-duct-flutes":     ("wind", "duct-flute"),
    "drone-flutes":           ("wind", "duct-flute"),
    "gemshorn":               ("wind", "vessel-flute"),
    "vessel-flutes":          ("wind", "vessel-flute"),
    "ocarina":                ("wind", "vessel-flute"),
    "shakuhachi":             ("wind", "open-pipe"),
    "kena":                   ("wind", "open-pipe"),
    "xiao":                   ("wind", "open-pipe"),
    "siku-zampona":           ("wind", "stopped-pipe"),
    "fujara":                 ("wind", "open-pipe"),
    "moseno":                 ("wind", "open-pipe"),
    "pistalka":               ("wind", "open-pipe"),
    "kaval-alghosazi-flutes": ("wind", "open-pipe"),
    "transverse-flute":       ("wind", "open-pipe"),
    "irish-flute":            ("wind", "open-pipe"),
    "tin-whistle":            ("wind", "duct-flute"),
    "duduk":                  ("wind", "reed"),
    "didgeridoo":             ("wind", "lip-driven"),
    "great-highland-bagpipe": ("wind", "reed"),
    "clarinet":               ("wind", "reed"),
    "chalumeau":              ("wind", "reed"),
    "flutes":                 ("wind", "duct-flute"),
    # WIND - free reed
    "hulusi":                 ("wind", "free-reed"),
    "sheng":                  ("wind", "free-reed"),
    "khaen":                  ("wind", "free-reed"),
    # STRING - harp / lute / zither / bowed
    "kora":                   ("string", "harp-lute"),
    "konghou":                ("string", "harp"),
    "ngoni":                  ("string", "harp-lute"),
    "sambuca":                ("string", "arched-harp"),
    "egyptian-harps":         ("string", "arched-harp"),
    "lyre":                   ("string", "lyre"),
    "floor-harp":             ("string", "harp"),
    "guzheng":                ("string", "zither"),
    "pipa":                   ("string", "lute"),
    "stave-lute-oud":         ("string", "lute"),
    "ukulele":                ("string", "lute"),
    "zephyr-zither":          ("string", "zither"),
    "haegeum":                ("string", "bowed"),
    "erhu":                   ("string", "bowed"),
    "acoustic-violin":        ("string", "bowed"),
    "electric-violin":        ("string", "bowed-electric"),
    "ceramic-electric-violin":("string", "bowed-electric"),
    "whamola-bass":           ("string", "bowed"),
    "cnc-guitar-bodies":      ("string", "plucked-electric"),
    "electric-guitar-bodies": ("string", "plucked-electric"),
    # DRUM - membrane
    "djembe":                 ("drum", "single-membrane"),
    "ashiko-drum-workshop":   ("drum", "single-membrane"),
    "dundun":                 ("drum", "double-membrane"),
    "udu":                    ("drum", "vessel-membrane"),
    "frame-drum":             ("drum", "single-membrane"),
    "conga":                  ("drum", "single-membrane"),
    "tongue-drum":            ("drum", "tongue-drum-wood"),
    "wood-shell-tongue-drum": ("drum", "tongue-drum-wood"),
    "ceramic-tongue-drum":    ("drum", "tongue-drum-ceramic"),
    "steel-tongue-drum":      ("drum", "tongue-drum-steel"),
    # IDIOPHONE - tuned bar / vessel
    "marimba":                ("idiophone", "tuned-bar"),
    "marimba-piano":          ("idiophone", "tuned-bar"),
    "xylophone":              ("idiophone", "tuned-bar"),
    "glockenspiel":           ("idiophone", "tuned-bar-metal"),
    "tubular-bells":          ("idiophone", "tuned-pipe"),
    "rainstick":              ("idiophone", "shaker"),
    "wind-chimes":            ("idiophone", "tuned-pipe"),
    "handpan":                ("idiophone", "tuned-shell"),
    "wooden-hang":            ("idiophone", "tuned-shell"),
    "ceramic-hang":           ("idiophone", "tuned-shell"),
    "steel-pan":              ("idiophone", "tuned-shell"),
    "duntong":                ("idiophone", "tuned-bar"),
    "cajon":                  ("drum", "box-drum"),
    "found-cavities":         ("idiophone", "tuned-shell"),
    "resonant-box":           ("idiophone", "resonator-aid"),
}


# --------------------------------------------------------------------------
# Data shapes
# --------------------------------------------------------------------------


@dataclass
class LibraryEntry:
    slug: str
    title: str = ""
    instrument: str = ""
    family: str = "other"
    acoustic_class: str = ""
    status: str = "unknown"
    status_label: str = "Unknown"
    explorer_path: str = ""    # relative from instrument-showcase/site/library.html
    has_explorer: bool = False
    cad: str = "none"
    cad_size_bytes: int = 0
    wolfram_state: str = "pending"
    wolfram_url: str = ""
    wolfram_notebook: str = ""
    family_count: int = 0
    family_members: list[str] = field(default_factory=list)
    has_manifest: bool = False
    hero_image_path: str = ""   # rel from site/library.html; "" when no hero image found
    has_hero: bool = False


# --------------------------------------------------------------------------
# Resolvers
# --------------------------------------------------------------------------


def load_embed_urls(workspace: Path) -> dict[str, dict]:
    """slug -> first matching row from wolfram_embed_urls.json (or {})"""
    p = workspace / "_meta" / "wolfram-cloud-sync" / "manifest" / "wolfram_embed_urls.json"
    if not p.exists():
        return {}
    out: dict[str, dict] = {}
    for r in json.loads(p.read_text(encoding="utf-8")):
        slug = r.get("repo")
        # Take the FIRST entry per slug (others are extras)
        if slug and slug not in out:
            out[slug] = r
    return out


def detect_cad(repo: Path) -> tuple[str, int]:
    cad_dir = repo / "cad"
    if not cad_dir.exists():
        return ("none", 0)
    glbs = sorted(cad_dir.glob("*.glb"), key=lambda p: p.stat().st_size, reverse=True)
    if glbs:
        size = glbs[0].stat().st_size
        if size <= INLINE_GLB_THRESHOLD:
            return ("inline-glb", size)
        return ("external-glb", size)
    for sub in (d for d in cad_dir.iterdir() if d.is_dir()):
        if any(sub.glob("*.gltf")):
            return ("gltf", 0)
    return ("none", 0)


def derive_wolfram_state(manifest: dict, embed_row: dict | None) -> tuple[str, str, str]:
    """Returns (state, url, notebook_name)."""
    # 1. Prefer manifest engineering.wolfram[]
    eng = (manifest.get("engineering") or {})
    arr = eng.get("wolfram")
    if isinstance(arr, list) and arr and isinstance(arr[0], dict):
        first = arr[0]
        perm = (first.get("permission") or "").strip()
        url = (first.get("cloud_url") or "").strip()
        nb = Path(first.get("source_file") or first.get("cloud_path") or "").stem
        if perm == "Public-Execute" and url:
            return ("live", url, nb)
        if perm == "Private":
            return ("owner-only", "", nb)
        if perm in ("failed", "missing"):
            return ("diagnostic", "", nb)
        return ("pending", "", nb)
    # 2. Fall back to embed-urls row
    if embed_row:
        perm = (embed_row.get("permission") or "").strip()
        url = (embed_row.get("cloud_url") or "").strip()
        nb = Path(embed_row.get("source_file") or "").stem
        if perm == "Public-Execute" and url:
            return ("live", url, nb)
        if perm == "Private":
            return ("owner-only", "", nb)
        if perm in ("failed", "missing"):
            return ("diagnostic", "", nb)
    return ("pending", "", "")


def derive_status(manifest: dict) -> tuple[str, str]:
    raw_val = manifest.get("release_status") or manifest.get("status") or ""
    raw = (raw_val if isinstance(raw_val, str) else "").lower()
    rg = manifest.get("release_gate") or {}
    if rg.get("public_candidate") is False or rg.get("required_before_public"):
        return ("blocked", "Public-release blocked")
    if "public" in raw and "candidate" not in raw:
        return ("public", "Public")
    if "private" in raw or "review" in raw:
        return ("private", "Private review")
    return ("unknown", raw.title() or "Unknown")


HERO_CANDIDATES = (
    "images/hero-render.png", "images/hero.png", "images/hero-render.jpg",
    "images/hero.jpg", "renders/hero.png", "explorer-assets/hero.png",
)


def detect_hero(repo: Path) -> str:
    """Return a repo-relative path to a hero image, or '' if none found.

    Checks well-known hero locations first, then falls back to the first
    image file under images/. Refs instrument-showcase#13 (library cards
    rendered without photos because the manifest had no image field).
    """
    for cand in HERO_CANDIDATES:
        if (repo / cand).is_file():
            return cand
    img_dir = repo / "images"
    if img_dir.is_dir():
        for p in sorted(img_dir.iterdir()):
            if p.is_file() and p.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp"):
                return f"images/{p.name}"
    return ""


def scan_workspace(workspace: Path) -> list[LibraryEntry]:
    embed_index = load_embed_urls(workspace)
    entries: list[LibraryEntry] = []

    instruments_root = workspace / "instruments"
    repo_candidates: list[tuple[str, Path]] = []
    for family_dir in INSTRUMENT_FAMILY_DIRS:
        fam_root = instruments_root / family_dir
        if not fam_root.is_dir():
            continue
        for repo in sorted(fam_root.iterdir()):
            if repo.is_dir():
                repo_candidates.append((family_dir, repo))
    repo_candidates.sort(key=lambda t: t[1].name)

    for family_dir, repo in repo_candidates:
        slug = repo.name
        if slug not in FAMILY_MAP:
            continue
        explorer = repo / "explorer.html"
        manifest_path = repo / "capstone-manifest.json"
        if not (explorer.exists() or manifest_path.exists()):
            continue

        manifest: dict = {}
        has_manifest = False
        if manifest_path.exists():
            try:
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                has_manifest = True
            except json.JSONDecodeError:
                manifest = {}

        title = (manifest.get("title") or manifest.get("instrument")
                 or slug.replace("-", " ").title())
        instrument = manifest.get("instrument") or title

        family, acoustic = FAMILY_MAP[slug]
        cad_kind, cad_size = detect_cad(repo)
        wstate, wurl, wnb = derive_wolfram_state(manifest, embed_index.get(slug))
        status, status_label = derive_status(manifest)
        fam_members = manifest.get("family_members") or []
        hero_rel = detect_hero(repo)
        hero_path = f"../../../{family_dir}/{slug}/{hero_rel}" if hero_rel else ""

        entries.append(LibraryEntry(
            slug=slug,
            title=title,
            instrument=instrument,
            family=family,
            acoustic_class=acoustic,
            status=status,
            status_label=status_label,
            explorer_path=f"../../../{family_dir}/{slug}/explorer.html",  # rel from instruments/_meta/instrument-showcase/site/library.html
            has_explorer=explorer.exists(),
            cad=cad_kind,
            cad_size_bytes=cad_size,
            wolfram_state=wstate,
            wolfram_url=wurl,
            wolfram_notebook=wnb,
            family_count=len(fam_members),
            family_members=fam_members,
            has_manifest=has_manifest,
            hero_image_path=hero_path,
            has_hero=bool(hero_rel),
        ))
    return entries


# --------------------------------------------------------------------------
# HTML rendering
# --------------------------------------------------------------------------


def esc(s) -> str:
    return _html.escape("" if s is None else str(s), quote=True)


CARD_TPL = """\
<article class="card" data-family="{family}" data-status="{status}" data-cad="{cad}" data-wolfram="{wolfram_state}" data-has-explorer="{has_explorer_str}">
  <header class="card-head">
    <a class="card-title" {open_attr}>{title}</a>
    {explorer_pill}
  </header>
  {hero_img}
  <div class="card-meta">
    <span class="badge badge-family family-{family}">{family}</span>
    <span class="badge badge-acoustic">{acoustic_class}</span>
    {family_count_badge}
  </div>
  <div class="card-pills">
    <span class="pill pill-status pill-{status}" title="{status_label}">{status_label}</span>
    <span class="pill pill-wolfram pill-w-{wolfram_state}" title="{wolfram_title}"><span class="dot"></span>Wolfram · {wolfram_label}</span>
    <span class="pill pill-cad pill-cad-{cad}" title="{cad_title}"><span class="dot"></span>CAD · {cad_label}</span>
  </div>
  <p class="card-slug"><code>{slug}</code></p>
</article>
"""


def render_card(e: LibraryEntry) -> str:
    has_explorer_str = "yes" if e.has_explorer else "no"
    if e.has_explorer:
        open_attr = f'href="{esc(e.explorer_path)}"'
        explorer_pill = '<span class="explorer-pill explorer-pill-yes">Explorer ready</span>'
    else:
        open_attr = ""
        explorer_pill = '<span class="explorer-pill explorer-pill-no">Awaiting explorer</span>'

    wolfram_labels = {
        "live": ("Live", "Public-Execute notebook iframe"),
        "owner-only": ("Owner-only", "Uploaded but not yet published"),
        "pending": ("Pending", "Awaiting upload or publish"),
        "diagnostic": ("Diagnostic", "Sync error — owner-visible only"),
    }
    wlabel, wtitle = wolfram_labels.get(e.wolfram_state, ("Unknown", e.wolfram_state))

    cad_labels = {
        "inline-glb":   ("Inline glb", f"{e.cad_size_bytes // 1024:,} KB packed; inlined into explorer.html"),
        "external-glb": ("External glb", f"{e.cad_size_bytes // 1024 // 1024:,} MB — too large to inline; referenced as file"),
        "gltf":         ("Multi-file glTF", "SolidWorks-exported; not yet packed into .glb"),
        "none":         ("None", "No CAD assets in cad/ yet"),
    }
    clabel, ctitle = cad_labels.get(e.cad, (e.cad, ""))

    family_count_badge = ""
    if e.family_count > 1:
        family_count_badge = f'<span class="badge badge-fam-count">{e.family_count} variants</span>'

    if e.hero_image_path:
        hero_img = (
            f'<a class="card-hero" {open_attr} style="display:block;margin:8px 0 2px;">'
            f'<img src="{esc(e.hero_image_path)}" alt="{esc(e.title)}" loading="lazy" '
            f'style="width:100%;height:150px;object-fit:cover;border-radius:8px;background:#f0ece3;"></a>'
        )
    else:
        hero_img = ""

    return CARD_TPL.format(
        family=esc(e.family),
        status=esc(e.status),
        cad=esc(e.cad),
        wolfram_state=esc(e.wolfram_state),
        has_explorer_str=has_explorer_str,
        open_attr=open_attr,
        title=esc(e.title),
        explorer_pill=explorer_pill,
        acoustic_class=esc(e.acoustic_class),
        family_count_badge=family_count_badge,
        status_label=esc(e.status_label),
        wolfram_title=esc(wtitle),
        wolfram_label=esc(wlabel),
        cad_title=esc(ctitle),
        cad_label=esc(clabel),
        slug=esc(e.slug),
        hero_img=hero_img,
    )


def render_library_html(entries: list[LibraryEntry], generated_at: str) -> str:
    # Sort by family then title
    entries_sorted = sorted(entries, key=lambda e: (e.family, e.title.lower()))

    # Stats
    total = len(entries_sorted)
    with_explorer = sum(1 for e in entries_sorted if e.has_explorer)
    live_wolfram = sum(1 for e in entries_sorted if e.wolfram_state == "live")
    inline_cad = sum(1 for e in entries_sorted if e.cad == "inline-glb")
    families = {}
    for e in entries_sorted:
        families[e.family] = families.get(e.family, 0) + 1

    cards_html = "\n".join(render_card(e) for e in entries_sorted)
    family_filter_buttons = " ".join(
        f'<button class="filter-btn" data-filter-key="family" data-filter-val="{f}">{f} <span class="count">{n}</span></button>'
        for f, n in sorted(families.items()))

    return LIBRARY_HTML.format(
        generated_at=esc(generated_at),
        total=total,
        with_explorer=with_explorer,
        live_wolfram=live_wolfram,
        inline_cad=inline_cad,
        family_filter_buttons=family_filter_buttons,
        cards=cards_html,
    )


LIBRARY_HTML = """\
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Heifer Zephyr · Studio Explorers Library</title>
<style>
:root{{
  --walnut:#3D2817; --cedar:#B98B47; --cream:#F8F4E9; --paper:#FFFFFF;
  --lapis:#1E3A8A; --gold:#D4A017; --ink:#1F1A14; --muted:#6B5E4D;
  --rule:#E0D6C5; --ok:#2E7D32; --warn:#C89220; --block:#A03A2A;
  --pill-bg:#FCEFC6; --pill-border:#D4A017;
  --hover:#EFE7D3;
  --serif:"Fraunces","Source Serif Pro",Georgia,serif;
  --ui:"Inter","Source Sans Pro","Helvetica Neue",Arial,sans-serif;
  --mono:"JetBrains Mono",Menlo,Consolas,monospace;
  --italic-serif:"Cormorant Garamond","EB Garamond",Georgia,serif;
}}
*,*::before,*::after{{box-sizing:border-box}}
html,body{{margin:0;padding:0;background:var(--cream);color:var(--ink);
  font-family:var(--ui);font-size:15px;line-height:1.5;-webkit-font-smoothing:antialiased}}
a{{color:var(--lapis);text-decoration:none}}
a:hover{{text-decoration:underline}}
code{{font-family:var(--mono);font-size:0.88em}}

.app-bar{{position:sticky;top:0;z-index:30;height:56px;
  background:var(--walnut);color:var(--cream);
  border-bottom:3px solid var(--gold);
  display:flex;align-items:center;gap:24px;padding:0 22px}}
.brand{{display:flex;align-items:baseline;gap:14px;flex:0 0 auto}}
.wordmark em{{font-family:var(--italic-serif);font-style:italic;
  font-size:22px;color:var(--gold);letter-spacing:0.01em}}
.tagline{{font-family:var(--serif);font-size:15px;color:var(--cream);
  border-left:1px solid rgba(248,244,233,0.3);padding-left:14px}}
.actions{{margin-left:auto;display:flex;align-items:center;gap:12px}}
.action-btn{{display:inline-block;font-family:var(--ui);font-size:12px;
  letter-spacing:0.04em;text-transform:uppercase;
  color:var(--cream);border:1px solid rgba(248,244,233,0.35);
  border-radius:3px;padding:6px 10px}}
.action-btn:hover{{background:rgba(248,244,233,0.12);text-decoration:none;color:var(--gold)}}

.wrap{{max-width:1400px;margin:0 auto;padding:28px 28px 80px}}
.hero{{margin-bottom:18px}}
.hero h1{{font-family:var(--serif);font-weight:600;font-size:34px;color:var(--walnut);
  margin:0 0 6px;letter-spacing:-0.005em}}
.hero h1 .eyebrow{{display:block;font-family:var(--ui);font-weight:500;
  font-size:11px;color:var(--lapis);text-transform:uppercase;
  letter-spacing:0.16em;margin-bottom:6px}}
.hero p{{color:var(--muted);font-size:14px;max-width:760px}}

.stats{{display:flex;gap:12px;margin:14px 0 18px;flex-wrap:wrap}}
.stat{{background:var(--paper);border:1px solid var(--rule);border-radius:5px;
  padding:10px 16px;min-width:140px}}
.stat .k{{font-family:var(--ui);font-size:11px;color:var(--muted);
  text-transform:uppercase;letter-spacing:0.06em;margin-bottom:3px}}
.stat .v{{font-family:var(--serif);font-size:22px;color:var(--walnut);font-weight:600;line-height:1.1}}

.controls{{display:flex;gap:14px;align-items:center;margin:10px 0 20px;flex-wrap:wrap;
  padding:14px 16px;background:var(--paper);border:1px solid var(--rule);border-radius:5px}}
.controls label{{font-family:var(--ui);font-size:11px;color:var(--muted);
  text-transform:uppercase;letter-spacing:0.08em;margin-right:6px}}
.search{{flex:1;min-width:240px;padding:8px 12px;font-family:var(--ui);font-size:14px;
  border:1px solid var(--rule);border-radius:4px;background:#FFFCF5}}
.search:focus{{outline:none;border-color:var(--lapis)}}
.filter-group{{display:flex;gap:6px;flex-wrap:wrap;align-items:center}}
.filter-group + .filter-group{{margin-left:8px;padding-left:14px;border-left:1px solid var(--rule)}}
.filter-btn{{font-family:var(--ui);font-size:12px;background:var(--cream);
  color:var(--walnut);border:1px solid var(--rule);border-radius:14px;
  padding:5px 11px;cursor:pointer;transition:background 80ms,border-color 80ms;
  letter-spacing:0.02em}}
.filter-btn:hover{{border-color:var(--lapis)}}
.filter-btn.active{{background:var(--walnut);color:var(--cream);border-color:var(--walnut)}}
.filter-btn .count{{font-family:var(--mono);font-size:10px;margin-left:5px;opacity:0.7}}
.filter-btn.active .count{{opacity:1;color:var(--gold)}}

.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(310px,1fr));gap:14px}}
.card{{background:var(--paper);border:1px solid var(--rule);border-radius:5px;
  padding:14px 16px 12px;display:flex;flex-direction:column;gap:8px;
  transition:transform 100ms,box-shadow 100ms,border-color 100ms}}
.card:hover{{transform:translateY(-1px);box-shadow:0 4px 10px rgba(31,26,20,0.08);
  border-color:var(--cedar)}}
.card.hidden{{display:none}}
.card-head{{display:flex;justify-content:space-between;align-items:flex-start;gap:10px}}
.card-title{{font-family:var(--serif);font-weight:600;font-size:17px;color:var(--walnut);
  line-height:1.25;letter-spacing:-0.003em}}
.card-title:hover{{text-decoration:none;color:var(--lapis)}}
.card-meta{{display:flex;gap:5px;flex-wrap:wrap;align-items:center}}
.badge{{display:inline-block;font-family:var(--ui);font-size:10px;
  text-transform:uppercase;letter-spacing:0.06em;font-weight:600;
  padding:2px 7px;border-radius:3px;background:var(--cream);color:var(--walnut);
  border:1px solid var(--rule)}}
.badge-family.family-wind{{background:#E6EAF5;color:var(--lapis);border-color:var(--lapis)}}
.badge-family.family-string{{background:#FCEFC6;color:#7A5814;border-color:var(--pill-border)}}
.badge-family.family-drum{{background:#F8E3DC;color:var(--block);border-color:var(--block)}}
.badge-family.family-idiophone{{background:#D8EBD3;color:#1F5520;border-color:var(--ok)}}
.badge-family.family-hybrid{{background:#EEEAE0;color:var(--muted);border-color:var(--muted)}}
.badge-fam-count{{background:transparent;color:var(--muted);border-style:dashed}}
.card-pills{{display:flex;gap:5px;flex-wrap:wrap}}
.pill{{display:inline-flex;align-items:center;gap:5px;font-family:var(--ui);
  font-size:10.5px;font-weight:600;letter-spacing:0.04em;text-transform:uppercase;
  padding:3px 9px;border-radius:11px;background:var(--cream);color:var(--walnut);
  border:1px solid var(--rule)}}
.pill .dot{{width:7px;height:7px;border-radius:50%;background:var(--muted)}}
.pill-status.pill-private{{background:var(--pill-bg);border-color:var(--pill-border)}}
.pill-status.pill-blocked{{background:#F5DBD2;color:var(--block);border-color:var(--block)}}
.pill-status.pill-public{{background:#D8EBD3;color:var(--ok);border-color:var(--ok)}}
.pill-wolfram.pill-w-live{{background:#E8F1E5;border-color:var(--ok);color:var(--ok)}}
.pill-wolfram.pill-w-live .dot{{background:var(--ok)}}
.pill-wolfram.pill-w-owner-only{{background:#EEEAE0;border-color:var(--muted);color:var(--muted)}}
.pill-wolfram.pill-w-owner-only .dot{{background:var(--muted)}}
.pill-wolfram.pill-w-pending{{background:#FCEFC6;border-color:var(--pill-border);color:#7A5814}}
.pill-wolfram.pill-w-pending .dot{{background:var(--warn)}}
.pill-wolfram.pill-w-diagnostic{{background:#F5DBD2;border-color:var(--block);color:var(--block)}}
.pill-wolfram.pill-w-diagnostic .dot{{background:var(--block)}}
.pill-cad.pill-cad-inline-glb{{background:#E8F1E5;border-color:var(--ok);color:var(--ok)}}
.pill-cad.pill-cad-inline-glb .dot{{background:var(--ok)}}
.pill-cad.pill-cad-external-glb{{background:#FCEFC6;border-color:var(--pill-border);color:#7A5814}}
.pill-cad.pill-cad-external-glb .dot{{background:var(--warn)}}
.pill-cad.pill-cad-gltf{{background:#EEEAE0;border-color:var(--muted);color:var(--muted)}}
.pill-cad.pill-cad-gltf .dot{{background:var(--muted)}}
.pill-cad.pill-cad-none{{background:var(--cream);border-color:var(--rule);color:var(--muted)}}

.explorer-pill{{font-family:var(--ui);font-size:10px;letter-spacing:0.06em;
  text-transform:uppercase;font-weight:700;padding:3px 7px;border-radius:3px;flex:0 0 auto}}
.explorer-pill-yes{{background:var(--lapis);color:var(--cream)}}
.explorer-pill-no{{background:var(--cream);color:var(--muted);border:1px dashed var(--rule)}}
.card-slug{{margin:auto 0 0;font-family:var(--mono);font-size:10.5px;color:var(--muted)}}

.no-results{{text-align:center;padding:40px 20px;color:var(--muted);
  font-family:var(--serif);font-size:18px}}

@media (max-width:680px){{
  .grid{{grid-template-columns:1fr}}
  .controls{{flex-direction:column;align-items:stretch}}
}}
</style>
</head>
<body>

<header class="app-bar">
  <div class="brand">
    <span class="wordmark"><em>Heifer Zephyr</em></span>
    <span class="tagline">Studio Explorers · Library</span>
  </div>
  <div class="actions">
    <a class="action-btn" href="index.html">Deliverables Hub</a>
    <a class="action-btn" href="manifest.html">Manifest</a>
    <a class="action-btn" href="https://github.com/tonykoop" target="_blank" rel="noopener">GitHub</a>
  </div>
</header>

<main class="wrap">
  <section class="hero">
    <h1><span class="eyebrow">Library</span>Browse every studio explorer in one place</h1>
    <p>One card per instrument repo. Click an "Explorer ready" card to open that repo's full studio explorer — sidebar TOC, file viewers, interactive Wolfram-Cloud acoustic model, and the inline 3D CAD viewer where present. Cards without an explorer yet have a capstone-manifest.json and are ready for a <code>generate_explorer.py</code> run.</p>
  </section>

  <section class="stats">
    <div class="stat"><div class="k">Repos in library</div><div class="v">{total}</div></div>
    <div class="stat"><div class="k">With explorer</div><div class="v">{with_explorer}</div></div>
    <div class="stat"><div class="k">Wolfram live</div><div class="v">{live_wolfram}</div></div>
    <div class="stat"><div class="k">CAD inlined</div><div class="v">{inline_cad}</div></div>
  </section>

  <section class="controls">
    <input id="search" class="search" placeholder="Search by name or slug…" aria-label="Search">
    <div class="filter-group" data-filter-key="family">
      <label>Family</label>
      <button class="filter-btn active" data-filter-key="family" data-filter-val="all">all</button>
      {family_filter_buttons}
    </div>
    <div class="filter-group" data-filter-key="cad">
      <label>CAD</label>
      <button class="filter-btn active" data-filter-key="cad" data-filter-val="all">all</button>
      <button class="filter-btn" data-filter-key="cad" data-filter-val="inline-glb">inline glb</button>
      <button class="filter-btn" data-filter-key="cad" data-filter-val="external-glb">ext glb</button>
      <button class="filter-btn" data-filter-key="cad" data-filter-val="gltf">gltf</button>
      <button class="filter-btn" data-filter-key="cad" data-filter-val="none">none</button>
    </div>
    <div class="filter-group" data-filter-key="wolfram">
      <label>Wolfram</label>
      <button class="filter-btn active" data-filter-key="wolfram" data-filter-val="all">all</button>
      <button class="filter-btn" data-filter-key="wolfram" data-filter-val="live">live</button>
      <button class="filter-btn" data-filter-key="wolfram" data-filter-val="owner-only">owner-only</button>
      <button class="filter-btn" data-filter-key="wolfram" data-filter-val="pending">pending</button>
    </div>
    <div class="filter-group" data-filter-key="has-explorer">
      <label>Explorer</label>
      <button class="filter-btn active" data-filter-key="has-explorer" data-filter-val="all">all</button>
      <button class="filter-btn" data-filter-key="has-explorer" data-filter-val="yes">ready</button>
      <button class="filter-btn" data-filter-key="has-explorer" data-filter-val="no">pending</button>
    </div>
  </section>

  <section class="grid" id="grid">
{cards}
  </section>

  <div class="no-results" id="no-results" style="display:none">No instruments match the current filters.</div>

  <p style="margin-top:36px;color:var(--muted);font-size:12px">
    Generated <time>{generated_at}</time> from <code>scripts/generate_library.py</code> walking the GitHub workspace.
    Companion data: <a href="../data/library-manifest.json"><code>../data/library-manifest.json</code></a>.
  </p>
</main>

<script>
(function(){{
  const grid = document.getElementById('grid');
  const cards = Array.from(grid.querySelectorAll('.card'));
  const noResults = document.getElementById('no-results');
  const search = document.getElementById('search');

  // Filter state per group
  const state = {{ family:'all', cad:'all', wolfram:'all', 'has-explorer':'all', q:'' }};

  function applyFilters(){{
    let visible = 0;
    cards.forEach(c => {{
      let show = true;
      for (const [k,v] of Object.entries(state)){{
        if (k === 'q') continue;
        if (v === 'all') continue;
        if ((c.dataset[camel(k)] || '') !== v){{ show = false; break; }}
      }}
      if (show && state.q){{
        const hay = (c.querySelector('.card-title').textContent + ' ' +
                     c.querySelector('.card-slug').textContent).toLowerCase();
        if (!hay.includes(state.q)){{ show = false; }}
      }}
      c.classList.toggle('hidden', !show);
      if (show) visible++;
    }});
    noResults.style.display = visible === 0 ? 'block' : 'none';
  }}

  function camel(k){{ return k.replace(/-(.)/g, (_,c)=>c.toUpperCase()); }}

  document.querySelectorAll('.filter-btn').forEach(btn => {{
    btn.addEventListener('click', () => {{
      const key = btn.dataset.filterKey;
      const val = btn.dataset.filterVal;
      state[key] = val;
      document.querySelectorAll(`.filter-btn[data-filter-key="${{key}}"]`).forEach(b => {{
        b.classList.toggle('active', b.dataset.filterVal === val);
      }});
      applyFilters();
    }});
  }});

  let t;
  search.addEventListener('input', () => {{
    clearTimeout(t);
    t = setTimeout(() => {{
      state.q = search.value.trim().toLowerCase();
      applyFilters();
    }}, 120);
  }});
}})();
</script>

</body>
</html>
"""


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Generate the Heifer Zephyr Studio Explorers Library page")
    p.add_argument("--workspace", type=Path, default=DEFAULT_WORKSPACE,
                   help="Path to the GitHub workspace root (default: parent of this script's repo)")
    p.add_argument("--output-html", type=Path,
                   default=SHOWCASE_DIR / "site" / "library.html",
                   help="Where to write the rendered library.html")
    p.add_argument("--output-data", type=Path,
                   default=SHOWCASE_DIR / "data" / "library-manifest.json",
                   help="Where to write the library-manifest.json")
    args = p.parse_args(argv)

    if not args.workspace.is_dir():
        print(f"workspace not a directory: {args.workspace}", file=sys.stderr)
        return 2

    entries = scan_workspace(args.workspace)
    if not entries:
        print("No instrument repos found in workspace", file=sys.stderr)
        return 1

    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # data/library-manifest.json
    data = {
        "schema": "instrument-showcase-library-manifest-v1",
        "generated_at": generated_at,
        "workspace": str(args.workspace),
        "entries": [asdict(e) for e in entries],
    }
    args.output_data.parent.mkdir(parents=True, exist_ok=True)
    args.output_data.write_text(json.dumps(data, indent=2), encoding="utf-8")

    # site/library.html
    args.output_html.parent.mkdir(parents=True, exist_ok=True)
    html_out = render_library_html(entries, generated_at)
    args.output_html.write_text(html_out, encoding="utf-8")

    # Summary
    print(f"generate_library: wrote {args.output_html} ({len(html_out):,} chars)")
    print(f"                  wrote {args.output_data}")
    print(f"  entries          : {len(entries)}")
    print(f"  with explorer    : {sum(1 for e in entries if e.has_explorer)}")
    print(f"  wolfram live     : {sum(1 for e in entries if e.wolfram_state == 'live')}")
    print(f"  cad inlined      : {sum(1 for e in entries if e.cad == 'inline-glb')}")
    print(f"  awaiting explorer: {sum(1 for e in entries if not e.has_explorer)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
