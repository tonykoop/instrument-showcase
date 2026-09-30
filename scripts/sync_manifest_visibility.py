#!/usr/bin/env python3
"""Make data/library-manifest.json public/private status match live GitHub visibility.

Rule (Tony): catalog status must match each repo's real GitHub visibility.
  PUBLIC repo  : 'private' / 'unknown' -> 'public'
  non-public   : 'public' / 'unknown'  -> 'private'
  'blocked' (a release blocker, not a visibility) is left in place.
Each entry also records the live `visibility` (PUBLIC/PRIVATE/INTERNAL), which
check_site.py uses for its count and scope gates. Any lookup failure aborts without writing (scripts/visibility.py).

Usage: python3 scripts/sync_manifest_visibility.py [--dry-run]
"""
import argparse, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from visibility import VisibilityError, reconcile_status, repo_visibility

MANIFEST = HERE.parent / "data" / "library-manifest.json"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    changed = 0
    try:
        for e in data["entries"]:
            vis = repo_visibility(e["slug"])
            if e.get("visibility") != vis:
                e["visibility"] = vis
                changed += 1
            status, label = reconcile_status(e["status"], e["status_label"], vis)
            if status == e["status"]:
                continue
            print(f"  {e['slug']}: {e['status']} -> {status}")
            e["status"], e["status_label"] = status, label
            changed += 1
    except VisibilityError as exc:
        sys.exit(f"sync_manifest_visibility: VISIBILITY GATE FAILED\n  {exc}")
    print(f"{changed} status(es) {'would change' if args.dry_run else 'updated'}")
    if not args.dry_run and changed:
        MANIFEST.write_text(json.dumps(data, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
