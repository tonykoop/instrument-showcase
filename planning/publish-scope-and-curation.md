# Publish scope & curation policy

_Issue #19. Defines what is allowed onto the public GitHub Pages site and how the
set is curated. Enforced mechanically by the pre-publish scope gate in
`scripts/check_site.py` (issue #24)._

## Principle: public is sticky

The source designs live in ~150 **private** instrument repos. Publishing is a
one-way door — once a design, render, or drawing is on a public Pages site it
must be treated as released, even if later deleted. So the default is **private**,
and an instrument joins the public set only by an explicit, reviewed decision.

## The curated set = `scripts/published.txt`

The public set is the newline-delimited list of slugs in
`scripts/published.txt`. In `--base-url` publish mode, **only** these slugs get
live links + images on the library; every other card renders as a clean,
non-clickable text card (no 404s, no leaked images) and upgrades automatically
when added to the list.

**First curated subset:** `ashiko-drum-workshop` + the Native American flutes
(`flutes`). These are the most complete, clearly-releasable builds.

## The scope gate (enforced, not advisory)

`scripts/check_site.py` runs before every publish and **fails the build** if any
slug in `published.txt` has manifest `status` of `private` or `blocked`
(`release_gate.public_candidate: false` or `required_before_public` set). This is
the single most important gate — it prevents an unreviewed or gate-blocked design
from slipping public. `scripts/build.sh` runs the gate automatically.

As of this writing the gate holds back 21 release-`blocked` slugs that are
otherwise polished (incl. `kora`, `ngoni`, `pipa` — explorer-complete but not yet
release-cleared). Completeness (a good explorer) is **orthogonal** to release
clearance (cleared to go public); both are required.

## How to add an instrument to the public set

1. **Clear its release gate** in the instrument repo's `capstone-manifest.json`:
   `release_gate.public_candidate: true` and no `required_before_public` items
   (i.e. IP / cultural-provenance / safety review done).
2. `python3 scripts/generate_library.py` to refresh the manifest/status.
3. Add the slug to `scripts/published.txt`.
4. `./scripts/build.sh` — the scope gate must pass (exit 0) before publishing.

## Out of scope (never published without separate sign-off)

- Patent-candidate or trade-secret designs.
- Client/employer-owned work (e.g. anything under a confidentiality notice).
- Raw full-resolution photo/CAD source (only web-optimized derivatives ship — see #21).

## Publish model

Each instrument publishes from its **own** repo's GitHub Pages site; the showcase
library links to `{base-url}/{slug}/` via `generate_library.py --base-url`. The
showcase repo itself publishes the library/index/wiki shell. (The alternative
self-contained `/docs` bundle is tracked in #20.)
