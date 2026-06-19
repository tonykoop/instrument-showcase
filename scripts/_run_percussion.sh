#!/usr/bin/env bash
# Driver: generate v2 explorer pages for all percussion instruments, one PR each.
set -u
REPO="tonykoop/instrument-showcase"
ISSUE=29

declare -A TITLES=(
  ["ashiko-drum-workshop"]="Ashiko Drum Workshop"
  ["bass-surface-drum"]="Bass Surface Drum"
  ["bowed-frame-drum"]="Bowed Frame Drum"
  ["cajon"]="Cajon Family Public-Review Prototype"
  ["compact-drum-kit"]="Compact Drum Kit"
  ["conga"]="Conga"
  ["djembe"]="Djembe Bare-Bones Starter Packet"
  ["dundun"]="Dundun Trio Bare-Bones Starter Packet"
  ["frame-drum"]="Frame Drum V5 Explorer Packet"
  ["modular-pedestal-drum-stack"]="Modular Pedestal Drum Stack"
  ["pitched-bell-cajon"]="Pitched Bell Cajon"
  ["sheet-metal-djembe"]="Sheet Metal Djembe"
  ["sheet-metal-talking-drum"]="Sheet Metal Talking Drum"
  ["timpani-sheetmetal"]="Timpani Sheetmetal"
  ["tunable-snare-frame-array"]="Tunable Snare Frame Array"
  ["udu"]="Slip-Cast Ceramic Udu Drum Family - V5 Explorer Readiness"
)

ORDER=(ashiko-drum-workshop bass-surface-drum bowed-frame-drum cajon compact-drum-kit conga djembe dundun frame-drum modular-pedestal-drum-stack pitched-bell-cajon sheet-metal-djembe sheet-metal-talking-drum timpani-sheetmetal tunable-snare-frame-array udu)
# These 4 have no repo on disk -> reported as skipped (no source)
MISSING=(ceramic-tongue-drum steel-tongue-drum tongue-drum wood-shell-tongue-drum)

CREATED=()
SKIPPED=()

for slug in "${ORDER[@]}"; do
  echo "=================================================================="
  echo ">>> $slug"
  branch="sprint/ov-instshow-percussion-$slug"

  git checkout -B "$branch" origin/main >/dev/null 2>&1 || { echo "SKIP $slug: checkout failed"; SKIPPED+=("$slug (checkout failed)"); continue; }

  if ! python3 scripts/make_docs_explorer.py --slug "$slug" --family-dir percussion --issue "$ISSUE"; then
    echo "SKIP $slug: generation failed"
    SKIPPED+=("$slug (generation failed)")
    git checkout -- . >/dev/null 2>&1
    continue
  fi

  git add "docs/instruments/percussion/$slug/" >/dev/null 2>&1
  if git diff --cached --quiet; then
    echo "SKIP $slug: no changes to commit"
    SKIPPED+=("$slug (no changes)")
    continue
  fi

  git commit -m "feat(#$ISSUE): add v2 explorer for $slug (Percussion)" >/dev/null 2>&1 || { echo "SKIP $slug: commit failed"; SKIPPED+=("$slug (commit failed)"); continue; }

  if ! git push -u origin "$branch" >/dev/null 2>&1; then
    echo "SKIP $slug: push failed"
    SKIPPED+=("$slug (push failed)")
    continue
  fi

  title="${TITLES[$slug]}"
  body="Adds v2 Explorer page for $slug: embedded Wolfram acoustic model where available, rendered concept gallery, BOM table, and release-gate summary.

Refs #$ISSUE"

  if pr_url=$(gh pr create --repo "$REPO" \
      --title "feat(#$ISSUE): $title — v2 Explorer (Percussion)" \
      --body "$body" --head "$branch" --base main 2>&1); then
    echo "PR: $pr_url"
    CREATED+=("$slug -> $pr_url")
  else
    echo "SKIP $slug: PR creation failed: $pr_url"
    SKIPPED+=("$slug (PR failed: $pr_url)")
  fi
done

for slug in "${MISSING[@]}"; do
  SKIPPED+=("$slug (no source repo on disk)")
done

echo ""
echo "=================== SUMMARY ==================="
echo "CREATED (${#CREATED[@]}):"
for c in "${CREATED[@]}"; do echo "  - $c"; done
echo "SKIPPED (${#SKIPPED[@]}):"
for s in "${SKIPPED[@]}"; do echo "  - $s"; done
