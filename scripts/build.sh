#!/usr/bin/env bash
# build.sh — one-command local rebuild + pre-publish gate for the Studio
# Explorers site (issues #22, #24). Runs locally where the private instrument
# repos are cloned; pushes nothing.
#
#   ./scripts/build.sh                 # regenerate library + manifest, then gate
#   ./scripts/build.sh --explorers     # also (re)generate scaffold explorer.generated.html
#   ./scripts/build.sh --base-url https://tonykoop.github.io/instrument-showcase \
#                      --published scripts/published.txt   # publish-mode library
#
# Remaining one-command pieces tracked separately: self-contained /docs bundle
# with rewritten links (#20) and the image-optimization pass (#21); wire those
# in here once they land, before a `git push`.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$HERE/.."

DO_EXPLORERS=0
GEN_ARGS=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    --explorers) DO_EXPLORERS=1; shift ;;
    *) GEN_ARGS+=("$1"); shift ;;
  esac
done

echo "==> [1/3] regenerating library.html + library-manifest.json"
python3 scripts/generate_library.py "${GEN_ARGS[@]}"

if [[ "$DO_EXPLORERS" -eq 1 ]]; then
  echo "==> [2/3] (re)generating explorer.generated.html for scaffold / in-progress repos"
  python3 scripts/generate_explorer_v2.py --all --only-scaffold
else
  echo "==> [2/3] skipping explorer regen (pass --explorers to include it)"
fi

echo "==> [3/3] pre-publish health check"
python3 scripts/check_site.py

echo "==> build complete"
