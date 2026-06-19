---
title: Bb Cornet Sheet-Metal Blueprint
slug: cornet-sheetmetal
wiki_type: instrument
status: active
sources:
  - path: ../../../../brass/cornet-sheetmetal/README.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../../brass/cornet-sheetmetal/design.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/conical-bore-brass
  - fabrication/sheet-metal-brass
  - fabrication/lofted-bend-bell
open_questions:
  - "Is a purchased piston-valve block available at the target bore station (0.470–0.500 in)? The packet calls out purchased valves but does not name a supplier."
  - "Valve combinations 1+3 and 1+2+3 are expected to run sharp — is a third-valve slide/kicker planned in the CAD?"
  - "What flat-pattern strategy is used for the Bessel-style bell flare (segmented frusta vs lofted bend)?"
  - "No capstone-manifest.json — not yet at V5 build-packet gate."
last_ingest: 2026-06-19
tags: [instrument, brass, cornet, valved, conical-bore, compact-wrap, brasswind]
---

# Bb Cornet — Sheet-Metal Blueprint

## Overview

A compact Bb, 3-valve cornet built around sheet-metal brass forming. Same practical fingering as a Bb trumpet, but with a continuously conical bore through the leadpipe, valve section, and bell tail — producing the cornet's characteristic darker, mellower response vs. the cylindrical trumpet. Target: compact short-wrap body 14–15 in before mouthpiece.

- **Family:** brasswind (Bb transposing)
- **Open sounding target:** C5 = 466.16 Hz (concert Bb4)
- **Bore profile:** continuous conical 0.348 → 0.500 in through leadpipe + valves; Bessel-style bell flare to 4.875 in rim
- **Materials:** C26800 yellow brass sheet and tube
- **Status:** L2 V5 blueprint — planning packet, no CAD, no prototype

Primary repo links:
- [README](../../../../brass/cornet-sheetmetal/README.md)
- [Design notes](../../../../brass/cornet-sheetmetal/design.md)
- [Fabrication plan](../../../../brass/cornet-sheetmetal/fabrication-plan.md)
- [Assembly manual](../../../../brass/cornet-sheetmetal/assembly-manual.md)

## Current Status

- Release state: L2 V5 build-packet candidate — blueprint, not fabrication-ready.
- Library family: brass.
- Acoustic class: Bb brasswind, continuously conical bore (cornet).
- Wolfram state: Wolfram Cloud Public-Execute URL available.
- CAD state: SolidWorks plan; no confirmed CAD artifacts or `.glb`.
- No `capstone-manifest.json`.

## Source Notes

- [README](../../../../brass/cornet-sheetmetal/README.md) — target, bore thesis, ergonomic envelope, build status, license.
- [design.md](../../../../brass/cornet-sheetmetal/design.md) — bore profile table (B0–B4 stations), valve length ratios, primary design targets with tolerance and confidence level.

Artifacts not ingested: `parameters.csv`, `validation.csv`, `bom.csv`, `fabrication-plan.md`, `tuning-notes.md`.

## Design Knowledge

The cornet's acoustic identity depends on a **continuously conical bore** from mouthpiece entry through the valve block — unlike a trumpet's mostly cylindrical 0.460 in mid-section. Bore stations:

| Station | Role | Diameter | Confidence |
|---|---|---|---|
| B0 | mouthpiece receiver / leadpipe entry | 0.348 in | medium |
| B1 | leadpipe exit / valve entry | 0.470 in | medium |
| B2 | valve block exit | 0.500 in | medium |
| B3 | bell tail | 0.600 in | medium |
| B4 | bell rim | 4.875 in | medium |

Valve length ratios (equal-temperament against effective open air column):

| Valve | Interval | Ratio |
|---|---|---|
| 2 | semitone | 0.0595 |
| 1 | whole tone | 0.1225 |
| 3 | minor third | 0.1892 |

Combinations 1+3 and 1+2+3 will run sharp without compensation; a third-valve slide/kicker is called out as a design provision.

Validation targets: bore station tolerance ±0.005 in; valve return force < 80 g; leak test zero bubbles at 1 psi; mass 1.0–1.1 kg.

## Cross-Links

- [[acoustic-classes/conical-bore-brass]]
- [[fabrication/sheet-metal-brass]]
- [[fabrication/lofted-bend-bell]]

## Open Questions

1. Is a purchased piston-valve block available at the target bore stations (0.470–0.500 in)? No supplier named in README.
2. Valve combinations 1+3 and 1+2+3 expected to run sharp — is the third-valve kicker in the CAD plan?
3. What flat-pattern strategy is used for the Bessel-style bell flare?
4. No `capstone-manifest.json` — not yet at V5 build-packet gate.

## Maintenance Notes

First ingest from README and design.md. Next pass: read `parameters.csv` for full bore table, `tuning-notes.md` for valve intonation strategy, and `fabrication-plan.md` for forming sequence.
