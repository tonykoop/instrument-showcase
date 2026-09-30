"""Live GitHub repo-visibility lookup for the public catalog gate.

Rule (Tony, 2026-09-29): an instrument is shown publicly only if its GitHub repo
(tonykoop/<slug>) is PUBLIC right now. Anything else -- PRIVATE, INTERNAL, repo
missing, gh failure, unparseable answer -- is an error, never a silent default.
"""
import argparse
import json
import re
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


STATUS_LABELS = {"public": "Public", "private": "Private"}


def reconcile_status(status, status_label, vis):
    """Status pill implied by live visibility. 'blocked' is a release blocker, not a
    visibility, so it is left in place. Returns (status, status_label)."""
    if status == "blocked":
        return status, status_label
    want = "public" if vis == "PUBLIC" else "private"
    return want, STATUS_LABELS[want]  # label normalised too: a stale hand-edited one cannot survive


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


def shipped_slugs(published_file, docs_dir):
    """Every slug the site ships: published.txt, the cards in docs/library.html and the
    explorer directories under docs/instruments/<family>/<slug>/."""
    docs = Path(docs_dir)
    slugs = {s.strip() for s in Path(published_file).read_text().split() if s.strip()}
    lib = docs / "library.html"
    if lib.is_file():
        slugs |= set(re.findall(r'<p class="card-slug"><code>([^<]+)</code>',
                                lib.read_text(encoding="utf-8", errors="ignore")))
    slugs |= {d.name for d in docs.glob("instruments/*/*") if d.is_dir()}
    return sorted(slugs)


def check_published(published_file, lookup=None, docs_dir=None):
    """Return the non-PUBLIC slugs among everything shipped. Raises VisibilityError
    if any lookup fails, so an unknown answer can never pass the gate."""
    slugs = shipped_slugs(published_file, docs_dir or Path(published_file).parent.parent / "docs")
    return public_slugs(slugs, lookup or repo_visibility)[1]


def main(argv=None):
    ap = argparse.ArgumentParser(description="Fail if any published slug's repo is not PUBLIC")
    ap.add_argument("--published", default=str(Path(__file__).with_name("published.txt")))
    ap.add_argument("--docs", default=str(Path(__file__).resolve().parent.parent / "docs"))
    args = ap.parse_args(argv)
    try:
        hidden = check_published(args.published, docs_dir=args.docs)
    except VisibilityError as exc:
        print(f"FAIL visibility: {exc}", file=sys.stderr)
        return 3
    if hidden:
        print(f"FAIL visibility: published slug(s) not PUBLIC: {', '.join(hidden)}", file=sys.stderr)
        return 1
    print("ok   visibility: every shipped slug (published.txt, library cards, explorer dirs) is PUBLIC")
    return 0


if __name__ == "__main__":
    sys.exit(main())
