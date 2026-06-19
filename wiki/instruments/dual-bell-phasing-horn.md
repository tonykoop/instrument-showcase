---
title: Dual-Bell Phasing Horn
slug: dual-bell-phasing-horn
wiki_type: instrument
status: active
sources:
  - path: ../../../../brass/dual-bell-phasing-horn/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/natural-brass-harmonic-series
  - fabrication/sheet-metal-brass
  - fabrication/y-junction-manifold
open_questions:
  - "Does the Y-junction branch selector shift pitch when switching between Bell A and Bell B, or is pitch truly preserved as designed?"
  - "How is the branch sealed at the inactive bell to prevent acoustic bleed between the two bell paths?"
  - "What are the specific Bessel vs conical profile parameters for Bell A and Bell B?"
  - "No capstone-manifest.json — not yet at V5 build-packet gate."
last_ingest: 2026-06-19
tags: [instrument, brass, experimental, dual-bell, selectable-timbre, y-junction, valved]
---

# Dual-Bell Phasing Horn

## Overview

A Bb trumpet-family sheet-metal brass instrument with a shared mouthpiece, leadpipe, and valve block feeding two selectable bells through a Y-junction. Bell A targets a brighter Bessel-like flare profile; Bell B targets a darker conical-first-pass profile. The branch selector changes timbre without shifting the nominal pitch class — the player chooses tone color, not pitch.

- **Family:** lip-reed brass / valved horn with selectable bell
- **Tuning:** Bb trumpet family (shared valve block)
- **Bells:** Bell A (bright, Bessel flare) / Bell B (dark, conical flare), selected via Y-junction
- **Status:** L2 V5 blueprint — design intent and parameter tables; no measured spectral data, no prototype

Primary repo links:
- [README](../../../../brass/dual-bell-phasing-horn/README.md)
- [Design notes](../../../../brass/dual-bell-phasing-horn/design.md)
- [Fabrication plan](../../../../brass/dual-bell-phasing-horn/fabrication-plan.md)
- [Assembly manual](../../../../brass/dual-bell-phasing-horn/assembly-manual.md)

## Current Status

- Release state: L2 V5 build-packet candidate — blueprint only; fabrication authority pending shop review and prototype measurement.
- Library family: brass.
- Wolfram state: Wolfram Cloud Public-Execute URL available.
- CAD state: placeholder DXFs; no confirmed `.glb`.
- No `capstone-manifest.json`.

## Source Notes

- [README](../../../../brass/dual-bell-phasing-horn/README.md) — core idea (same pitch, two bell colors), packet status, key files list.

Artifacts not ingested: `design.md`, `parameters.csv`, `validation.csv`, `risks.md`.

## Design Knowledge

The instrument preserves the Bb trumpet acoustic length and valve intervals through the shared leadpipe + valve block. At the Y-junction, the player selects which bell path is active (the other is capped or stopped). The bell profiles differ in flare exponent: Bell A's Bessel profile produces a brighter, higher spectral centroid; Bell B's more gradual conical profile produces a darker response. The design goal is a timbre switch without a pitch shift.

The Y-junction is the critical fabrication and acoustic risk — the branch transition must be area-matched to avoid impedance discontinuity and branch bleed.

## Cross-Links

- [[acoustic-classes/natural-brass-harmonic-series]]
- [[fabrication/sheet-metal-brass]]
- [[fabrication/y-junction-manifold]]

## Open Questions

1. Does the Y-junction branch selector shift pitch when switching bells, or is pitch truly preserved?
2. How is the inactive bell sealed against acoustic bleed?
3. What are the specific Bessel vs conical parameters for Bell A and Bell B?
4. No `capstone-manifest.json` — not yet at V5 build-packet gate.

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for Y-junction acoustic model and bell profile parameters, and `risks.md` for branch-bleed and pitch-shift risk analysis.
