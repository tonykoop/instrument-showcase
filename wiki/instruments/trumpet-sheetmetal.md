---
title: Bb Trumpet Sheet-Metal Blueprint
slug: trumpet-sheetmetal
wiki_type: instrument
status: active
sources:
  - path: ../../../../brass/trumpet-sheetmetal/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/cylindrical-bore-brass
  - fabrication/sheet-metal-brass
  - fabrication/lofted-bend-bell
open_questions:
  - "Is the valve block bought (recommended) or fabricated in-house — and if bought, what part number at what bore station?"
  - "What flat-pattern strategy is used for the Bessel-style bell flare (segmented frusta vs single lofted surface)?"
  - "Valve combinations 1+3 and 1+2+3 run sharp without compensation — is a third-valve slide/kicker in the design?"
  - "No capstone-manifest.json — not yet at V5 build-packet gate."
last_ingest: 2026-06-19
tags: [instrument, brass, trumpet, valved, cylindrical-bore, brasswind, small-bore]
---

# Bb Trumpet — Sheet-Metal Blueprint

## Overview

A Bb 3-valve trumpet built around sheet-metal brass forming, bought precision valve parts, and a parametric acoustic model. Same nominal pitch target and valve intervals as a standard Bb trumpet; the sheet-metal sprint scope covers the leadpipe, bell, braces, and rolled tubing, while the precision valve block is explicitly called out as a buy/outsource item.

- **Family:** brasswind (Bb transposing, 3 piston valves)
- **Written reference:** C5 sounding concert Bb4 at 466.16 Hz (A4 = 440 Hz)
- **Main tube length:** 1480 mm (58.27 in)
- **Bore:** 0.460 in through cylindrical sections and valve ports
- **Leadpipe:** 0.348 in → 0.460 in over 7.5 in
- **Bell:** 0.460 in throat → 4.875 in rim over 13 in, Bessel-style flare
- **Ergonomic envelope:** 18.5–21 in overall hand-held wrap
- **Status:** L1 blueprint packet — review surface; no CAD authority, no prototype

Primary repo links:
- [README](../../../../brass/trumpet-sheetmetal/README.md)
- [Design notes](../../../../brass/trumpet-sheetmetal/design.md)
- [Wolfram model](../../../../brass/trumpet-sheetmetal/trumpet-sheetmetal-starter.wl)
- [Tuning notes](../../../../brass/trumpet-sheetmetal/tuning-notes.md)
- [Fabrication plan](../../../../brass/trumpet-sheetmetal/fabrication-plan.md)

## Current Status

- Release state: L1 packet (V5 migration) — blueprint and placeholder DXF/CNC surfaces; no CAD/DXF authority, no prototype.
- Library family: brass.
- Acoustic class: cylindrical bore brasswind (Bb trumpet).
- Wolfram state: acoustic and valve model (`.wl`) present; Wolfram Cloud Public-Execute URL available.
- CAD state: SolidWorks plan described; no confirmed `.glb`.
- No `capstone-manifest.json`.

## Source Notes

- [README](../../../../brass/trumpet-sheetmetal/README.md) — design thesis (three coupled systems: acoustic length, sheet-metal bell/leadpipe, bought valve block), targets (1480 mm, 0.460 in bore, 4.875 in bell, 18.5–21 in wrap), packet map.

Artifacts not ingested: `design.md`, `parameters.csv`, `tuning-notes.md`, `validation.csv`, `bom.csv`.

## Design Knowledge

The design explicitly treats the trumpet as three coupled systems:
1. **Acoustic**: 1480 mm effective tube length → C5 sounding on written Bb trumpet at A4 = 440 Hz.
2. **Sheet-metal**: leadpipe (rolled cylinder, 0.348 → 0.460 in over 7.5 in), bell (Bessel-style flare, 0.460 → 4.875 in over 13 in), braces, rolled tubing, and crooks — all within sheet-metal sprint methods.
3. **Valve block**: explicitly a buy or outsource item unless the builder has reaming, porting, and jig-brazing capability.

Valve length ratios (equal temperament):

| Valve | Semitones | Ratio |
|---|---|---|
| 2 | 1 | 0.0595 |
| 1 | 2 | 0.1225 |
| 3 | 3 | 0.1892 |

Combinations 1+3 and 1+2+3 will run sharp; third-valve kicker recommended.

## Cross-Links

- [[acoustic-classes/cylindrical-bore-brass]]
- [[fabrication/sheet-metal-brass]]
- [[fabrication/lofted-bend-bell]]

## Open Questions

1. Is the valve block bought or fabricated — and if bought, what part number at what bore station?
2. What flat-pattern strategy is used for the Bessel-style bell flare?
3. Is a third-valve slide/kicker in the design to address 1+3 and 1+2+3 sharpness?
4. No `capstone-manifest.json` — not yet at V5 build-packet gate.

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for bore profile and valve-block strategy, `tuning-notes.md` for intonation analysis, and `validation.csv` for measurement gates.
