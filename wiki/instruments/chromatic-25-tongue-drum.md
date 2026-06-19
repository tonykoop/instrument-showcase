---
title: Chromatic 25-Note Tongue Drum Blueprint
slug: chromatic-25-tongue-drum
wiki_type: instrument
status: active
sources:
  - path: ../../../../idiophones/chromatic-25-tongue-drum/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/slit-tongue-idiophone
  - instruments/steel-tongue-drum
  - instruments/handpan
  - instruments/chromatic-25-tongue-drum
open_questions:
  - "How are 25 U-shaped tongue slots arranged on a 500 mm disc — single ring, inner+outer rings, or custom layout?"
  - "What is the coupon validation plan — which tongues to cut first (C3, A3, C4, C5)?"
  - "Does nitriding consistently shift pitch by a predictable amount that can be factored into tongue lengths pre-nitride?"
  - "How does shell curvature affect the cantilever model vs flat coupon tests?"
last_ingest: 2026-06-19
tags: [instrument, idiophone, tongue-drum, chromatic, 25-note, C3-C5, handpan-scale, steel, nitrided, L2]
---

# Chromatic 25-Note Tongue Drum Blueprint

## Overview

A Round 4 idiophone blueprint: a 500 mm OD handpan-scale circular steel shell with 25 U-shaped tongues cut into the top field, targeting a chromatic C3–C5 range (A4 = 440 Hz). The tongue geometry follows a first-order fixed-free steel tongue model; shell curvature, dense note coupling, and nitriding are treated as measured coupon variables rather than solved facts.

- **Family:** idiophone / slit-tongue steel disc
- **Shell:** 500 mm OD, 1.0 mm cold-rolled steel, nitrided after coupon trials
- **Notes:** 25, chromatic C3–C5
- **Tongue type:** U-shaped (two parallel cuts + curved end cut)
- **Status:** L2 V5 build-packet candidate — private blueprint, coupon-validation required before fabrication release

Primary repo links:
- [README](../../../../idiophones/chromatic-25-tongue-drum/README.md)
- [Design notes](../../../../idiophones/chromatic-25-tongue-drum/design.md)
- [Wolfram starter](../../../../idiophones/chromatic-25-tongue-drum/chromatic-25-tongue-drum-starter.wl)

## Current Status

- Release state: L2 V5 build-packet candidate. CAD, DXF, CNC, and tuning authority remain pending coupon measurements.
- Library family: idiophone.
- Acoustic class: slit-tongue idiophone (steel disc, U-slots).
- Wolfram state: fixed-free steel tongue model (`.wl`) present; Wolfram Cloud Public-Execute URL available.
- CAD state: SolidWorks plan and design laid out; pending coupon-validated DXF release.

## Source Notes

- [README](../../../../idiophones/chromatic-25-tongue-drum/README.md) — targets (500 mm OD, 25 U-tongues, chromatic C3–C5, 1.0 mm CRS, nitrided), coupon validation boundary (flat C3/A3/C4/C5 tongues + crowned-shell U-slot coupon + nitriding witness coupon before full cut).

Artifacts not ingested: `design.md`, `parameters.csv`, `validation.csv`.

## Design Knowledge

The handpan-scale disc (500 mm) with 25 chromatic tongues is significantly more complex than a 6–9 tongue pentatonic steel tongue drum. Key engineering challenges:

1. **Note density**: 25 tongues on 500 mm means tongues at adjacent chromatic pitches are spatially close — vibrational coupling between adjacent tongues can produce cross-talk and pitch pull.
2. **Shell curvature**: a curved shell modifies the effective cantilever stiffness vs flat plate coupons. The curved geometry must be validated with coupon tests before committing the full note layout.
3. **Nitriding**: nitriding (iron nitride case hardening) hardens the steel surface, which typically raises tongue pitch by a predictable ΔHz. The nitriding witness coupon measures this shift so tongue blanks can be cut slightly flat.
4. **Coupon sequence**: flat C3, A3, C4, C5 tongues → curved shell U-slot coupon → nitriding witness → then and only then cut the production top shell.

Related: [[instruments/steel-tongue-drum]] (smaller 12 in round vessel, simpler 6–9 tongue pentatonic), [[instruments/handpan]] (same 500 mm scale shell, no tongues — formed tone fields instead).

## Cross-Links

- [[acoustic-classes/slit-tongue-idiophone]]
- [[instruments/steel-tongue-drum]]
- [[instruments/handpan]]

## Open Questions

1. How are 25 tongues arranged on the 500 mm disc — single ring, inner+outer rings, custom layout?
2. Which coupon tongues to cut first (C3, A3, C4, C5)?
3. Does nitriding shift pitch by a consistent, pre-factorable amount?
4. How does shell curvature affect the cantilever model?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for tongue layout and coupon protocol, `chromatic-25-tongue-drum-starter.wl` for tongue length predictions.
