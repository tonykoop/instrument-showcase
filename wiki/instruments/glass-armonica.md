---
title: Glass Armonica Blueprint (Franklin-Style Nested Bowl Friction Idiophone)
slug: glass-armonica
wiki_type: instrument
status: active
sources:
  - path: ../../../../idiophones/glass-armonica/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/friction-idiophone
  - instruments/glass-harp
  - instruments/cristal-baschet
open_questions:
  - "How many graduated glass bowls are planned — traditional armonica has ~37 bowls covering 3+ octaves?"
  - "What drive ratio and rotation speed for the treadle/flywheel system?"
  - "What is the bowl nesting clearance and spindle bearing spec?"
  - "What wetting system keeps all bowl rims moist during performance?"
last_ingest: 2026-06-19
tags: [instrument, idiophone, glass-armonica, franklin, friction, nested-bowls, treadle, flywheel, L3-candidate]
---

# Glass Armonica Blueprint — Franklin-Style Nested Bowl Friction Idiophone

## Overview

A Franklin-style glass armonica: graduated glass bowls nested coaxially on a horizontal spindle, rotated by a foot treadle and flywheel so both hands remain free, and played by touching wetted finger rims against the rotating bowls. Benjamin Franklin invented this instrument in 1761; it was widely played in the late 18th century. This packet is L3-candidate with deepened protocols, tolerances, assembly notes, and FMEA.

- **Family:** idiophone / friction glass bowl instrument
- **Mechanism:** foot treadle + flywheel → rotating nested glass bowls → wetted finger contact → sustained pitch
- **Pitch:** governed by bowl geometry and glass properties (no pitch table yet)
- **Status:** L3-candidate V5 packet — design study; no fabricated geometry, pitch map, or measured data

Primary repo links:
- [README](../../../../idiophones/glass-armonica/README.md)
- [Design notes](../../../../idiophones/glass-armonica/design.md)
- [Decision record](../../../../idiophones/glass-armonica/decision-record.md)

## Current Status

- Release state: L3-candidate V5 packet (deepened: protocols, tolerances, assembly, FMEA). No fabricated dimensions, no pitch table, no glass recipe or spindle drawings.
- Library family: idiophone.
- Acoustic class: friction idiophone (rotating glass bowl).

## Source Notes

- [README](../../../../idiophones/glass-armonica/README.md) — mechanism (graduated nested bowls on spindle, treadle+flywheel drive, wet-finger contact), engineering focus (quiet spindle support, stable bowl spacing, controlled wetting, safe guarding, serviceable mounting), packet map.

Artifacts not ingested: `design.md`, `bom.csv`, `cut-list.csv`, `decision-record.md`.

## Design Knowledge

The glass armonica works by the same friction principle as wine-glass harps: a wet finger on a rotating glass rim excites sustained oscillation via stick-slip friction. The armonica's advantage over the glass harp: the rotation means the rim always comes to the player's finger, allowing continuous sustained tones without the player's hand moving — enabling two-handed playing and chord voices.

Franklin's design nests bowls coaxially on a spindle (each bowl's rim exposed outward, from the open end facing the player). The graduated diameters produce pitch; each bowl is a fixed-pitch resonator. Playing involves touching multiple rims simultaneously for chords.

Key engineering challenges:
- **Spindle**: must be quiet (low-noise bearings), horizontal (for gravity-stable bowl mounting), and accessible for bowl removal/replacement
- **Treadle**: must maintain steady rotation against variable load (finger pressure changes bowl damping); flywheel smooths the rotation
- **Bowl spacing**: nesting clearance must allow individual bowl access without inter-bowl contact
- **Wetting**: a continuous water trough or felt applicator keeps rims moist throughout performance; splash management is a practical concern

Related: [[instruments/glass-harp]] (same friction principle, no rotation mechanism), [[instruments/cristal-baschet]] (glass rod variant with whisker radiators).

## Cross-Links

- [[acoustic-classes/friction-idiophone]]
- [[instruments/glass-harp]]
- [[instruments/cristal-baschet]]

## Open Questions

1. How many graduated glass bowls — what range (traditional ~37 bowls, 3+ octaves)?
2. What drive ratio and rotation speed for the treadle/flywheel?
3. What is the bowl nesting clearance and spindle bearing spec?
4. What wetting system keeps all bowl rims moist during performance?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for spindle and treadle mechanism. Note: L3-candidate status implies deeper analysis than most L2 instruments in the library.
