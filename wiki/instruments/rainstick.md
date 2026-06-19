---
title: Rainstick Blueprint (Gravity-Driven Percussion, CAD-Backed)
slug: rainstick
wiki_type: instrument
status: active
sources:
  - path: ../../../../idiophones/rainstick/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/shaker-idiophone
  - fabrication/polycarbonate-tube
  - instruments/wind-chimes
open_questions:
  - "Have the cascade duration, fill mass, pin/baffle retention, cap-seal, and handling safety tests been recorded in validation.csv?"
  - "What is the measured cascade duration for the baseline (glass microbeads, 10% fill, 48 baffles)?"
  - "What alternative fill media were tested — does media type affect tone color significantly?"
  - "Have the hardwood end caps been tested for airtight / watertight seal with the removable-test-first workflow?"
last_ingest: 2026-06-19
tags: [instrument, idiophone, rainstick, gravity-driven, cascade, polycarbonate-tube, birch-dowel, glass-microbeads, L2]
---

# Rainstick Blueprint — Gravity-Driven Percussion, CAD-Backed

## Overview

A CAD-backed rainstick: a 36-in clear polycarbonate tube with 48 birch-dowel spiral baffles and a glass-microbead fill, producing a broadband rain texture as media cascades through the baffle field when tilted. One of the more complete packets in the library — bar schedule, SolidWorks CAD, parametric workbook, validation tables, and print/deck source files present.

- **Family:** idiophone / gravity-driven shaker
- **Tube:** 36 in clear polycarbonate, 3.000 in OD, 0.125 in wall (2.750 in ID)
- **Baffles:** 3/16 in birch dowels, 0.75 in spiral pitch, 48 positions
- **Fill:** glass microbeads, 10% volume (baseline)
- **End caps:** turned hardwood, removable-test-first workflow
- **Status:** L2 V5 build-packet candidate — complete shop packet, SolidWorks CAD; no measured cascade/retention/seal results yet

Primary repo links:
- [README](../../../../idiophones/rainstick/README.md)
- [Section drawing](../../../../idiophones/rainstick/drawings/rainstick-section.svg)
- [Validation](../../../../idiophones/rainstick/validation.csv)

## Current Status

- Release state: L2 V5 build-packet candidate. Complete shop packet with SolidWorks anchors. Fabrication authority from `rainstick-design-table.xlsx` and SolidWorks CAD. No measured cascade duration, fill mass, pin/baffle retention, cap-seal, or handling safety data yet.
- Library family: idiophone.
- Acoustic class: shaker/gravity-driven cascade idiophone.
- Wolfram state: Wolfram Cloud Public-Execute URL available.
- CAD state: SolidWorks CAD folder present; SVG section drawing; `capstone-manifest.json` present.

## Source Notes

- [README](../../../../idiophones/rainstick/README.md) — baseline (36 in polycarbonate, 3.000 in OD, 48 birch-dowel baffles at 0.75 in pitch, glass microbeads 10% fill), removable-test-first end cap workflow, full shop packet description.

Artifacts not ingested: `design.md`, `rainstick-design-table.xlsx`, `validation.csv`, `bom.csv`.

## Design Knowledge

The rainstick's acoustic character depends on two variables: fill media and baffle density. Glass microbeads produce a fine, continuous rain sound with long cascade duration. Larger media (rice, seeds, pebbles) produce coarser, shorter cascades with more individual strike sounds. Baffle density (0.75 in pitch = 48 baffles in 36 in) controls how often the media encounters an obstruction and is redirected — more baffles = longer cascade duration, softer sound.

The polycarbonate tube provides visual transparency (can see the cascade in action, a visual design element) and good acoustic ring. The birch-dowel baffles insert through drilled holes in the tube wall and extend across the inner diameter in a spiral pattern, causing media to zigzag as they fall.

End cap design: the removable-test-first approach allows changing fill type and density experimentally before committing to a permanent-sealed end cap. Hardwood turned caps with an O-ring or friction fit are typical.

Sister repos: [[instruments/glockenspiel]], [[instruments/xylophone]], [[instruments/cajon]], [[instruments/wind-chimes]] — all in the tonykoop/instrument-maker catalogue.

## Cross-Links

- [[acoustic-classes/shaker-idiophone]]
- [[fabrication/polycarbonate-tube]]
- [[instruments/wind-chimes]]

## Open Questions

1. Have cascade duration, fill mass, pin/baffle retention, cap-seal, and safety tests been measured?
2. What is the measured cascade duration for the baseline fill?
3. What alternative fill media were tested?
4. Have the hardwood end caps been tested for airtight seal?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for baffle geometry and `validation.csv` for any measured cascade data.
