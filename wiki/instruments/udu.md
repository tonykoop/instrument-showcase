---
title: Udu (Slip-Cast Ceramic Dual-Helmholtz) Blueprint
slug: udu
wiki_type: instrument
status: active
sources:
  - path: ../../../../percussion/udu/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/helmholtz-resonator-drum
  - fabrication/slip-cast-ceramic
  - instruments/ceramic-hang
open_questions:
  - "What are the exact dimensions and neck diameters for the two Helmholtz openings on each of the 4 family sizes?"
  - "What is the clay body / firing schedule — earthenware, stoneware, or terracotta, and what temperature?"
  - "How does the dual-Helmholtz coupling between the two openings affect the modal response — and has this been measured vs modeled?"
  - "What are the four family sizes (target pitches or shell volumes)?"
last_ingest: 2026-06-19
tags: [instrument, drum, udu, ceramic, slip-cast, helmholtz, dual-resonator, 4-size-family, terracotta]
---

# Udu — Slip-Cast Ceramic Dual-Helmholtz Blueprint

## Overview

A slip-cast ceramic udu drum — a Nigerian Igbo instrument that produces pitched bass tones by striking the top opening (hand slap) and producing coupled Helmholtz resonance through the two openings. This packet covers a 4-size family, each cast from slip in a plaster mold, with two openings of different diameters that produce coupled resonance modes.

- **Family:** membranophone / ceramic vessel drum
- **Acoustic mechanism:** dual-Helmholtz cavity resonance + membrane-less struck-opening
- **Construction:** slip-cast ceramic, two openings, no membrane
- **Family:** 4 size variants (volumes / pitches graded across the family)
- **Origin:** Igbo, Nigeria
- **Status:** blueprint packet — mold geometry and Helmholtz model defined

Primary repo links:
- [README](../../../../percussion/udu/README.md)
- [Design notes](../../../../percussion/udu/design.md)

## Current Status

- Release state: blueprint packet; no confirmed empirical validation.
- Library family: drum (listed by family classification — functions as both percussive and pitched resonator).
- Acoustic class: Helmholtz resonator drum (vessel drum, ceramic).
- Wolfram state: acoustic model present; Wolfram Cloud Public-Execute URL available.
- CAD state: vessel geometry defined for slip-casting; no confirmed `.glb`.

## Source Notes

- [README](../../../../percussion/udu/README.md) — udu concept (Nigerian Igbo vessel drum, dual-Helmholtz, slip-cast ceramic), 4-size family, acoustic mechanism (coupled Helmholtz resonance on top + side openings).

Artifacts not ingested: `design.md`, `parameters.csv`, mold drawings, `bom.csv`.

## Design Knowledge

The udu differs from all other percussion instruments in the library: it has no membrane. Sound is produced by:
1. **Side-slap**: palm strikes the side opening, rapidly displacing the air inside — a short, high-pressure impulse that excites the cavity's Helmholtz mode.
2. **Top-hole slap**: hand covers and uncovers the top opening, changing the effective volume and pitch.
3. **Finger waving**: fingers wave across one opening while the other is covered or open, producing a continuous tone similar to blowing across a bottle neck.

The dual openings create two coupled Helmholtz resonances: one for each opening, with the cavity coupling them. This produces a richer set of available tones than a single-opening vessel.

Slip casting is ideal for the udu's complex pinched-pot profile: plaster molds capture the subtle shoulder, neck, and opening geometries that would be difficult to consistently throw by hand. The clay body must be semi-porous or glazed to avoid unwanted tone dampening.

Related: [[instruments/ceramic-hang]] (ceramic idiophone, similar ceramic fabrication lineage).

## Cross-Links

- [[acoustic-classes/helmholtz-resonator-drum]]
- [[fabrication/slip-cast-ceramic]]
- [[instruments/ceramic-hang]]

## Open Questions

1. What are the dimensions and neck diameters for the two Helmholtz openings on each of the 4 sizes?
2. What clay body / firing schedule — earthenware, stoneware, or terracotta?
3. Has the dual-Helmholtz coupling been measured or only modeled?
4. What are the four family sizes (target pitches or shell volumes)?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for Helmholtz math and mold geometry. Wolfram model likely covers cavity resonance calculations.
