---
title: Modular Pedestal Drum Stack Blueprint
slug: modular-pedestal-drum-stack
wiki_type: instrument
status: active
sources:
  - path: ../../../../percussion/modular-pedestal-drum-stack/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/cylindrical-shell-drum
  - fabrication/rolled-sheet-metal-shell
  - instruments/compact-drum-kit
open_questions:
  - "What are the exact shell diameters and depths for each of the 5 drums in the stack?"
  - "How are the drums mechanically coupled to the central pedestal — bolted flanges, hose clamps, or custom brackets?"
  - "What is the pedestal material and how is it tuned for stability vs portability?"
  - "Is this playable by one person or does each drum require a dedicated player?"
  - "What is the intended playing technique — sticks, mallets, hands?"
last_ingest: 2026-06-19
tags: [instrument, drum, pedestal, modular, 5-piece, vertical-stack, sheet-metal, 300mm, 100mm]
---

# Modular Pedestal Drum Stack Blueprint

## Overview

A 5-drum percussion instrument arranged vertically on a central pedestal column. Shell diameters decrease from 300 mm at the base to 100 mm at the top, creating a stacked tower of drums with a range spanning roughly two octaves. Each drum is independently tunable; the pedestal allows one player to access all five drums from a single standing position.

- **Family:** membranophone / vertical modular drum stack
- **Pieces:** 5 drums, diameters 300, 250, 200, 150, 100 mm
- **Shell material:** rolled sheet-metal cylinders
- **Mounting:** central pedestal column
- **Status:** v0.1.0-blueprint packet — geometry and concept defined; no confirmed prototype

Primary repo links:
- [README](../../../../percussion/modular-pedestal-drum-stack/README.md)
- [Design notes](../../../../percussion/modular-pedestal-drum-stack/design.md)

## Current Status

- Release state: v0.1.0-blueprint packet; no confirmed empirical validation.
- Library family: drum.
- Acoustic class: cylindrical shell drum (modular stack).
- CAD state: shell geometry and pedestal structure defined; no confirmed `.glb`.

## Source Notes

- [README](../../../../percussion/modular-pedestal-drum-stack/README.md) — 5-piece stack configuration (300→100mm diameters), pedestal mounting, sheet-metal shell method, v0.1.0 blueprint state.

Artifacts not ingested: `design.md`, `parameters.csv`, `bom.csv`.

## Design Knowledge

The vertical stack configuration is ergonomically optimized for single-player use: the largest (lowest-pitched) drum is at the bottom where the player's hands naturally fall, and the smallest (highest-pitched) drums are at the top. The 300:100 mm diameter ratio produces approximately a 2-octave pitch spread across the stack (at equal head tension — actual pitch spread depends on shell depth and head material as well as diameter).

Sheet-metal cylindrical shells are well-suited to this design because they can be standardized to the same depth while varying only in diameter, simplifying fabrication and allowing matched bearing edges across the set.

The pedestal structural design must resist the combined torque of the largest drum (highest mass, lowest position) while remaining light enough for transport. Common solutions: welded steel tube center column, removable drum-holder brackets per level.

The instrument occupies the same niche as a conga/bongo table or a steel-drum rack — all five drums accessible from one standing position.

Related: [[instruments/compact-drum-kit]] (sheet-metal cylindrical shells, horizontal kit layout).

## Cross-Links

- [[acoustic-classes/cylindrical-shell-drum]]
- [[fabrication/rolled-sheet-metal-shell]]
- [[instruments/compact-drum-kit]]

## Open Questions

1. What are the exact shell diameters and depths for each of the 5 drums?
2. How are drums mechanically coupled to the pedestal (bolted flanges, hose clamps, custom brackets)?
3. What is the pedestal material and stability spec?
4. Is this playable by one person or requires multiple players?
5. What playing technique is intended — sticks, mallets, hands?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for pedestal engineering and `parameters.csv` for shell specifications.
