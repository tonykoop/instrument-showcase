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
    # ----------------------------------------------------------------------
    # 2026-05-31: curated entries for the remaining 82 instrument repos
    # (all already have explorer.html; previously dropped by the FAMILY_MAP gate).
    # ----------------------------------------------------------------------
    # BRASS - lip-reed aerophones (sheet-metal + experimental horns)
    "bell-stack-chord-horn":      ("brass", "lip-reed"),
    "branching-multibell-horn":   ("brass", "lip-reed"),
    "brass-marine-reed-horn":     ("brass", "reed"),
    "bugle-sheetmetal":           ("brass", "lip-reed"),
    "centaur-duet-horn":          ("brass", "lip-reed"),
    "cornet-sheetmetal":          ("brass", "lip-reed"),
    "disc-trumpet":               ("brass", "lip-reed"),
    "dual-bell-phasing-horn":     ("brass", "lip-reed"),
    "iris-bell-tonal-horn":       ("brass", "lip-reed"),
    "mute-tuned-natural-horn":    ("brass", "lip-reed"),
    "octave-doubling-shofar":     ("brass", "lip-reed"),
    "serpent-sheet-metal-packet": ("brass", "lip-reed"),
    "slide-cornetto":             ("brass", "lip-reed"),
    "spiral-conch-horn":          ("brass", "lip-reed"),
    "trombone-sheetmetal":        ("brass", "lip-reed"),
    "trumpet-sheetmetal":         ("brass", "lip-reed"),
    # WIND - additional aerophones (sheet-metal flutes + organs)
    "barrel-organ":                  ("wind", "organ-pipe"),
    "hydraulophone":                 ("wind", "fluid"),
    "portable-calliope":             ("wind", "steam-whistle"),
    "portative-organ":               ("wind", "organ-pipe"),
    "saxophone-sheetmetal":          ("wind", "reed"),
    "sea-organ":                     ("wind", "organ-pipe"),
    "sheet-metal-bass-clarinet":     ("wind", "reed"),
    "sheet-metal-pan-flute":         ("wind", "stopped-pipe"),
    "sheet-metal-recorder-quartet":  ("wind", "duct-flute"),
    "sheet-metal-tin-whistle-set":   ("wind", "duct-flute"),
    "steam-train-whistle":           ("wind", "steam-whistle"),
    "transverse-flute-sheetmetal":   ("wind", "open-pipe"),
    # STRING - additional chordophones (bowed / keyboard / zither / resonator)
    "aeolian-harp-pillar":             ("string", "aeolian"),
    "autoharp-inspired":               ("string", "zither"),
    "bowed-metal-psaltery":            ("string", "bowed-zither"),
    "bowed-sheet-metal-sarod":         ("string", "bowed"),
    "brian-boru-harp-replica":         ("string", "harp"),
    "clavichord":                      ("string", "struck-keyboard"),
    "folding-travel-resonator-guitar": ("string", "resonator"),
    "harpsichord":                     ("string", "plucked-keyboard"),
    "magnetic-chromatic-harp":         ("string", "harp-electric"),
    "marxophone":                      ("string", "zither"),
    "multi-bridge-sheet-zither":       ("string", "zither"),
    "nyckelharpa":                     ("string", "bowed-keyed"),
    "octobass":                        ("string", "bowed"),
    "pianola":                         ("string", "struck-keyboard"),
    "resophonic-bouzouki":             ("string", "resonator"),
    "spun-aluminum-cello":             ("string", "bowed"),
    "sympathetic-sarangi-fiddle":      ("string", "bowed"),
    "telescoping-bass-profundo":       ("string", "bowed"),
    "triple-cone-slide-guitar":        ("string", "resonator"),
    "tromba-marina":                   ("string", "bowed"),
    "wheelharp":                       ("string", "bowed-keyed"),
    "hurdy-gurdy":                     ("string", "bowed-keyed"),
    # DRUM - additional membranophones (sheet-metal + experimental)
    "bass-surface-drum":            ("drum", "single-membrane"),
    "bowed-frame-drum":             ("drum", "single-membrane"),
    "compact-drum-kit":             ("drum", "multi-membrane"),
    "modular-pedestal-drum-stack":  ("drum", "multi-membrane"),
    "pitched-bell-cajon":           ("drum", "box-drum"),
    "sheet-metal-djembe":           ("drum", "single-membrane"),
    "sheet-metal-talking-drum":     ("drum", "double-membrane"),
    "timpani-sheetmetal":           ("drum", "kettle-membrane"),
    "tunable-snare-frame-array":    ("drum", "snare-membrane"),
    # IDIOPHONE - additional (lamellophone / friction / tuned-shell / bell / plate)
    "array-mbira":                  ("idiophone", "lamellophone"),
    "bowed-dish":                   ("idiophone", "friction"),
    "carillon":                     ("idiophone", "tuned-bell"),
    "celesta":                      ("idiophone", "tuned-bar-metal"),
    "chromatic-25-tongue-drum":     ("idiophone", "tongue-drum-steel"),
    "cristal-baschet":              ("idiophone", "friction"),
    "daxophone":                    ("idiophone", "friction"),
    "glass-armonica":               ("idiophone", "friction"),
    "glass-harp":                   ("idiophone", "friction"),
    "handpan-sheetmetal":           ("idiophone", "tuned-shell"),
    "inverted-pan-tower":           ("idiophone", "tuned-shell"),
    "jal-tarang":                   ("idiophone", "tuned-vessel"),
    "music-box":                    ("idiophone", "lamellophone"),
    "musical-saw":                  ("idiophone", "friction"),
    "pitched-bell-ladder":          ("idiophone", "tuned-bell"),
    "sheet-metal-mbira":            ("idiophone", "lamellophone"),
    "solenoid-disc-idiophone":      ("idiophone", "struck-metal"),
    "spiral-chime-tower":           ("idiophone", "tuned-pipe"),
    "steel-pan-organ":              ("idiophone", "tuned-shell"),
    "steel-pot-drum":               ("idiophone", "tuned-shell"),
    "tuned-slit-drum-bank":         ("idiophone", "slit-drum"),
    "waterphone":                   ("idiophone", "friction"),
    "wind-gong-sheetmetal":         ("idiophone", "tuned-plate"),
}

# Folder -> broad family fallback, used when a slug isn't explicitly in FAMILY_MAP
# (keeps new instruments from being silently dropped from the library).
FOLDER_FAMILY: dict[str, str] = {
    "strings": "string",
    "woodwind": "wind",
    "brass": "brass",
    "percussion": "drum",
    "idiophones": "idiophone",
}

# Display labels for the catalog (maps internal family tokens to the 5 canonical
# family names used by the completeness trackers #26-#31).
FAMILY_LABELS: dict[str, str] = {
    "string": "Strings", "wind": "Woodwind", "brass": "Brass",
    "drum": "Percussion", "idiophone": "Idiophones",
    "hybrid": "Hybrid", "other": "Other",
}
COMPLETENESS_LABELS = {
    "complete": "Complete", "near": "Near",
    "in-progress": "In progress", "scaffold": "Scaffold",
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
    # Explorer completeness axis (issue #31): W = live Wolfram, I = rendered
    # images shown in explorer, 3D = <model-viewer>. score 0-3.
    wolfram_live: bool = False
    images_present: bool = False
    viewer_present: bool = False
    completeness_score: int = 0
    completeness_state: str = "scaffold"  # complete | near | in-progress | scaffold


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


def detect_explorer_features(explorer: Path) -> tuple[bool, bool, bool]:
    """Report (wolfram_present, images_present, viewer_present) from explorer.html,
    matching the per-family completeness trackers (issue #31), which assess the
    EXPLORER's interactive completeness:
      W  = embeds a live Wolfram Cloud model (a wolframcloud.com URL).
      I  = displays at least one rendered concept image (an <img> element).
      3D = embeds a <model-viewer> element.
    All three are read from the explorer, not the manifest: a Wolfram model can
    be published in the manifest while the explorer is still a scaffold that
    doesn't embed it (e.g. cnc-guitar-bodies). The tracker counts the explorer,
    so we do too. (manifest wolfram_state is kept separately for the Wolfram
    pill/filter — "is a model published" — a different axis from "shown here".)
    """
    if not explorer.exists():
        return (False, False, False)
    try:
        html = explorer.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return (False, False, False)
    wolfram_present = "wolframcloud.com" in html
    viewer_present = "model-viewer" in html
    images_present = "<img" in html
    return (wolfram_present, images_present, viewer_present)


COMPLETENESS_STATE = {3: "complete", 2: "near", 1: "in-progress", 0: "scaffold"}


def scan_workspace(workspace: Path, base_url: str = "",
                   published: "frozenset[str]" = frozenset()) -> list[LibraryEntry]:
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

        family, acoustic = FAMILY_MAP.get(slug) or (FOLDER_FAMILY.get(family_dir, "other"), "unclassified")
        cad_kind, cad_size = detect_cad(repo)
        wstate, wurl, wnb = derive_wolfram_state(manifest, embed_index.get(slug))
        status, status_label = derive_status(manifest)
        fam_members = manifest.get("family_members") or []
        hero_rel = detect_hero(repo)
        # Explorer completeness (issue #31): W + I + 3D all read from the explorer.
        wolfram_present, images_present, viewer_present = detect_explorer_features(explorer)
        wolfram_live = wolfram_present  # completeness W axis = explorer embeds a live model
        comp_score = int(wolfram_live) + int(images_present) + int(viewer_present)
        comp_state = COMPLETENESS_STATE[comp_score]
        if base_url:
            # Publishing mode: each instrument is its own GitHub Pages site at
            # {base_url}/{slug}/. Only repos in the `published` set (public +
            # Pages-live) get live links/images; the rest render as clean,
            # non-clickable text cards so the page never shows 404s or broken
            # images, and they upgrade automatically as more are published.
            root = base_url.rstrip("/")
            if slug in published:
                explorer_path = f"{root}/{slug}/explorer.html"
                hero_path = f"{root}/{slug}/{hero_rel}" if hero_rel else ""
            else:
                explorer_path = ""
                hero_path = ""
        else:
            explorer_path = f"../../../{family_dir}/{slug}/explorer.html"
            hero_path = f"../../../{family_dir}/{slug}/{hero_rel}" if hero_rel else ""

        entries.append(LibraryEntry(
            slug=slug,
            title=title,
            instrument=instrument,
            family=family,
            acoustic_class=acoustic,
            status=status,
            status_label=status_label,
            explorer_path=explorer_path,  # local ../../../ path, or absolute Pages URL in publishing mode
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
            wolfram_live=wolfram_live,
            images_present=images_present,
            viewer_present=viewer_present,
            completeness_score=comp_score,
            completeness_state=comp_state,
        ))
    return entries


# --------------------------------------------------------------------------
# HTML rendering
# --------------------------------------------------------------------------


def esc(s) -> str:
    return _html.escape("" if s is None else str(s), quote=True)


CARD_TPL = """\
<article class="card" data-family="{family}" data-status="{status}" data-cad="{cad}" data-wolfram="{wolfram_state}" data-has-explorer="{has_explorer_str}" data-completeness="{completeness_state}" data-score="{completeness_score}">
  <header class="card-head">
    <a class="card-title" {open_attr}>{title}</a>
    {explorer_pill}
  </header>
  {hero_img}
  <div class="card-meta">
    <span class="badge badge-family family-{family}">{family_label}</span>
    <span class="badge badge-acoustic">{acoustic_class}</span>
    {family_count_badge}
  </div>
  {completeness_pill}
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
    if e.has_explorer and e.explorer_path:
        open_attr = f'href="{esc(e.explorer_path)}"'
        explorer_pill = '<span class="explorer-pill explorer-pill-yes">Explorer ready</span>'
    elif e.has_explorer:
        # Explorer is built but the repo isn't published yet (private / no Pages).
        open_attr = ""
        explorer_pill = '<span class="explorer-pill explorer-pill-yes">Explorer built</span>'
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

    # Completeness pill (issue #31 axis): state label + W / I / 3D mini-chips.
    def _axis(on: bool, label: str) -> str:
        return f'<b class="ax {"on" if on else "off"}">{label}</b>'
    completeness_pill = (
        f'<div class="comp-row" title="Explorer completeness — W: live Wolfram model · '
        f'I: rendered concept images · 3D: model-viewer">'
        f'<span class="comp-state comp-{esc(e.completeness_state)}">'
        f'{COMPLETENESS_LABELS.get(e.completeness_state, e.completeness_state)}</span>'
        f'<span class="comp-axes">'
        f'{_axis(e.wolfram_live, "W")}{_axis(e.images_present, "I")}{_axis(e.viewer_present, "3D")}'
        f'</span></div>'
    )
    family_label = FAMILY_LABELS.get(e.family, e.family)

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
        family_label=esc(family_label),
        completeness_pill=completeness_pill,
        completeness_state=esc(e.completeness_state),
        completeness_score=e.completeness_score,
    )


def render_library_html(entries: list[LibraryEntry], generated_at: str) -> str:
    # Sort by family then title
    entries_sorted = sorted(entries, key=lambda e: (e.family, e.title.lower()))

    # Stats
    total = len(entries_sorted)
    with_explorer = sum(1 for e in entries_sorted if e.has_explorer)
    live_wolfram = sum(1 for e in entries_sorted if e.wolfram_state == "live")
    complete_count = sum(1 for e in entries_sorted if e.completeness_state == "complete")

    # Per-family tallies + completeness progress (issue #31 dashboard).
    fam_total: dict[str, int] = {}
    fam_complete: dict[str, int] = {}
    for e in entries_sorted:
        fam_total[e.family] = fam_total.get(e.family, 0) + 1
        if e.completeness_state == "complete":
            fam_complete[e.family] = fam_complete.get(e.family, 0) + 1

    cards_html = "\n".join(render_card(e) for e in entries_sorted)
    family_filter_buttons = " ".join(
        f'<button class="filter-btn" data-filter-key="family" data-filter-val="{esc(f)}">'
        f'{esc(FAMILY_LABELS.get(f, f))} <span class="count">{n}</span></button>'
        for f, n in sorted(fam_total.items(), key=lambda kv: FAMILY_LABELS.get(kv[0], kv[0])))

    # Per-family progress bars
    rows = []
    for f, n in sorted(fam_total.items(), key=lambda kv: FAMILY_LABELS.get(kv[0], kv[0])):
        done = fam_complete.get(f, 0)
        pct = round(100 * done / n) if n else 0
        rows.append(
            f'<div class="fam-prog"><span class="fam-prog-label">{esc(FAMILY_LABELS.get(f, f))}</span>'
            f'<span class="fam-prog-bar"><span class="fam-prog-fill" style="width:{pct}%"></span></span>'
            f'<span class="fam-prog-count">{done}/{n}</span></div>'
        )
    family_progress = "\n".join(rows)

    return LIBRARY_HTML.format(
        generated_at=esc(generated_at),
        total=total,
        with_explorer=with_explorer,
        live_wolfram=live_wolfram,
        complete_count=complete_count,
        family_filter_buttons=family_filter_buttons,
        family_progress=family_progress,
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
  --walnut:#15181d; --cedar:#5b626d; --cream:#f6f7f9; --paper:#ffffff;
  --lapis:#d6562b; --gold:#d6562b; --ink:#15181d; --muted:#5b626d;
  --rule:#e3e6ea; --rule-strong:#cdd2d9; --ok:#2f8f5b; --warn:#c79100; --block:#c4453a;
  --pill-bg:#fbe9e2; --pill-border:#d6562b;
  --hover:#eef0f3;
  --shadow:0 1px 2px rgba(20,24,29,.05),0 4px 16px rgba(20,24,29,.04);
  --ui:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  --serif:var(--ui); --italic-serif:var(--ui);
  --mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
}}
[data-theme="dark"]{{
  --walnut:#e8ecf1; --cedar:#9aa4b2; --cream:#0e1116; --paper:#171d25;
  --lapis:#f0794f; --gold:#f0794f; --ink:#e8ecf1; --muted:#9aa4b2;
  --rule:#262d37; --rule-strong:#333c48; --ok:#4fb37e; --warn:#d9b13e; --block:#e0695e;
  --pill-bg:#2a1c16; --pill-border:#f0794f; --hover:#1d232c;
  --shadow:0 1px 2px rgba(0,0,0,.3),0 4px 18px rgba(0,0,0,.28);
}}
*,*::before,*::after{{box-sizing:border-box}}
html,body{{margin:0;padding:0;background:var(--cream);color:var(--ink);
  font-family:var(--ui);font-size:15px;line-height:1.5;-webkit-font-smoothing:antialiased}}
a{{color:var(--lapis);text-decoration:none}}
a:hover{{text-decoration:underline}}
code{{font-family:var(--mono);font-size:0.88em}}

.app-bar{{position:sticky;top:0;z-index:30;height:58px;
  background:color-mix(in srgb,var(--paper) 86%,transparent);
  -webkit-backdrop-filter:saturate(160%) blur(10px);backdrop-filter:saturate(160%) blur(10px);
  color:var(--ink);border-bottom:1px solid var(--rule);
  display:flex;align-items:center;gap:18px;padding:0 22px}}
.brand{{display:flex;align-items:center;gap:11px;flex:0 0 auto}}
.brand .dot{{width:11px;height:11px;border-radius:3px;background:var(--gold);transform:rotate(45deg)}}
.wordmark{{text-decoration:none;display:inline-flex;align-items:baseline;gap:11px}}
.wordmark:hover{{text-decoration:none}}
.wordmark:hover em{{color:var(--gold)}}
.wordmark em{{font-family:var(--italic-serif);font-style:italic;
  font-size:22px;color:var(--ink);letter-spacing:0.005em;transition:color 120ms}}
.tagline{{font-family:var(--ui);font-size:13px;color:var(--muted);
  border-left:1px solid var(--rule);padding-left:12px}}
.actions{{margin-left:auto;display:flex;align-items:center;gap:8px}}
.action-btn{{display:inline-block;font-family:var(--ui);font-size:12px;font-weight:500;
  color:var(--muted);border:1px solid var(--rule);background:var(--paper);
  border-radius:8px;padding:7px 11px;cursor:pointer}}
.action-btn:hover{{background:var(--hover);text-decoration:none;color:var(--ink)}}

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

/* Completeness pill (issue #31 axis: W live Wolfram · I images · 3D viewer) */
.comp-row{{display:flex;align-items:center;gap:8px;margin:-1px 0 1px}}
.comp-state{{font-family:var(--ui);font-size:10px;font-weight:700;letter-spacing:0.05em;
  text-transform:uppercase;padding:3px 9px;border-radius:11px;border:1px solid var(--rule)}}
.comp-complete{{background:#D8EBD3;color:var(--ok);border-color:var(--ok)}}
.comp-near{{background:#FCEFC6;color:#7A5814;border-color:var(--pill-border)}}
.comp-in-progress{{background:#EEEAE0;color:var(--muted);border-color:var(--muted)}}
.comp-scaffold{{background:var(--cream);color:var(--muted);border-color:var(--rule);border-style:dashed}}
.comp-axes{{display:inline-flex;gap:3px}}
.comp-axes .ax{{font-family:var(--mono);font-size:9px;font-weight:700;min-width:19px;text-align:center;
  padding:2px 3px;border-radius:3px;line-height:1}}
.comp-axes .ax.on{{background:var(--ok);color:#fff}}
.comp-axes .ax.off{{background:var(--cream);color:#C9BEA9;border:1px solid var(--rule)}}

/* Per-family completeness dashboard (issue #31) */
.progress-panel{{background:var(--paper);border:1px solid var(--rule);border-radius:5px;
  padding:14px 18px;margin:0 0 18px}}
.progress-head{{display:flex;justify-content:space-between;align-items:baseline;gap:14px;
  flex-wrap:wrap;margin-bottom:10px}}
.progress-title{{font-family:var(--serif);font-weight:600;font-size:15px;color:var(--walnut)}}
.progress-legend{{font-family:var(--ui);font-size:11px;color:var(--muted)}}
.progress-legend b{{color:var(--walnut)}}
.fam-prog{{display:grid;grid-template-columns:104px minmax(120px,360px) 52px;align-items:center;gap:12px;margin:5px 0}}
.fam-prog-label{{font-family:var(--ui);font-size:12px;font-weight:600;color:var(--walnut)}}
.fam-prog-bar{{height:8px;background:var(--cream);border:1px solid var(--rule);border-radius:6px;overflow:hidden}}
.fam-prog-fill{{display:block;height:100%;background:linear-gradient(90deg,var(--cedar),var(--ok));border-radius:6px}}
.fam-prog-count{{font-family:var(--mono);font-size:11px;color:var(--muted);text-align:right}}
.stat-complete .of{{font-family:var(--ui);font-size:13px;color:var(--muted);font-weight:500;margin-left:3px}}
.sort-select{{font-family:var(--ui);font-size:12px;padding:5px 8px;border:1px solid var(--rule);
  border-radius:4px;background:#FFFCF5;color:var(--walnut);cursor:pointer}}

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
    <span class="dot"></span>
    <a class="wordmark" href="library.html" title="Back to the library"><em>Heifer Zephyr</em></a>
    <span class="tagline">Studio Explorers · Library</span>
  </div>
  <div class="actions">
    <a class="action-btn" href="index.html">Deliverables Hub</a>
    <a class="action-btn" href="manifest.html">Manifest</a>
    <a class="action-btn" href="https://github.com/tonykoop" target="_blank" rel="noopener">GitHub</a>
    <button class="action-btn" id="theme-toggle" title="Toggle light / dark" aria-label="Toggle theme">◐ Theme</button>
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
    <div class="stat stat-complete"><div class="k">Explorers complete</div><div class="v">{complete_count}<span class="of">/ {total}</span></div></div>
  </section>

  <section class="progress-panel">
    <div class="progress-head">
      <span class="progress-title">Explorer completeness by family</span>
      <span class="progress-legend">Complete = live <b>W</b>olfram model · rendered <b>I</b>mages · <b>3D</b> model-viewer</span>
    </div>
    {family_progress}
  </section>

  <section class="controls">
    <input id="search" class="search" placeholder="Search by name or slug…" aria-label="Search">
    <div class="filter-group" data-filter-key="completeness">
      <label>Completeness</label>
      <button class="filter-btn active" data-filter-key="completeness" data-filter-val="all">all</button>
      <button class="filter-btn" data-filter-key="completeness" data-filter-val="complete">complete</button>
      <button class="filter-btn" data-filter-key="completeness" data-filter-val="near">near</button>
      <button class="filter-btn" data-filter-key="completeness" data-filter-val="in-progress">in&nbsp;progress</button>
      <button class="filter-btn" data-filter-key="completeness" data-filter-val="scaffold">scaffold</button>
    </div>
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
    <div class="filter-group sort-group">
      <label>Sort</label>
      <select id="sort" class="sort-select">
        <option value="completeness">Most complete</option>
        <option value="family">Family</option>
        <option value="name">Name</option>
      </select>
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
  const state = {{ completeness:'all', family:'all', cad:'all', wolfram:'all', 'has-explorer':'all', q:'' }};

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

  // Sort (default: most complete first)
  const sortSel = document.getElementById('sort');
  const titleOf = c => c.querySelector('.card-title').textContent.toLowerCase();
  function applySort(){{
    const mode = sortSel ? sortSel.value : 'completeness';
    cards.slice().sort((a,b) => {{
      if (mode === 'completeness')
        return ((b.dataset.score|0) - (a.dataset.score|0)) || titleOf(a).localeCompare(titleOf(b));
      if (mode === 'family')
        return (a.dataset.family||'').localeCompare(b.dataset.family||'') || titleOf(a).localeCompare(titleOf(b));
      return titleOf(a).localeCompare(titleOf(b));
    }}).forEach(c => grid.appendChild(c));
  }}
  if (sortSel) sortSel.addEventListener('change', applySort);
  applySort();  // apply default sort on load
}})();
</script>
<script>
(function(){{
  var KEY='hz-theme';
  try{{var s=localStorage.getItem(KEY); if(s) document.documentElement.setAttribute('data-theme',s);}}catch(e){{}}
  var b=document.getElementById('theme-toggle');
  if(b) b.addEventListener('click',function(){{
    var dark=document.documentElement.getAttribute('data-theme')!=='dark';
    if(dark) document.documentElement.setAttribute('data-theme','dark'); else document.documentElement.removeAttribute('data-theme');
    try{{localStorage.setItem(KEY,dark?'dark':'');}}catch(e){{}}
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
    p.add_argument("--base-url", default="",
                   help="If set (e.g. https://tonykoop.github.io), emit absolute "
                        "GitHub Pages URLs instead of local ../../../ paths.")
    p.add_argument("--published", default="",
                   help="Comma-separated slugs OR a path to a newline-delimited file "
                        "listing repos that are public + Pages-live. With --base-url, "
                        "only these get live links/images; others render as text cards.")
    args = p.parse_args(argv)

    published: "frozenset[str]" = frozenset()
    if args.published:
        pub_path = Path(args.published)
        if pub_path.is_file():
            published = frozenset(s.strip() for s in pub_path.read_text().split() if s.strip())
        else:
            published = frozenset(s.strip() for s in args.published.split(",") if s.strip())

    if not args.workspace.is_dir():
        print(f"workspace not a directory: {args.workspace}", file=sys.stderr)
        return 2

    entries = scan_workspace(args.workspace, base_url=args.base_url, published=published)
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
    if args.base_url:
        # Belt-and-suspenders: hide any hero image that fails to load (e.g. a
        # repo whose Pages went live but whose hero render isn't committed yet).
        fallback = ("<script>document.querySelectorAll('img').forEach(function(im){"
                    "im.addEventListener('error',function(){this.style.display='none'});});</script>\n")
        html_out = html_out.replace("</body>", fallback + "</body>", 1)
    args.output_html.write_text(html_out, encoding="utf-8")

    # Summary
    print(f"generate_library: wrote {args.output_html} ({len(html_out):,} chars)")
    print(f"                  wrote {args.output_data}")
    print(f"  entries          : {len(entries)}")
    print(f"  with explorer    : {sum(1 for e in entries if e.has_explorer)}")
    print(f"  published live   : {sum(1 for e in entries if e.slug in published)}")
    print(f"  awaiting explorer: {sum(1 for e in entries if not e.has_explorer)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
