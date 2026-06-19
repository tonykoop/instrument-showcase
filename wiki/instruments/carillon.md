---
title: Carillon Blueprint (Tower Bells with Baton Keyboard)
slug: carillon
wiki_type: instrument
status: active
sources:
  - path: ../../../../idiophones/carillon/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/bell-idiophone
  - fabrication/bronze-casting
  - instruments/tubular-bells
open_questions:
  - "How many bells are in scope — traditional carillon minimum is 23; what is the target for this design?"
  - "Is bronze casting in scope (traditional), or is a cast-iron or machined-steel bell approach considered?"
  - "What is the action mule design — baton travel, pedal leverage, wire routing, return springs, clapper clearance?"
  - "What is the tower structure design — timber, steel, or existing structure adaptation?"
last_ingest: 2026-06-19
tags: [instrument, idiophone, carillon, tower-bells, baton-keyboard, bronze, clapper, L3-candidate]
---

# Carillon Blueprint — Tower Bells with Baton Keyboard

## Overview

A full carillon: a set of tuned bronze tower bells played from a baton-and-pedal keyboard, with mechanical transmission from batons to external clappers. The carillon is among the most acoustically and mechanically complex instruments in the library — bells must be founded (cast), tuned (lathe-turned), hung, connected to an action, and mounted in a tower structure. This packet is L3-candidate with deepened protocols, tolerances, assembly notes, and FMEA.

- **Family:** idiophone / tower bell carillon
- **Bells:** tuned bronze (traditional foundry or equivalent)
- **Action:** baton-and-pedal keyboard, mechanical wire transmission to clappers
- **Status:** L3-candidate V5 packet — design-planning authority only, no bell founding/fabrication

Primary repo links:
- [README](../../../../idiophones/carillon/README.md)
- [Design notes](../../../../idiophones/carillon/design.md)
- [Decision record](../../../../idiophones/carillon/decision-record.md)

## Current Status

- Release state: L3-candidate packet with deepened protocols, tolerances, assembly, FMEA. Not fabrication-ready; no fabricated bell dimensions, tuning table, or tower loads calculated.
- Library family: idiophone.
- Acoustic class: bell idiophone (cast bronze).
- Next step: non-sounding action mule — baton travel, pedal leverage, wire routing, return springs, clapper clearance, mechanical lost motion.

## Source Notes

- [README](../../../../idiophones/carillon/README.md) — instrument overview (bronze tower bells, baton-and-pedal keyboard, mechanical clappers), packet map, L2 review scope (action mule before bell founding).

Artifacts not ingested: `design.md`, `bom.csv`, `decision-record.md`.

## Design Knowledge

A carillon is divided into subsystems: bells, action, tower. The bells are the most technically demanding: traditional carillon bells are cast in bell bronze (4:1 Cu:Sn), tuned on a lathe to achieve the classic partial structure (hum, prime, tierce, quint, nominal). Each bell has 5 named partials that must be in specific ratios. This is specialized foundry work.

The action separates the keyboard mechanics from the bell tuning problem: clapper clearance, wire tension, baton travel (typically 7–10 cm), pedal leverage, and return spring force all affect playability. A non-sounding action mule (no bells, just the keyboard → wire → clapper mechanism) is the correct first prototype to validate action ergonomics before committing to expensive bell founding.

The tower structure must support the combined weight of all bells (can be several tons for a large carillon), the wind and dynamic loads from swinging clappers, and provide acoustic projection.

Related: [[instruments/tubular-bells]] (simpler tube-bell approximation using hollow tube fundamentals rather than cast bell partials).

## Cross-Links

- [[acoustic-classes/bell-idiophone]]
- [[fabrication/bronze-casting]]
- [[instruments/tubular-bells]]

## Open Questions

1. How many bells are in scope — what is the target range (traditional minimum is 23)?
2. Is bronze casting in scope, or is a cast-iron / machined-steel bell approach considered?
3. What is the action mule design for baton travel and clapper mechanism?
4. What is the tower structure design?

## Maintenance Notes

First ingest from README only. This is the largest-scale instrument in the library in terms of structural engineering and fabrication complexity. Next pass: read `design.md` for bell founding and action design, `decision-record.md` for scope decisions.
