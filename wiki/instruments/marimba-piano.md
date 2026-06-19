---
title: Marimba Piano Blueprint (Modular Keyboard Idiophone)
slug: marimba-piano
wiki_type: instrument
status: active
sources:
  - path: ../../../../idiophones/marimba-piano/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/struck-bar-idiophone
  - instruments/marimba
  - instruments/celesta
open_questions:
  - "How does the right-side platen lever clamp the tone-bar frame and seal the aperture plate against the resonator bank?"
  - "How does the left-side hammer selector rotate/index across the full keyboard range?"
  - "What tone-bar frame materials are planned (wood, synthetic, aluminum) and have any been coupon-tested?"
  - "What is the P0 coupon protocol result — A4/C5 one-note coupon for bar/support/hammer/aperture/resonator?"
last_ingest: 2026-06-19
tags: [instrument, idiophone, marimba-piano, keyboard, modular, interchangeable-toneframe, L1]
---

# Marimba Piano Blueprint — Modular Keyboard Idiophone

## Overview

A keyboard-driven modular idiophone: piano-style keys and hammers stay in the chassis; the sound source is a removable tone-bar frame that can be swapped for different acoustic profiles (wood, synthetic, aluminum, or other tested materials). Three modular systems: interchangeable tone-bar frames on the front plane, a right-side platen lever that clamps the frame and seals its aperture plate, and a left-side hammer selector that indexes multiple hammer-face materials across the full keyboard.

- **Family:** idiophone / modular keyboard-driven bar instrument
- **Mechanism:** piano-style keys → felt/hard hammers → swappable tone-bar frame → resonator bank
- **Modular systems:** (1) interchangeable tone-bar frames, (2) platen/aperture seal lever, (3) hammer-face selector
- **Range:** C4–C5 initial module (13 notes); extensible
- **Status:** L1 concept packet — not build-ready; P0 coupon protocol defined

Primary repo links:
- [README](../../../../idiophones/marimba-piano/README.md)
- [Design notes](../../../../idiophones/marimba-piano/design.md)
- [Prototype plan](../../../../idiophones/marimba-piano/prototype-plan.md)
- [P0 coupon protocol](../../../../idiophones/marimba-piano/p0-coupon-protocol.md)

## Current Status

- Release state: L1 concept packet. P0 through P3 build sequence defined; one-note A4/C5 coupon is the first physical step.
- Library family: idiophone.
- Acoustic class: struck-bar idiophone (modular keyboard, interchangeable tone-bar frame).

## Source Notes

- [README](../../../../idiophones/marimba-piano/README.md) — modular architecture (interchangeable tone-bar frames, platen lever, hammer-face selector), P0 one-note coupon (A4/C5, bar/support/hammer/aperture/resonator), C4–C5 initial range (13 notes), `references/sketch-20260514.jpg` (original morning sketch).

Artifacts not ingested: `design.md`, `prototype-plan.md`, `p0-coupon-protocol.md`, `validation.csv`.

## Design Knowledge

The core innovation is the interchangeable tone-bar frame: rather than building a dedicated instrument for each bar material, the chassis (keyboard action, hammer bank, resonator bank, platen/aperture assembly) remains fixed while the tone-bar frame is replaced as a module. This allows a single chassis to compare wood bars vs aluminum bars vs synthetic bars without rebuilding the entire instrument.

The platen lever is the structural coupling element: it clamps the tone-bar frame in position and seals the aperture plate against the resonator bank openings, ensuring consistent acoustic coupling between bars and resonators regardless of which frame is installed.

The hammer selector: rotating or indexing multiple hammer-face materials (hard, medium, soft) across the keyboard allows comparing attack characters with the same tone-bar frame. Combined with frame swaps, this produces a 2D experimental matrix: (hammer material) × (bar material).

The aperture plate: a thin plate between bar and resonator with openings at the anti-nodes of each bar. It affects resonator coupling efficiency and air-path geometry.

Related: [[instruments/marimba]] (fixed-frame orchestral marimba, the reference instrument for bar physics), [[instruments/celesta]] (similar keyboard-driven idiophone, different mechanism).

## Cross-Links

- [[acoustic-classes/struck-bar-idiophone]]
- [[instruments/marimba]]
- [[instruments/celesta]]

## Open Questions

1. How does the platen lever clamp the tone-bar frame and seal the aperture plate?
2. How does the hammer selector rotate/index across the full keyboard?
3. What tone-bar frame materials are planned — have any been coupon-tested?
4. What were the P0 coupon results (one-note A4/C5 for bar/support/hammer/aperture/resonator)?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for architecture detail and `p0-coupon-protocol.md` for the measurement procedure.
