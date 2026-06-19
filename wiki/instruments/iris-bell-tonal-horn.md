---
title: Iris-Bell Tonal Horn
slug: iris-bell-tonal-horn
wiki_type: instrument
status: active
sources:
  - path: ../../../../brass/iris-bell-tonal-horn/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/natural-brass-harmonic-series
  - fabrication/sheet-metal-brass
  - fabrication/hammer-forming
open_questions:
  - "Do the eight overlapping petals seal well enough at any aperture setting to prevent leakage that would detune the instrument?"
  - "What mechanism drives petal aperture — manual ring, thumbscrew, or other — and does it hold its position under playing pressure?"
  - "Is the 800–1500 Hz spectral centroid shift achievable with the petal geometry, or is it masked by the fixed bore's resonances?"
  - "No capstone-manifest.json — not yet at V5 build-packet gate."
last_ingest: 2026-06-19
tags: [instrument, brass, experimental, adjustable-bell, iris, hammer-formed, tonal-variation]
---

# Iris-Bell Tonal Horn

## Overview

A Bb trumpet-class brass instrument with a fixed tube length and an eight-petal adjustable iris bell. The aperture ranges from 2 in (closed) to 5 in (open), shifting the spectral centroid from ~800 Hz to ~1500 Hz — muted to open-bell brightness — from a single instrument with no mute to insert or remove.

- **Family:** brass / lip-buzzed horn
- **Acoustic intent:** Bb trumpet-class harmonic identity, variable terminal bell aperture
- **Bell mechanism:** eight overlapping hammer-formed yellow-brass petals
- **Aperture range:** 2 in closed → 5 in open
- **Tone target:** 800–1500 Hz spectral centroid shift between closed and open states
- **Status:** L2 V5 blueprint — petal forming, mechanism motion, and acoustic measurement pending

Primary repo links:
- [README](../../../../brass/iris-bell-tonal-horn/README.md)
- [Design notes](../../../../brass/iris-bell-tonal-horn/design.md)
- [Wolfram model](../../../../brass/iris-bell-tonal-horn/iris-bell-tonal-horn-starter.wl)
- [Fabrication plan](../../../../brass/iris-bell-tonal-horn/fabrication-plan.md)

## Current Status

- Release state: L2 V5 blueprint — concept/design planning; stop-work gates for petal forming, mechanism motion, leak testing, and acoustic measurement.
- Library family: brass.
- Wolfram state: first-order harmonic, aperture, and mechanism model (`.wl`) present; Wolfram Cloud Public-Execute URL available.
- CAD state: SolidWorks plan present; no confirmed `.glb`.
- No `capstone-manifest.json`.

## Source Notes

- [README](../../../../brass/iris-bell-tonal-horn/README.md) — design snapshot (family, aperture range, tone target, lineage), packet map, stop-work gates.

Artifacts not ingested: `design.md`, `parameters.csv`, `risks.md`, `validation.csv`.

## Design Knowledge

Lineage: Round 1 timpani hammer-forming craft applied to small brass petals. Each of the eight petals is individually hammer-formed from yellow brass sheet to a consistent profile, then assembled with overlapping edges that slide against each other as the aperture changes. The mechanism must maintain a seal (or controlled low-leak gap) at all aperture settings to avoid detuning the instrument through acoustic bleed.

The Wolfram model computes first-order harmonic series, aperture area, and mechanism geometry. The spectral centroid target (800–1500 Hz shift) is a design intent, not a measured result.

## Cross-Links

- [[acoustic-classes/natural-brass-harmonic-series]]
- [[fabrication/sheet-metal-brass]]
- [[fabrication/hammer-forming]]

## Open Questions

1. Do the eight overlapping petals seal well enough to prevent acoustic bleed at any aperture?
2. What mechanism drives petal aperture, and does it hold under playing pressure?
3. Is the 800–1500 Hz spectral centroid shift achievable, or masked by the fixed bore resonances?
4. No `capstone-manifest.json` — not yet at V5 build-packet gate.

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for iris mechanism architecture and `risks.md` for petal-seal and aperture-stability risk details.
