---
title: Folding Travel Resonator Guitar
slug: folding-travel-resonator-guitar
wiki_type: instrument
status: active
sources:
  - path: ../../../strings/folding-travel-resonator-guitar/README.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/folding-travel-resonator-guitar/design.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/folding-travel-resonator-guitar/validation.csv
    kind: spreadsheet
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/resonator-guitar
  - fabrication/brake-formed-sheet-metal
  - fabrication/folding-hinge-mechanism
  - synthesis/wolfram-model-patterns
open_questions:
  - "Has the hinge hardware been sourced and tested for repeatable open/close indexing?"
  - "Has the cone diameter and resonator-body air volume been confirmed at design dimensions?"
  - "Has the gasket compression seal been validated to maintain air volume when folded open?"
  - "Has the bought-neck geometry been confirmed for neck pocket fit?"
  - "Has the fold-cycle test been run (fold/open cycles without pitch change)?"
answers_filed: []
last_ingest: 2026-06-19
last_lint: 2026-06-19
review_due: 2026-09-19
tags:
  - instrument
  - strings
  - guitar
  - resonator
  - folding
  - travel
  - sheet-metal
  - round3
---

# Folding Travel Resonator Guitar

## Overview

The `folding-travel-resonator-guitar` repo is an L2 V5 build-packet candidate for a sheet-metal resonator guitar whose body folds at the lower bout for carry-on travel. Lower half carries neck, strings, bridge, cone, and tailpiece; upper half contributes resonant volume and soundhole radiation when open, folds over the lower half for transport.

Primary repo links:

- [README](../../../../strings/folding-travel-resonator-guitar/README.md)
- [Design](../../../../strings/folding-travel-resonator-guitar/design.md)
- [Parameters](../../../../strings/folding-travel-resonator-guitar/parameters.csv)
- [Tuning notes](../../../../strings/folding-travel-resonator-guitar/tuning-notes.md)
- [Validation](../../../../strings/folding-travel-resonator-guitar/validation.csv)

## Current Status

- Release state: L2 V5 build-packet candidate; prototype-planning stage.
- Build target: folding steel-string resonator guitar, carry-on travel size.
- Acoustic class: [[acoustic-classes/resonator-guitar]] — spun-aluminum cone under saddle, sheet-metal body.
- Fabrication: sheet-metal body + hinge mechanism + cone + bought neck.
- Wolfram model: `folding-travel-resonator-guitar-starter.wl` live at Public-Execute cloud URL.
- Release blockers: hinge hardware; cone diameter; gasket compression; bought-neck geometry; fold-cycle test.

## Design Thesis

The folding seam is treated as a precision musical mechanism:
- Hinge locates motion
- Locking pins index the open state
- Magnetic latches retain positions
- Gasketed land preserves resonator-body air volume when open

String load stays in the lower half so the hinge solves only sealing and repeatable closure — not full neck/tailpiece structural load.

## Readiness

Critical dimensions (hinge hardware, cone diameter, bought-neck geometry, gasket compression) remain `pending_measurement` and block L3 promotion. Not build-ready, travel-safe, airline-ready, or stage-ready until a measured prototype closes the hinge/gasket, string-load, cone-response, mass, and fold-cycle validation gates.

## Source Notes

- [repo] [README](../../../../strings/folding-travel-resonator-guitar/README.md) — design thesis, packet map, readiness statement.
- [repo] [design.md](../../../../strings/folding-travel-resonator-guitar/design.md) — intent, geometry, acoustic position, and formed-part classification.
- [spreadsheet] [validation.csv](../../../../strings/folding-travel-resonator-guitar/validation.csv) — hinge, gasket, cone-response, fold-cycle checks; all rows pending until prototype.

## Cross-Links

- [[acoustic-classes/resonator-guitar]]
- [[fabrication/brake-formed-sheet-metal]]
- [[fabrication/folding-hinge-mechanism]]
- [[synthesis/wolfram-model-patterns]]

## Open Questions

1. Has the hinge hardware been sourced and tested for repeatable open/close indexing?
2. Has the cone diameter and resonator-body air volume been confirmed?
3. Has the gasket compression seal been validated to maintain air volume when folded open?
4. Has the bought-neck geometry been confirmed for neck pocket fit?
5. Has the fold-cycle test been run (fold/open cycles without pitch change)?

## Maintenance Notes

Next ingest should pull in hinge hardware tests, cone selection, gasket compression measurements, and fold-cycle results. Update [[fabrication/folding-hinge-mechanism]] with empirical hinge indexing data.
