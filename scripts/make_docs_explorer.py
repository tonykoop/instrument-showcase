#!/usr/bin/env python3
"""
make_docs_explorer.py — generate a v2 explorer page for one instrument and write
it to docs/instruments/<family_dir>/<slug>/ with an adapted hero image.

Usage:
    python3 scripts/make_docs_explorer.py --slug array-mbira --family-dir idiophones --issue 28
    python3 scripts/make_docs_explorer.py --slug cajon --family-dir percussion --issue 29
    python3 scripts/make_docs_explorer.py --slug bugle-sheetmetal --family-dir brass --issue 30

Writes:
    docs/instruments/<family_dir>/<slug>/explorer.html
    docs/instruments/<family_dir>/<slug>/images/<hero>   (hero image only)

Adapts the generated HTML so library links point to ../../../index.html
(the GitHub Pages catalog root) instead of the private _meta path.
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

SHOWCASE = Path(__file__).resolve().parent.parent
WORKSPACE = Path("/mnt/c/Users/Tony/Documents/GitHub")

sys.path.insert(0, str(SHOWCASE / "scripts"))
import generate_explorer_v2 as gev2
import generate_library as gl


PRIVATE_LIB_PATTERN = re.compile(
    r"(?:../../_meta/instrument-showcase/site/(?:library|index|manifest)\.html|"
    r"../../_meta/instrument-showcase/site/library\.html)",
    re.IGNORECASE,
)


def adapt_html(html: str) -> str:
    """Replace private _meta paths with docs-relative paths."""
    # All three nav links → root index
    html = html.replace(
        "../../_meta/instrument-showcase/site/library.html",
        "../../../index.html",
    )
    html = html.replace(
        "../../_meta/instrument-showcase/site/index.html",
        "../../../index.html",
    )
    html = html.replace(
        "../../_meta/instrument-showcase/site/manifest.html",
        "../../../index.html",
    )
    # Prev/next pager links adjust automatically (already relative ../slug/explorer.html)
    return html


def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--slug", required=True)
    p.add_argument("--family-dir", required=True, choices=["idiophones", "percussion", "brass"])
    p.add_argument("--issue", type=int, required=True)
    p.add_argument("--workspace", type=Path, default=WORKSPACE)
    args = p.parse_args(argv)

    repo = args.workspace / "instruments" / args.family_dir / args.slug
    if not repo.is_dir():
        print(f"ERROR: repo not found at {repo}", file=sys.stderr)
        return 1

    embed_index = gl.load_embed_urls(args.workspace)
    d = gev2.gather(repo, args.family_dir, embed_index)

    # Build family order for prev/next paging (only within this family_dir)
    fam_repos = sorted(
        (r for r in (args.workspace / "instruments" / args.family_dir).iterdir()
         if r.is_dir() and ((r / "capstone-manifest.json").exists() or (r / "explorer.html").exists())),
        key=lambda r: (d2 := gev2.gather(r, args.family_dir, embed_index)).title.lower()
        if False else r.name,  # cheap: sort by slug name not title
    )
    order = [(r.name, gev2.gather(r, args.family_dir, embed_index).title) for r in fam_repos]
    idx = next((i for i, (s, _) in enumerate(order) if s == args.slug), -1)
    prev_item = order[idx - 1] if idx > 0 else None
    next_item = order[idx + 1] if 0 <= idx < len(order) - 1 else None

    html = gev2.render_explorer(d, prev=prev_item, nxt=next_item)
    html = adapt_html(html)
    # Also fix wiki path if present
    html = html.replace(
        f"../../_meta/instrument-showcase/wiki/instruments/{args.slug}.md",
        f"https://github.com/tonykoop/instrument-showcase/blob/main/wiki/instruments/{args.slug}.md",
    )

    # Destination in docs/
    dest_dir = SHOWCASE / "docs" / "instruments" / args.family_dir / args.slug
    dest_dir.mkdir(parents=True, exist_ok=True)

    out_html = dest_dir / "explorer.html"
    out_html.write_text(html, encoding="utf-8")
    print(f"wrote {out_html.relative_to(SHOWCASE)}  [{d.comp_state}]")

    # Copy hero image (only)
    if d.hero_rel:
        src_img = repo / d.hero_rel
        dst_img = dest_dir / d.hero_rel
        dst_img.parent.mkdir(parents=True, exist_ok=True)
        if src_img.exists():
            shutil.copy2(src_img, dst_img)
            print(f"copied {d.hero_rel}")
        else:
            print(f"warn: hero not found at {src_img}")
    else:
        print("warn: no hero image detected")

    # Also copy gallery images (up to 6) for richer pages — images folder only, skip deep subdirs
    img_dir = repo / "images"
    if img_dir.is_dir():
        dest_img_dir = dest_dir / "images"
        dest_img_dir.mkdir(parents=True, exist_ok=True)
        exts = (".png", ".jpg", ".jpeg", ".webp")
        skip = ("favicon", "logo", "wordmark", "sprite", "icon-")
        count = 0
        for src in sorted(img_dir.iterdir()):
            if src.is_file() and src.suffix.lower() in exts:
                name = src.name.lower()
                if any(s in name for s in skip):
                    continue
                dst = dest_img_dir / src.name
                if not dst.exists():
                    shutil.copy2(src, dst)
                    count += 1
                if count >= 6:
                    break
        if count:
            print(f"copied {count} gallery images")

    return 0


if __name__ == "__main__":
    sys.exit(main())
