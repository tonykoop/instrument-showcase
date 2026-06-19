---
title: Multi-Bridge Sheet Zither
slug: multi-bridge-sheet-zither
wiki_type: instrument
status: active
sources:
  - path: ../../../strings/multi-bridge-sheet-zither/README.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/multi-bridge-sheet-zither/design.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/multi-bridge-sheet-zither/validation.csv
    kind: spreadsheet
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/radial-zither
  - fabrication/dished-steel-soundboard
  - fabrication/bridge-ring-mechanism
  - synthesis/wolfram-model-patterns
open_questions:
  - "Has the SolidWorks dish (600 mm, 10 mm shallow, 1.2 mm CRS) been designed and reviewed?"
  - "Have the three concentric bridge ring parts been modeled?"
  - "Have flat patterns been validated (DXF) for the dish and bridge rings?"
  - "Has string linear density been measured (required for Mersenne-Taylor pitch prediction)?"
  - "Has the 48-string tension schedule been validated against the measured linear density?"
answers_filed: []
last_ingest: 2026-06-19
last_lint: 2026-06-19
review_due: 2026-09-19
tags:
  - instrument
  - strings
  - zither
  - radial
  - sheet-metal
  - dished-soundboard
  - multi-bridge
  - experimental
---

# Multi-Bridge Sheet Zither

## Overview

The `multi-bridge-sheet-zither` repo is an L2 V5 build-packet candidate for a radial zither: a shallow 600 mm dished steel soundboard with 48 bought music-wire strings and three adjustable bridge rings that create 144 measurable string sections. Blueprint lineage from Round 1 handpan dish-sinking craft applied to a flatter, stiffer steel soundboard.

Primary repo links:

- [README](../../../../strings/multi-bridge-sheet-zither/README.md)
- [Design](../../../../strings/multi-bridge-sheet-zither/design.md)
- [Parameters](../../../../strings/multi-bridge-sheet-zither/parameters.csv)
- [Validation](../../../../strings/multi-bridge-sheet-zither/validation.csv)

## Current Status

- Release state: L2 V5 build-packet; v0.1 blueprint; not build-ready.
- Build target: 600 mm radial zither, 48 strings, 3 concentric bridge rings.
- Acoustic class: [[acoustic-classes/radial-zither]] — Mersenne-Taylor string law; 144 measurable sections from 48 strings × 3 bridge positions.
- Fabrication: 600 mm, 1.2 mm CRS shallow dished soundboard; bridge rings; radial string layout.
- Wolfram model: `multi-bridge-sheet-zither-starter.wl` live at Public-Execute cloud URL.
- Release blockers: SolidWorks dish + bridge rings; DXF flat patterns; string linear density measurement.

## Design Snapshot

| Parameter | Value |
|-----------|-------|
| Soundboard | 600 mm diameter, 1.2 mm CRS, 10 mm shallow dish |
| Strings | 48 radial music-wire strings |
| Bridges | 3 adjustable concentric bridge rings |
| Sections | 144 measurable string sections (48 × 3) |
| Pitch model | Mersenne-Taylor with measured linear density required |

## Source Notes

- [repo] [README](../../../../strings/multi-bridge-sheet-zither/README.md) — design snapshot, packet map, readiness statement.
- [repo] [design.md](../../../../strings/multi-bridge-sheet-zither/design.md) — design thesis, geometry, acoustic intent, authority boundary.
- [spreadsheet] [validation.csv](../../../../strings/multi-bridge-sheet-zither/validation.csv) — string tension, dish, bridge ring, and pitch checks; all rows pending until build.

## Cross-Links

- [[acoustic-classes/radial-zither]]
- [[fabrication/dished-steel-soundboard]]
- [[fabrication/bridge-ring-mechanism]]
- [[synthesis/wolfram-model-patterns]]

## Open Questions

1. Has the SolidWorks dish (600 mm, 10 mm shallow, 1.2 mm CRS) been designed and reviewed?
2. Have the three concentric bridge ring parts been modeled?
3. Have flat patterns been validated (DXF) for the dish and bridge rings?
4. Has string linear density been measured (required for Mersenne-Taylor pitch prediction)?
5. Has the 48-string tension schedule been validated against the measured linear density?

## Maintenance Notes

Next ingest should pull in SolidWorks model review, DXF flat pattern validation, and string linear density measurements. Update [[acoustic-classes/radial-zither]] with any empirical section-pitch data.
