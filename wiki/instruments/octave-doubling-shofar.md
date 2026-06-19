---
title: Octave-Doubling Shofar-Form Horn
slug: octave-doubling-shofar
wiki_type: instrument
status: active
sources:
  - path: ../../../../brass/octave-doubling-shofar/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/natural-brass-harmonic-series
  - synthesis/chord-radiation-brass
  - fabrication/sheet-metal-brass
open_questions:
  - "Does the Y-branch octave resonator in practice produce two clearly distinct radiating pitches, or does the shared bore blur them into a dense single-pitch spectrum?"
  - "What is the acoustic coupling loss at the Y-branch junction — does the half-length branch siphon energy from the main bore?"
  - "What shaping strategy converts a quasi-conical duct into the shofar silhouette while maintaining bore continuity?"
  - "No capstone-manifest.json — not yet at V5 build-packet gate."
last_ingest: 2026-06-19
tags: [instrument, brass, ceremonial, shofar, octave-doubling, y-branch, ritual, experimental]
---

# Octave-Doubling Shofar-Form Horn

## Overview

A sheet-brass ceremonial horn in the shofar (ram's-horn) silhouette with a Y-branched octave-up resonator. A single buzz from one mouthpiece radiates two pitches simultaneously: Eb3 from the full-length main shofar curve and Eb4 from a half-length branch tube. Both bells exit forward, producing a droning octave-chord impossible from a single-bore horn.

- **Family:** ritual / ceremonial brass, lip-buzzed quasi-conical
- **Pitch targets:** Eb3 (155.56 Hz) + Eb4 (311.13 Hz) simultaneously
- **Envelope:** ~600 mm tip-to-tip chord; ~850 mm acoustic path along the curve; < 700 g; two-handed hold
- **Status:** v0.1.0 blueprint — parametric design + acoustic model + DFM packet; no fabrication yet

Primary repo links:
- [README](../../../../brass/octave-doubling-shofar/README.md)
- [Design notes](../../../../brass/octave-doubling-shofar/design.md)
- [Fabrication plan](../../../../brass/octave-doubling-shofar/fabrication-plan.md)

## Current Status

- Release state: L2 V5 build-packet candidate — v0.1.0 blueprint; fabrication and validation deferred to v0.2 prototype round.
- Library family: brass.
- Wolfram state: Wolfram Cloud Public-Execute URL available.
- CAD state: SolidWorks plan present; no confirmed `.glb`.
- No `capstone-manifest.json`.

## Source Notes

- [README](../../../../brass/octave-doubling-shofar/README.md) — design thesis (Y-branched bore exposes the lip buzz to two quasi-conical loads in parallel — main path resonant at f₀, half-length path resonant at 2f₀), targets, envelope, repo status.

Artifacts not ingested: `design.md`, `parameters.csv`, `validation.csv`.

## Design Knowledge

Conventional brass plays one mode at a time because the bore + lip-reed system has a single dominant resonance peak. The Y-branched bore exposes the buzz simultaneously to two quasi-conical loads: the long path (850 mm, resonant at Eb3 = 155 Hz) and the half-length branch (resonant at Eb4 = 311 Hz). Both modes are excited continuously by the harmonic content of the lip buzz; both bells radiate forward.

This is the simplest case of the "single-player chord" instrument family: one octave, one embouchure input. The shofar silhouette grounds the design aesthetically in ceremonial brass traditions.

Related work: [[synthesis/chord-radiation-brass]] (see also bell-stack-chord-horn for the H1/H3/H5 triad variant).

## Cross-Links

- [[acoustic-classes/natural-brass-harmonic-series]]
- [[synthesis/chord-radiation-brass]]
- [[fabrication/sheet-metal-brass]]

## Open Questions

1. Does the Y-branch produce two clearly distinct radiating pitches, or does the shared bore blur them into a dense spectrum?
2. What is the acoustic coupling loss at the Y-branch junction — does the half-length branch siphon energy from the main bore?
3. What shaping strategy converts a quasi-conical duct into the shofar silhouette while maintaining bore continuity?
4. No `capstone-manifest.json` — not yet at V5 build-packet gate.

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for Y-branch acoustic coupling analysis. File `synthesis/chord-radiation-brass` if a comparison page across bell-stack-chord-horn, octave-doubling-shofar, and branching-multibell-horn would be useful.
