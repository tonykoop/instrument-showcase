"""Live GitHub repo-visibility lookup for the public catalog gate.

Rule (Tony, 2026-09-29): an instrument is shown publicly only if its GitHub repo
(tonykoop/<slug>) is PUBLIC right now. Anything else -- PRIVATE, INTERNAL, repo
missing, gh failure, unparseable answer -- is an error, never a silent default.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

OWNER = "tonykoop"


class VisibilityError(RuntimeError):
    pass


def repo_visibility(slug, owner=OWNER):
    try:
        r = subprocess.run(["gh", "repo", "view", f"{owner}/{slug}", "--json", "visibility"],
                           capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.SubprocessError) as exc:
        raise VisibilityError(f"{owner}/{slug}: gh failed to run: {exc}") from exc
    if r.returncode != 0:
        raise VisibilityError(f"{owner}/{slug}: gh repo view failed: {r.stderr.strip()}")
    try:
        vis = json.loads(r.stdout)["visibility"]
    except (ValueError, KeyError, TypeError) as exc:
        raise VisibilityError(f"{owner}/{slug}: unparseable visibility: {r.stdout!r}") from exc
    if vis not in ("PUBLIC", "PRIVATE", "INTERNAL"):
        raise VisibilityError(f"{owner}/{slug}: unexpected visibility {vis!r}")
    return vis


def public_slugs(slugs, lookup=repo_visibility):
    """Return (public, non_public) lists. Raises VisibilityError if any lookup fails."""
    errors, public, hidden = [], [], []
    for s in slugs:
        try:
            (public if lookup(s) == "PUBLIC" else hidden).append(s)
        except VisibilityError as exc:
            errors.append(str(exc))
    if errors:
        raise VisibilityError(f"cannot determine visibility for {len(errors)} entr(ies):\n  " + "\n  ".join(errors))
    return public, hidden


def check_published(published_file, lookup=None):
    """Return the non-PUBLIC slugs listed in published_file. Raises VisibilityError
    if any lookup fails, so an unknown answer can never pass the gate."""
    slugs = [s.strip() for s in Path(published_file).read_text().split() if s.strip()]
    return public_slugs(slugs, lookup or repo_visibility)[1]


def main(argv=None):
    ap = argparse.ArgumentParser(description="Fail if any published slug's repo is not PUBLIC")
    ap.add_argument("--published", default=str(Path(__file__).with_name("published.txt")))
    args = ap.parse_args(argv)
    try:
        hidden = check_published(args.published)
    except VisibilityError as exc:
        print(f"FAIL visibility: {exc}", file=sys.stderr)
        return 3
    if hidden:
        print(f"FAIL visibility: published slug(s) not PUBLIC: {', '.join(hidden)}", file=sys.stderr)
        return 1
    print("ok   visibility: every published slug is PUBLIC")
    return 0


if __name__ == "__main__":
    sys.exit(main())
