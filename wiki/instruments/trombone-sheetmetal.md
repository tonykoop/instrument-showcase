---
title: Trombone Sheet-Metal Blueprint
slug: trombone-sheetmetal
wiki_type: instrument
status: active
sources:
  - path: ../../../../brass/trombone-sheetmetal/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/cylindrical-bore-brass
  - fabrication/sheet-metal-brass
  - fabrication/precision-slide
open_questions:
  - "What supplier provides precision drawn tubing at 0.500 in bore suitable for lapping to slide tolerances?"
  - "What is the target slide friction spec and the lap/alignment jig design?"
  - "How is the bell tail (sheet-metal) joined to the bought slide tubing without bore-step discontinuity?"
  - "No capstone-manifest.json — not yet at V5 build-packet gate."
last_ingest: 2026-06-19
tags: [instrument, brass, trombone, slide, small-bore, valveless, brasswind]
---

# Trombone Sheet-Metal Blueprint

## Overview

A small-bore Bb tenor trombone with hand slide. Bell, tail, braces, and slide bracket are designed for sheet-metal shop authoring; precision slide tubes are bought drawn tubing and lap/alignment-aligned as a controlled sub-assembly. Seven slide positions cover the chromatic scale from the open Bb.

- **Family:** brasswind (Bb tenor trombone, valveless slide)
- **Bore:** 0.500 in through cylindrical sections and slide path
- **Bell rim:** 8.0 in
- **Slide positions:** 7
- **Materials:** yellow brass sheet (bell, tail, braces); bought precision-drawn tubing (slide)
- **Status:** L2 V5 blueprint — not a measured, CAD-reviewed, or build-ready trombone

Primary repo links:
- [README](../../../../brass/trombone-sheetmetal/README.md)
- [Design notes](../../../../brass/trombone-sheetmetal/design.md)
- [Tuning notes](../../../../brass/trombone-sheetmetal/tuning-notes.md)
- [Wolfram model](../../../../brass/trombone-sheetmetal/trombone-sheetmetal-starter.wl)
- [Fabrication plan](../../../../brass/trombone-sheetmetal/fabrication-plan.md)

## Current Status

- Release state: L2 V5 build-packet candidate — blueprint and prototype-planning packet; not fabrication-ready.
- Library family: brass.
- Acoustic class: cylindrical bore brasswind (trombone).
- Wolfram state: first-order acoustic and slide-extension model (`.wl`) present; Wolfram Cloud Public-Execute URL available.
- CAD state: SolidWorks plan and Master Layout Part approach described; no confirmed `.glb`.
- No `capstone-manifest.json`.

## Source Notes

- [README](../../../../brass/trombone-sheetmetal/README.md) — design thesis (three coupled systems: acoustic length + sheet-metal bell/tail/braces + precision-bought slide), targets (0.500 in bore, 8 in bell, 7 positions), packet map, current readiness statement.

Artifacts not ingested: `design.md`, `parameters.csv`, `tuning-notes.md`, `validation.csv`, `bom.csv`.

## Design Knowledge

The design explicitly splits the trombone into sub-systems by fabrication authority:
- **Sheet-metal parts** (bell, tail, braces, slide bracket): designed for sprint-shop methods — rolled brass, silver-brazed seams, lofted-bend bell flare.
- **Precision slide**: bought drawn tubing, lapped and aligned on a dedicated jig. This is the highest-risk sub-system — straightness, parallelism, lap fit, stocking geometry, and low friction must be proven before any build-ready claim.
- **Acoustic model**: Wolfram starter model covers acoustic length (Bb fundamental), slide extension per position, and harmonic stack.

Slide position math and harmonic stack are in `tuning-notes.md` with placeholder measured-data columns in `validation.csv`.

## Cross-Links

- [[acoustic-classes/cylindrical-bore-brass]]
- [[fabrication/sheet-metal-brass]]
- [[fabrication/precision-slide]]

## Open Questions

1. What supplier provides precision drawn tubing at 0.500 in bore suitable for lapping?
2. What is the target slide friction spec and the lap/alignment jig design?
3. How is the sheet-metal bell tail joined to the bought slide tubing without bore-step discontinuity?
4. No `capstone-manifest.json` — not yet at V5 build-packet gate.

## Maintenance Notes

First ingest from README only. Next pass: read `tuning-notes.md` for slide-position math, `design.md` for bore profile detail, and `validation.csv` for slide friction and intonation measurement gates.
