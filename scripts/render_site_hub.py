#!/usr/bin/env python3
"""Render a static deliverables hub from the manifest seed."""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
from collections import Counter
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
CANONICAL_REPO_NAME = "instrument-showcase"
DEFAULT_MANIFEST = REPO_ROOT / "data" / "deliverables-manifest.json"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "site"
SITE_SOURCE_CSS = REPO_ROOT / "site-src" / "hub.css"

FAMILY_ACCENT_RULES = [
    (re.compile(r"drum|idiophone|percuss|tongue|bell|pan|marimba|xylo|glock", re.I),
     "hz-family-percussion"),
    (re.compile(r"flute|whistle|pipe|kena|fujara|shakuh|duduk|chalumeau|gemshorn|ocarin|didger|clarinet|sheng|hulusi", re.I),
     "hz-family-winds"),
    (re.compile(r"violin|guitar|kora|ngoni|lute|oud|harp|ukulele|lyre|guzheng|pipa|konghou|erhu", re.I),
     "hz-family-strings"),
    (re.compile(r"electric|midi|synth|electron", re.I),
     "hz-family-electronic"),
]


def discover_workspace_root() -> Path:
    candidates = [
        Path.cwd(),
        REPO_ROOT.parent,
        Path("/mnt/c/Users/Tony/Documents/GitHub"),
        Path.home() / "Documents" / "GitHub",
    ]
    for candidate in candidates:
        if (candidate / "docs" / "plans").exists() and (candidate / "instrument-showcase").exists():
            return candidate.resolve()
    return REPO_ROOT.parent.resolve()


WORKSPACE_ROOT = discover_workspace_root()
CANONICAL_REPO_ROOT = (
    (WORKSPACE_ROOT / CANONICAL_REPO_NAME).resolve()
    if (WORKSPACE_ROOT / CANONICAL_REPO_NAME).exists()
    else REPO_ROOT
)


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "item"


def titleize_slug(slug: str) -> str:
    return slug.replace("-", " ").title()


def is_external_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"}


def derive_family_accent(*parts: str) -> str:
    haystack = " ".join(parts)
    for pattern, css_class in FAMILY_ACCENT_RULES:
        if pattern.search(haystack):
            return css_class
    return "hz-family-percussion"


def normalize_label(value: str | None, fallback: str) -> str:
    if not value:
        return fallback
    return value.replace("_", "-")


def runtime_label_for_item(item: dict[str, Any]) -> str:
    explicit = item.get("runtime_label")
    if explicit:
        return str(explicit)
    artifact_types = {str(kind).lower() for kind in item.get("artifact_types", [])}
    if "wolfram" in artifact_types:
        return "manifest-unset"
    return "not-applicable"


def resolve_reference(raw_value: str | None, manifest_path: Path) -> str | Path | None:
    if not raw_value:
        return None
    if is_external_url(raw_value):
        return raw_value
    if raw_value.startswith("/"):
        return WORKSPACE_ROOT / raw_value.lstrip("/")
    return (CANONICAL_REPO_ROOT / raw_value).resolve()


def href_for_page(target: str | Path | None, page_dir: Path) -> str | None:
    if target is None:
        return None
    if isinstance(target, str):
        return target
    return Path(shutil.os.path.relpath(target, page_dir)).as_posix()


def escaped_json(data: Any) -> str:
    return html.escape(json.dumps(data, indent=2, ensure_ascii=True))


def badge(label: str, tone: str) -> str:
    return (
        f'<span class="hub-badge hub-badge-{slugify(tone)}">'
        f"{html.escape(label)}"
        "</span>"
    )


def render_stat_cards(counter: Counter[str], label: str) -> str:
    cards = []
    for key, count in sorted(counter.items()):
        cards.append(
            '<article class="hub-stat-card">'
            f'<p class="hub-stat-label">{html.escape(label)}</p>'
            f'<h3>{html.escape(key)}</h3>'
            f'<p class="hub-stat-value">{count}</p>'
            "</article>"
        )
    return "\n".join(cards)


def page_shell(title: str, body: str, page_dir: Path, output_dir: Path) -> str:
    css_href = Path(shutil.os.path.relpath(output_dir / "assets" / "hub.css", page_dir)).as_posix()
    home_href = Path(shutil.os.path.relpath(output_dir / "index.html", page_dir)).as_posix()
    manifest_href = Path(shutil.os.path.relpath(output_dir / "manifest.html", page_dir)).as_posix()
    markup = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="{css_href}">
</head>
<body>
<div class="hub-shell">
  <header class="hub-topbar">
    <div>
      <p class="hub-kicker">Heifer Zephyr · Round 24 Sprint</p>
      <h1 class="hub-wordmark">Instrument Deliverables Hub</h1>
    </div>
    <nav class="hub-nav">
      <a href="{home_href}">Hub</a>
      <a href="{manifest_href}">Manifest</a>
    </nav>
  </header>
  {body}
</div>
</body>
</html>
"""
    return "\n".join(line.rstrip() for line in markup.splitlines()) + "\n"


def build_item_context(item: dict[str, Any], manifest_path: Path, page_dir: Path) -> dict[str, Any]:
    slug = str(item["slug"])
    artifact_types = [str(kind) for kind in item.get("artifact_types", [])]
    rounds = list(item.get("rounds", []))
    draft_prs = list(item.get("draft_prs", []))
    notes = list(item.get("notes", []))
    repo_target = resolve_reference(item.get("repo_path") or item.get("links", {}).get("repo"), manifest_path)
    repo_href = href_for_page(repo_target, page_dir) if isinstance(repo_target, Path) and repo_target.exists() else item.get("github_repo")
    repo_is_local = isinstance(repo_target, Path) and repo_target.exists()

    links = []
    for link_name, link_value in sorted(item.get("links", {}).items()):
        resolved = resolve_reference(str(link_value), manifest_path)
        link_exists = not isinstance(resolved, Path) or resolved.exists()
        href = href_for_page(resolved, page_dir) if link_exists else None
        links.append(
            {
                "name": link_name.replace("_", " "),
                "href": href,
                "exists": link_exists,
                "resolved_path": str(resolved) if isinstance(resolved, Path) else str(link_value),
            }
        )

    rounds_display = []
    for round_info in rounds:
        rounds_display.append(
            {
                "round": round_info.get("round"),
                "pane": round_info.get("pane", ""),
                "lane": round_info.get("lane", ""),
                "branch": round_info.get("branch", ""),
                "worktree": round_info.get("worktree", ""),
            }
        )

    accent = derive_family_accent(slug, " ".join(artifact_types), " ".join(str(r.get("lane", "")) for r in rounds))

    return {
        "slug": slug,
        "title": titleize_slug(slug),
        "status_label": normalize_label(item.get("status_label"), "status-unspecified"),
        "readiness_label": normalize_label(item.get("readiness_label"), "readiness-unspecified"),
        "runtime_label": normalize_label(runtime_label_for_item(item), "runtime-unspecified"),
        "github_repo": item.get("github_repo"),
        "repo_href": repo_href,
        "repo_is_local": repo_is_local,
        "artifact_types": artifact_types,
        "artifact_count": len(artifact_types),
        "rounds": rounds_display,
        "round_count": len(rounds_display),
        "draft_prs": draft_prs,
        "notes": notes,
        "links": links,
        "accent_class": accent,
    }


def render_round_rows(rounds: list[dict[str, Any]]) -> str:
    if not rounds:
        return '<p class="hub-empty">No sprint round metadata declared.</p>'
    rows = []
    for round_info in rounds:
        rows.append(
            "<tr>"
            f"<td>R{html.escape(str(round_info['round']))}</td>"
            f"<td>{html.escape(str(round_info['pane']))}</td>"
            f"<td>{html.escape(str(round_info['lane']))}</td>"
            f"<td><code>{html.escape(str(round_info['branch']))}</code></td>"
            f"<td><code>{html.escape(str(round_info['worktree']))}</code></td>"
            "</tr>"
        )
    return (
        '<table class="hub-table">'
        "<thead><tr><th>Round</th><th>Pane</th><th>Lane</th><th>Branch</th><th>Worktree</th></tr></thead>"
        f"<tbody>{''.join(rows)}</tbody></table>"
    )


def render_link_list(links: list[dict[str, Any]]) -> str:
    if not links:
        return '<p class="hub-empty">No artifact links declared.</p>'
    items = []
    for link_info in links:
        if link_info["href"]:
            target = html.escape(str(link_info["href"]))
            items.append(
                "<li>"
                f'<a href="{target}">{html.escape(link_info["name"])}</a>'
                f'<span class="hub-link-meta">{html.escape(link_info["resolved_path"])}</span>'
                "</li>"
            )
        else:
            items.append(
                "<li>"
                f"{html.escape(link_info['name'])}"
                f'<span class="hub-link-meta">unavailable locally: {html.escape(link_info["resolved_path"])}</span>'
                "</li>"
            )
    return f'<ul class="hub-link-list">{"".join(items)}</ul>'


def render_pr_list(prs: list[dict[str, Any]]) -> str:
    if not prs:
        return '<p class="hub-empty">No draft PR references declared.</p>'
    items = []
    for pr in prs:
        url = html.escape(str(pr.get("url", "")))
        label = f"PR #{pr.get('id')} · {pr.get('state', 'state-unknown')}"
        meta = pr.get("lane", "")
        items.append(
            "<li>"
            f'<a href="{url}">{html.escape(label)}</a>'
            f'<span class="hub-link-meta">{html.escape(str(meta))}</span>'
            "</li>"
        )
    return f'<ul class="hub-link-list">{"".join(items)}</ul>'


def render_notes(notes: list[str]) -> str:
    if not notes:
        return ""
    items = "".join(f"<li>{html.escape(note)}</li>" for note in notes)
    return f'<section class="hub-detail-block"><h2>Notes</h2><ul class="hub-notes">{items}</ul></section>'


def render_index_page(manifest: dict[str, Any], contexts: list[dict[str, Any]], output_dir: Path) -> str:
    page_dir = output_dir
    readiness_counts = Counter(ctx["readiness_label"] for ctx in contexts)
    status_counts = Counter(ctx["status_label"] for ctx in contexts)
    runtime_counts = Counter(ctx["runtime_label"] for ctx in contexts)
    artifact_counts = Counter(kind for ctx in contexts for kind in ctx["artifact_types"])

    filter_cards = []
    for ctx in contexts:
        detail_href = Path("instruments") / f"{ctx['slug']}.html"
        rounds = ",".join(sorted({str(round_info["round"]) for round_info in ctx["rounds"]})) or "none"
        artifacts = ",".join(slugify(kind) for kind in ctx["artifact_types"]) or "none"
        pr_count = len(ctx["draft_prs"])
        repo_link = ""
        if ctx["repo_href"]:
            repo_target = html.escape(str(ctx["repo_href"]))
            repo_label = "Open local repo" if ctx["repo_is_local"] else "Open GitHub repo"
            repo_link = f'<a class="hub-card-link-secondary" href="{repo_target}">{repo_label}</a>'

        filter_cards.append(
            f'''
            <article class="hub-card {ctx["accent_class"]}"
              data-readiness="{slugify(ctx["readiness_label"])}"
              data-status="{slugify(ctx["status_label"])}"
              data-runtime="{slugify(ctx["runtime_label"])}"
              data-rounds="{html.escape(rounds)}"
              data-artifacts="{html.escape(artifacts)}">
              <div class="hub-card-stripe"></div>
              <div class="hub-card-body">
                <p class="hub-card-kicker">{html.escape(ctx["title"])}</p>
                <h2>{html.escape(ctx["title"])}</h2>
                <div class="hub-badge-row">
                  {badge(ctx["status_label"], "status")}
                  {badge(ctx["readiness_label"], "readiness")}
                  {badge(ctx["runtime_label"], "runtime")}
                </div>
                <p class="hub-card-copy">
                  {ctx["round_count"]} sprint round entries · {ctx["artifact_count"]} artifact labels · {pr_count} draft PR references
                </p>
                <div class="hub-meta-grid">
                  <p><strong>Rounds</strong><span>{html.escape(rounds)}</span></p>
                  <p><strong>Artifacts</strong><span>{html.escape(", ".join(ctx["artifact_types"]))}</span></p>
                </div>
                <div class="hub-card-actions">
                  <a class="hub-card-link-primary" href="{html.escape(detail_href.as_posix())}">Open detail page</a>
                  {repo_link}
                </div>
              </div>
            </article>
            '''
        )

    source_plan = resolve_reference(str(manifest.get("source_plan", "")), DEFAULT_MANIFEST)
    source_plan_href = href_for_page(source_plan, page_dir) if isinstance(source_plan, Path) and source_plan.exists() else None
    source_plan_html = ""
    if source_plan_href:
        source_plan_html = f'<a href="{html.escape(source_plan_href)}">Open sprint contract</a>'

    body = f"""
<main class="hub-home">
  <section class="hub-hero">
    <div class="hub-hero-copy">
      <p class="hub-kicker">Static, local-first, relative-link friendly</p>
      <h2>Round 23 and Round 24 instrument deliverables in one browsable hub.</h2>
      <p>
        This site surfaces sprint lanes, artifact types, readiness labels, and draft-PR context
        without overstating build validation. Wolfram outputs and HTML previews are review artifacts;
        fabrication authority still belongs to measured templates, design tables, CAD, and DXF.
      </p>
    </div>
    <div class="hub-hero-meta">
      <p><strong>Manifest schema</strong><span>{html.escape(str(manifest.get("schema_version", "unknown")))}</span></p>
      <p><strong>Generated</strong><span>{html.escape(str(manifest.get("generated_at", "unknown")))}</span></p>
      <p><strong>Rounds</strong><span>{html.escape(", ".join(f"R{value}" for value in manifest.get("source_rounds", [])))}</span></p>
      <p><strong>Source plan</strong><span>{source_plan_html or html.escape(str(manifest.get("source_plan", "not declared")))}</span></p>
    </div>
  </section>

  <section class="hub-summary-grid">
    {render_stat_cards(readiness_counts, "Readiness")}
    {render_stat_cards(status_counts, "Status")}
    {render_stat_cards(runtime_counts, "Runtime")}
  </section>

  <section class="hub-summary-grid hub-summary-grid-artifacts">
    {render_stat_cards(artifact_counts, "Artifact")}
  </section>

  <section class="hub-filter-panel">
    <div>
      <p class="hub-filter-label">Readiness</p>
      <div class="hub-filter-row">
        <button type="button" class="hub-filter-button is-active" data-filter-group="readiness" data-filter-value="all">All</button>
        <button type="button" class="hub-filter-button" data-filter-group="readiness" data-filter-value="not-build-ready">Not build ready</button>
        <button type="button" class="hub-filter-button" data-filter-group="readiness" data-filter-value="availability-check">Availability check</button>
      </div>
    </div>
    <div>
      <p class="hub-filter-label">Runtime</p>
      <div class="hub-filter-row">
        <button type="button" class="hub-filter-button is-active" data-filter-group="runtime" data-filter-value="all">All</button>
        <button type="button" class="hub-filter-button" data-filter-group="runtime" data-filter-value="manifest-unset">Manifest unset</button>
        <button type="button" class="hub-filter-button" data-filter-group="runtime" data-filter-value="not-applicable">Not applicable</button>
      </div>
    </div>
    <div>
      <p class="hub-filter-label">Round</p>
      <div class="hub-filter-row">
        <button type="button" class="hub-filter-button is-active" data-filter-group="rounds" data-filter-value="all">All</button>
        <button type="button" class="hub-filter-button" data-filter-group="rounds" data-filter-value="23">Round 23</button>
        <button type="button" class="hub-filter-button" data-filter-group="rounds" data-filter-value="24">Round 24</button>
      </div>
    </div>
  </section>

  <section class="hub-card-grid">
    {''.join(filter_cards)}
  </section>
</main>
<script>
const activeFilters = {{ readiness: "all", runtime: "all", rounds: "all" }};
const cards = [...document.querySelectorAll(".hub-card")];
const buttons = [...document.querySelectorAll(".hub-filter-button")];

function applyFilters() {{
  cards.forEach((card) => {{
    const readinessOk = activeFilters.readiness === "all" || card.dataset.readiness === activeFilters.readiness;
    const runtimeOk = activeFilters.runtime === "all" || card.dataset.runtime === activeFilters.runtime;
    const roundsOk = activeFilters.rounds === "all" || card.dataset.rounds.split(",").includes(activeFilters.rounds);
    card.hidden = !(readinessOk && runtimeOk && roundsOk);
  }});
}}

buttons.forEach((button) => {{
  button.addEventListener("click", () => {{
    const group = button.dataset.filterGroup;
    activeFilters[group] = button.dataset.filterValue;
    buttons
      .filter((candidate) => candidate.dataset.filterGroup === group)
      .forEach((candidate) => candidate.classList.toggle("is-active", candidate === button));
    applyFilters();
  }});
}});

applyFilters();
</script>
"""
    return page_shell("Instrument Deliverables Hub", body, page_dir, output_dir)


def render_detail_page(context: dict[str, Any], output_dir: Path) -> str:
    page_dir = output_dir / "instruments"
    repo_target_html = ""
    if context["repo_href"]:
        repo_label = "Open local repo" if context["repo_is_local"] else "Open GitHub repo"
        repo_target_html = f'<a class="hub-card-link-primary" href="{html.escape(str(context["repo_href"]))}">{repo_label}</a>'

    artifact_badges = "".join(badge(kind, "artifact") for kind in context["artifact_types"])
    status_badges = "".join(
        [
            badge(context["status_label"], "status"),
            badge(context["readiness_label"], "readiness"),
            badge(context["runtime_label"], "runtime"),
        ]
    )
    body = f"""
<main class="hub-detail {context["accent_class"]}">
  <section class="hub-detail-hero">
    <div class="hub-detail-stripe"></div>
    <p class="hub-kicker">Instrument detail</p>
    <h2>{html.escape(context["title"])}</h2>
    <div class="hub-badge-row">{status_badges}</div>
    <p class="hub-card-copy">
      Static hub entry for {html.escape(context["title"])}. Runtime evidence is shown only when the manifest
      declares it; absent fields remain visibly unset instead of inferred into stronger claims.
    </p>
    <div class="hub-card-actions">
      {repo_target_html}
      <a class="hub-card-link-secondary" href="{html.escape(context["github_repo"] or "#")}">GitHub repo</a>
    </div>
  </section>

  <section class="hub-detail-block">
    <h2>Artifact types</h2>
    <div class="hub-badge-row">{artifact_badges}</div>
  </section>

  <section class="hub-detail-block">
    <h2>Sprint rounds</h2>
    {render_round_rows(context["rounds"])}
  </section>

  <section class="hub-detail-block">
    <h2>Artifact links</h2>
    {render_link_list(context["links"])}
  </section>

  <section class="hub-detail-block">
    <h2>Draft PRs</h2>
    {render_pr_list(context["draft_prs"])}
  </section>

  {render_notes(context["notes"])}
</main>
"""
    return page_shell(f"{context['title']} · Deliverables Hub", body, page_dir, output_dir)


def render_manifest_page(manifest: dict[str, Any], output_dir: Path) -> str:
    page_dir = output_dir
    body = f"""
<main class="hub-manifest">
  <section class="hub-detail-block">
    <p class="hub-kicker">Machine-readable source</p>
    <h2>Deliverables manifest</h2>
    <p>
      This is the raw seed consumed by the site renderer. It stays checked in under <code>data/</code>
      so the hub works without a server-side API or local <code>fetch()</code> dependency.
    </p>
    <pre class="hub-json-block">{escaped_json(manifest)}</pre>
  </section>
</main>
"""
    return page_shell("Deliverables Manifest", body, page_dir, output_dir)


def render_site(manifest_path: Path, output_dir: Path) -> None:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    output_dir.mkdir(parents=True, exist_ok=True)
    instruments_dir = output_dir / "instruments"
    assets_dir = output_dir / "assets"
    instruments_dir.mkdir(parents=True, exist_ok=True)
    assets_dir.mkdir(parents=True, exist_ok=True)

    shutil.copy2(SITE_SOURCE_CSS, assets_dir / "hub.css")
    shutil.copy2(manifest_path, assets_dir / "deliverables-manifest.json")

    index_contexts = [
        build_item_context(item, manifest_path, output_dir)
        for item in manifest.get("items", [])
    ]
    index_contexts.sort(key=lambda item: item["title"])

    (output_dir / "index.html").write_text(
        render_index_page(manifest, index_contexts, output_dir),
        encoding="utf-8",
    )
    (output_dir / "manifest.html").write_text(
        render_manifest_page(manifest, output_dir),
        encoding="utf-8",
    )

    for item in sorted(manifest.get("items", []), key=lambda entry: titleize_slug(str(entry["slug"]))):
        context = build_item_context(item, manifest_path, instruments_dir)
        detail_page = instruments_dir / f"{context['slug']}.html"
        detail_page.write_text(
            render_detail_page(context, output_dir),
            encoding="utf-8",
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render the instrument deliverables hub.")
    parser.add_argument(
        "--manifest",
        type=Path,
        default=DEFAULT_MANIFEST,
        help=f"Path to the deliverables manifest (default: {DEFAULT_MANIFEST})",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Output directory for static site files (default: {DEFAULT_OUTPUT_DIR})",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    render_site(args.manifest.resolve(), args.output_dir.resolve())
    print(f"Rendered site hub to {args.output_dir.resolve()}")


if __name__ == "__main__":
    main()
