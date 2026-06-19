---
title: Glass Harp Blueprint (Wine Glass Friction Idiophone)
slug: glass-harp
wiki_type: instrument
status: active
sources:
  - path: ../../../../idiophones/glass-harp/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/friction-idiophone
  - instruments/glass-armonica
  - instruments/cristal-baschet
  - instruments/jal-tarang
open_questions:
  - "How many glasses are in scope — and what pitch range (C4–C6, C4–C7)?"
  - "What glass selection protocol — specific brand/model, or a measurement-based selection from a pool?"
  - "What is the fill-height tuning procedure — does this instrument commit to fixed fill or allow real-time adjustment?"
  - "What table / staging layout prevents spills and resonance interference between adjacent glasses?"
last_ingest: 2026-06-19
tags: [instrument, idiophone, glass-harp, wine-glass, friction, wet-finger, water-fill, tunable, L2]
---

# Glass Harp Blueprint — Wine Glass Friction Idiophone

## Overview

A glass harp: a set of tuned wine glasses played by wet fingers around the rims, with pitch selected by glass choice and adjusted by water fill level. Unlike the glass armonica (which rotates the glasses), the glass harp is stationary — the player's finger moves around each rim. Performance requires continuous wetting and careful glass/water management.

- **Family:** idiophone / friction glass vessel instrument
- **Mechanism:** wetted finger circling glass rim → friction-excited resonance → sustained pitch
- **Tuning:** glass selection (dominant) + water fill level (fine adjustment)
- **Status:** L2 V5 build-packet candidate — design study, no glass specification, fill table, or acoustic measurements

Primary repo links:
- [README](../../../../idiophones/glass-harp/README.md)
- [Design notes](../../../../idiophones/glass-harp/design.md)
- [Decision record](../../../../idiophones/glass-harp/decision-record.md)

## Current Status

- Release state: L2 V5 build-packet candidate — design study and review scaffold only. Glass selection, water level, rim behavior, table layout, damping, and playability are all pending measurement.
- Library family: idiophone.
- Acoustic class: friction idiophone (glass vessel, wet-finger excited).

## Source Notes

- [README](../../../../idiophones/glass-harp/README.md) — mechanism (friction idiophone, glass selection, water level tuning), first build problem (selection, labeling, fill control, spill-safe staging), packet map.

Artifacts not ingested: `design.md`, `bom.csv`, `cut-list.csv`, `decision-record.md`.

## Design Knowledge

The glass harp works by wet-finger stick-slip: a wetted finger dragged around the rim excites a mode of the glass body. Pitch depends primarily on the glass geometry (diameter, height, wall profile, rim thickness) and secondarily on water level (water damps higher modes and shifts the effective vibrating length).

The first build challenge is not physics but logistics: selecting a consistent set of glasses with adequate pitch spacing, labeling and staging them for performance access, maintaining appropriate wetting, and managing water spill risk on a horizontal surface with many glasses.

Glass selection is not deterministic from geometry alone — identical-looking glasses from the same production run can have pitch variations of ±50 cents. A measurement pass is needed: strike each glass, measure Hz, sort by pitch, then assign fill levels to adjust to target pitches.

Related: [[instruments/glass-armonica]] (same friction principle, rotating spindle — allows chord playing with both hands), [[instruments/jal-tarang]] (similar concept using ceramic/porcelain bowls struck, not rubbed).

## Cross-Links

- [[acoustic-classes/friction-idiophone]]
- [[instruments/glass-armonica]]
- [[instruments/cristal-baschet]]
- [[instruments/jal-tarang]]

## Open Questions

1. How many glasses in scope — what pitch range?
2. What glass selection protocol (brand-specific or measurement-based)?
3. Fixed fill (rehearsal-set) or real-time water adjustment during performance?
4. What table/staging layout prevents spills and inter-glass resonance?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for glass selection criteria and `decision-record.md` for staging and fill protocol.
