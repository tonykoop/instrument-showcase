---
title: Irish Flute
slug: irish-flute
wiki_type: instrument
status: active
sources:
  - path: ../../../woodwind/irish-flute/README.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/irish-flute/design.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/irish-flute/validation.csv
    kind: spreadsheet
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/open-pipe-cylindrical
  - fabrication/reamed-hardwood-tube
  - synthesis/embouchure-tuning
  - synthesis/wolfram-model-patterns
open_questions:
  - "Has a D4 prototype been built and first-sound validated?"
  - "Have tone-hole positions been confirmed from undersize against actual pitch measurements?"
  - "Has the embouchure cut been optimized for pitch stability and tone?"
  - "Have validation.csv rows been populated with measured bore and tuning data?"
  - "Has source availability been verified for hardwood tube stock?"
answers_filed: []
last_ingest: 2026-06-19
last_lint: 2026-06-19
review_due: 2026-09-19
tags:
  - instrument
  - woodwind
  - transverse-flute
  - irish-flute
  - keyless
  - open-pipe
  - cylindrical
  - hardwood
---

# Irish Flute

## Overview

The `irish-flute` repo is an L2 V5 build-packet candidate for a keyless D4 Irish flute — a six-hole wooden transverse flute with a cylindrical first-pass bore, simple embouchure, and open-pipe acoustic model. No prototype measurements, render pass, or source-availability check has been completed.

Primary repo links:

- [README](../../../../woodwind/irish-flute/README.md)
- [Design](../../../../woodwind/irish-flute/design.md)
- [Design table](../../../../woodwind/irish-flute/irish-flute-design-table.xlsx)
- [Validation](../../../../woodwind/irish-flute/validation.csv)
- [Jig decisions](../../../../woodwind/irish-flute/jig-decision.md)

## Current Status

- Release state: L2 V5 build-packet candidate; no physical prototype.
- Build target: D4 prototype (six-hole keyless transverse flute).
- Acoustic class: [[acoustic-classes/open-pipe-cylindrical]] — open-open cylindrical pipe model (instrument-maker v4.3 baseline).
- CAD: layout SVG starter (`drawings/irish-flute-d4-layout.svg`); OpenSCAD starter in `cad/`.
- Wolfram model: `irish-flute-starter.wl` live at Public-Execute cloud URL.
- Release blockers: D4 prototype build; tone-hole position confirmation; embouchure cut optimization.

## Design Snapshot

| Parameter | D4 prototype | Status |
|-----------|-------------|--------|
| Fundamental | D4, 293.66 Hz | target |
| Bore ID | 0.750 in | assumption |
| Wall | 0.125 in | assumption |
| Effective acoustic length | 23.08 in | calculated |
| Physical bore length | 22.63 in | first-order |
| Blank length | 24.50 in | includes trim/setup allowance |
| Tone holes | 6 front holes | first-order |
| Construction | Reamed hardwood tube, hand-cut embouchure | L2 plan |

## Acoustic Model

Open-open cylindrical pipe (instrument-maker v4.3). Tony's NAF K2 corrections are intentionally excluded — they are specific to Native American flutes with slow-air chambers. Irish flute tuning depends strongly on embouchure cut, bore finish, hole diameter, and player technique. All hole positions are starting geometry; confirm by tuning from undersize.

## Build Posture

This is an Irish tradition instrument. See `resources.md` for provenance and cultural attribution notes. The packet uses the cylindrical open-pipe model as a first-order scaffold. Embouchure cut and bore finish dominate intonation in practice; the Wolfram model provides the acoustic baseline, not the final geometry.

## Source Notes

- [repo] [README](../../../../woodwind/irish-flute/README.md) — D4 design snapshot, packet map, build posture, license.
- [repo] [design.md](../../../../woodwind/irish-flute/design.md) — governing model, D4 assumptions, first-order tone-hole table.
- [spreadsheet] [validation.csv](../../../../woodwind/irish-flute/validation.csv) — dimensional and tuning checks; all rows pending until first build.

## Cross-Links

- [[acoustic-classes/open-pipe-cylindrical]]
- [[fabrication/reamed-hardwood-tube]]
- [[synthesis/embouchure-tuning]]
- [[synthesis/wolfram-model-patterns]]

## Open Questions

1. Has a D4 prototype been built and first-sound validated?
2. Have tone-hole positions been confirmed from undersize against actual pitch measurements?
3. Has the embouchure cut been optimized for pitch stability and tone?
4. Have `validation.csv` rows been populated with measured bore and tuning data?
5. Has source availability been verified for hardwood tube stock?

## Maintenance Notes

Next ingest should pull in D4 prototype measurements: bore ID, actual tone-hole sizes and positions, embouchure cut geometry, and pitch deviations from target. Update [[acoustic-classes/open-pipe-cylindrical]] with any empirical bore-end correction data.
