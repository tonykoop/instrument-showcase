---
title: Cylinder Music Box Blueprint (Pinned Cylinder + Steel Comb)
slug: music-box
wiki_type: instrument
status: active
sources:
  - path: ../../../../idiophones/music-box/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/plucked-comb-idiophone
  - instruments/celesta
open_questions:
  - "How many comb teeth / notes — and what pitch range is targeted?"
  - "What is the governor/escapement design — fly governor (rotating vanes), centrifugal governor, or escapement wheel?"
  - "What is the cylinder diameter and pin layout (spiral or straight rows)?"
  - "What is the tune(s) programmed into the cylinder — and how are custom tunes encoded?"
last_ingest: 2026-06-19
tags: [instrument, idiophone, music-box, cylinder, comb, governor, escapement, L2]
---

# Cylinder Music Box Blueprint — Pinned Cylinder + Steel Comb

## Overview

A cylinder music box: a pinned rotating cylinder (the stored program) plucks tuned teeth on a steel comb while a governor and escapement regulate playback speed. The design focus is the mechanical timing chain from barrel pins to comb teeth, plus speed control, damping, and service access.

- **Family:** idiophone / mechanically-actuated plucked comb (clockwork)
- **Cylinder:** pinned barrel with programmed tune(s)
- **Comb:** steel comb with tuned teeth
- **Speed control:** governor and escapement mechanism
- **Status:** L2 V5 build-packet candidate — mechanism study; no released comb tooth lengths, cylinder diameter, pin coordinates, or governor speed target

Primary repo links:
- [README](../../../../idiophones/music-box/README.md)
- [Design notes](../../../../idiophones/music-box/design.md)
- [Decision record](../../../../idiophones/music-box/decision-record.md)

## Current Status

- Release state: L2 V5 build-packet candidate. Mechanism study complete; no fabricated geometry or dimensions.
- Library family: idiophone.
- Acoustic class: plucked-comb idiophone (mechanically actuated).

## Source Notes

- [README](../../../../idiophones/music-box/README.md) — mechanism (rotating pinned cylinder, steel comb teeth, governor/escapement speed control), design focus (mechanical timing chain, speed control, damping, service access), packet map.

Artifacts not ingested: `design.md`, `bom.csv`, `cut-list.csv`, `decision-record.md`.

## Design Knowledge

The music box is a clockwork instrument: energy stored in a wound spring (or applied by crank) drives the pinned cylinder. As the cylinder rotates, pins (small raised bumps) contact the tips of steel comb teeth, deflecting and releasing them — each tooth vibrates at its own resonant pitch determined by length and mass.

Steel comb teeth obey the same cantilever-beam formula as tongue drums: `f = K × t / L²`. Comb teeth are typically cut from a single flat steel blank, with decreasing lengths from bass to treble — the comb is one piece, not individual bars.

Governor types: fly governor (rotating vanes that create air resistance proportional to speed — simplest, used in traditional music boxes), centrifugal governor (balls on hinged arms that engage a brake above target speed), or Swiss-lever escapement (more precise, used in high-quality instruments). The governor determines playback speed consistency and tuning stability.

The cylinder program: pins are positioned at precise angular and axial locations. For a hand-built cylinder, programming requires either CNC or a jig for placing pins by hand in a correct layout.

## Cross-Links

- [[acoustic-classes/plucked-comb-idiophone]]
- [[instruments/celesta]]

## Open Questions

1. How many comb teeth / notes and what pitch range?
2. What governor/escapement design?
3. What cylinder diameter and pin layout?
4. What tune(s) are programmed and how are custom tunes encoded?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for comb tooth schedule and governor design, `decision-record.md` for pin encoding approach.
