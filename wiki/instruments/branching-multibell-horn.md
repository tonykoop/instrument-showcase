---
title: Branching Multibell Ensemble Horn
slug: branching-multibell-horn
wiki_type: instrument
status: active
sources:
  - path: ../../../../brass/branching-multibell-horn/README.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../../brass/branching-multibell-horn/design.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/conical-bore-brass
  - fabrication/sheet-metal-brass
  - fabrication/y-junction-manifold
open_questions:
  - "What is the actual stopped-port bleed / leak at the inactive bell mouths, and does it detune the active branch?"
  - "Can a player swap between bells fluidly mid-phrase with pad/cap ergonomics?"
  - "Does the two-stage Y-Y manifold maintain monotonic bore area growth across the active path in practice?"
  - "No capstone-manifest.json — has this reached V5 build-packet gate?"
last_ingest: 2026-06-19
tags: [instrument, brass, experimental, multibell, selectable-pitch, ensemble, no-valves]
---

# Branching Multibell Ensemble Horn

## Overview

A greenfield sheet-metal brass instrument with one mouthpiece and shared conical leadpipe feeding a Y-Y manifold and three forward-facing bell arms. The player selects an active bell by stopping the other two ports with soft caps or hand pads, making the horn a slow chord-machine and drone instrument for ensemble cues. Three selectable pitches: Bb1, F2, and C3 concert.

- **Family:** lip-reed brass / sheet-metal horn
- **Bell pitches:** Bb1 (long, ~2700 mm), F2 (middle, ~1800 mm), C3 (short, ~1200 mm)
- **Materials:** yellow brass sheet, brazed seams, wired rims
- **Status:** private-review V5 blueprint — no prototype built, all pitch targets are model predictions

Primary repo links:
- [README](../../../../brass/branching-multibell-horn/README.md)
- [Design notes](../../../../brass/branching-multibell-horn/design.md)
- [Fabrication plan](../../../../brass/branching-multibell-horn/fabrication-plan.md)
- [Assembly manual](../../../../brass/branching-multibell-horn/assembly-manual.md)
- [Wolfram model](../../../../brass/branching-multibell-horn/branching-multibell-horn-starter.wl)

## Current Status

- Release state: private-review V5 blueprint — concept and fabrication packet, not a measured production instrument.
- Library family: brass.
- Acoustic class: conical bore, multi-branch selectable-bell brass.
- Wolfram state: `.wl` first-pass acoustic length model present; Wolfram Cloud Public-Execute URL available.
- CAD state: SolidWorks plan and flat-pattern checklist written; no confirmed CAD artifacts or `.glb` yet.
- No `capstone-manifest.json`.

## Source Notes

- [README](../../../../brass/branching-multibell-horn/README.md) — target pitches, packet map, V5 authority boundary (blueprint surface only; no produced DXF/STEP, no prototype).
- [design.md](../../../../brass/branching-multibell-horn/design.md) — acoustic model (effective half-wave lengths per branch), bore branching strategy (two-stage Y-Y), player interface (pad/cap stopping), fabrication lineage (Round 1 conical taper math, Round 2 Y-junction craft).

Artifacts not ingested: `parameters.csv`, `validation.csv`, `tuning-notes.md`, `bom.csv`, `sourcing.csv`, `solidworks-plan.md`, `flat-pattern-checklist.md`.

## Design Knowledge

Bore runs: mouthpiece receiver → shared conical leadpipe → primary Y → [long branch / secondary Y → (middle branch / short branch)]. Each branch is formed from rolled yellow-brass frusta with a wired bell rim. Splitting into two sequential Y-pant fittings keeps each node to a two-way fitting that can be developed, checked, brazed, and leak-tested independently.

| Bell | Pitch | MIDI | Freq | Nom. centerline | Model L_eff |
|---|---|---|---|---|---|
| A long | Bb1 | 34 | 58.27 Hz | 2700 mm | 2943 mm |
| B middle | F2 | 41 | 87.31 Hz | 1800 mm | 1964 mm |
| C short | C3 | 48 | 130.81 Hz | 1200 mm | 1311 mm |

The gap between nominal centerline and model effective length is an allowance for bell end-correction, mouthpiece/receiver, and trim. All values are prototype targets until measured.

Key design constraints: bore area must grow monotonically across the active path; Y crotches blended with large internal fillets; trim rings placed near each bell throat before the flare locks geometry.

## Cross-Links

- [[acoustic-classes/conical-bore-brass]]
- [[fabrication/sheet-metal-brass]]
- [[fabrication/y-junction-manifold]]

## Open Questions

1. What is the actual stopped-port bleed/leak at inactive bell mouths, and does it detune the active branch?
2. Can a player swap between bells mid-phrase with pad/cap ergonomics?
3. Does the two-stage Y-Y manifold maintain monotonic bore area growth across the active path in practice?
4. No `capstone-manifest.json` — has this reached V5 build-packet gate?

## Maintenance Notes

First ingest from README and design.md only. Next pass: read `parameters.csv`, `validation.csv`, `fabrication-plan.md`, and the `.wl` model. After first prototype, update pitch targets with measured values.
