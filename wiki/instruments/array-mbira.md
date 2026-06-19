---
title: Array Mbira Blueprint (Chromatic Isomorphic Tine Instrument)
slug: array-mbira
wiki_type: instrument
status: active
sources:
  - path: ../../../../idiophones/array-mbira/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/lamellaphone-idiophone
  - instruments/sheet-metal-mbira
open_questions:
  - "What is the isomorphic layout — hexagonal, Wicki-Hayden, or a custom grid?"
  - "What tine material (spring steel, phosphor bronze, stainless) and cross-section?"
  - "What resonator type (box, tube, gourd) and coupling mechanism to each tine?"
  - "How many notes / octave range is the target chromatic layout?"
last_ingest: 2026-06-19
tags: [instrument, idiophone, mbira, array, chromatic, isomorphic, tine, resonator, L2]
---

# Array Mbira Blueprint — Chromatic Isomorphic Tine Instrument

## Overview

A chromatic, isomorphic mbira: tuned metal tines mounted over individual resonators in a spatial layout where interval relationships remain geometrically consistent across the playing surface. Unlike traditional mbira (which use African regional tunings on a small number of tines), the array mbira targets chromatic coverage with a regular spatial layout — any chord shape works anywhere on the board.

- **Family:** idiophone / lamellaphone (plucked-tine)
- **Layout:** isomorphic — consistent interval relationships across the grid
- **Tuning:** chromatic, range TBD
- **Tine mounting:** over individual resonators
- **Status:** L2 V5 build-packet candidate — design study, no fabricated geometry or tuning table yet

Primary repo links:
- [README](../../../../idiophones/array-mbira/README.md)
- [Design notes](../../../../idiophones/array-mbira/design.md)
- [Decision record](../../../../idiophones/array-mbira/decision-record.md)

## Current Status

- Release state: L2 V5 build-packet candidate. No fabricated dimensions, tine lengths, tuning table, resonator volumes, CAD geometry, or measured validation data.
- Library family: idiophone.
- Acoustic class: lamellaphone (plucked-tine idiophone).
- Next step: small non-public mule with a few removable tines, adjustable bridge pressure, and interchangeable resonators.

## Source Notes

- [README](../../../../idiophones/array-mbira/README.md) — design concept (chromatic isomorphic layout, tuned tines over resonators), L2 boundary, packet map.

Artifacts not ingested: `design.md`, `bom.csv`, `cut-list.csv`, `decision-record.md`.

## Design Knowledge

Isomorphic layouts for chromatic instruments arrange notes so that any given chord or scale pattern has the same shape regardless of transposition. Common isomorphic grids: Wicki-Hayden, Harmonic Table, hexagonal isomorphic. Applied to a mbira, this means each tine position has a consistent interval relationship to its neighbors — musicians can play a pattern in any key without re-learning the hand shape.

The engineering challenge: tine length must be precisely controlled for each pitch (cantilever beam, `f = K × t / L²`), and resonator volumes must be matched to each tine's fundamental. Bridge pressure consistency across the grid is critical — variable bridge pressure shifts pitch non-uniformly.

Promotion to L3 requires: measured tine response, reviewed layout spacing, bridge/clamp evidence, resonator comparison data, and CAD authority for every fabricated part.

Related: [[instruments/sheet-metal-mbira]] (traditional 17-tine Shona layout, steel soundbox).

## Cross-Links

- [[acoustic-classes/lamellaphone-idiophone]]
- [[instruments/sheet-metal-mbira]]

## Open Questions

1. What isomorphic layout (hexagonal, Wicki-Hayden, custom grid)?
2. What tine material and cross-section?
3. What resonator type (box, tube, gourd) and coupling mechanism?
4. How many notes / what octave range?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for layout geometry and `decision-record.md` for tine/resonator trade-offs.
