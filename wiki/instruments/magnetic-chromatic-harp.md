---
title: Magnetic Chromatic Harp
slug: magnetic-chromatic-harp
wiki_type: instrument
status: active
sources:
  - path: ../../../strings/magnetic-chromatic-harp/README.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/magnetic-chromatic-harp/design.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/magnetic-chromatic-harp/validation.csv
    kind: spreadsheet
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/electric-harp-pickup
  - fabrication/brake-formed-sheet-metal
  - fabrication/triangular-frame-structural
  - synthesis/electromagnetic-pickup
  - synthesis/wolfram-model-patterns
open_questions:
  - "Has the SolidWorks master layout been created and reviewed for the triangular frame?"
  - "Have flat patterns been coupon-tested for spring-back on the 1018 steel column?"
  - "Has a staged-load test been run on the triangular frame under ~600 kgf string load?"
  - "Have electromagnetic pickup channels been sourced and tested per string?"
  - "Has the 36-string chromatic tuning schedule been validated against measured string tensions?"
answers_filed: []
last_ingest: 2026-06-19
last_lint: 2026-06-19
review_due: 2026-09-19
tags:
  - instrument
  - strings
  - harp
  - chromatic
  - electric
  - electromagnetic-pickup
  - sheet-metal
  - 36-string
---

# Magnetic Chromatic Harp

## Overview

The `magnetic-chromatic-harp` repo is an L2 V5 build-packet candidate for a greenfield 36-string chromatic electric harp: sheet-metal triangular frame, 1018 steel structural column, aluminum bridge rails, steel strings, and a split-coil electromagnetic pickup bar under every string. Intentionally pickup-first — the sheet-metal body holds ~600 kgf of string load and provides a hardware platform for silent/headphone or amplified performance.

Primary repo links:

- [README](../../../../strings/magnetic-chromatic-harp/README.md)
- [Design](../../../../strings/magnetic-chromatic-harp/design.md)
- [Parameters](../../../../strings/magnetic-chromatic-harp/parameters.csv)
- [Validation](../../../../strings/magnetic-chromatic-harp/validation.csv)

## Current Status

- Release state: L2 V5 build-packet candidate; no CAD, DXF, or fabrication drawings yet.
- Build target: 36-string chromatic harp, full range, electromagnetic pickup bar per string.
- Acoustic class: [[acoustic-classes/electric-harp-pickup]] — electromagnetic (not piezo); silent/amplified operation; body is structural, not acoustic.
- Fabrication: sheet-metal triangular frame + 1018 steel column + aluminum bridge rails.
- Wolfram model: `magnetic-chromatic-harp-starter.wl` live at Public-Execute cloud URL.
- Release blockers: SolidWorks master layout; flat-pattern coupon tests; staged-load frame test.

## Design Philosophy

The body is not asked to behave like a carved wooden soundbox. Its job is:
1. Hold ~600 kgf of string load with stable geometry
2. Provide an inspectable hardware platform for each pickup channel
3. Enable silent/headphone practice or amplified performance

All geometry is design-intent from `parameters.csv` — no authoritative CAD/DXF exists yet.

## Source Notes

- [repo] [README](../../../../strings/magnetic-chromatic-harp/README.md) — design intent, packet map, authority boundary.
- [repo] [design.md](../../../../strings/magnetic-chromatic-harp/design.md) — scale range, structural design, pickup channel design.
- [spreadsheet] [validation.csv](../../../../strings/magnetic-chromatic-harp/validation.csv) — structural, string, and pickup checks; all rows pending until build.

## Cross-Links

- [[acoustic-classes/electric-harp-pickup]]
- [[fabrication/brake-formed-sheet-metal]]
- [[fabrication/triangular-frame-structural]]
- [[synthesis/electromagnetic-pickup]]
- [[synthesis/wolfram-model-patterns]]

## Open Questions

1. Has the SolidWorks master layout been created and reviewed for the triangular frame?
2. Have flat patterns been coupon-tested for spring-back on the 1018 steel column?
3. Has a staged-load test been run on the triangular frame under ~600 kgf string load?
4. Have electromagnetic pickup channels been sourced and tested per string?
5. Has the 36-string chromatic tuning schedule been validated against measured string tensions?

## Maintenance Notes

Next ingest should pull in SolidWorks MLP review results, coupon test data, and staged-load frame test. Update [[synthesis/electromagnetic-pickup]] with any per-string pickup channel characterization data.
