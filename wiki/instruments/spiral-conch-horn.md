---
title: Spiral Conch Horn Blueprint
slug: spiral-conch-horn
wiki_type: instrument
status: active
sources:
  - path: ../../../../brass/spiral-conch-horn/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/natural-brass-harmonic-series
  - fabrication/sheet-metal-brass
  - fabrication/lofted-bend-bell
open_questions:
  - "Do the 48 trapezoidal strake modules maintain bore continuity and acoustic equivalence to a smooth conical-ish duct?"
  - "What is the effective acoustic behavior of a planar logarithmic spiral duct vs a straight-tube brass instrument — are the harmonic resonances shifted by the curved path?"
  - "How is the 5 in in-plane oval bell rim aperture formed from the spiral's outer terminus?"
  - "No capstone-manifest.json — not yet at V5 build-packet gate."
last_ingest: 2026-06-19
tags: [instrument, brass, natural-horn, spiral, conch, logarithmic-spiral, wall-mount, strake]
---

# Spiral Conch Horn Blueprint

## Overview

A natural brass aerophone folded into a flat four-turn logarithmic spiral, inspired by the conch/nautilus profile. The bore is built from 48 local trapezoidal/lofted strake modules forming a 2940 mm effective acoustic path coiled into a 350 mm plan-view diameter body only 80 mm thick. The result is wall-mountable — functionally a bugle-class Bb1 horn in a display-worthy planar disc.

- **Family:** natural brass aerophone / lip-buzzed spiral horn
- **Target tuning:** Bb1 effective fundamental (~58 Hz)
- **Acoustic length:** ~2940 mm in a 350 mm diameter × 80 mm thick body
- **Bell:** 5 in in-plane oval rim aperture
- **Materials:** C26800 yellow brass, segmented strake construction, silver-brazed seams, brass rim wire
- **Status:** L2 V5 blueprint — acoustic and fabrication blueprint; no CAD, no prototype

Primary repo links:
- [README](../../../../brass/spiral-conch-horn/README.md)
- [Design notes](../../../../brass/spiral-conch-horn/design.md)
- [Fabrication plan](../../../../brass/spiral-conch-horn/fabrication-plan.md)

## Current Status

- Release state: L2 V5 build-packet candidate — blueprint assumptions only; CAD/DXF, paper-pattern checks, leak tests, and acoustic measurements are open V5 gates.
- Library family: brass.
- Wolfram state: Wolfram Cloud Public-Execute URL available.
- CAD state: SolidWorks plan and V5 authority register present; no confirmed `.glb`.
- No `capstone-manifest.json`.

## Source Notes

- [README](../../../../brass/spiral-conch-horn/README.md) — design thesis (logarithmic spiral acoustic centerline, 48 strake modules), targets (2940 mm, 350 mm dia, Bb1 fundamental, 5 in oval bell), V5 authority note.

Artifacts not ingested: `design.md`, `parameters.csv`, `validation.csv`.

## Design Knowledge

The design centerline is a large-center logarithmic spiral. Each of the 48 strake modules is a trapezoidal flat pattern (or lofted strake) that, when formed and brazed in sequence, follows the spiral's curvature while growing in cross-section from mouthpiece receiver to bell mouth. The assembly is braided along the outer edge with brass rim wire.

A planar spiral duct may behave differently acoustically from a straight-tube brass instrument of the same effective length — curved paths can introduce centrifugal mode effects. The packet explicitly notes this is a blueprint for CAD, paper-pattern tests, and acoustic coupons, not a claim of orchestral-horn behavior.

The instrument borrows the bugle's acoustic targets (same Bb1 fundamental, ~2940 mm effective length) but replaces the conventional folded tube with the planar spiral form. It hangs on a wall, not a player's hand.

## Cross-Links

- [[acoustic-classes/natural-brass-harmonic-series]]
- [[fabrication/sheet-metal-brass]]
- [[fabrication/lofted-bend-bell]]

## Open Questions

1. Do 48 trapezoidal strake modules maintain bore continuity and acoustic equivalence to a smooth duct?
2. Does the curved planar spiral path shift harmonic resonances vs a straight-tube brass instrument?
3. How is the 5 in oval bell rim aperture formed from the spiral's outer terminus?
4. No `capstone-manifest.json` — not yet at V5 build-packet gate.

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for spiral geometry math and strake module parameterization, and `validation.csv` for acoustic measurement gates. Compare bugle-sheetmetal's acoustic model for cross-reference.
