---
title: Native American Style Flutes
slug: flutes
wiki_type: instrument
status: active
sources:
  - path: ../../../woodwind/flutes/README.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/flutes/design.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/flutes/capstone-manifest.json
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/flutes/family-spec.csv
    kind: spreadsheet
    last_seen: 2026-06-19
  - path: ../../../woodwind/flutes/validation.csv
    kind: spreadsheet
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/native-american-flute
  - fabrication/bore-and-toneholes
  - fabrication/cnc-routing
  - synthesis/wolfram-model-patterns
open_questions:
  - "Have the family-spec.csv rows been extracted from the parametric design table workbook (flute-dimensions-parametric.xlsx)?"
  - "Have CAD/DXF family rows been mapped to current SolidWorks/OpenSCAD geometry and checked against physical measurements?"
  - "Which of the 150+ build-registry flutes have current measured data vs. historical build notes?"
  - "Has validation.csv been updated with current blockers and gate status?"
answers_filed: []
last_ingest: 2026-06-19
last_lint: 2026-06-19
review_due: 2026-09-19
tags:
  - instrument
  - woodwind
  - native-american-flute
  - two-chamber-flute
  - parametric
  - build-registry
  - private-review
---

# Native American Style Flutes

## Overview

The `flutes` repo is the engineering documentation archive for 150+ Native American style (NAF) wooden flutes built between roughly 2018–2021, plus the parametric design table and build registry. The packet is an L1 V5 scaffold: strong historical design-table and build-registry evidence, but not V5 build-ready until family rows are extracted, mapped to current CAD/DXF, and verified against physical measurements.

Primary repo links:

- [README](../../../../woodwind/flutes/README.md)
- [Design notes](../../../../woodwind/flutes/design.md)
- [Parametric design table](../../../../woodwind/flutes/design-table/flute-dimensions-parametric.xlsx)
- [Capstone manifest](../../../../woodwind/flutes/capstone-manifest.json)

## Current Status

- Release state: private review / L1 V5 packet scaffold.
- Build history: 150+ serial-numbered flutes; wood species, key, dimensions, failure modes, final status recorded in build registry.
- Scope: F4 to E5, pentatonic minor scale (3-2-2-3-2 semitone hole pattern).
- Acoustic class: [[acoustic-classes/native-american-flute]] — two-chamber fipple-class flute; SAC + playing chamber; external bird/fetish block.
- Design table: `design-table/flute-dimensions-parametric.xlsx` — 284-formula parametric Excel workbook; columns = keys (F4–E5); rows = inputs (green) and calculated dimensions (red).
- Wolfram model: `Flutes_Acoustic_Model.nb` is live at Public-Execute cloud URL.
- Lineage: Blue Bear Flutes (YouTube) build methodology; computationally connected to WSS-2019 Wolfram Summer School final project.

## Source Notes

- [repo] [README](../../../../woodwind/flutes/README.md) — four threads: parametric design table, build registry (150+), CAD geometry, lineage. Cultural attribution: instruments are NAF-style (inspired by, not part of the Indigenous tradition); builder is non-Indigenous. K1/K2 acoustic-length corrections close the tuning loop in the design table.
- [spreadsheet] [Family spec](../../../../woodwind/flutes/family-spec.csv) — multi-flute family rows with acoustic-law and measurement gates; currently L1 starter.
- [spreadsheet] [Validation](../../../../woodwind/flutes/validation.csv) — current blockers before becoming a build-ready V5 packet.

## Design Knowledge

The Native American flute is a two-chamber end-blown fipple flute:

1. **Slow Air Chamber (SAC)**: player's breath enters; air routes through a flue across the True Sound Hole.
2. **Bird/fetish block**: external block on top, with underside channel directing air into the True Sound Hole at the tuning angle.
3. **Playing chamber**: main bore with six finger holes for the pentatonic minor scale.

The parametric design table derives every build dimension from the target fundamental:

```text
f_fundamental = c / (2 * (L_playing_chamber + K1 * bore_ID + K2 * correction))
```

K1 and K2 are empirical corrections from the 150+ flute build dataset. The table covers F4 to E5; inputs are user-set variables (bore ID, wall thickness, flue, hole diameters); outputs include blank length, board feet, nest position, and hole spacings.

## Cultural Provenance

NAF-style flutes hold deep spiritual and cultural significance in many Indigenous North American communities. This repo documents craft and engineering knowledge as passed to Tony through publicly-available channels (Blue Bear Flutes). The instruments are "Native American style" — inspired by the tradition, not part of it. The deeper cultural practice belongs to the Indigenous communities from whom the instrument originates.

## Build And Validation Logic

V5 gates (from README):

1. Extract family-spec.csv rows from the design-table workbook for each key.
2. Map to current CAD/DXF (OpenSCAD scaffold exists; not a production model).
3. Check against physical measurements from the build registry.
4. Update `validation.csv` with current gate status.

## Cross-Links

- [[acoustic-classes/native-american-flute]]
- [[fabrication/bore-and-toneholes]]
- [[fabrication/cnc-routing]]
- [[synthesis/wolfram-model-patterns]]

## Open Questions

1. Have `family-spec.csv` rows been extracted from the parametric design table for each key?
2. Have CAD/DXF family rows been mapped to current geometry and checked against physical flute measurements?
3. Which build-registry flutes have current measured data (vs. historical build notes from 2018–2021)?
4. Has `validation.csv` been updated with current blockers?

## Maintenance Notes

Next ingest should pull in V5 family extraction results and CAD mapping status. Update [[acoustic-classes/native-american-flute]] and [[synthesis/wolfram-model-patterns]] when V5 gates clear.
