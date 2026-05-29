#!/usr/bin/env python3
"""Fix checked-in showcase site HTML: replace local relative repo links with
canonical GitHub URLs and fix availability-label filter placement.

Fixes for instrument-showcase issue #3.

What this script changes:
  - href="../../<repo-slug>" → href="https://github.com/tonykoop/<repo-slug>"
  - href="../../<repo-slug>/path" → href="https://github.com/tonykoop/<repo-slug>/blob/main/path"
  - href="../../../<repo-slug>" → same (detail pages one level deeper)
  - href="../../docs/plans/..." → removes the link (internal sprint planning, not public)
  - Moves availability-check from readiness filter group to status filter group in index.html

Usage:
    python3 fix_site_links.py [--dry-run] [--site-dir site]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

GITHUB_BASE = "https://github.com/tonykoop"

# Repo slugs that have public repos (not just local paths)
KNOWN_REPOS = {
    "ceramic-electric-violin", "clarinet", "cnc-guitar-bodies", "didgeridoo",
    "duduk", "dundun", "electric-guitar-bodies", "erhu", "fujara", "guzheng",
    "hulusi", "konghou", "kora", "ngoni", "pipa", "sambuca", "sheng",
    "stave-lute-oud", "tongue-drum", "whamola-bass", "cajon", "marimba",
    "handpan", "haegeum", "udu", "ocarina", "gemshorn", "kena",
    "transverse-flute", "shakuhachi", "moseno", "ceramic-tongue-drum",
}


def fix_relative_repo_link(href: str) -> str:
    """Return corrected href for a relative repo link, or None to drop it."""
    # Strip leading ../ sequences
    stripped = re.sub(r"^(\.\./)+(\.\./?)?", "", href)
    if stripped.startswith("docs/plans/") or stripped.startswith("docs/"):
        # Internal sprint planning link — not public-safe; remove
        return None

    parts = stripped.split("/", 1)
    repo_slug = parts[0]
    file_path = parts[1] if len(parts) > 1 else ""

    if repo_slug not in KNOWN_REPOS:
        # Could be an unknown repo or a relative path within the site; skip
        return None

    if file_path:
        return f"{GITHUB_BASE}/{repo_slug}/blob/main/{file_path}"
    return f"{GITHUB_BASE}/{repo_slug}"


def fix_html(text: str, filename: str) -> tuple[str, list[str]]:
    changes: list[str] = []

    # Fix href="../../<repo>" and href="../../../<repo>" style links
    def replace_href(m: re.Match) -> str:
        full = m.group(0)
        quote = m.group(1)
        href = m.group(2)

        # Only process links that start with ../ chains
        if not href.startswith("../"):
            return full

        # Only process links where the resolved path looks like a repo slug
        stripped = re.sub(r"^(\.\./)+(\.\./?)?", "", href)
        if not stripped:
            return full

        new_href = fix_relative_repo_link(href)
        if new_href is None:
            # Drop the anchor element entirely if it's an internal sprint link
            if "docs/plans" in href:
                changes.append(f"  removed internal sprint link: {href!r}")
                # Replace with just the text content — extract text from anchor
                inner_m = re.search(r">([^<]+)</a>", m.string[m.start():], re.DOTALL)
                if inner_m:
                    return inner_m.group(1)
                return ""
            return full

        if new_href != href:
            changes.append(f"  {href!r} → {new_href!r}")
        return f"href={quote}{new_href}{quote}"

    text = re.sub(r"href=([\"'])((?:\.\./)[\w./-]+)\1", replace_href, text)

    # Fix stale availability-check filter group in index.html
    if "index.html" in filename:
        old = 'data-filter-group="readiness" data-filter-value="availability-check"'
        new = 'data-filter-group="status" data-filter-value="availability-check"'
        if old in text:
            text = text.replace(old, new)
            changes.append(f"  fixed availability-check filter group: readiness → status")

    return text, changes


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Report changes without writing")
    parser.add_argument("--site-dir", type=Path, default=Path(__file__).parent.parent / "site")
    args = parser.parse_args(argv)

    site = args.site_dir.resolve()
    if not site.exists():
        print(f"ERROR: site dir not found: {site}", file=sys.stderr)
        return 1

    total_changes = 0
    for html_file in sorted(site.rglob("*.html")):
        text = html_file.read_text(encoding="utf-8")
        new_text, changes = fix_html(text, html_file.name)
        if changes:
            total_changes += len(changes)
            rel = html_file.relative_to(site)
            print(f"{rel}: {len(changes)} change(s)")
            for c in changes:
                print(c)
            if not args.dry_run:
                html_file.write_text(new_text, encoding="utf-8")

    if total_changes == 0:
        print("No changes needed.")
    elif args.dry_run:
        print(f"\n[dry-run] {total_changes} change(s) would be applied.")
    else:
        print(f"\nApplied {total_changes} change(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
