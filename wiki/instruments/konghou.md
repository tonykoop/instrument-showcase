---
title: Modern Konghou
slug: konghou
wiki_type: instrument
status: active
sources:
  - path: ../../../strings/konghou/README.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/konghou/design.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/konghou/capstone-manifest.json
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/konghou/cultural-provenance.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/konghou/public-readiness.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/konghou/risks.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/konghou/validation.csv
    kind: spreadsheet
    last_seen: 2026-06-19
  - path: ../../../strings/konghou/string-schedule.csv
    kind: spreadsheet
    last_seen: 2026-06-19
  - path: ../../../strings/konghou/konghou-starter.wl
    kind: wolfram
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/harp-lute
  - fabrication/frame-load-analysis
  - synthesis/public-release-blockers
  - synthesis/wolfram-model-patterns
open_questions:
  - "Has KGH-MULE-01 (single-row structural mule) been built and proof-loaded?"
  - "What measured string speaking lengths and tensions exist for the mule build?"
  - "Has the frame/soundboard/pin/anchor load ledger been reviewed with real string data?"
  - "Has the proof-load coupon plan (proof-load-coupon-plan.md) been executed?"
  - "What cultural-review outcome has been recorded in cultural-provenance.md?"
  - "Is the public-readiness.md gate ledger current, and which gates remain blocked?"
answers_filed: []
last_ingest: 2026-06-19
last_lint: 2026-06-19
review_due: 2026-09-19
tags:
  - instrument
  - string
  - harp-lute
  - konghou
  - chinese
  - double-row
  - private-review
---

# Modern Konghou

## Overview

The `konghou` repo is an L2 V5 build-packet candidate for a modern paired-course konghou-inspired instrument. The packet follows a mule-first strategy: build `KGH-MULE-01` (single-row structural mule) first, execute proof-load checks, then promote to the full double-row `KGH-PAIR-01` only after mule gates pass. The repo explicitly identifies itself as a modern engineering prototype, not a historically authoritative konghou.

Primary repo links:

- [README](../../../../strings/konghou/README.md)
- [Design notes](../../../../strings/konghou/design.md)
- [Cultural provenance](../../../../strings/konghou/cultural-provenance.md)
- [Public readiness](../../../../strings/konghou/public-readiness.md)
- [Risks](../../../../strings/konghou/risks.md)
- [Capstone manifest](../../../../strings/konghou/capstone-manifest.json)

## Current Status

- Release state: private review / L2 scaffold.
- Build target: `KGH-MULE-01` single-row mule first; `KGH-PAIR-01` double-row only after mule gate passes.
- Acoustic class: [[acoustic-classes/harp-lute]] — double-row paired-course plucked instrument; vertical harp-style frame.
- Fabrication authority: none yet. DXF and OpenSCAD files are source-only scaffolds for mule review and load-path planning.
- Wolfram model: `konghou-starter.wl` is local (Mersenne-Taylor tension starter). Live cloud embed now active via Public-Execute URL.
- `public-readiness.md` is the single source of truth for readiness level; it overrides any other file in the repo.
- Release blockers: mule proof-load, measured string data, reviewed CAD/DXF, cultural review, public-readiness gate ledger.

## Source Notes

- [repo] [README](../../../../strings/konghou/README.md) — mule-first strategy; `KGH-MULE-01` (single-row mule) is the only authorized first build; `KGH-PAIR-01` blocked until mule gates pass. Fabrication authority: none yet — DXF and SCAD files are load-path planning scaffolds only.
- [repo] [Design notes](../../../../strings/konghou/design.md) — family intent, staged build path, assumptions, and promotion rules.
- [repo] [Cultural provenance](../../../../strings/konghou/cultural-provenance.md) — authority statement, source gaps, and cultural-review gate; engineering prototype scope only.
- [repo] [Public readiness](../../../../strings/konghou/public-readiness.md) — binding readiness ladder, gate ledger, and polish-claim block list; single source of truth for readiness level.
- [spreadsheet] [String schedule](../../../../strings/konghou/string-schedule.csv) — starting target schedule with measured-data columns left for the build log.
- [spreadsheet] [Validation](../../../../strings/konghou/validation.csv) — proof-load and measured-update gates.
- [wolfram] [Wolfram starter](../../../../strings/konghou/konghou-starter.wl) — Mersenne-Taylor tension starter; Public-Execute cloud URL now live at `wolframcloud.com`.

## Design Knowledge

The konghou is a vertical double-row harp-like instrument with paired courses (two strings per note, one on each side of the soundboard). The modern reinterpretation in this packet preserves the paired-course concept while using a modern engineering scaffold. The mule strategy isolates structural risk: the single-row mule proves the frame load path and string attachment before the full double-row build is committed.

Frame load path: string tension transfers from pins on the soundboard, through the soundboard and frame structure (neck, pillar or column, and base), to the anchor points. Per the `frame-load-ledger.csv`, all calculated fields remain blocked until supplier or measured unit weights exist. The `proof-load-coupon-plan.md` defines a coupon test sequence before paired-course scaling is permitted.

String schedule is Mersenne-Taylor governed:

```text
f = (1 / (2L)) * sqrt(T / mu)
```

All tension values in `tension-study.csv` are calculated from guesses; they remain blocked until real string data replaces the scaffold assumptions.

## Acoustic And Structural Model

The soundboard transfers string load laterally to the frame and acts as the primary acoustic radiator. Frame section sizing must account for the cantilever moment from the neck (analogous to a harp neck) and the column compression in the pillar. The `frame-string-scaling.csv` defines gate conditions for scaling from mule to paired-course, covering frame section, soundboard transfer, and row spacing.

## Build And Validation Logic

Mule-first gate sequence (from README):

1. Read `design.md`.
2. Build only `KGH-MULE-01`, the single-row structural mule.
3. Run proof-load checks in `validation.csv` and `proof-load-coupon-plan.md`.
4. Update `string-schedule.csv` with measured speaking lengths, real string data, and measured tensions.
5. Promote to `KGH-PAIR-01` only after every mule gate passes.

`public-readiness.md` is the binding gate ledger. If any other file disagrees about readiness level, `public-readiness.md` wins.

## Release And Provenance Constraints

This is a modern engineering prototype, not a culturally authoritative konghou or historical reconstruction. See `cultural-provenance.md` for the authority statement and source gaps. The `public-readiness.md` polish-claim block list defines what may NOT be stated in any public copy. Cultural review is a required gate before any public release claim.

## Cross-Links

- [[acoustic-classes/harp-lute]]
- [[fabrication/frame-load-analysis]]
- [[fabrication/bridge-and-string-layout]]
- [[synthesis/public-release-blockers]]
- [[synthesis/wolfram-model-patterns]]

## Open Questions

1. Has `KGH-MULE-01` been built, and have proof-load checks been executed per `proof-load-coupon-plan.md`?
2. What measured string speaking lengths and tensions exist from a mule or reference instrument?
3. Has the frame/soundboard/pin/anchor load ledger been reviewed with real (not scaffold) string data?
4. What cultural-review outcome has been recorded in `cultural-provenance.md`?
5. Which gates in `public-readiness.md` are currently blocked vs. cleared?
6. Has the `tension-study.csv` been updated from scaffold assumptions to measured or published string data?

## Maintenance Notes

Next ingest should pull in mule proof-load results, measured string data, and cultural-review outcome. `public-readiness.md` is the gate ledger; update [[synthesis/public-release-blockers]] when public-readiness gates clear.
