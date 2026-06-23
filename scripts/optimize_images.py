#!/usr/bin/env python3
"""Optimize images for web publishing.

Resizes to longest-edge ≤ 1600 px, re-encodes as progressive JPEG q82,
strips EXIF (but honors camera-rotation before stripping), preserves
directory structure under --output.

Usage:
    python3 scripts/optimize_images.py --source <dir> --output <dir>
    python3 scripts/optimize_images.py --source /workspace/flutes/images \
        --output docs/instruments/woodwind/flutes/images --dry-run
"""
import argparse
import sys
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError:
    sys.exit("Pillow required: pip install Pillow")

MAX_EDGE = 1600
JPEG_QUALITY = 82
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff"}


def _optimize_one(src: Path, dst: Path, dry_run: bool) -> tuple[int, int]:
    orig_bytes = src.stat().st_size
    if dry_run:
        return orig_bytes, orig_bytes

    img = Image.open(src)
    img = ImageOps.exif_transpose(img)  # apply EXIF rotation, then strip

    if max(img.size) > MAX_EDGE:
        img.thumbnail((MAX_EDGE, MAX_EDGE), Image.LANCZOS)

    img = img.convert("RGB")  # ensure no alpha channel before JPEG encode
    dst.parent.mkdir(parents=True, exist_ok=True)
    img.save(dst, "JPEG", quality=JPEG_QUALITY, progressive=True, optimize=True)

    out_bytes = dst.stat().st_size
    return orig_bytes, out_bytes


def optimize_directory(
    src_root: Path,
    dst_root: Path,
    dry_run: bool = False,
    verbose: bool = True,
) -> tuple[int, int, int]:
    """Optimize all images under src_root into dst_root.

    Returns (count, total_before_bytes, total_after_bytes).
    """
    total_before = total_after = count = 0
    for src in sorted(src_root.rglob("*")):
        if src.is_dir() or src.suffix.lower() not in IMAGE_EXTS:
            continue
        rel = src.relative_to(src_root)
        dst = dst_root / rel.with_suffix(".jpg")
        before, after = _optimize_one(src, dst, dry_run)
        total_before += before
        total_after += after
        count += 1
        if verbose:
            saved = (1 - after / before) * 100 if before else 0
            tag = "[dry]" if dry_run else "ok  "
            print(f"  {tag}  {rel}  {before // 1024}KB → {after // 1024}KB  ({saved:.0f}% saved)")
    return count, total_before, total_after


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Optimize images for GitHub Pages bundle.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    ap.add_argument("--source", required=True, help="Source image directory")
    ap.add_argument("--output", required=True, help="Destination directory for optimized images")
    ap.add_argument("--dry-run", action="store_true", help="Show what would be done without writing")
    ap.add_argument("--quiet", action="store_true", help="Suppress per-file output")
    args = ap.parse_args()

    src_root = Path(args.source)
    dst_root = Path(args.output)

    if not src_root.exists():
        sys.exit(f"source not found: {src_root}")

    count, before_b, after_b = optimize_directory(
        src_root, dst_root, dry_run=args.dry_run, verbose=not args.quiet
    )

    if count == 0:
        print("no image files found")
        return

    saved_mb = (before_b - after_b) / 1_048_576
    print(
        f"\n{count} image(s)  "
        f"{before_b / 1_048_576:.1f} MB → {after_b / 1_048_576:.1f} MB  "
        f"({saved_mb:.1f} MB saved)"
    )


if __name__ == "__main__":
    main()
