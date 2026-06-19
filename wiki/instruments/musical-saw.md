---
title: Musical Saw Blueprint (Bowed Flexible Blade)
slug: musical-saw
wiki_type: instrument
status: active
sources:
  - path: ../../../../idiophones/musical-saw/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/friction-idiophone
  - instruments/daxophone
  - instruments/bowed-dish
open_questions:
  - "What saw blade profile — industrial handsaw dimensions, or a purpose-made musical saw blank?"
  - "What steel specification and temper for optimal sustained bowing response?"
  - "What is the recommended S-curve bending approach for the player — seated knee-bend, hand-at-tip technique, or other?"
  - "Has any prototype bowing test been done — and what pitch range was achievable?"
last_ingest: 2026-06-19
tags: [instrument, idiophone, musical-saw, bowed, flexible-blade, S-curve, friction, L1]
---

# Musical Saw Blueprint — Bowed Flexible Blade

## Overview

A musical saw: a flexible hand-saw blade played by bowing or striking while bent into an S-curve. Pitch is controlled continuously by changing the bend, torsion, support point, and bow contact location — no fixed frets or tuned bars. The S-curve creates a local "sweet spot" where a standing wave can exist, and the player moves this point along the blade to select pitch.

- **Family:** idiophone / bowed flexible plate
- **Excitation:** bow (primary) or strike (secondary test mode)
- **Pitch control:** blade flex (S-curve geometry), torsion, hand support, bow contact point
- **Status:** L1 concept packet — not build-ready; no blade profile, steel spec, bowing force, or tuning data

Primary repo links:
- [README](../../../../idiophones/musical-saw/README.md)
- [Design notes](../../../../idiophones/musical-saw/design.md)
- [Decision record](../../../../idiophones/musical-saw/decision-record.md)

## Current Status

- Release state: L1 concept packet. No released dimensions, tuning table, blade profile, steel spec, bowing force, or fabrication instructions.
- Library family: idiophone.
- Acoustic class: friction idiophone (bowed flexible plate).

## Source Notes

- [README](../../../../idiophones/musical-saw/README.md) — mechanism (flexible blade, S-curve bend, bowed edge excitation, pitch by flex/torsion/contact point), first-order risks (blade edge safety, flex repeatability, measurement repeatability).

Artifacts not ingested: `design.md`, `bom.csv`, `decision-record.md`.

## Design Knowledge

The musical saw pitch mechanism: bending the saw blade into an S-curve creates a nodal line at the inflection point where the curvature reverses. The region near this inflection point is locally flat and can sustain a standing wave transverse to the blade. The player selects pitch by varying the bend radius (which moves the nodal line) and by controlling bow contact relative to the node.

Sustain is highly sensitive to blade dimensions: too stiff (thick blade, high-modulus steel) → poor response; too flexible (thin blade) → poor sustain and pitch instability. Musical saw blades are specifically designed and tempered for this use — typically 0.040–0.060 in thick, 4–6 in wide, 24–36 in long, with high-carbon blade steel.

Bowed excitation works best when the bow hair contacts the blade near the loop (anti-node) of the vibrating region, perpendicular to the blade length. Rosin application is required. Struck playing is possible but produces a different (damped, transient) tone.

Safety: blade edge handling during playing (bare metal teeth or smooth edge?), flex fatigue (blade will work-harden at the S-curve over repeated playing), and vibration exposure are key risks.

Related: [[instruments/daxophone]] (bowed wooden tongue, same stick-slip excitation on flexible material), [[instruments/bowed-dish]] (bowed rod into aluminum dish radiator, single fixed pitch).

## Cross-Links

- [[acoustic-classes/friction-idiophone]]
- [[instruments/daxophone]]
- [[instruments/bowed-dish]]

## Open Questions

1. What saw blade profile (industrial vs purpose-made musical saw blank)?
2. What steel specification and temper for optimal bowing response?
3. What S-curve bending technique is recommended?
4. Has any prototype bowing test been done — what pitch range was achievable?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for blade specification and flex/resonance model.
