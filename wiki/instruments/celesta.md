---
title: Celesta Blueprint (Keyboard Steel-Bar Idiophone)
slug: celesta
wiki_type: instrument
status: active
sources:
  - path: ../../../../idiophones/celesta/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/struck-bar-idiophone
  - instruments/glockenspiel
  - instruments/marimba-piano
open_questions:
  - "What is the target range — traditional celesta is C4 to C8 (4 octaves)?"
  - "What bar material — steel (traditional) or aluminum?"
  - "What hammer felt hardness and action travel spec?"
  - "What resonator box material and how are boxes tuned to each bar?"
last_ingest: 2026-06-19
tags: [instrument, idiophone, celesta, keyboard, steel-bar, hammer, resonator, damper, L2]
---

# Celesta Blueprint — Keyboard Steel-Bar Idiophone

## Overview

A celesta: a keyboard idiophone where piano-style keys drive felt hammers into graduated steel bars suspended above individual resonator boxes, with dampers controlling sustain and release. The celesta's delicate, bell-like tone comes from the combination of struck steel bars and box resonators that reinforce each bar's fundamental.

- **Family:** idiophone / keyboard-driven struck-bar instrument
- **Mechanism:** piano-style key → felt hammer → tuned steel bar → box resonator → damper
- **Range:** multi-octave (traditional C4–C8; exact target TBD)
- **Status:** L2 V5 build-packet candidate — mechanism study; no released dimensions or tuning table

Primary repo links:
- [README](../../../../idiophones/celesta/README.md)
- [Design notes](../../../../idiophones/celesta/design.md)
- [Decision record](../../../../idiophones/celesta/decision-record.md)

## Current Status

- Release state: L2 V5 build-packet candidate. Mechanism study complete; no fabricated bar dimensions, hammer weights, action geometry, resonator sizes, or DXF.
- Library family: idiophone.
- Acoustic class: struck-bar idiophone (keyboard-driven).

## Source Notes

- [README](../../../../idiophones/celesta/README.md) — mechanism summary (key → felt hammer → steel bar → resonator → damper), L2 boundary, packet map.

Artifacts not ingested: `design.md`, `bom.csv`, `cut-list.csv`, `decision-record.md`.

## Design Knowledge

The celesta differs from the glockenspiel in having: (1) box resonators beneath each bar, (2) felt dampers, and (3) a piano-style action with hammer rebound escape. The result is a softer, more controlled attack and significantly longer sustain than an open mallet glockenspiel.

Key subsystem interfaces:
- **Action**: hammer must strike cleanly and rebound without bouncing (requires escapement or at minimum a blocking rest). Felt hardness determines attack character — softer felt → quieter, rounder tone.
- **Bar suspension**: bars must be supported only at node points (22.4% and 77.6% of length) so free-free vibration is not damped by the mounts.
- **Resonator**: wooden box beneath each bar is tuned to reinforce the bar's fundamental by closing the box at the anti-node — box length ≈ quarter-wave of the target pitch.
- **Damper**: raises when the key is pressed, releases when key is released — must not rattle against bar between strokes.

Related: [[instruments/glockenspiel]] (no resonators, no dampers, open mallets), [[instruments/marimba-piano]] (modular keyboard + interchangeable tone-bar frame concept).

## Cross-Links

- [[acoustic-classes/struck-bar-idiophone]]
- [[instruments/glockenspiel]]
- [[instruments/marimba-piano]]

## Open Questions

1. What is the target range (traditional C4–C8)?
2. What bar material — steel (traditional celesta) or aluminum?
3. What hammer felt hardness and action travel spec?
4. What resonator box material and how are boxes tuned to each bar?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for mechanism and bar specification, `decision-record.md` for bar material and resonator design decisions.
