---
title: Handpan Sheet-Metal Blueprint (D Kurd, Sheet-Metal-First)
slug: handpan-sheetmetal
wiki_type: instrument
status: active
sources:
  - path: ../../../../idiophones/handpan-sheetmetal/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - instruments/handpan
  - acoustic-classes/tuned-shell-idiophone
  - fabrication/sheet-metal-spinning
open_questions:
  - "What blank prep (thickness, diameter, edge preparation) and sinking sequence is specified?"
  - "What forming fixture (sand bag, deep-dish form, post die) is recommended for the initial sinking pass?"
  - "What coupon validation gates exist before the tone-field forming step?"
  - "How does the equator joining method (brazing, welding, mechanical lock) affect acoustic behavior?"
last_ingest: 2026-06-19
tags: [instrument, idiophone, handpan, D-kurd, sheet-metal, hammered, nitrided, blueprint, 530mm, L2]
---

# Handpan Sheet-Metal Blueprint — D Kurd, Sheet-Metal-First

## Overview

A sheet-metal-first blueprint for a 9-note D Kurd handpan, complementing the sibling research packet. This repo focuses on the execution path: blank prep, sinking, dishing, tone-field forming, nitriding, equator joining, and the validation gates a human tuner needs before the instrument can be called playable.

- **Family:** idiophone / tuned steel shell instrument
- **Scale:** D Kurd 9, A4 = 440 Hz (D3 Ding + A3, Bb3, C4, D4, E4, F4, G4, A4)
- **Shell:** 530 mm outside diameter, 240 mm total height
- **Material:** 1.0 mm cold-rolled mild steel preferred; 1.2 mm DC04 alternate
- **Finish path:** nitride after rough forming, before final tuning
- **Status:** L2 V5 build-packet candidate — shop review, template layout, material sourcing, coupon planning; not build-ready recipe

Primary repo links:
- [README](../../../../idiophones/handpan-sheetmetal/README.md)
- [Design notes](../../../../idiophones/handpan-sheetmetal/design.md)
- [Parameters](../../../../idiophones/handpan-sheetmetal/parameters.csv)
- [Validation](../../../../idiophones/handpan-sheetmetal/validation.csv)

## Current Status

- Release state: L2 V5 build-packet candidate — v0.1 blueprint. CAD layouts, tone-field sizes, and model predictions remain planning authority only until a real shell is formed, nitrided, measured, tuned, rested, and reviewed by a competent handpan tuner.
- Library family: idiophone.
- Acoustic class: tuned shell idiophone (handpan, sheet-metal execution).
- Wolfram state: acoustic starter model present; Wolfram Cloud Public-Execute URL available.
- CAD state: SolidWorks/CNC/drawing briefs defined.

## Source Notes

- [README](../../../../idiophones/handpan-sheetmetal/README.md) — shell targets (530 mm, 240 mm height, 1.0 mm CRS, D Kurd 9), fabrication process (blank prep → sinking → dishing → tone-field forming → nitriding → equator joining), authority boundary (sibling handpan/ supplies acoustic target; this repo supplies sheet-metal execution surface).

Artifacts not ingested: `design.md`, `parameters.csv`, `fabrication-plan.md`, `validation.csv`, `risks.md`.

## Design Knowledge

The sheet-metal handpan execution path:
1. **Blank prep**: cut circular blanks from 1.0 mm CRS, edge-dress, mark centers
2. **Sinking**: hammer-sink the top shell into a concave form (sand-bag/log-round/post die) to achieve the dome shape
3. **Dishing**: refine the shell profile, approach target dome height (240 mm / 2 = 120 mm per shell half)
4. **Tone-field forming**: mark dimple positions, sink tone-field ellipses with a rounded forming hammer and profile template
5. **Nitriding**: send to a commercial nitriding shop (gas or plasma) — hardens surface, reduces future drift
6. **Tuning pass**: strike each tone field, FFT, hammer-correct — iterative until fundamental + octave + fifth partials are within target
7. **Equator joining**: braze or weld the top and bottom shells at the equator rim; evaluate acoustic effect

The 530 mm diameter (vs handpan 21 in = 533 mm) is slightly smaller — a sheet-metal-friendly round number. The 240 mm height is the standard two-shell stacked height.

Related: [[instruments/handpan]] (acoustic target source — D Kurd partial table, validation loop, risks), [[fabrication/sheet-metal-spinning]] (spinning may be an alternate to hammer-sinking for the initial dome form).

## Cross-Links

- [[instruments/handpan]]
- [[acoustic-classes/tuned-shell-idiophone]]
- [[fabrication/sheet-metal-spinning]]

## Open Questions

1. What blank prep and sinking sequence is specified?
2. What forming fixture is recommended for the initial sinking pass?
3. What coupon validation gates exist before tone-field forming?
4. How does the equator joining method affect acoustic behavior?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for the execution thesis and `fabrication-plan.md` for the forming sequence. Compare `validation.csv` with the sibling handpan/ measurement template.
