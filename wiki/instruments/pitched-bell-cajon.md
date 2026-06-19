---
title: Pitched Bell Cajón Blueprint
slug: pitched-bell-cajon
wiki_type: instrument
status: active
sources:
  - path: ../../../../percussion/pitched-bell-cajon/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - instruments/cajon
  - acoustic-classes/struck-bar-idiophone
  - fabrication/brass-bell-tuning
open_questions:
  - "What are the exact bell dimensions (length, diameter, alloy) for each of the 5 pitches (G major pentatonic)?"
  - "How are the foot-pedal levers mechanically linked to the internal mallet strikers — cable, push rod, or direct pivot?"
  - "Is the cajon box body tuned to reinforce one of the bell pitches, or is it acoustically decoupled from the bells?"
  - "Can all 5 bells be played simultaneously (chord) or only one at a time?"
last_ingest: 2026-06-19
tags: [instrument, drum, cajon, brass-bells, foot-pedal, pitched, G-major-pentatonic, hybrid, mallet]
---

# Pitched Bell Cajón Blueprint

## Overview

A hybrid percussive instrument that integrates a standard sheet-metal cajón body with 5 internal brass bells, each tuned to a pitch of the G major pentatonic scale, and activated by foot-pedal mallet levers. The player performs conventional hand drumming on the cajón front face while using foot pedals (like a hi-hat or kick pedal) to ring individual bells — simultaneous melodic and rhythmic playing from one instrument and one player.

- **Family:** membranophone + idiophone hybrid / cajón with internal bells
- **Box body:** CRS sheet-metal cajón (standard snare-enabled design)
- **Bells:** 5 brass bells, tuned to G major pentatonic (G, A, B, D, E)
- **Activation:** foot-pedal mallet levers, one pedal per bell
- **Status:** blueprint packet — geometry, bell tuning, and pedal mechanism defined; no confirmed prototype

Primary repo links:
- [README](../../../../percussion/pitched-bell-cajon/README.md)
- [Design notes](../../../../percussion/pitched-bell-cajon/design.md)

## Current Status

- Release state: blueprint packet; no confirmed empirical validation.
- Library family: drum (parent body is cajón / percussive primary).
- Acoustic class: hybrid (membranophone box + struck-bar idiophone).
- CAD state: bell dimensions and pedal geometry defined; no confirmed `.glb`.

## Source Notes

- [README](../../../../percussion/pitched-bell-cajon/README.md) — instrument concept (cajón body + 5 brass bells + foot pedals, G major pentatonic), mechanical linkage description, player ergonomics overview.

Artifacts not ingested: `design.md`, `parameters.csv`, `validation.csv`, `bom.csv`.

## Design Knowledge

The G major pentatonic (G2/A2/B2/D3/E3 or an octave higher) is a 5-note scale with no semitone intervals, making it easy to play in any combination without dissonance — a good choice for an instrument designed for rhythmic-melodic simultaneous playing where the melodic part may not follow a key signature closely.

Brass bells (tube bells or cast bells) are the strike element: they must be individually tuned (cut to length for tube bells, or adjusted by weight-removal for cast bells) and mounted inside the cajón body on rigid posts to avoid damping. The mallet striker is a soft or medium-hardness tip on a pivot arm actuated by the foot pedal via a push rod or Bowden cable.

The cajón body provides acoustic separation: it acts as a resonance box for the hand-drumming voice and as an enclosure that keeps the bell strikers hidden and mechanically protected. If the box is tuned to a bell pitch, sympathetic resonance is possible.

The pedal mechanism must allow smooth, independent actuation of each of the 5 bells while the player's foot rests on a common rail or individual pedal pads.

Related: [[instruments/cajon]] (parent instrument, box-body design), [[acoustic-classes/struck-bar-idiophone]] (bell acoustic class).

## Cross-Links

- [[instruments/cajon]]
- [[acoustic-classes/struck-bar-idiophone]]
- [[fabrication/brass-bell-tuning]]

## Open Questions

1. What are the brass bell dimensions (length, diameter, alloy) for each of the 5 pentatonic pitches?
2. How are foot-pedal levers linked to internal mallet strikers (cable, push rod, direct pivot)?
3. Is the cajón box body tuned to reinforce a bell pitch, or acoustically decoupled?
4. Can all 5 bells be played simultaneously (chord), or only one at a time?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for bell tuning math and pedal mechanism detail.
