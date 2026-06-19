---
title: Transverse Flute (Slip-Cast Ceramic)
slug: transverse-flute
wiki_type: instrument
status: active
sources:
  - path: ../../../woodwind/transverse-flute/README.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/transverse-flute/design.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/transverse-flute/validation.csv
    kind: spreadsheet
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/open-pipe-cylindrical
  - fabrication/slip-cast-ceramic
  - fabrication/3d-printed-master-plaster-mold
  - synthesis/doe-round1-ceramic-flute
  - synthesis/wolfram-model-patterns
open_questions:
  - "Has Round 1 DoE been executed (clay body, wall targets, bore profiles, embouchure geometry)?"
  - "Have shrinkage factors (X/Y/Z) been measured from fired test tiles?"
  - "Has the mold workflow been validated for long thin cylindrical sections?"
  - "Have bore/hole dimensions been corrected based on Round 1 measurements?"
  - "Has a first-sound result been recorded from any fired prototype?"
answers_filed: []
last_ingest: 2026-06-19
last_lint: 2026-06-19
review_due: 2026-09-19
tags:
  - instrument
  - woodwind
  - transverse-flute
  - slip-cast
  - ceramic
  - doe
  - open-pipe
  - experimental
---

# Transverse Flute (Slip-Cast Ceramic)

## Overview

The `transverse-flute` repo is a V5 build-packet candidate for an experimental slip-cast ceramic transverse flute family (D4, F4, G4, A4, C5). The design is not yet physically built, tuned, fired, or validated. All dimensions are first-pass engineering targets — `target`, `assumption`, or `starting point` — not proven instrument dimensions.

Primary repo links:

- [README](../../../../woodwind/transverse-flute/README.md)
- [Design](../../../../woodwind/transverse-flute/design.md)
- [DoE plan](../../../../woodwind/transverse-flute/doe-plan.md)
- [Mold workflow](../../../../woodwind/transverse-flute/mold-workflow.md)
- [Validation](../../../../woodwind/transverse-flute/validation.csv)
- [Design workbook](../../../../woodwind/transverse-flute/Slip-Cast-Transverse-Flute-Family.xlsx)

## Current Status

- Release state: V5 build-packet candidate; preparatory/laboratory phase.
- Build target: Round 1 DoE set (D4 / F4 / G4 / A4 / C5 fired targets).
- Acoustic class: [[acoustic-classes/open-pipe-cylindrical]] — open-open air column excited at embouchure edge.
- CAD: OpenSCAD body starter in `cad/`; drawings in `drawings/`; CNC in `cnc/`.
- Wolfram model: `transverse-flute-starter.wl` live at Public-Execute cloud URL.
- Release blockers: Round 1 DoE execution; shrinkage measurement; embouchure edge geometry validation.

## Why Slip-Cast Changes the Flute Problem

Slip casting adds a correction-loop that metal/wood flute making does not have:

- Master ≠ final size (must scale for shrinkage at each stage)
- X/Y/Z shrinkage may be unequal
- Long thin tubes can sag or ovalize during firing
- Wall buildup changes tone-hole chimney height
- Glaze can damage acoustic edges at embouchure, bore, or holes

Round 1 is primarily about learning the clay/process correction factors. Round 2 is where the design becomes acoustically serious.

## DoE Round 1 Plan

The `doe-plan.md` compares: clay bodies × wall targets × bore profiles × embouchure geometry × mold/drain orientation. All variables are recorded so Round 2 can isolate which factors most affect pitch accuracy and tone quality.

## Acoustic Model

Open-open cylindrical pipe (standard transverse flute model). Tone-hole positions must be recalculated after shrinkage correction from Round 1 measurements. Embouchure cut geometry is empirical — plan for iterative adjustment.

## Source Notes

- [repo] [README](../../../../woodwind/transverse-flute/README.md) — slip-cast rationale, status warning, acoustic model, DoE plan overview.
- [repo] [design.md](../../../../woodwind/transverse-flute/design.md) — governing acoustic model, first-pass targets.
- [spreadsheet] [validation.csv](../../../../woodwind/transverse-flute/validation.csv) — dimensional and tuning checks; all rows pending until Round 1 is executed.

## Cross-Links

- [[acoustic-classes/open-pipe-cylindrical]]
- [[fabrication/slip-cast-ceramic]]
- [[fabrication/3d-printed-master-plaster-mold]]
- [[synthesis/doe-round1-ceramic-flute]]
- [[synthesis/wolfram-model-patterns]]

## Open Questions

1. Has Round 1 DoE been executed?
2. Have shrinkage factors (X/Y/Z) been measured from fired test tiles?
3. Has the mold workflow been validated for long thin cylindrical sections?
4. Have bore/hole dimensions been corrected based on Round 1 measurements?
5. Has a first-sound result been recorded from any fired prototype?

## Maintenance Notes

Next ingest should pull in Round 1 DoE results: shrinkage measurements, bore dimensional changes, first-sound results, and embouchure cut observations. Update [[synthesis/doe-round1-ceramic-flute]] with any empirical data.
