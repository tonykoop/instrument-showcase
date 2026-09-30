"""Live GitHub repo-visibility lookup for the public catalog gate.

Rule (Tony, 2026-09-29): an instrument is shown publicly only if its GitHub repo
(tonykoop/<slug>) is PUBLIC right now. Anything else -- PRIVATE, INTERNAL, repo
missing, gh failure, unparseable answer -- is an error, never a silent default.
"""
import json
import subprocess

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
