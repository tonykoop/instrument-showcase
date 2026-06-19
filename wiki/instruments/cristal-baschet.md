---
title: Cristal Baschet Blueprint (Wet-Finger Glass Rod Friction Idiophone)
slug: cristal-baschet
wiki_type: instrument
status: active
sources:
  - path: ../../../../idiophones/cristal-baschet/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/friction-idiophone
  - instruments/bowed-dish
  - instruments/glass-armonica
  - instruments/glass-harp
open_questions:
  - "How many glass rods / pitches are in scope — traditional Cristal Baschet instruments have 54 notes across 4.5 octaves?"
  - "What are the target rod diameters and effective lengths for the planned pitch range?"
  - "What is the whisker radiator geometry — material, dimensions, and mounting?"
  - "What are the cone/flap resonator dimensions — and how are they coupled to the threaded metal stems?"
last_ingest: 2026-06-19
tags: [instrument, idiophone, cristal-baschet, glass-rod, friction, whisker-radiator, wet-finger, sculptural, L2]
---

# Cristal Baschet Blueprint — Wet-Finger Glass Rod Friction Idiophone

## Overview

A Cristal Baschet-inspired instrument: wet fingers rub glass rods to excite stick-slip vibration; vibration transfers through threaded metal stems with adjustable masses to large cone/flap resonators and a sculptural whisker-style radiator. The original Cristal Baschet (Bernard and François Baschet, 1952) is an iconic 20th-century sound sculpture played by the same wet-finger technique as the glass harp.

- **Family:** idiophone / friction-excited glass rod instrument
- **Excitation:** wet finger rubbing on glass rods
- **Transmission:** threaded metal stems with adjustable mass positions
- **Radiators:** cone or flap resonators + tall whisker-style radiator
- **Status:** L2 V5 planning packet — not fabrication-ready; all rod/stem/resonator dimensions pending measurement

Primary repo links:
- [README](../../../../idiophones/cristal-baschet/README.md)
- [Design notes](../../../../idiophones/cristal-baschet/design.md)
- [Decision record](../../../../idiophones/cristal-baschet/decision-record.md)

## Current Status

- Release state: L2 V5 shop-packet planning handoff — glass-rod friction idiophone study only, not fabrication-ready. All dimensions and geometry are pending measurement.
- Library family: idiophone.
- Acoustic class: friction idiophone (wet-finger glass rod).

## Source Notes

- [README](../../../../idiophones/cristal-baschet/README.md) — mechanism (wet finger → glass rod → threaded stem → adjustable mass → cone/flap resonator + whisker radiator), conservative scope (no released geometry), packet map.

Artifacts not ingested: `design.md`, `bom.csv`, `cut-list.csv`, `decision-record.md`.

## Design Knowledge

The Cristal Baschet mechanism: wet fingers create a stick-slip friction contact with the glass rod surface, exciting bending vibration in the rod. The rod couples through a threaded stem (acting as a vibration transmitter, not a tuning element per se — the glass rod is the tuned element). Adjustable masses on stems allow subtle tuning and damping control. The cone or flap resonator acts as a large radiating surface that converts the small rod vibration into audible room-scale sound.

The whisker radiator (a distinctive tall metal strip or bundle) produces the instrument's characteristic visual silhouette and a diffuse, sculptural radiation pattern. The whisker's own vibrational mode adds a high-frequency shimmer component.

Glass rods are selected by diameter and length to achieve target pitches; tuning is done by grinding the rod end. Safety is a significant constraint: broken glass rods are a real risk; the packet calls out edge preparation and guarding requirements.

Related: [[instruments/bowed-dish]] (single-pitch variant with steel rod → aluminum dish), [[instruments/glass-armonica]] (nested glass bowls, treadle-driven), [[instruments/glass-harp]] (wine glasses, wet finger, no transmission chain).

## Cross-Links

- [[acoustic-classes/friction-idiophone]]
- [[instruments/bowed-dish]]
- [[instruments/glass-armonica]]
- [[instruments/glass-harp]]

## Open Questions

1. How many glass rods / pitches are in scope?
2. What are the target rod diameters and effective lengths for the planned pitch range?
3. What is the whisker radiator geometry?
4. What are the cone/flap resonator dimensions and coupling to the stems?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for rod specification and stem/resonator coupling, `decision-record.md` for scope decisions.
