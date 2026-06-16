#!/usr/bin/env python3
"""
generate_explorer_v2.py — the unified per-instrument Explorer v2 generator.

Phase 2 of the catalog modernization. Produces a consistent, brand-disciplined
`explorer.html` for any instrument repo from its own data files, binding the
three completeness axes the catalog's per-family dashboard tracks (issue #31):

    W  — live Wolfram Cloud model  (iframe embed of the published notebook)
    I  — rendered concept images   (a hero + gallery grid from images/)
    3D — interactive model-viewer  (cad/*.glb)

plus structured sections pulled from the repo: overview (design.md), bill of
materials (bom.csv), validation gates (capstone-manifest release_gate),
artifact file list, and a cross-link to the engineering wiki. The shared
app-bar carries the Heifer Zephyr wordmark linking back to the library, so
every generated explorer routes home with one click.

Design language is harvested from the hand-built `kora/explorer-v2.html`
prototype (dark-mode tokens, hero + spec strip, sidebar TOC).

SAFETY — no dual-generator clobber. By default this writes
`explorer.generated.html` (review/diff, never destroys a hand-authored
`explorer.html`). Use `--write-explorer` to promote it to `explorer.html`
(intended for scaffold repos with no bespoke explorer), and `--force` to
overwrite an existing one deliberately.

Usage:
    python3 generate_explorer_v2.py --slug kora            # one repo -> explorer.generated.html
    python3 generate_explorer_v2.py --slug kora --write-explorer
    python3 generate_explorer_v2.py --all                  # every repo (generated.html)
    python3 generate_explorer_v2.py --all --only-scaffold --write-explorer
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

# Reuse the catalog generator's resolvers + brand vocabulary.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import generate_library as gl  # noqa: E402

esc = gl.esc

GALLERY_EXTS = (".png", ".jpg", ".jpeg", ".webp")
# Images we never want in a gallery grid (chrome, not concept art).
GALLERY_SKIP = ("favicon", "logo", "wordmark", "sprite", "icon-")


# --------------------------------------------------------------------------
# Per-instrument data gathering
# --------------------------------------------------------------------------


@dataclass
class ExplorerData:
    slug: str
    family_dir: str
    repo: Path
    title: str = ""
    instrument: str = ""
    family: str = "other"
    family_label: str = "Other"
    acoustic_class: str = ""
    status: str = "unknown"
    status_label: str = "Unknown"
    overview: str = ""              # HTML paragraphs from design.md
    hero_rel: str = ""             # relative path to hero image (within repo)
    gallery: list[str] = field(default_factory=list)   # relative image paths
    glb_rel: str = ""              # relative path to a .glb for model-viewer
    cad_kind: str = "none"
    wolfram_url: str = ""          # live Public-Execute cloud_url, or ""
    wolfram_state: str = "pending"
    bom_rows: list[list[str]] = field(default_factory=list)
    bom_header: list[str] = field(default_factory=list)
    gates: list[tuple[str, str]] = field(default_factory=list)  # (label, note)
    artifacts: list[str] = field(default_factory=list)
    has_wiki: bool = False
    family_members: list[str] = field(default_factory=list)
    # completeness axes (computed)
    axis_w: bool = False
    axis_i: bool = False
    axis_3d: bool = False

    @property
    def score(self) -> int:
        return int(self.axis_w) + int(self.axis_i) + int(self.axis_3d)

    @property
    def comp_state(self) -> str:
        return gl.COMPLETENESS_STATE[self.score]


def _read_design_overview(repo: Path, max_paras: int = 3) -> str:
    """Pull the first few real paragraphs out of design.md as HTML."""
    md = repo / "design.md"
    if not md.exists():
        return ""
    try:
        lines = md.read_text(encoding="utf-8", errors="ignore").splitlines()
    except OSError:
        return ""
    paras: list[str] = []
    buf: list[str] = []
    for ln in lines:
        s = ln.strip()
        if s.startswith("#") or s.startswith("```") or s.startswith("|") or s.startswith(">"):
            if buf:
                paras.append(" ".join(buf)); buf = []
            continue
        if not s:
            if buf:
                paras.append(" ".join(buf)); buf = []
            continue
        buf.append(s)
        if len(paras) >= max_paras:
            break
    if buf and len(paras) < max_paras:
        paras.append(" ".join(buf))
    paras = [p for p in paras if len(p) > 40][:max_paras]
    return "".join(f"<p>{esc(p)}</p>" for p in paras)


def _collect_gallery(repo: Path) -> list[str]:
    img_dir = repo / "images"
    if not img_dir.is_dir():
        return []
    out: list[str] = []
    for p in sorted(img_dir.rglob("*")):
        if p.suffix.lower() not in GALLERY_EXTS:
            continue
        name = p.name.lower()
        if any(skip in name for skip in GALLERY_SKIP):
            continue
        out.append(str(p.relative_to(repo)).replace("\\", "/"))
    return out[:12]


def _read_bom(repo: Path, max_rows: int = 14) -> tuple[list[str], list[list[str]]]:
    bom = repo / "bom.csv"
    if not bom.exists():
        return ([], [])
    try:
        with bom.open(encoding="utf-8", errors="ignore", newline="") as f:
            rows = list(csv.reader(f))
    except OSError:
        return ([], [])
    rows = [r for r in rows if any(c.strip() for c in r)]
    if not rows:
        return ([], [])
    return (rows[0], rows[1:max_rows + 1])


def _read_gates(manifest: dict) -> list[tuple[str, str]]:
    rg = manifest.get("release_gate") or {}
    gates: list[tuple[str, str]] = []
    if isinstance(rg, dict):
        for k, v in rg.items():
            label = k.replace("_", " ").title()
            if isinstance(v, bool):
                gates.append((label, "Yes" if v else "No"))
            elif isinstance(v, (str, int, float)):
                gates.append((label, str(v)))
            elif isinstance(v, list):
                gates.append((label, ", ".join(str(x) for x in v)[:120]))
    return gates


def gather(repo: Path, family_dir: str, embed_index: dict) -> ExplorerData:
    slug = repo.name
    manifest: dict = {}
    mpath = repo / "capstone-manifest.json"
    if mpath.exists():
        try:
            manifest = json.loads(mpath.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            manifest = {}

    title = manifest.get("title") or manifest.get("instrument") or slug.replace("-", " ").title()
    instrument = manifest.get("instrument") or title
    family, acoustic = gl.FAMILY_MAP.get(slug) or (gl.FOLDER_FAMILY.get(family_dir, "other"), "unclassified")
    status, status_label = gl.derive_status(manifest)
    wstate, wurl, _ = gl.derive_wolfram_state(manifest, embed_index.get(slug))
    cad_kind, _ = gl.detect_cad(repo)

    glb_rel = ""
    cad_dir = repo / "cad"
    if cad_dir.is_dir():
        glbs = sorted(cad_dir.glob("*.glb"), key=lambda p: p.stat().st_size, reverse=True)
        if glbs:
            glb_rel = str(glbs[0].relative_to(repo)).replace("\\", "/")

    hero_rel = gl.detect_hero(repo)
    gallery = _collect_gallery(repo)
    bom_header, bom_rows = _read_bom(repo)
    gates = _read_gates(manifest)
    artifacts = [a for a in (manifest.get("artifacts") or []) if isinstance(a, str)][:24]
    fam_members = manifest.get("family_members") or []
    has_wiki = (gl.DEFAULT_WORKSPACE / "instruments" / "_meta" / "instrument-showcase"
                / "wiki" / "instruments" / f"{slug}.md").exists()

    d = ExplorerData(
        slug=slug, family_dir=family_dir, repo=repo,
        title=title, instrument=instrument,
        family=family, family_label=gl.FAMILY_LABELS.get(family, family),
        acoustic_class=acoustic, status=status, status_label=status_label,
        overview=_read_design_overview(repo),
        hero_rel=hero_rel, gallery=gallery, glb_rel=glb_rel, cad_kind=cad_kind,
        wolfram_url=wurl, wolfram_state=wstate,
        bom_header=bom_header, bom_rows=bom_rows, gates=gates,
        artifacts=artifacts, has_wiki=has_wiki, family_members=fam_members,
    )
    # Completeness axes mirror the catalog's explorer-based detection.
    d.axis_w = bool(wurl)
    d.axis_i = bool(hero_rel) or bool(gallery)
    d.axis_3d = bool(glb_rel)
    return d


# --------------------------------------------------------------------------
# Rendering
# --------------------------------------------------------------------------

EXPLORER_CSS = """<style>
:root{
  --ink:#15181d; --ink-2:#15181d; --ink-3:#5b626d; --ink-faint:#9aa1ac;
  --rule:#e3e6ea; --rule-soft:#eef0f3; --rule-strong:#cdd2d9;
  --paper:#ffffff; --paper-2:#ffffff; --paper-3:#f6f7f9;
  --accent:#d6562b; --accent-soft:#fbe9e2; --cedar:#5b626d;
  --gold:#d6562b; --gold-soft:#fbe9e2;
  --ok:#2f8f5b; --ok-soft:#e3f1ea; --warn:#c79100; --block:#c4453a;
  --ui:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  --serif:var(--ui); --italic-serif:var(--ui);
  --mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
  --radius:12px; --shadow:0 1px 2px rgba(20,24,29,.05),0 4px 16px rgba(20,24,29,.04);
}
[data-theme="dark"]{
  --ink:#e8ecf1; --ink-2:#e8ecf1; --ink-3:#9aa4b2; --ink-faint:#69727f;
  --rule:#262d37; --rule-soft:#1d232c; --rule-strong:#333c48;
  --paper:#0e1116; --paper-2:#171d25; --paper-3:#151a21;
  --accent:#f0794f; --accent-soft:#2a1c16; --cedar:#9aa4b2;
  --gold:#f0794f; --gold-soft:#2a1c16;
  --ok:#4fb37e; --ok-soft:#15301f; --warn:#d9b13e; --block:#e0695e;
  --shadow:0 1px 2px rgba(0,0,0,.3),0 4px 18px rgba(0,0,0,.28);
}
*,*::before,*::after{box-sizing:border-box}
html,body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--ui);
  font-size:14.5px;line-height:1.6;-webkit-font-smoothing:antialiased;transition:background .2s,color .2s}
a{color:var(--accent);text-decoration:none} a:hover{color:var(--ink-2)}
code{font-family:var(--mono);font-size:.86em}
.appbar{position:sticky;top:0;z-index:30;background:color-mix(in srgb,var(--paper) 86%,transparent);
  -webkit-backdrop-filter:saturate(160%) blur(10px);backdrop-filter:saturate(160%) blur(10px);
  color:var(--ink);border-bottom:1px solid var(--rule);
  display:grid;grid-template-columns:auto 1fr auto;align-items:center;gap:24px;padding:12px 26px}
.brand{display:flex;align-items:center;gap:11px}
.brand .dot{width:11px;height:11px;border-radius:3px;background:var(--accent);transform:rotate(45deg);flex:0 0 auto}
.wordmark{text-decoration:none;display:inline-flex;align-items:baseline;gap:11px}
.wordmark:hover em{color:var(--accent)}
.wordmark em{font-family:var(--italic-serif);font-style:italic;font-size:22px;color:var(--ink);line-height:1;transition:color .12s}
.instrument-tag{font-family:var(--ui);font-size:13px;color:var(--ink-3);
  border-left:1px solid var(--rule);padding-left:12px;font-style:normal}
.appnav{display:flex;gap:3px;justify-self:center}
.appnav a{font-family:var(--ui);font-size:13px;font-weight:500;color:var(--ink-3);
  padding:7px 11px;border-radius:8px;transition:background .12s,color .12s}
.appnav a:hover{background:var(--paper-3);color:var(--ink)}
.icon-btn{display:inline-flex;align-items:center;justify-content:center;height:32px;padding:0 12px;
  border-radius:8px;color:var(--ink-3);background:var(--paper-2);border:1px solid var(--rule);
  cursor:pointer;font-family:var(--ui);font-size:13px}
.icon-btn:hover{color:var(--accent);border-color:var(--rule-strong)}
.hero{border-bottom:1px solid var(--rule);background:
  radial-gradient(900px 360px at 90% -20%,var(--gold-soft) 0%,transparent 60%),
  radial-gradient(700px 320px at 10% -10%,var(--paper-3) 0%,transparent 65%),var(--paper)}
.hero-inner{max-width:1320px;margin:0 auto;padding:34px 26px 24px;display:grid;
  grid-template-columns:1fr 360px;gap:36px;align-items:end}
@media(max-width:980px){.hero-inner{grid-template-columns:1fr;gap:18px}}
.eyebrow{font-family:var(--ui);font-weight:600;font-size:11px;color:var(--accent);
  text-transform:uppercase;letter-spacing:.18em;display:inline-flex;align-items:center;gap:8px;margin-bottom:12px}
.eyebrow::before{content:"";width:18px;height:1px;background:var(--accent)}
.hero h1{font-family:var(--serif);font-weight:500;font-size:clamp(32px,4.2vw,44px);color:var(--ink);
  line-height:1.05;margin:0 0 14px;letter-spacing:-.02em}
.meta-line{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:0 0 16px}
.pill{font-family:var(--ui);font-size:11px;font-weight:600;letter-spacing:.05em;text-transform:uppercase;
  padding:4px 10px;border-radius:3px;border:1px solid var(--rule);background:var(--paper-3);color:var(--ink-2)}
.pill-public{background:var(--ok-soft);color:var(--ok);border-color:var(--ok)}
.pill-private{background:var(--gold-soft);color:#7A5814;border-color:var(--gold)}
.pill-blocked{background:#F5DBD2;color:var(--block);border-color:var(--block)}
.pill-fam{font-family:var(--mono);letter-spacing:0;text-transform:none}
.hero p{color:var(--ink-3);max-width:640px;margin:0 0 18px;font-size:15px}
.hero-cover{aspect-ratio:4/3;background:var(--paper-3);border:1px solid var(--rule);
  border-radius:var(--radius);overflow:hidden;display:flex;align-items:center;justify-content:center}
.hero-cover img{width:100%;height:100%;object-fit:cover;display:block}
.hero-cover .ph{font-family:var(--mono);font-size:12px;color:var(--ink-3)}
/* completeness chips */
.comp{display:flex;align-items:center;gap:8px;margin-top:4px}
.comp-state{font-family:var(--ui);font-size:11px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;
  padding:4px 10px;border-radius:11px;border:1px solid var(--rule)}
.comp-complete{background:var(--ok-soft);color:var(--ok);border-color:var(--ok)}
.comp-near{background:var(--gold-soft);color:#7A5814;border-color:var(--gold)}
.comp-in-progress{background:var(--paper-3);color:var(--ink-3);border-color:var(--ink-3)}
.comp-scaffold{background:var(--paper);color:var(--ink-3);border:1px dashed var(--rule)}
.axes{display:inline-flex;gap:3px}
.ax{font-family:var(--mono);font-size:9.5px;font-weight:700;min-width:20px;text-align:center;padding:3px 4px;border-radius:3px;line-height:1}
.ax.on{background:var(--ok);color:#fff} .ax.off{background:var(--paper-3);color:var(--ink-3);border:1px solid var(--rule)}
.specstrip{max-width:1320px;margin:0 auto;padding:0 26px 22px;display:grid;
  grid-template-columns:repeat(6,1fr);border-top:1px solid var(--rule)}
@media(max-width:680px){.specstrip{grid-template-columns:repeat(3,1fr)}}
.spec{padding:13px 14px;border-right:1px solid var(--rule)} .spec:last-child{border-right:none}
.spec .k{font-family:var(--ui);font-size:10px;color:var(--ink-3);text-transform:uppercase;letter-spacing:.1em;font-weight:600;margin-bottom:5px}
.spec .v{font-family:var(--serif);font-size:18px;font-weight:500;color:var(--ink);line-height:1.1}
.app{max-width:1320px;margin:0 auto;display:grid;grid-template-columns:240px 1fr;gap:36px;padding:30px 26px 80px}
@media(max-width:980px){.app{grid-template-columns:1fr}}
.toc{position:sticky;top:78px;align-self:start;font-family:var(--ui);font-size:13px}
.toc a{display:block;color:var(--ink-3);padding:5px 10px;border-left:2px solid var(--rule);margin:1px 0}
.toc a:hover{color:var(--accent);border-left-color:var(--accent)}
.toc .toc-group{font-size:10px;text-transform:uppercase;letter-spacing:.1em;color:var(--cedar);font-weight:700;margin:14px 0 5px 10px}
section.card{background:var(--paper-2);border:1px solid var(--rule);border-radius:var(--radius);
  padding:24px 28px;margin:0 0 22px;box-shadow:var(--shadow);scroll-margin-top:78px}
section.card>h2{font-family:var(--serif);font-weight:600;font-size:23px;color:var(--ink);margin:0 0 4px;letter-spacing:-.01em}
section.card>.lede{color:var(--ink-3);margin:0 0 16px;font-size:13.5px}
section.card p{color:var(--ink-2)}
.mv-wrap,.wolfram-wrap{width:100%;aspect-ratio:16/10;border:1px solid var(--rule);border-radius:var(--radius);overflow:hidden;background:var(--paper-3)}
model-viewer{width:100%;height:100%;background:var(--paper-3)}
.wolfram-wrap iframe{width:100%;height:100%;border:0}
.gallery{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:10px}
.gallery a{display:block;border:1px solid var(--rule);border-radius:var(--radius);overflow:hidden;background:var(--paper-3)}
.gallery img{width:100%;height:150px;object-fit:cover;display:block;transition:transform .15s}
.gallery a:hover img{transform:scale(1.03)}
table.bom{width:100%;border-collapse:collapse;font-size:13px}
table.bom th,table.bom td{text-align:left;padding:7px 10px;border-bottom:1px solid var(--rule-soft)}
table.bom th{font-family:var(--ui);font-size:10.5px;text-transform:uppercase;letter-spacing:.06em;color:var(--ink-3);background:var(--paper-3)}
.gates{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:8px}
.gates li{display:flex;justify-content:space-between;gap:10px;padding:9px 12px;border:1px solid var(--rule);border-radius:var(--radius);background:var(--paper-3);font-size:13px}
.gates .gk{color:var(--ink-3)} .gates .gv{font-weight:600;color:var(--ink)}
.files{columns:2;font-family:var(--mono);font-size:12px;color:var(--ink-3)}
@media(max-width:680px){.files{columns:1}}
.empty-axis{padding:14px 16px;border:1px dashed var(--rule);border-radius:var(--radius);color:var(--ink-3);font-size:13px;background:var(--paper-3)}
footer.foot{max-width:1320px;margin:0 auto;padding:24px 26px 60px;color:var(--ink-3);font-size:12px;font-family:var(--ui)}
footer.foot a{color:var(--cedar)}
/* ----- in-page navigation ----- */
html{scroll-behavior:smooth}
.breadcrumb{font-family:var(--ui);font-size:12px;color:var(--ink-3);margin-bottom:14px;display:flex;gap:7px;align-items:center;flex-wrap:wrap}
.breadcrumb a{color:var(--cedar)} .breadcrumb a:hover{color:var(--accent)} .breadcrumb .sep{opacity:.45}
.toc a.active{color:var(--accent);border-left-color:var(--accent);background:var(--accent-soft);font-weight:600}
.pager{display:flex;justify-content:space-between;gap:14px;margin:4px 0 0}
.pager a{flex:1 1 0;min-width:0;padding:13px 16px;border:1px solid var(--rule);border-radius:var(--radius);
  background:var(--paper-2);color:var(--ink-2);box-shadow:var(--shadow)}
.pager a:hover{border-color:var(--cedar);color:var(--accent)}
.pager .prev:only-child{margin-right:auto;max-width:48%} .pager .next:only-child{margin-left:auto;max-width:48%}
.pager .dir{font-family:var(--ui);font-size:10px;text-transform:uppercase;letter-spacing:.1em;color:var(--ink-3);display:block;margin-bottom:3px}
.pager .nm{font-family:var(--serif);font-size:15px;font-weight:500;display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.pager .next{text-align:right}
.totop{position:fixed;right:22px;bottom:22px;width:42px;height:42px;border-radius:50%;
  background:var(--ink-2);color:var(--paper);border:none;cursor:pointer;font-size:18px;line-height:1;
  box-shadow:var(--shadow);opacity:0;pointer-events:none;transition:opacity .2s;z-index:40}
.totop.show{opacity:.92;pointer-events:auto} .totop:hover{background:var(--accent)}
</style>"""

THEME_SCRIPT = """<script>
(function(){
  var KEY='hz-theme';
  try{var s=localStorage.getItem(KEY); if(s) document.documentElement.setAttribute('data-theme',s);}catch(e){}
  var b=document.getElementById('theme-toggle');
  if(b) b.addEventListener('click',function(){
    var d=document.documentElement.getAttribute('data-theme')==='dark'?'':'dark';
    if(d) document.documentElement.setAttribute('data-theme','dark'); else document.documentElement.removeAttribute('data-theme');
    try{localStorage.setItem(KEY,d);}catch(e){}
  });
  document.querySelectorAll('img').forEach(function(im){im.addEventListener('error',function(){var w=this.closest('.hero-cover,.gallery a');if(w)w.style.display='none';});});
})();
</script>"""

NAV_SCRIPT = """<script>
(function(){
  var links=[].slice.call(document.querySelectorAll('.toc a')), map={};
  links.forEach(function(a){map[a.getAttribute('href').slice(1)]=a;});
  var secs=[].slice.call(document.querySelectorAll('main section[id]'));
  if('IntersectionObserver' in window && secs.length){
    var obs=new IntersectionObserver(function(es){
      es.forEach(function(e){ if(e.isIntersecting){
        links.forEach(function(l){l.classList.remove('active');});
        var a=map[e.target.id]; if(a) a.classList.add('active');
      }});
    },{rootMargin:'-40% 0px -55% 0px',threshold:0});
    secs.forEach(function(s){obs.observe(s);});
  }
  var t=document.getElementById('totop');
  if(t){
    window.addEventListener('scroll',function(){t.classList.toggle('show',window.scrollY>520);},{passive:true});
    t.addEventListener('click',function(){window.scrollTo({top:0,behavior:'smooth'});});
  }
})();
</script>"""


def _axis_chip(on: bool, label: str) -> str:
    return f'<b class="ax {"on" if on else "off"}">{label}</b>'


def render_explorer(d: ExplorerData, prev=None, nxt=None) -> str:
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    status_pill = f'<span class="pill pill-{esc(d.status)}">{esc(d.status_label)}</span>'
    comp = (
        f'<div class="comp" title="Explorer completeness (#31): W live Wolfram · I rendered images · 3D model-viewer">'
        f'<span class="comp-state comp-{d.comp_state}">{gl.COMPLETENESS_LABELS[d.comp_state]}</span>'
        f'<span class="axes">{_axis_chip(d.axis_w, "W")}{_axis_chip(d.axis_i, "I")}{_axis_chip(d.axis_3d, "3D")}</span>'
        f'</div>'
    )
    variants = f"{len(d.family_members)}" if d.family_members else "1"

    # ---- in-page navigation: breadcrumb + prev/next pager ----
    lib = "../../_meta/instrument-showcase/site/library.html"
    breadcrumb = (
        f'<nav class="breadcrumb"><a href="{lib}">Library</a>'
        f'<span class="sep">›</span><span>{esc(d.family_label)}</span>'
        f'<span class="sep">›</span><span>{esc(d.title)}</span></nav>'
    )

    def _pager_link(item, cls, dirlabel):
        if not item:
            return ''
        s, t = item
        return (f'<a class="{cls}" href="../{esc(s)}/explorer.html">'
                f'<span class="dir">{dirlabel}</span><span class="nm">{esc(t)}</span></a>')
    pager = ''
    if prev or nxt:
        pager = (f'<nav class="pager">{_pager_link(prev, "prev", "← Previous")}'
                 f'{_pager_link(nxt, "next", "Next →")}</nav>')

    # ---- sections (only those with data; build TOC alongside) ----
    toc: list[tuple[str, str, str]] = []  # (group, id, label)
    body: list[str] = []

    def add(group, sid, label, html):
        toc.append((group, sid, label))
        body.append(f'<section class="card" id="{sid}">{html}</section>')

    if d.overview:
        add("Project", "overview", "Overview",
            f'<h2>Overview</h2><div class="lede">From <code>design.md</code></div>{d.overview}')

    # 3D — completeness axis
    if d.glb_rel:
        add("Design", "cad", "3D Model",
            f'<h2>3D Model</h2><div class="lede">Interactive {esc(d.cad_kind)} — drag to orbit.</div>'
            f'<div class="mv-wrap"><model-viewer src="{esc(d.glb_rel)}" camera-controls auto-rotate '
            f'shadow-intensity="1" exposure="0.9" alt="{esc(d.title)} 3D model"></model-viewer></div>')

    # I — completeness axis
    if d.gallery:
        cells = "".join(
            f'<a href="{esc(g)}" target="_blank" rel="noopener"><img src="{esc(g)}" loading="lazy" alt=""></a>'
            for g in d.gallery)
        add("Design", "gallery", "Gallery",
            f'<h2>Concept &amp; Render Gallery</h2><div class="lede">{len(d.gallery)} rendered images from <code>images/</code></div>'
            f'<div class="gallery">{cells}</div>')

    if d.bom_rows:
        thead = "".join(f"<th>{esc(c)}</th>" for c in d.bom_header)
        trows = "".join("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in r) + "</tr>" for r in d.bom_rows)
        add("Build", "bom", "Bill of Materials",
            f'<h2>Bill of Materials</h2><div class="lede">From <code>bom.csv</code> (first {len(d.bom_rows)} rows)</div>'
            f'<table class="bom"><thead><tr>{thead}</tr></thead><tbody>{trows}</tbody></table>')

    # W — completeness axis
    if d.wolfram_url:
        add("Validate", "wolfram", "Run It · Wolfram",
            f'<h2>Run It — Wolfram Cloud</h2><div class="lede">Live Public-Execute acoustic model.</div>'
            f'<div class="wolfram-wrap"><iframe src="{esc(d.wolfram_url)}" loading="lazy" '
            f'title="{esc(d.title)} Wolfram model"></iframe></div>'
            f'<p style="margin-top:10px"><a href="{esc(d.wolfram_url)}" target="_blank" rel="noopener">Open notebook ↗</a></p>')

    if d.gates:
        items = "".join(f'<li><span class="gk">{esc(k)}</span><span class="gv">{esc(v)}</span></li>' for k, v in d.gates)
        add("Validate", "validation", "Release Gates",
            f'<h2>Release Gates</h2><div class="lede">From <code>capstone-manifest.json</code></div><ul class="gates">{items}</ul>')

    if d.artifacts:
        files = "".join(f'<div>{esc(a)}</div>' for a in d.artifacts)
        add("Project", "files", "Artifacts",
            f'<h2>Artifacts</h2><div class="lede">{len(d.artifacts)} files in this packet</div><div class="files">{files}</div>')

    if d.has_wiki:
        wiki_url = f"../../_meta/instrument-showcase/wiki/instruments/{esc(d.slug)}.md"
        add("Project", "wiki", "Engineering Wiki",
            f'<h2>Engineering Wiki</h2><p>This instrument has a cross-linked engineering memory page — sources, '
            f'open questions, and acoustic-class patterns. <a href="{wiki_url}">Open the wiki page ↗</a></p>')

    # Missing-axis nudges so a "Near" explorer shows what it needs to be Complete.
    missing = []
    if not d.axis_w: missing.append("a live Wolfram model (W)")
    if not d.axis_i: missing.append("rendered concept images (I)")
    if not d.axis_3d: missing.append("a 3D model-viewer (3D)")
    if missing and d.comp_state != "complete":
        body.append(
            f'<section class="card" id="next"><h2>To reach Complete</h2>'
            f'<div class="empty-axis">This explorer is <b>{gl.COMPLETENESS_LABELS[d.comp_state]}</b>. '
            f'Add {", ".join(missing)} to complete the {esc(d.family_label)} family tracker (#31).</div></section>')
        toc.append(("Validate", "next", "To reach Complete"))

    # ---- TOC ----
    toc_html = []
    last_group = None
    for group, sid, label in toc:
        if group != last_group:
            toc_html.append(f'<div class="toc-group">{esc(group)}</div>')
            last_group = group
        toc_html.append(f'<a href="#{sid}">{esc(label)}</a>')
    toc_block = "\n".join(toc_html)

    # ---- spec strip ----
    specs = [
        ("Family", d.family_label), ("Acoustic class", d.acoustic_class or "—"),
        ("Status", d.status_label), ("Variants", variants),
        ("Wolfram", d.wolfram_state), ("CAD", d.cad_kind),
    ]
    spec_html = "".join(f'<div class="spec"><div class="k">{esc(k)}</div><div class="v">{esc(v)}</div></div>' for k, v in specs)

    hero_cover = (
        f'<div class="hero-cover"><img src="{esc(d.hero_rel)}" alt="{esc(d.title)}"></div>'
        if d.hero_rel else
        '<div class="hero-cover"><span class="ph">no hero render yet</span></div>'
    )

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(d.title)} · Studio Explorer · Heifer Zephyr</title>
<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
{EXPLORER_CSS}
</head>
<body>
<header class="appbar">
  <div class="brand">
    <span class="dot"></span>
    <a class="wordmark" href="../../_meta/instrument-showcase/site/library.html" title="Back to the library"><em>Heifer Zephyr</em></a>
    <span class="instrument-tag">{esc(d.title)}</span>
  </div>
  <nav class="appnav">
    <a href="../../_meta/instrument-showcase/site/library.html">Library</a>
    <a href="../../_meta/instrument-showcase/site/index.html">Deliverables</a>
    <a href="../../_meta/instrument-showcase/site/manifest.html">Manifest</a>
    <a href="https://github.com/tonykoop" target="_blank" rel="noopener">GitHub</a>
  </nav>
  <div class="appbar-tools">
    <button class="icon-btn" id="theme-toggle" title="Toggle light / dark">◐ Theme</button>
  </div>
</header>

<section class="hero">
  <div class="hero-inner">
    <div class="hero-text">
      {breadcrumb}
      <span class="eyebrow">{esc(d.family_label)} · {esc(d.acoustic_class or "instrument")}</span>
      <h1>{esc(d.title)}</h1>
      <div class="meta-line">
        {status_pill}
        <span class="pill pill-fam">{esc(d.slug)}</span>
      </div>
      {comp}
      <p>{esc(d.instrument)} — studio explorer generated from the build packet: 3D model, render gallery, live Wolfram acoustic model, bill of materials, and release gates, where each is present.</p>
    </div>
    {hero_cover}
  </div>
  <div class="specstrip">{spec_html}</div>
</section>

<div class="app">
  <nav class="toc">{toc_block}</nav>
  <main>
{chr(10).join(body)}
    {pager}
  </main>
</div>

<button class="totop" id="totop" title="Back to top" aria-label="Back to top">↑</button>

<footer class="foot">
  Generated <time>{generated_at}</time> by <code>generate_explorer_v2.py</code> from this repo's build packet.
  <a href="../../_meta/instrument-showcase/site/library.html">← Back to the Studio Explorers Library</a>
</footer>
{THEME_SCRIPT}
{NAV_SCRIPT}
</body>
</html>
"""


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def _iter_repos(workspace: Path):
    root = workspace / "instruments"
    for family_dir in gl.INSTRUMENT_FAMILY_DIRS:
        fam_root = root / family_dir
        if not fam_root.is_dir():
            continue
        for repo in sorted(fam_root.iterdir()):
            if repo.is_dir() and ((repo / "capstone-manifest.json").exists() or (repo / "explorer.html").exists()):
                yield family_dir, repo


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Generate per-instrument Explorer v2 pages")
    p.add_argument("--workspace", type=Path, default=gl.DEFAULT_WORKSPACE)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--slug", help="Generate for a single instrument slug")
    g.add_argument("--repo", type=Path, help="Generate for a single repo path")
    g.add_argument("--all", action="store_true", help="Generate for every instrument repo")
    p.add_argument("--write-explorer", action="store_true",
                   help="Write explorer.html (default writes explorer.generated.html)")
    p.add_argument("--force", action="store_true",
                   help="With --write-explorer, overwrite an existing explorer.html")
    p.add_argument("--only-scaffold", action="store_true",
                   help="With --all, only (re)write repos whose explorer is scaffold/missing")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args(argv)

    embed_index = gl.load_embed_urls(args.workspace)

    # Build the work list
    targets: list[tuple[str, Path]] = []
    if args.all:
        targets = list(_iter_repos(args.workspace))
    else:
        if args.slug:
            match = [(fd, r) for fd, r in _iter_repos(args.workspace) if r.name == args.slug]
            if not match:
                print(f"slug not found: {args.slug}", file=sys.stderr)
                return 2
            targets = match
        else:
            repo = args.repo.resolve()
            targets = [(repo.parent.name, repo)]

    # Per-family ordering (by title) for prev/next paging.
    def _title_of(repo: Path) -> str:
        mp = repo / "capstone-manifest.json"
        if mp.exists():
            try:
                m = json.loads(mp.read_text(encoding="utf-8"))
                return m.get("title") or m.get("instrument") or repo.name.replace("-", " ").title()
            except json.JSONDecodeError:
                pass
        return repo.name.replace("-", " ").title()

    fam_repos: dict[str, list[Path]] = {}
    for fd, r in _iter_repos(args.workspace):
        fam_repos.setdefault(fd, []).append(r)
    fam_order: dict[str, list[tuple[str, str]]] = {
        fd: [(r.name, _title_of(r)) for r in sorted(rs, key=lambda r: _title_of(r).lower())]
        for fd, rs in fam_repos.items()
    }

    written = skipped = 0
    for family_dir, repo in targets:
        d = gather(repo, family_dir, embed_index)
        order = fam_order.get(family_dir, [])
        idx = next((i for i, (s, _) in enumerate(order) if s == repo.name), -1)
        prev = order[idx - 1] if idx > 0 else None
        nxt = order[idx + 1] if 0 <= idx < len(order) - 1 else None

        if args.only_scaffold and d.comp_state not in ("scaffold", "in-progress"):
            skipped += 1
            continue

        out_name = "explorer.html" if args.write_explorer else "explorer.generated.html"
        out = repo / out_name
        if out_name == "explorer.html" and out.exists() and not args.force:
            # Never clobber an existing authored explorer without --force.
            out = repo / "explorer.generated.html"
            note = " (explorer.html exists; wrote .generated instead — use --force to overwrite)"
        else:
            note = ""

        html = render_explorer(d, prev=prev, nxt=nxt)
        if args.dry_run:
            print(f"DRY {repo.name}: {d.comp_state} (W{int(d.axis_w)} I{int(d.axis_i)} 3D{int(d.axis_3d)}) -> {out.name}{note}")
        else:
            out.write_text(html, encoding="utf-8")
            print(f"wrote {out.relative_to(args.workspace)}  [{d.comp_state}]{note}")
        written += 1

    print(f"\n{written} explorer(s) {'previewed' if args.dry_run else 'written'}, {skipped} skipped")
    return 0


if __name__ == "__main__":
    sys.exit(main())
