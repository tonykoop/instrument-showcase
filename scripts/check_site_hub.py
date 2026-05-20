#!/usr/bin/env python3
"""Check the checked-in static hub for public-link hygiene."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SITE_DIR = REPO_ROOT / "site"
PUBLIC_FILE_SUFFIXES = {".html", ".json"}
LOCAL_PATH_PATTERNS = (
    re.compile(r"file://", re.I),
    re.compile(r"(?<![A-Za-z])[A-Za-z]:[\\/]"),
    re.compile(r"/mnt/"),
    re.compile(r"/tmp/"),
    re.compile(r"/home/"),
    re.compile(r"/Users/"),
)


def public_files(site_dir: Path) -> list[Path]:
    return sorted(
        path
        for path in site_dir.rglob("*")
        if path.is_file() and path.suffix in PUBLIC_FILE_SUFFIXES
    )


def check_public_paths(site_dir: Path) -> list[str]:
    findings: list[str] = []
    for path in public_files(site_dir):
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(site_dir)
        for pattern in LOCAL_PATH_PATTERNS:
            for match in pattern.finditer(text):
                line_no = text.count("\n", 0, match.start()) + 1
                findings.append(f"{rel}:{line_no}: local path fragment {match.group(0)!r}")
    return findings


def check_availability_labels(site_dir: Path) -> list[str]:
    findings: list[str] = []
    index_html = site_dir / "index.html"
    if index_html.exists():
        text = index_html.read_text(encoding="utf-8")
        stale_filter = 'data-filter-group="readiness" data-filter-value="availability-check"'
        if stale_filter in text:
            findings.append("index.html: availability-check is still rendered as a readiness filter")
        expected_filter = 'data-filter-group="status" data-filter-value="availability-check"'
        if expected_filter not in text:
            findings.append("index.html: availability-check status filter is missing")

    manifest_path = site_dir / "assets" / "deliverables-manifest.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        for item in manifest.get("items", []):
            slug = str(item.get("slug", "<unknown>"))
            if item.get("readiness_label") == "availability-check":
                findings.append(f"assets/deliverables-manifest.json:{slug}: availability-check used as readiness_label")
    return findings


def run_checks(site_dir: Path) -> list[str]:
    findings: list[str] = []
    if not site_dir.exists():
        return [f"{site_dir}: site directory does not exist"]
    findings.extend(check_public_paths(site_dir))
    findings.extend(check_availability_labels(site_dir))
    return findings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check generated hub files for public-link hygiene.")
    parser.add_argument(
        "--site-dir",
        type=Path,
        default=DEFAULT_SITE_DIR,
        help=f"Static site directory to scan (default: {DEFAULT_SITE_DIR})",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    findings = run_checks(args.site_dir.resolve())
    if findings:
        print("site hub check failed:", file=sys.stderr)
        for finding in findings:
            print(f"  - {finding}", file=sys.stderr)
        return 1
    print(f"site hub check passed: {args.site_dir.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
