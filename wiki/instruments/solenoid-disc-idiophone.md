---
title: Solenoid-Struck Idiophone Disc Blueprint (1 m Bronze MIDI Disc)
slug: solenoid-disc-idiophone
wiki_type: instrument
status: active
sources:
  - path: ../../../../idiophones/solenoid-disc-idiophone/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/struck-plate-idiophone
  - fabrication/large-bronze-disc
  - instruments/wind-gong-sheetmetal
open_questions:
  - "How are the 25 solenoid strike points mapped to Chladni modes of the disc — and what is the initial strike-point layout?"
  - "What is the MIDI controller and driver circuit design for 25 solenoid channels?"
  - "What is the mallet tip material on each solenoid — and how does tip hardness affect mode selection?"
  - "Have any Chladni patterns been measured on a prototype disc — or is all mode mapping conceptual?"
last_ingest: 2026-06-19
tags: [instrument, idiophone, solenoid, bronze-disc, MIDI, Chladni, 1m, 25-channel, L1]
---

# Solenoid-Struck Idiophone Disc Blueprint — 1 m Bronze MIDI Disc

## Overview

A greenfield blueprint for a 1.0 m B8 bronze idiophone disc with 25 rear-face MIDI-controlled solenoid mallets. The instrument is a modal exploration rig first: Chladni pattern mapping, spectrum measurements, cross-talk characterization, and mallet tip selection determine whether the 25 solenoid strike points become stable musical pitches. Not a pre-tuned scale instrument.

- **Family:** idiophone / struck metal plate (MIDI-actuated)
- **Disc:** 1000 mm diameter, 1.5 mm B8 bronze (planished or flat)
- **Actuation:** 25 bought 12 V solenoid mallets, rear-face mounting
- **Controller:** MIDI input, protected driver outputs
- **Validation:** 25 distinct audible pitches, responsive velocity mapping, no adjacent cross-talk above −10 dB
- **Status:** L1 V5 blueprint — concept/design-planning only; no FEA, Chladni/spectrum data, or prototype build evidence

Primary repo links:
- [README](../../../../idiophones/solenoid-disc-idiophone/README.md)
- [Design notes](../../../../idiophones/solenoid-disc-idiophone/design.md)

## Current Status

- Release state: L1 V5 blueprint / measurement-required packet. No reviewed native CAD, released DXF, FEA, measured Chladni/spectrum data, tuned strike map, or prototype build evidence.
- Library family: idiophone.
- Acoustic class: struck plate idiophone (large bronze disc, MIDI actuation).

## Source Notes

- [README](../../../../idiophones/solenoid-disc-idiophone/README.md) — instrument thesis (single planished bronze disc, 25 rear solenoids at Chladni nodes, MIDI-playable modal instrument), targets (1000 mm, 1.5 mm B8 bronze, 25 solenoids, MIDI, −10 dB cross-talk spec), blueprint status.

Artifacts not ingested: `design.md`.

## Design Knowledge

A 1 m bronze disc has a rich set of vibrational modes (Chladni patterns). Striking the disc at different points excites different modal combinations — some points are anti-nodes of a specific mode (loud, sustained pitch), others are nodes (quiet, damped). The 25 solenoid positions are chosen to map to the anti-nodes of 25 target modal pitches.

Chladni pattern visualization: fine sand or powder scattered on the disc surface, bow excitation at a specific edge point → sand migrates to nodes and draws the mode shape. This is the physical measurement needed to validate the strike-point map before committing solenoid positions.

MIDI controller: 25 solenoid channels require a MIDI-to-parallel-output circuit (e.g., MIDI → microcontroller → 25-channel driver board). Velocity mapping requires PWM or timed current pulses proportional to MIDI velocity byte.

B8 bronze (phosphor bronze 92% Cu, 8% Sn) has a bright, resonant ring characteristic; at 1.5 mm it has enough stiffness for the large diameter while remaining planishable.

Related: [[instruments/wind-gong-sheetmetal]] (similar planished bronze disc, but 560 mm and acoustic rather than MIDI-actuated).

## Cross-Links

- [[acoustic-classes/struck-plate-idiophone]]
- [[fabrication/large-bronze-disc]]
- [[instruments/wind-gong-sheetmetal]]

## Open Questions

1. How are 25 solenoid strike points mapped to Chladni modes — what is the initial strike-point layout?
2. What is the MIDI controller and driver circuit design for 25 channels?
3. What mallet tip material on each solenoid — and how does tip hardness affect mode selection?
4. Have any Chladni patterns been measured on a prototype disc?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for Chladni mode mapping strategy and solenoid/MIDI circuit plan.
