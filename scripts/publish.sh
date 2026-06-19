#!/usr/bin/env bash
# publish.sh — Heifer Zephyr instrument publisher (WSL/Linux port of publish.ps1, issue #22)
#
# One-command flow to publish the public instrument library to GitHub Pages.
# Runs locally where the private instrument repos are cloned; needs the GitHub CLI.
#
# One-time setup:
#   1. Install the GitHub CLI:  https://cli.github.com   (Ubuntu/WSL: sudo apt install gh)
#   2. Authenticate:            gh auth login
#
# Usage:
#   ./scripts/publish.sh                  # regenerate library + push it live (safe default)
#   ./scripts/publish.sh --make-public    # ALSO flip each repo in published.txt to public
#                                         #   and enable GitHub Pages (one-time, irreversible)
#   ./scripts/publish.sh --workspace ~/Documents/GitHub
#   ./scripts/publish.sh --dry-run        # show what would happen, change nothing
#
# Difference vs publish.ps1: the irreversible "make repos public + enable Pages"
# step is OPT-IN here (--make-public) instead of always-on, so a routine library
# refresh can't accidentally change repo visibility. Everything else mirrors the
# proven PowerShell flow.
set -euo pipefail

OWNER="tonykoop"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SHOWCASE="$(cd "$HERE/.." && pwd)"
WORKSPACE="${WORKSPACE:-$HOME/Documents/GitHub}"
PUBLISHED="$SHOWCASE/scripts/published.txt"
GEN="$SHOWCASE/scripts/generate_library.py"
BASE_URL="https://tonykoop.github.io"
MAKE_PUBLIC=0
DRY_RUN=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --make-public) MAKE_PUBLIC=1; shift ;;
    --dry-run)     DRY_RUN=1; shift ;;
    --workspace)   WORKSPACE="$2"; shift 2 ;;
    --base-url)    BASE_URL="$2"; shift 2 ;;
    -h|--help)     sed -n '2,21p' "$0"; exit 0 ;;
    *) echo "Unknown argument: $1" >&2; exit 2 ;;
  esac
done

run() { if [[ "$DRY_RUN" -eq 1 ]]; then echo "DRY-RUN: $*"; else "$@"; fi; }

# Resolve python (python3 preferred), and require an authenticated gh.
PY="python3"; command -v "$PY" >/dev/null 2>&1 || PY="python"
command -v "$PY" >/dev/null 2>&1 || { echo "python not found on PATH" >&2; exit 1; }
command -v gh   >/dev/null 2>&1 || { echo "GitHub CLI (gh) not found. Install from https://cli.github.com then run: gh auth login" >&2; exit 1; }
gh auth status  >/dev/null 2>&1 || { echo "gh is not authenticated. Run: gh auth login" >&2; exit 1; }
[[ -f "$PUBLISHED" ]] || { echo "published.txt not found at $PUBLISHED" >&2; exit 1; }

if [[ "$MAKE_PUBLIC" -eq 1 ]]; then
  echo "== Step 1: make repos public + enable Pages (one-time) =="
  while IFS= read -r slug || [[ -n "$slug" ]]; do
    slug="$(echo "$slug" | tr -d '[:space:]')"
    [[ -z "$slug" || "$slug" == \#* ]] && continue
    echo "  publishing $slug"
    run gh repo edit "$OWNER/$slug" --visibility public --accept-visibility-change-consequences || true
    run gh api -X POST "repos/$OWNER/$slug/pages" -f "source[branch]=main" -f "source[path]=/" >/dev/null 2>&1 || true
  done < "$PUBLISHED"
else
  echo "== Step 1: skipped (pass --make-public to flip repo visibility + enable Pages) =="
fi

echo "== Step 2: regenerate library =="
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
run "$PY" "$GEN" \
  --workspace "$WORKSPACE" \
  --base-url "$BASE_URL" \
  --published "$PUBLISHED" \
  --output-html "$TMP/hz_library.html" \
  --output-data "$TMP/hz_manifest.json"
if [[ "$DRY_RUN" -eq 0 && ! -f "$TMP/hz_library.html" ]]; then
  echo "Generation failed — no library.html produced." >&2; exit 1
fi

echo "== Step 3: push library live (temp clone of $OWNER.github.io, avoids sync lock) =="
SITE="$TMP/tksite"
run gh repo clone "$OWNER/$OWNER.github.io" "$SITE"
if [[ "$DRY_RUN" -eq 0 ]]; then
  cp "$TMP/hz_library.html" "$SITE/library.html"
  git -C "$SITE" add library.html
  if git -C "$SITE" diff --cached --quiet; then
    echo "  library.html unchanged — nothing to push."
  else
    git -C "$SITE" commit -m "Refresh instrument library"
    git -C "$SITE" push
  fi
fi

echo ""
echo "Done. Live at $BASE_URL/library.html in about a minute."
