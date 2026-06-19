---
title: Bb Military Bugle Sheet-Metal Blueprint
slug: bugle-sheetmetal
wiki_type: instrument
status: active
sources:
  - path: ../../../../brass/bugle-sheetmetal/README.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../../brass/bugle-sheetmetal/design.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/natural-brass-harmonic-series
  - fabrication/sheet-metal-brass
  - fabrication/lofted-bend-bell
open_questions:
  - "Will the tuning-slide range compensate for the difference between the seed length (2944 mm) and the effective acoustic length after mouthpiece/flare corrections?"
  - "What is the lean-slip-roll tolerance on the 24-inch taper branch — is a lofted-bend approach required?"
  - "No capstone-manifest.json — not yet at V5 build-packet gate."
last_ingest: 2026-06-19
tags: [instrument, brass, bugle, valveless, natural-brass, military, harmonic-series]
---

# Bb Military Bugle — Sheet-Metal Blueprint

## Overview

A valveless Bb military bugle built from sheet brass with a bought trumpet-style mouthpiece. Cylindrical leadpipe and main sections, conical taper branch, segmented-or-lofted-bend bell flare, two 180° crooks, and a short tuning slide. Blueprint packet for controlled shop review — not a measured fabrication release.

- **Family:** natural brass aerophone / valveless bugle
- **Tuning:** written C sounding concert Bb; effective fundamental Bb1 (~58.27 Hz)
- **Acoustic length:** ~2944 mm folded into a compact military-bugle outline
- **Ergonomics:** hand-held; target body ~11 in long with 5.0–5.5 in bell rim
- **Materials:** thin yellow brass, annealed and formed by slip roll, strake forming, and brazing
- **Status:** L2 V5 blueprint — no prototype, no measured tuning

Primary repo links:
- [README](../../../../brass/bugle-sheetmetal/README.md)
- [Design notes](../../../../brass/bugle-sheetmetal/design.md)
- [Fabrication plan](../../../../brass/bugle-sheetmetal/fabrication-plan.md)
- [Assembly manual](../../../../brass/bugle-sheetmetal/assembly-manual.md)

## Current Status

- Release state: L2 V5 build-packet candidate — blueprint level, no reviewed CAD or prototype.
- Library family: brass.
- Acoustic class: natural brass / valveless bugle (harmonic-series instrument).
- Wolfram state: Wolfram Cloud Public-Execute URL available.
- CAD state: SolidWorks plan and flat-pattern strategy described; no confirmed `.glb`.
- No `capstone-manifest.json`.

## Source Notes

- [README](../../../../brass/bugle-sheetmetal/README.md) — status, target tuning, acoustic envelope, shop posture, design thesis (keep acoustic model simple, let the sheet-metal packet own forming complexity).
- [design.md](../../../../brass/bugle-sheetmetal/design.md) — acoustic position (harmonic series table H2–H8), bore layout table, sheet-metal part classification, seed length derivation.

Artifacts not ingested: `parameters.csv`, `bom.csv`, `validation.csv`, `fabrication-plan.md`.

## Design Knowledge

The bugle plays the harmonic series of its effective tube length. Useful played harmonics:

| Harmonic | Written | Sounding | Hz | Use |
|---|---|---|---|---|
| H2 | C4 | Bb3 | 233 | low call |
| H3 | G4 | F4 | 349 | call tones |
| H4 | C5 | Bb4 | 466 | Reveille anchor |
| H5 | E5 | D5 | 587 | Taps tone |
| H6 | G5 | F5 | 698 | call tones |
| H8 | C6 | Bb5 | 932 | high call |

Seed bore layout:

| Section | Length | Form |
|---|---|---|
| Mouthpipe | 7.0 in | rolled cylinder (0.460 in ID) |
| Main cylinder | 16.0 in | rolled cylinder (0.460 in ID) |
| Taper branch | 24.0 in | slip-rolled cone (0.460 → 1.200 in ID) |
| Bell flare | 12.0 in | segmented horn flare (1.200 → 5.250 in ID) |
| Crook allowance | 56.9 in | supported U-bends, folded branches |

The tuning slide provides final trim; first-order seed length (2944 mm) is not the final effective acoustic length after mouthpiece, flare, and end corrections.

## Cross-Links

- [[acoustic-classes/natural-brass-harmonic-series]]
- [[fabrication/sheet-metal-brass]]
- [[fabrication/lofted-bend-bell]]

## Open Questions

1. Will the tuning-slide range compensate for the gap between seed length and effective acoustic length after corrections?
2. Is a lofted-bend approach required for the 24-inch taper branch, or is a slip-rolled cone achievable?
3. No `capstone-manifest.json` — not yet at V5 build-packet gate.

## Maintenance Notes

First ingest from README and design.md. Next pass: read `parameters.csv` for full bore dimensions, `validation.csv` for prototype test gates, and `fabrication-plan.md` for forming sequence detail.
