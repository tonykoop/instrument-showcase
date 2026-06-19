---
title: Bowed Metal Psaltery
slug: bowed-metal-psaltery
wiki_type: instrument
status: active
sources:
  - path: ../../../strings/bowed-metal-psaltery/README.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/bowed-metal-psaltery/design.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/bowed-metal-psaltery/validation.csv
    kind: spreadsheet
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/bowed-zither
  - fabrication/brake-formed-sheet-metal
  - fabrication/planished-bronze
  - synthesis/wolfram-model-patterns
open_questions:
  - "Has the B8 bronze top plate been sourced and planished?"
  - "Has the steel backing frame and pin rail been fabricated and assembled?"
  - "Have all 25 strings been installed and tuned chromatically?"
  - "Has the body ring decay been measured (target: ≥3 s)?"
  - "Has pin creep been checked after tension settling?"
answers_filed: []
last_ingest: 2026-06-19
last_lint: 2026-06-19
review_due: 2026-09-19
tags:
  - instrument
  - strings
  - bowed-zither
  - psaltery
  - sheet-metal
  - bronze
  - chromatic
  - round3-lane08
---

# Bowed Metal Psaltery

## Overview

The `bowed-metal-psaltery` repo is an L2 V5 build-packet candidate for a greenfield bowed metal psaltery: a 25-string chromatic bowed zither with a planished B8 bronze top plate, steel backing frame, and a sustained metallic halo inspired by the Round 1 wind gong. Part of Round 3 Lane 08 of the Sheet-Metal Musical Instruments Sprint.

Primary repo links:

- [README](../../../../strings/bowed-metal-psaltery/README.md)
- [Design](../../../../strings/bowed-metal-psaltery/design.md)
- [Parameters](../../../../strings/bowed-metal-psaltery/parameters.csv)
- [Validation](../../../../strings/bowed-metal-psaltery/validation.csv)

## Current Status

- Release state: L2 V5 build-packet candidate; prototype-planning stage.
- Build target: 25-string chromatic psaltery, A3–A5.
- Acoustic class: [[acoustic-classes/bowed-zither]] — direct one-string-per-note bowed zither with sheet-metal body resonance.
- Fabrication: 1.5 mm B8 bronze top (planished, lightly crowned), 1018 steel perimeter frame and pin rails; trapezoid body ~350×500×55 mm.
- Wolfram model: `bowed-metal-psaltery-starter.wl` live at Public-Execute cloud URL.
- Release blockers: bronze sourcing and planishing; frame fab; 25-string installation; tuning and ring-decay validation.

## Design Thesis

Keeps the direct playability of a bowed psaltery while replacing the traditional wooden resonator with a shallow bronze/steel body. The lightly crowned, planished B8 bronze top excites a sympathetic metallic body ring that decays behind the string tone — giving sustained metallic halo characteristic of sheet-metal instruments.

## Current Targets

| Parameter | Value |
|-----------|-------|
| Strings | 25 chromatic, A3–A5 |
| Body shape | Trapezoid, ~350 × 500 × 55 mm |
| Top plate | 1.5 mm B8 bronze, planished |
| Frame | 1018 steel perimeter + pin rails |
| Body ring decay | ≥3 s target |
| Bow access | Clean at each string end |

## Source Notes

- [repo] [README](../../../../strings/bowed-metal-psaltery/README.md) — design thesis, targets, packet map.
- [repo] [design.md](../../../../strings/bowed-metal-psaltery/design.md) — design intent, geometry, materials, acoustic authority.
- [spreadsheet] [validation.csv](../../../../strings/bowed-metal-psaltery/validation.csv) — tuning, ring-decay, pin-creep checks; all rows pending until build.

## Cross-Links

- [[acoustic-classes/bowed-zither]]
- [[fabrication/brake-formed-sheet-metal]]
- [[fabrication/planished-bronze]]
- [[synthesis/wolfram-model-patterns]]

## Open Questions

1. Has the B8 bronze top plate been sourced and planished?
2. Has the steel backing frame and pin rail been fabricated and assembled?
3. Have all 25 strings been installed and tuned chromatically?
4. Has the body ring decay been measured (target: ≥3 s)?
5. Has pin creep been checked after tension settling?

## Maintenance Notes

Next ingest should pull in first-build results: bronze planishing notes, frame assembly, string tension measurements, and body ring decay data. Update [[acoustic-classes/bowed-zither]] with empirical body-ring coupling data when available.
