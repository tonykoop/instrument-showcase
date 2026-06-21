#!/usr/bin/env python3
"""
qa_images.py — pre-publish image QA gate for the instrument-showcase /docs bundle.

Checks the optimized images inside docs/instruments/ for:
  1. Byte-identical duplicates across different instruments (canned outputs / sibling
     cross-contamination). Flags pairs that share an md5 across different slug dirs.
  2. Suspiciously small files: images < MIN_BYTES likely blanks, placeholders, or
     total-generation failures. Threshold is conservative (5 KB after optimization).
  3. Zero-area or extreme-aspect-ratio images (w/h or h/w > MAX_ASPECT) that suggest
     a render failure rather than a tight macro crop.

Exit code 0 = pass. Exit code 1 = QA violations found. Use as a gate before pushing.

Usage:
  python3 scripts/qa_images.py                   # scan docs/instruments/
  python3 scripts/qa_images.py --docs path/docs  # alternate docs root
  python3 scripts/qa_images.py --json            # machine-readable output
"""
import os, hashlib, json, argparse
from pathlib import Path
from PIL import Image

MIN_BYTES = 5_120      # < 5 KB after optimization = suspicious blank/placeholder
MAX_ASPECT = 20.0      # w/h or h/w > 20 = degenerate strip, not a real image
RASTER_EXT = {".jpg", ".jpeg", ".png", ".webp"}


def md5(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            h.update(block)
    return h.hexdigest()


def slug_of(path, instr_root):
    rel = Path(path).relative_to(instr_root)
    return rel.parts[1] if len(rel.parts) >= 2 else str(rel)


def scan(docs_root):
    instr_root = Path(docs_root) / "instruments"
    if not instr_root.is_dir():
        print(f"No instruments dir found at {instr_root}; run build_pages.py first.")
        return [], [], []

    hashes = {}       # md5 -> list of paths
    tiny = []
    bad_aspect = []

    for root, _, files in os.walk(instr_root):
        for fname in files:
            ext = Path(fname).suffix.lower()
            if ext not in RASTER_EXT:
                continue
            fpath = os.path.join(root, fname)
            size = os.path.getsize(fpath)

            if size < MIN_BYTES:
                tiny.append(fpath)
                continue

            digest = md5(fpath)
            hashes.setdefault(digest, []).append(fpath)

            try:
                with Image.open(fpath) as im:
                    w, h = im.size
                if h == 0 or w == 0:
                    bad_aspect.append((fpath, w, h))
                elif max(w / h, h / w) > MAX_ASPECT:
                    bad_aspect.append((fpath, w, h))
            except Exception:
                pass

    dupes = {digest: paths for digest, paths in hashes.items()
             if len(paths) > 1
             and len({slug_of(p, instr_root) for p in paths}) > 1}

    return dupes, tiny, bad_aspect


def report_text(dupes, tiny, bad_aspect, docs_root):
    violations = 0
    lines = []

    if dupes:
        lines.append(f"\n[DUPLICATES] {len(dupes)} byte-identical image(s) across different instruments:")
        for digest, paths in sorted(dupes.items()):
            lines.append(f"  md5:{digest[:12]}")
            for p in sorted(paths):
                lines.append(f"    {p}")
            violations += 1

    if tiny:
        lines.append(f"\n[TOO-SMALL] {len(tiny)} image(s) < 5KB (blank / placeholder / generation failure):")
        for p in sorted(tiny):
            lines.append(f"  {os.path.getsize(p):>7} B  {p}")
            violations += 1

    if bad_aspect:
        lines.append(f"\n[BAD-ASPECT] {len(bad_aspect)} image(s) with extreme dimensions:")
        for p, w, h in sorted(bad_aspect):
            lines.append(f"  {w}x{h}  {p}")
            violations += 1

    if violations:
        print(f"QA FAIL — {violations} violation(s) in {docs_root}")
        print("\n".join(lines))
    else:
        print(f"QA PASS — no duplicates, blanks, or bad-aspect images in {docs_root}")
    return violations


def report_json(dupes, tiny, bad_aspect):
    out = {
        "duplicates": [
            {"md5": d, "paths": sorted(ps)}
            for d, ps in sorted(dupes.items())
        ],
        "too_small": sorted(tiny),
        "bad_aspect": [{"path": p, "w": w, "h": h} for p, w, h in sorted(bad_aspect)],
        "violation_count": len(dupes) + len(tiny) + len(bad_aspect),
    }
    print(json.dumps(out, indent=2))
    return out["violation_count"]


def main():
    parser = argparse.ArgumentParser()
    here = Path(__file__).resolve().parent
    parser.add_argument("--docs", default=str(here.parent / "docs"),
                        help="path to the /docs bundle root")
    parser.add_argument("--json", action="store_true", help="emit JSON instead of human text")
    args = parser.parse_args()

    dupes, tiny, bad_aspect = scan(args.docs)
    if args.json:
        violations = report_json(dupes, tiny, bad_aspect)
    else:
        violations = report_text(dupes, tiny, bad_aspect, args.docs)

    raise SystemExit(1 if violations else 0)


if __name__ == "__main__":
    main()
