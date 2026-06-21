#!/usr/bin/env bash
# build.sh — one-command local rebuild + pre-publish gate for the Studio
# Explorers site (issues #20, #21, #22, #24). Runs locally where the private
# instrument repos are cloned; pushes nothing.
#
#   ./scripts/build.sh                 # regenerate library + manifest + pages bundle, then gate
#   ./scripts/build.sh --explorers     # also (re)generate scaffold explorer.generated.html
#   ./scripts/build.sh --skip-bundle   # skip the /docs pages bundle step (faster for library-only)
#   ./scripts/build.sh --base-url https://tonykoop.github.io/instrument-showcase \
#                      --published scripts/published.txt   # publish-mode library
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$HERE/.."

DO_EXPLORERS=0
SKIP_BUNDLE=0
GEN_ARGS=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    --explorers)   DO_EXPLORERS=1; shift ;;
    --skip-bundle) SKIP_BUNDLE=1;  shift ;;
    *) GEN_ARGS+=("$1"); shift ;;
  esac
done

echo "==> [1/4] regenerating library.html + library-manifest.json"
python3 scripts/generate_library.py "${GEN_ARGS[@]}"

if [[ "$DO_EXPLORERS" -eq 1 ]]; then
  echo "==> [2/4] (re)generating explorer.generated.html for scaffold / in-progress repos"
  python3 scripts/generate_explorer_v2.py --all --only-scaffold
else
  echo "==> [2/4] skipping explorer regen (pass --explorers to include it)"
fi

if [[ "$SKIP_BUNDLE" -eq 1 ]]; then
  echo "==> [3/5] skipping /docs pages bundle (--skip-bundle set)"
  echo "==> [4/5] skipping image QA gate (no bundle built)"
else
  echo "==> [3/5] building self-contained /docs pages bundle (#20/#21)"
  python3 scripts/build_pages.py
  echo "==> [4/5] image QA gate: duplicates + blanks + bad-aspect check (#25)"
  python3 scripts/qa_images.py
fi

echo "==> [5/5] pre-publish health check"
python3 scripts/check_site.py

echo "==> build complete"
