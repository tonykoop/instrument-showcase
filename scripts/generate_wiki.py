#!/usr/bin/env python3
"""Generate site/wiki.html — a browsable Heifer Zephyr brand-styled view of the wiki.

Walks wiki/**/*.md, parses YAML frontmatter (best-effort, no PyYAML required),
renders markdown to HTML (minimal in-house renderer, no external deps),
resolves [[wikilinks]] to page anchors, and ships a single self-contained HTML file
with sidebar nav, search, filter by wiki_type/status, and per-page rendered content.

Usage:
  python3 scripts/generate_wiki.py                 # default paths
  python3 scripts/generate_wiki.py --wiki PATH     # override wiki root
  python3 scripts/generate_wiki.py --output PATH   # override site/wiki.html
"""

from __future__ import annotations

import argparse
import html as _html
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SHOWCASE_DIR = SCRIPT_DIR.parent
DEFAULT_WIKI = SHOWCASE_DIR / "wiki"
DEFAULT_OUTPUT = SHOWCASE_DIR / "site" / "wiki.html"

# ---------- minimal YAML frontmatter parser ----------

_FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    m = _FM_RE.match(text)
    if not m:
        return {}, text
    fm_raw = m.group(1)
    body = text[m.end():]
    data: dict = {}
    current_key: str | None = None
    current_list: list | None = None
    for line in fm_raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - "):
            # list item under current_key
            val = line[4:].strip()
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            if current_list is None:
                current_list = []
                data[current_key] = current_list  # type: ignore[index]
            # try to parse inline dict like "path: foo, kind: repo"
            if ":" in val and not val.startswith("/"):
                # treat as dict only if it doesn't look like a path
                pass
            current_list.append(val)
        elif line.startswith("    "):
            # nested key under list item — flatten by appending "key: value" to last item
            if current_list and current_list:
                last = current_list[-1]
                if isinstance(last, str):
                    current_list[-1] = last + " · " + line.strip()
        elif ":" in line and not line.startswith(" "):
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()
            if not val:
                # opens a list or dict block
                current_key = key
                current_list = None
                data[key] = []
                continue
            if val.startswith("[") and val.endswith("]"):
                inner = val[1:-1].strip()
                items = [x.strip().strip('"').strip("'") for x in inner.split(",") if x.strip()]
                data[key] = items
            elif val.startswith('"') and val.endswith('"'):
                data[key] = val[1:-1]
            else:
                data[key] = val
            current_key = None
            current_list = None
    return data, body


# ---------- minimal markdown → HTML renderer ----------

_WIKILINK_RE = re.compile(r"\[\[([^\]\|]+)(?:\|([^\]]+))?\]\]")
_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_INLINE_CODE_RE = re.compile(r"`([^`]+)`")
_BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
_ITALIC_RE = re.compile(r"(?<!\*)\*([^*]+)\*(?!\*)")


def slugify(s: str) -> str:
    return re.sub(r"[^a-z0-9-]+", "-", s.lower()).strip("-")


def render_inline(s: str, page_index: dict[str, str]) -> str:
    s = _html.escape(s, quote=False)
    # Restore backticks for inline code
    s = _INLINE_CODE_RE.sub(lambda m: f"<code>{m.group(1)}</code>", s)

    def _wikilink(m: re.Match) -> str:
        target = m.group(1).strip()
        label = (m.group(2) or target).strip()
        anchor = page_index.get(target.replace(".md", ""), "")
        if anchor:
            return f'<a class="wikilink" href="#{anchor}">{label}</a>'
        return f'<a class="wikilink broken" href="#" title="No page found for {target}">{label}</a>'

    s = _WIKILINK_RE.sub(_wikilink, s)
    s = _LINK_RE.sub(lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', s)
    s = _BOLD_RE.sub(lambda m: f"<strong>{m.group(1)}</strong>", s)
    s = _ITALIC_RE.sub(lambda m: f"<em>{m.group(1)}</em>", s)
    return s


def render_markdown(body: str, page_index: dict[str, str]) -> str:
    lines = body.splitlines()
    out: list[str] = []
    i = 0
    in_code = False
    code_buf: list[str] = []
    list_stack: list[str] = []  # "ul" or "ol"

    def close_lists():
        while list_stack:
            out.append(f"</{list_stack.pop()}>")

    while i < len(lines):
        line = lines[i]
        # fenced code
        if line.startswith("```"):
            if in_code:
                out.append("<pre><code>" + _html.escape("\n".join(code_buf)) + "</code></pre>")
                code_buf = []
                in_code = False
            else:
                close_lists()
                in_code = True
            i += 1
            continue
        if in_code:
            code_buf.append(line)
            i += 1
            continue
        # heading
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            close_lists()
            level = len(m.group(1))
            text = render_inline(m.group(2).strip(), page_index)
            anchor = slugify(m.group(2).strip())
            out.append(f'<h{level} id="{anchor}">{text}</h{level}>')
            i += 1
            continue
        # blockquote
        if line.startswith("> "):
            close_lists()
            out.append(f"<blockquote>{render_inline(line[2:], page_index)}</blockquote>")
            i += 1
            continue
        # unordered list
        m = re.match(r"^(\s*)-\s+(.*)$", line)
        if m:
            if not list_stack or list_stack[-1] != "ul":
                close_lists()
                out.append("<ul>")
                list_stack.append("ul")
            out.append(f"<li>{render_inline(m.group(2), page_index)}</li>")
            i += 1
            continue
        # ordered list
        m = re.match(r"^\s*\d+\.\s+(.*)$", line)
        if m:
            if not list_stack or list_stack[-1] != "ol":
                close_lists()
                out.append("<ol>")
                list_stack.append("ol")
            out.append(f"<li>{render_inline(m.group(1), page_index)}</li>")
            i += 1
            continue
        # blank
        if not line.strip():
            close_lists()
            i += 1
            continue
        # paragraph
        close_lists()
        # collect contiguous non-empty, non-special lines into one paragraph
        para_lines = [line]
        j = i + 1
        while j < len(lines):
            nxt = lines[j]
            if (not nxt.strip()
                    or nxt.startswith("#")
                    or nxt.startswith("```")
                    or nxt.startswith("> ")
                    or re.match(r"^\s*-\s+", nxt)
                    or re.match(r"^\s*\d+\.\s+", nxt)):
                break
            para_lines.append(nxt)
            j += 1
        para = " ".join(l.strip() for l in para_lines)
        out.append(f"<p>{render_inline(para, page_index)}</p>")
        i = j
    close_lists()
    return "\n".join(out)


# ---------- wiki walk ----------

def collect_pages(wiki_root: Path) -> list[dict]:
    pages: list[dict] = []
    if not wiki_root.exists():
        return pages
    for md in sorted(wiki_root.rglob("*.md")):
        rel = md.relative_to(wiki_root).as_posix()
        if rel.startswith("."):
            continue
        text = md.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        # derive defaults
        rel_no_ext = rel[:-3] if rel.endswith(".md") else rel
        page_type = fm.get("wiki_type") or rel.split("/")[0] if "/" in rel else "index"
        if rel_no_ext in ("index", "log", "AGENTS"):
            page_type = fm.get("wiki_type") or rel_no_ext
        status = fm.get("status") or ("active" if rel_no_ext in ("index", "log", "AGENTS") else "stub")
        title = fm.get("title") or rel_no_ext.split("/")[-1].replace("-", " ").title()
        # counts
        sources = fm.get("sources") or []
        oqs = fm.get("open_questions") or []
        source_count = len(sources) if isinstance(sources, list) else int(sources or 0)
        oq_count = len(oqs) if isinstance(oqs, list) else int(oqs or 0)
        pages.append({
            "rel": rel,
            "rel_no_ext": rel_no_ext,
            "slug": rel_no_ext.replace("/", "__"),
            "title": title,
            "wiki_type": page_type,
            "status": status,
            "last_updated": fm.get("last_updated") or fm.get("last_ingest") or "",
            "tags": fm.get("tags") or [],
            "crosslinks": fm.get("crosslinks") or [],
            "source_count": source_count,
            "open_questions": oq_count,
            "body": body,
            "fm": fm,
        })
    return pages


# ---------- HTML emit ----------

TYPE_LABELS = {
    "index": "Index",
    "log": "Log",
    "AGENTS": "Agent Guide",
    "instrument": "Instrument",
    "instruments": "Instrument",
    "acoustic-class": "Acoustic Class",
    "acoustic-classes": "Acoustic Class",
    "fabrication": "Fabrication",
    "material": "Material",
    "materials": "Material",
    "synthesis": "Synthesis",
    "source-distillation": "Source",
    "sources": "Source",
}

STATUS_STYLE = {
    "active": ("var(--ok)", "Active"),
    "stub": ("var(--muted)", "Stub"),
    "review-needed": ("var(--warn)", "Review"),
    "stale": ("var(--warn)", "Stale"),
    "missing": ("var(--block)", "Missing"),
}


def build_html(pages: list[dict], generated_at: str) -> str:
    # page index for wikilink resolution
    page_index = {p["rel_no_ext"]: p["slug"] for p in pages}
    # also accept short forms like "instruments/kora" → "instruments__kora"
    for p in pages:
        # alt key without folder, e.g. "kora"
        leaf = p["rel_no_ext"].split("/")[-1]
        page_index.setdefault(leaf, p["slug"])

    # group by type
    groups: dict[str, list[dict]] = {}
    for p in pages:
        t = p["wiki_type"]
        groups.setdefault(t, []).append(p)

    # sidebar
    nav_html_parts: list[str] = []
    type_order = ["index", "synthesis", "instrument", "instruments",
                  "acoustic-class", "acoustic-classes",
                  "fabrication", "material", "materials",
                  "source-distillation", "sources", "log", "AGENTS"]
    seen_types = set()
    for t in type_order + sorted(groups.keys()):
        if t in seen_types or t not in groups:
            continue
        seen_types.add(t)
        nav_html_parts.append(
            f'<div class="nav-group" data-type="{_html.escape(t)}"><div class="nav-label">{_html.escape(TYPE_LABELS.get(t, t.title()))}</div>'
        )
        for p in sorted(groups[t], key=lambda x: x["title"].lower()):
            color, lbl = STATUS_STYLE.get(p["status"], ("var(--muted)", p["status"]))
            nav_html_parts.append(
                f'<a class="nav-item" data-slug="{p["slug"]}" data-status="{_html.escape(p["status"])}" '
                f'data-search="{_html.escape((p["title"] + " " + " ".join(p["tags"])).lower())}" '
                f'href="#{p["slug"]}">'
                f'<span class="nav-title">{_html.escape(p["title"])}</span>'
                f'<span class="nav-meta"><span class="dot" style="background:{color}"></span>'
                f'{p["source_count"]}s · {p["open_questions"]}q</span></a>'
            )
        nav_html_parts.append("</div>")
    nav_html = "\n".join(nav_html_parts)

    # content
    content_parts: list[str] = []
    for p in pages:
        rendered = render_markdown(p["body"], page_index)
        color, lbl = STATUS_STYLE.get(p["status"], ("var(--muted)", p["status"]))
        tags_html = "".join(
            f'<span class="tag">{_html.escape(t)}</span>' for t in (p["tags"] or [])
        )
        meta_pills = (
            f'<span class="pill"><span class="dot" style="background:{color}"></span>{_html.escape(lbl)}</span>'
            f'<span class="pill mono">{p["source_count"]} sources</span>'
            f'<span class="pill mono">{p["open_questions"]} open questions</span>'
        )
        if p["last_updated"]:
            meta_pills += f'<span class="pill mono">updated {_html.escape(p["last_updated"])}</span>'
        content_parts.append(
            f'<article class="page" id="{p["slug"]}" data-type="{_html.escape(p["wiki_type"])}" data-status="{_html.escape(p["status"])}">'
            f'<header class="page-head"><div class="eyebrow">{_html.escape(TYPE_LABELS.get(p["wiki_type"], p["wiki_type"]))}'
            f' · <code>{_html.escape(p["rel"])}</code></div>'
            f'<h1>{_html.escape(p["title"])}</h1>'
            f'<div class="meta">{meta_pills}</div>'
            f'<div class="tags">{tags_html}</div></header>'
            f'<div class="page-body">{rendered}</div></article>'
        )
    content_html = "\n".join(content_parts)

    total = len(pages)
    active = sum(1 for p in pages if p["status"] == "active")
    sources_total = sum(p["source_count"] for p in pages)
    questions_total = sum(p["open_questions"] for p in pages)

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Heifer Zephyr · Instrument Wiki</title>
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
  font-family:var(--ui);font-size:15px;line-height:1.55;-webkit-font-smoothing:antialiased}}
a{{color:var(--lapis);text-decoration:none}}
a:hover{{text-decoration:underline}}
code{{font-family:var(--mono);font-size:0.88em;background:#FFFCF5;padding:1px 4px;border-radius:3px;border:1px solid var(--rule)}}
pre{{background:#FFFCF5;border:1px solid var(--rule);border-radius:5px;padding:12px 14px;overflow-x:auto;font-family:var(--mono);font-size:13px;line-height:1.5}}
pre code{{background:transparent;border:0;padding:0}}

.app-bar{{position:sticky;top:0;z-index:30;height:56px;
  background:var(--walnut);color:var(--cream);
  border-bottom:3px solid var(--gold);
  display:flex;align-items:center;gap:24px;padding:0 22px}}
.wordmark em{{font-family:var(--italic-serif);font-style:italic;
  font-size:22px;color:var(--gold);letter-spacing:0.01em}}
.tagline{{font-family:var(--serif);font-size:15px;color:var(--cream);
  border-left:1px solid rgba(248,244,233,0.3);padding-left:14px}}
.actions{{margin-left:auto;display:flex;align-items:center;gap:12px}}
.action-btn{{display:inline-block;font-family:var(--ui);font-size:12px;
  letter-spacing:0.04em;text-transform:uppercase;color:var(--cream);
  border:1px solid rgba(248,244,233,0.35);border-radius:3px;padding:6px 10px}}
.action-btn:hover{{background:rgba(248,244,233,0.12);text-decoration:none;color:var(--gold)}}

.shell{{display:grid;grid-template-columns:280px 1fr;min-height:calc(100vh - 56px)}}
.sidebar{{background:var(--paper);border-right:1px solid var(--rule);
  height:calc(100vh - 56px);overflow-y:auto;position:sticky;top:56px;padding:18px 16px 60px}}
.search{{width:100%;padding:8px 12px;font-family:var(--ui);font-size:13px;
  border:1px solid var(--rule);border-radius:4px;background:#FFFCF5;margin-bottom:10px}}
.search:focus{{outline:none;border-color:var(--lapis)}}
.filter-row{{display:flex;gap:5px;flex-wrap:wrap;margin-bottom:14px}}
.filter-btn{{font-family:var(--ui);font-size:11px;background:var(--cream);
  color:var(--walnut);border:1px solid var(--rule);border-radius:12px;
  padding:3px 9px;cursor:pointer;letter-spacing:0.02em}}
.filter-btn.active{{background:var(--walnut);color:var(--cream);border-color:var(--walnut)}}
.nav-group{{margin-bottom:18px}}
.nav-label{{font-family:var(--ui);font-size:10px;color:var(--muted);
  text-transform:uppercase;letter-spacing:0.12em;margin-bottom:6px;padding-bottom:4px;
  border-bottom:1px solid var(--rule)}}
.nav-item{{display:flex;justify-content:space-between;gap:8px;padding:5px 6px;
  border-radius:3px;color:var(--ink);font-size:13px}}
.nav-item:hover{{background:var(--hover);text-decoration:none}}
.nav-item.active{{background:var(--cream);border-left:2px solid var(--gold);padding-left:8px}}
.nav-title{{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}
.nav-meta{{font-family:var(--mono);font-size:10px;color:var(--muted);display:flex;align-items:center;gap:5px;flex:0 0 auto}}
.dot{{width:8px;height:8px;border-radius:50%;display:inline-block}}

.main{{padding:28px 36px 80px;max-width:980px}}
.hero{{margin-bottom:22px}}
.hero h1{{font-family:var(--serif);font-weight:600;font-size:32px;color:var(--walnut);margin:0 0 6px;letter-spacing:-0.005em}}
.hero h1 .eyebrow{{display:block;font-family:var(--ui);font-weight:500;
  font-size:11px;color:var(--lapis);text-transform:uppercase;letter-spacing:0.16em;margin-bottom:6px}}
.hero p{{color:var(--muted);font-size:14px;max-width:760px}}
.stats{{display:flex;gap:10px;margin:14px 0 22px;flex-wrap:wrap}}
.stat{{background:var(--paper);border:1px solid var(--rule);border-radius:5px;padding:10px 16px;min-width:130px}}
.stat .k{{font-family:var(--ui);font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:0.06em;margin-bottom:3px}}
.stat .v{{font-family:var(--serif);font-size:22px;color:var(--walnut);font-weight:600;line-height:1.1}}

.page{{background:var(--paper);border:1px solid var(--rule);border-radius:5px;
  padding:28px 32px;margin-bottom:26px;scroll-margin-top:72px}}
.page.hidden{{display:none}}
.page-head{{margin-bottom:18px;padding-bottom:14px;border-bottom:1px solid var(--rule)}}
.page-head .eyebrow{{font-family:var(--ui);font-size:11px;color:var(--lapis);
  text-transform:uppercase;letter-spacing:0.14em;margin-bottom:5px}}
.page-head h1{{font-family:var(--serif);font-weight:600;font-size:26px;color:var(--walnut);margin:0 0 10px}}
.meta{{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:6px}}
.pill{{display:inline-flex;align-items:center;gap:5px;background:var(--cream);
  border:1px solid var(--rule);border-radius:11px;padding:2px 9px;font-size:11px;color:var(--ink);font-family:var(--ui)}}
.pill.mono{{font-family:var(--mono)}}
.tags{{display:flex;gap:5px;flex-wrap:wrap;margin-top:4px}}
.tag{{font-family:var(--mono);font-size:10px;color:var(--muted);background:#FFFCF5;border:1px solid var(--rule);border-radius:3px;padding:1px 6px}}

.page-body h1,.page-body h2,.page-body h3,.page-body h4{{font-family:var(--serif);color:var(--walnut);font-weight:600;letter-spacing:-0.005em;margin:1.6em 0 0.5em}}
.page-body h1{{display:none}} /* duplicate of page-head title */
.page-body h2{{font-size:20px;border-bottom:1px solid var(--rule);padding-bottom:5px}}
.page-body h3{{font-size:17px}}
.page-body ul,.page-body ol{{padding-left:22px}}
.page-body li{{margin:4px 0}}
.page-body blockquote{{border-left:3px solid var(--gold);padding:6px 14px;margin:14px 0;background:#FFFCF5;color:var(--muted);font-family:var(--serif);font-style:italic}}
.wikilink{{color:var(--lapis);border-bottom:1px dashed var(--lapis)}}
.wikilink.broken{{color:var(--block);border-bottom-style:dotted}}
.wikilink:hover{{background:#FFFCF5;text-decoration:none}}
</style>
</head>
<body>
<header class="app-bar">
  <div class="brand">
    <div class="wordmark"><em>Heifer Zephyr</em></div>
    <div class="tagline">Instrument Wiki</div>
  </div>
  <div class="actions">
    <a class="action-btn" href="./library.html">Library</a>
    <a class="action-btn" href="../portfolio.html">Portfolio</a>
  </div>
</header>

<div class="shell">
  <aside class="sidebar">
    <input class="search" id="search" placeholder="Search wiki…" autocomplete="off">
    <div class="filter-row" id="status-filters">
      <button class="filter-btn active" data-status="all">All</button>
      <button class="filter-btn" data-status="active">Active</button>
      <button class="filter-btn" data-status="stub">Stub</button>
      <button class="filter-btn" data-status="review-needed">Review</button>
      <button class="filter-btn" data-status="stale">Stale</button>
    </div>
    {nav_html}
  </aside>

  <main class="main">
    <div class="hero">
      <h1><span class="eyebrow">Knowledge Layer</span>Instrument Wiki</h1>
      <p>Living, cross-linked engineering memory for the Heifer Zephyr instrument design library. Browse pages by type at left, click <span class="pill">wikilinks</span> to jump between pages, and search across titles and tags. Edit in Obsidian; regenerate this view with <code>python3 scripts/generate_wiki.py</code>.</p>
    </div>
    <div class="stats">
      <div class="stat"><div class="k">Pages</div><div class="v">{total}</div></div>
      <div class="stat"><div class="k">Active</div><div class="v">{active}</div></div>
      <div class="stat"><div class="k">Sources cited</div><div class="v">{sources_total}</div></div>
      <div class="stat"><div class="k">Open questions</div><div class="v">{questions_total}</div></div>
      <div class="stat"><div class="k">Generated</div><div class="v" style="font-size:13px;font-family:var(--mono)">{generated_at}</div></div>
    </div>
    {content_html}
  </main>
</div>

<script>
(function(){{
  const search = document.getElementById('search');
  const items = Array.from(document.querySelectorAll('.nav-item'));
  const pages = Array.from(document.querySelectorAll('.page'));
  const filters = Array.from(document.querySelectorAll('#status-filters .filter-btn'));
  let activeStatus = 'all';

  function apply(){{
    const q = search.value.trim().toLowerCase();
    items.forEach(it => {{
      const matchQ = !q || it.dataset.search.includes(q);
      const matchS = activeStatus === 'all' || it.dataset.status === activeStatus;
      it.style.display = (matchQ && matchS) ? 'flex' : 'none';
    }});
    pages.forEach(pg => {{
      const slug = pg.id;
      const navItem = items.find(it => it.dataset.slug === slug);
      const visible = navItem && navItem.style.display !== 'none';
      pg.classList.toggle('hidden', !visible);
    }});
  }}
  search.addEventListener('input', apply);
  filters.forEach(b => b.addEventListener('click', () => {{
    filters.forEach(x => x.classList.remove('active'));
    b.classList.add('active');
    activeStatus = b.dataset.status;
    apply();
  }}));

  // Highlight active nav item on scroll
  const observer = new IntersectionObserver((entries) => {{
    entries.forEach(e => {{
      if (e.isIntersecting) {{
        const slug = e.target.id;
        items.forEach(it => it.classList.toggle('active', it.dataset.slug === slug));
      }}
    }});
  }}, {{rootMargin: '-30% 0px -60% 0px'}});
  pages.forEach(p => observer.observe(p));
}})();
</script>
</body>
</html>
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--wiki", type=Path, default=DEFAULT_WIKI)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args(argv)
    pages = collect_pages(args.wiki)
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    html_out = build_html(pages, generated_at)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(html_out, encoding="utf-8")
    print(f"Wrote {args.output} with {len(pages)} pages.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
