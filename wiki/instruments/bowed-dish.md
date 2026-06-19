---
title: Bowed Dish (Cristal-Baschet Inspired, C4)
slug: bowed-dish
wiki_type: instrument
status: active
sources:
  - path: ../../../../idiophones/bowed-dish/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/friction-idiophone
  - instruments/cristal-baschet
  - instruments/musical-saw
open_questions:
  - "What is the effective bending length adjustment mechanism for the 12 mm steel rod?"
  - "How is the rod coupled to the dish — brazed, clamped, or pressed against the dish center?"
  - "What material property of the 1100-O aluminum dish enables the sustained bow response?"
  - "Has a sustained bowed tone (≥10 s, ±10 cents) been achieved on a prototype?"
last_ingest: 2026-06-19
tags: [instrument, idiophone, bowed-dish, friction, C4, aluminum-dish, steel-rod, cristal-baschet-inspired, L1]
---

# Bowed Dish — Cristal-Baschet Inspired Single-Pitch Idiophone

## Overview

A single-pitch sheet-metal idiophone inspired by Cristal Baschet playing technique. A rosined finger or bow excites a 12 mm OD vertical steel rod; vibration transfers through the rod into a 400 mm diameter × 80 mm deep 1100-O aluminum dish, which radiates the tone. Target pitch: C4 (261.63 Hz). Final tuning by dish curvature, thinning, and rod effective length adjustment.

- **Family:** idiophone / bowed friction-excited resonator
- **Pitch:** C4 (~261.63 Hz)
- **Radiator:** 400 mm dia, 80 mm deep, 1100-O aluminum dish
- **Exciter:** 12 mm OD steel rod, 200 mm physical length, adjustable effective bending length
- **Validation:** sustained bowed tone ≥10 s, within ±10 cents
- **Status:** L1 V5 design packet — concept/design-planning only, not fabrication-ready

Primary repo links:
- [README](../../../../idiophones/bowed-dish/README.md)
- [Design notes](../../../../idiophones/bowed-dish/design.md)
- [Wolfram starter](../../../../idiophones/bowed-dish/bowed-dish-starter.wl)

## Current Status

- Release state: L1 V5 design packet — blueprint and concept only. Rod/dish coupling model requires prototype measurements before build-ready claim.
- Library family: idiophone.
- Acoustic class: friction idiophone (bowed rod → dish radiator).
- Wolfram state: starter rod/dish frequency model present; Wolfram Cloud Public-Execute URL available.
- CAD state: SolidWorks plan described; no confirmed `.glb`.

## Source Notes

- [README](../../../../idiophones/bowed-dish/README.md) — target (C4, 261.63 Hz), radiator (400 mm × 80 mm 1100-O aluminum), exciter (12 mm OD steel rod, adjustable effective length), validation gate (10 s sustained, ±10 cents).

Artifacts not ingested: `design.md`, `parameters.csv`, `validation.csv`, fabrication plan.

## Design Knowledge

Cristal Baschet technique: wet or rosined fingers rub a glass or metal rod to induce stick-slip vibration (same mechanism as a musical saw or wine-glass harp). In this design, a steel rod substitutes for glass, and the vibration transfers to a large aluminum dish that acts as a radiating panel.

1100-O aluminum is fully annealed (O temper), giving maximum ductility and low damping coefficient — important for long sustain. The dish profile (400 mm, 80 mm deep) is the principal radiating area; its resonance near C4 must be tuned by curvature (hammering) or thickness reduction (thinning the center).

Rod effective bending length determines the rod's fundamental frequency, which must couple efficiently to the dish. The adjustment mechanism (sliding clamp, adjustable mass) allows fine-tuning.

Related: [[instruments/cristal-baschet]] (full multi-rod version with whisker radiators), [[instruments/musical-saw]] (flexible blade bowed at S-curve, continuous pitch control).

## Cross-Links

- [[acoustic-classes/friction-idiophone]]
- [[instruments/cristal-baschet]]
- [[instruments/musical-saw]]

## Open Questions

1. What is the rod effective length adjustment mechanism?
2. How is the rod coupled to the dish?
3. What aluminum dish property enables the sustained bow response?
4. Has a ≥10 s, ±10 cents sustained prototype tone been achieved?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for rod/dish coupling model and `bowed-dish-starter.wl` for frequency predictions.
