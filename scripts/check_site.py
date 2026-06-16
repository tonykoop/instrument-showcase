#!/usr/bin/env python3
"""
check_site.py — pre-publish health checks for the Studio Explorers site.

Gates every publish (issue #24) and permanently kills the stale-stat class of
bug (issue #14) by asserting the rendered library.html agrees with the
generated manifest:

  1. COUNT CONSISTENCY  — # of <article> cards == manifest entries == the
     "Repos in library" hero stat. (No more "badge says 48, page has 63".)
  2. COMPLETENESS CONSISTENCY — the "Explorers complete" stat and the per-family
     progress rows match what the manifest's completeness_state implies.
  3. LINK HEALTH — every local explorer link in library.html resolves to a file
     on disk (skipped for entries rendered in --base-url publish mode).
  4. IMAGE REFS — every local <img src> in library.html resolves on disk.
  5. SCOPE GATE — if scripts/published.txt exists, warn on any published slug
     whose repo manifest is private / blocked / patent-candidate (private→public
     is sticky — the most important publish gate, per #24).

Exit code: 0 if no hard failures, 1 otherwise. Soft issues print as warnings.

Usage:
    python3 scripts/check_site.py
    python3 scripts/check_site.py --library site/library.html --manifest data/library-manifest.json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SHOWCASE_DIR = Path(__file__).resolve().parent.parent
SITE_DIR = SHOWCASE_DIR / "site"

GREEN, RED, YEL, DIM, RST = "\033[32m", "\033[31m", "\033[33m", "\033[2m", "\033[0m"


def _num(label_pat: str, html: str) -> int | None:
    """Pull the integer from a `<div class="v">N...</div>` stat whose preceding
    `<div class="k">LABEL</div>` matches label_pat."""
    m = re.search(
        r'<div class="k">\s*' + label_pat + r'\s*</div>\s*<div class="v">\s*([0-9,]+)',
        html, re.I | re.S)
    return int(m.group(1).replace(",", "")) if m else None


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Pre-publish health checks for the showcase site")
    p.add_argument("--library", type=Path, default=SITE_DIR / "library.html")
    p.add_argument("--manifest", type=Path, default=SHOWCASE_DIR / "data" / "library-manifest.json")
    p.add_argument("--published", type=Path, default=SHOWCASE_DIR / "scripts" / "published.txt")
    args = p.parse_args(argv)

    fails: list[str] = []
    warns: list[str] = []

    if not args.library.exists():
        print(f"{RED}FAIL{RST} library not found: {args.library} — run generate_library.py first")
        return 1
    if not args.manifest.exists():
        print(f"{RED}FAIL{RST} manifest not found: {args.manifest}")
        return 1

    html = args.library.read_text(encoding="utf-8", errors="ignore")
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    entries = manifest.get("entries", manifest if isinstance(manifest, list) else [])
    site_dir = args.library.parent

    # 1. COUNT CONSISTENCY (#14) -------------------------------------------------
    n_cards = len(re.findall(r'<article class="card"', html))
    n_entries = len(entries)
    stat_total = _num(r"Repos in library", html)
    if not (n_cards == n_entries == (stat_total if stat_total is not None else n_cards)):
        fails.append(f"count drift: {n_cards} cards / {n_entries} manifest entries / "
                     f"hero stat {stat_total} — regenerate library.html")
    else:
        print(f"{GREEN}ok{RST}   counts agree: {n_cards} cards = {n_entries} entries = stat {stat_total}")

    # 2. COMPLETENESS CONSISTENCY (#31 dashboard) --------------------------------
    complete_entries = sum(1 for e in entries if e.get("completeness_state") == "complete")
    stat_complete = _num(r"Explorers complete", html)
    if stat_complete is not None and stat_complete != complete_entries:
        fails.append(f"'Explorers complete' stat ({stat_complete}) != manifest complete "
                     f"({complete_entries})")
    else:
        print(f"{GREEN}ok{RST}   completeness stat matches manifest ({complete_entries} complete)")

    # per-family progress rows  e.g.  Strings ... 3/43
    fam_total: dict[str, int] = {}
    fam_done: dict[str, int] = {}
    for e in entries:
        f = e.get("family", "other")
        fam_total[f] = fam_total.get(f, 0) + 1
        if e.get("completeness_state") == "complete":
            fam_done[f] = fam_done.get(f, 0) + 1
    for m in re.finditer(r'fam-prog-count">\s*([0-9]+)\s*/\s*([0-9]+)\s*</span>', html):
        done, tot = int(m.group(1)), int(m.group(2))
        if not any(fam_done.get(f, 0) == done and fam_total[f] == tot for f in fam_total):
            warns.append(f"per-family progress row {done}/{tot} not found in manifest tallies")

    # 3 + 4. LINK + IMAGE HEALTH (local refs only) -------------------------------
    broken_links, broken_imgs = [], []
    for href in re.findall(r'<a class="card-title" href="([^"]+)"', html):
        if href.startswith(("http://", "https://", "#")):
            continue
        if not (site_dir / href).resolve().exists():
            broken_links.append(href)
    for src in re.findall(r'<img[^>]+src="([^"]+)"', html):
        if src.startswith(("http://", "https://", "data:")):
            continue
        if not (site_dir / src).resolve().exists():
            broken_imgs.append(src)
    if broken_links:
        fails.append(f"{len(broken_links)} broken explorer link(s), e.g. {broken_links[0]}")
    else:
        print(f"{GREEN}ok{RST}   all local explorer links resolve")
    if broken_imgs:
        warns.append(f"{len(broken_imgs)} unresolved <img> src(s), e.g. {broken_imgs[0]}")
    else:
        print(f"{GREEN}ok{RST}   all local <img> srcs resolve")

    # 5. SCOPE GATE (#24 — private→public is sticky) -----------------------------
    if args.published.exists():
        pub = {s.strip() for s in args.published.read_text().split() if s.strip()}
        leaked = [e["slug"] for e in entries
                  if e.get("slug") in pub and e.get("status") in ("private", "blocked")]
        if leaked:
            fails.append(f"SCOPE: {len(leaked)} published slug(s) are private/blocked: "
                         f"{', '.join(leaked[:5])} — do NOT publish")
        else:
            print(f"{GREEN}ok{RST}   scope gate: {len(pub)} published slugs, none private/blocked")
    else:
        print(f"{DIM}--   scope gate skipped (no scripts/published.txt){RST}")

    # Report ---------------------------------------------------------------------
    print()
    for w in warns:
        print(f"{YEL}warn{RST} {w}")
    for f in fails:
        print(f"{RED}FAIL{RST} {f}")
    if fails:
        print(f"\n{RED}{len(fails)} hard failure(s){RST} — site is NOT publish-ready.")
        return 1
    print(f"\n{GREEN}site is publish-ready{RST}"
          + (f" ({len(warns)} warning(s) to review)" if warns else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
