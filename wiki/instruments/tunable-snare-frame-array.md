---
title: Tunable Snare Frame Array Blueprint
slug: tunable-snare-frame-array
wiki_type: instrument
status: active
sources:
  - path: ../../../../percussion/tunable-snare-frame-array/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/frame-drum
  - fabrication/cr-steel-frame
  - instruments/frame-drum
open_questions:
  - "What are the exact shell ODs and depths for the three frame drums (150/200/250 mm)?"
  - "What is the head material — calfskin, Remo Ambassador, or a coated synthetic?"
  - "How are the snare wires mounted and tensioned on each frame drum?"
  - "Is the shared bracket rigid or adjustable — can spacing between drums be changed?"
  - "What are the actual measured pitches for the D3/A3/D4 targets under the snare tension?"
last_ingest: 2026-06-19
tags: [instrument, drum, frame-drum, snare, 3-piece, tunable, shared-bracket, D-minor-triad, 150mm, 200mm, 250mm]
---

# Tunable Snare Frame Array Blueprint

## Overview

Three independently-tunable snare frame drums — 150, 200, and 250 mm diameter — mounted on a common shared bracket. Target pitches are D3, A3, and D4 (a D minor triad spanning one octave). Each drum has its own snare wire set. The array is designed to be played by one player using two sticks, accessing all three drums simultaneously.

- **Family:** membranophone / snare frame drum set
- **Drums:** 3 frame drums, 150 / 200 / 250 mm OD
- **Target pitches:** D3 / A3 / D4 (D minor triad)
- **Snare:** individual snare wire set on each drum
- **Mounting:** shared bracket, fixed inter-drum spacing
- **Status:** blueprint packet — geometry, tuning targets, and bracket design defined; no confirmed prototype

Primary repo links:
- [README](../../../../percussion/tunable-snare-frame-array/README.md)
- [Design notes](../../../../percussion/tunable-snare-frame-array/design.md)

## Current Status

- Release state: blueprint packet; no confirmed empirical validation.
- Library family: drum.
- Acoustic class: snare frame drum (3-piece array).
- CAD state: frame drum shells and shared bracket geometry defined; no confirmed `.glb`.

## Source Notes

- [README](../../../../percussion/tunable-snare-frame-array/README.md) — 3-drum snare array (150/200/250 mm, D3/A3/D4 targets, shared bracket), individual snare wire sets, one-player configuration.

Artifacts not ingested: `design.md`, `parameters.csv`, `validation.csv`, `bom.csv`.

## Design Knowledge

Tuned snare frame drums are a non-standard instrument: conventional snare drums are not pitched, but a small-diameter frame drum with a taut head can produce a recognizable fundamental pitch while still retaining the snare texture. The 150–250 mm range allows pitching in the D3–D4 octave with achievable membrane tensions.

The D minor triad (D–A–D) is harmonically simple and generates chord-like rolls when all three drums are struck together. The shared bracket constrains their relative positions so the player can execute consistent single-stroke patterns across all three.

Snare wire placement on a frame drum (unlike a full-depth snare shell) must account for the shallow shell depth: the snare wires lie close to the resonant head (if any) or are mounted on a snare-side batten attached to the shell ring. Frame drums often use a single coil-spring or wire-strand snare rather than a full multi-strand snare unit.

Related: [[instruments/frame-drum]] (parent instrument class), [[instruments/bowed-frame-drum]] (CR-steel frame variant with tone bar).

## Cross-Links

- [[acoustic-classes/frame-drum]]
- [[fabrication/cr-steel-frame]]
- [[instruments/frame-drum]]

## Open Questions

1. What are the exact shell ODs and depths for the three drums?
2. What head material is specified?
3. How are snare wires mounted and tensioned on a shallow frame drum shell?
4. Is the shared bracket rigid or adjustable?
5. What are the actual measured pitches under snare tension — vs the D3/A3/D4 targets?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for shell geometry and snare-mount detail.
