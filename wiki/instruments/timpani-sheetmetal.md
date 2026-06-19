---
title: Timpani Sheet-Metal Blueprint
slug: timpani-sheetmetal
wiki_type: instrument
status: active
sources:
  - path: ../../../../percussion/timpani-sheetmetal/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/tunable-membrane-bowl
  - fabrication/copper-sheet-spinning
  - fabrication/tensioning-hardware
  - instruments/compact-drum-kit
open_questions:
  - "Is the 26 in bowl formed by spinning over a wooden or metal mandrel — and what is the target bowl depth?"
  - "How do the 8 T-handle tuning rods couple to the counter-hoop — threaded directly into the hoop, or through a spider bracket?"
  - "What is the target pitch range across the tuning range — D2 to A2 (typical 26 in concert timpano)?"
  - "Is there a pedal/ratchet mechanism for continuous tuning, or only manual T-handle adjustment?"
last_ingest: 2026-06-19
tags: [instrument, drum, timpani, sheet-metal, copper, 26-inch, T-handle, orchestral, tunable]
---

# Timpani — Sheet-Metal Blueprint

## Overview

A 26-inch concert-style timpano with a parabolic copper bowl formed from sheet copper, and 8 T-handle tuning rods providing manual pitch adjustment. The design targets orchestral timpani acoustic behavior — a tunable bass membrane radiator with a dominant fundamental and long decay — at sprint-shop fabrication cost.

- **Family:** membranophone / orchestral timpani (kettledrum)
- **Bowl:** 26 in parabolic copper, sheet-metal formed
- **Tuning:** 8 M8 T-handle tuning rods
- **Head:** calfskin or Remo Renaissance equivalent
- **Status:** blueprint packet — bowl geometry and tuning system defined; no confirmed prototype

Primary repo links:
- [README](../../../../percussion/timpani-sheetmetal/README.md)
- [Design notes](../../../../percussion/timpani-sheetmetal/design.md)

## Current Status

- Release state: blueprint packet; no confirmed empirical validation.
- Library family: drum.
- Acoustic class: tunable membrane bowl (orchestral timpani).
- Wolfram state: acoustic/modal model present; Wolfram Cloud Public-Execute URL available.
- CAD state: bowl geometry and tuning-rod arrangement defined; no confirmed `.glb`.

## Source Notes

- [README](../../../../percussion/timpani-sheetmetal/README.md) — 26 in copper bowl, 8 M8 T-handle tuning rods, sheet-metal forming approach, acoustic target (orchestral timpani).

Artifacts not ingested: `design.md`, `parameters.csv`, `validation.csv`, `bom.csv`.

## Design Knowledge

Orchestral timpani acoustics are dominated by the coupling between the membrane (calfskin or Mylar head) and the air column inside the bowl cavity. The parabolic bowl shape (as opposed to hemispherical or cylindrical) is a design choice that optimizes cavity volume and port location for the inharmonic membrane modes — specifically suppressing the (0,1) mode relative to the (1,1) mode to produce a more pitched, less noisy tone.

26 in is the standard "large" concert timpano, pitched in the D2–A2 range. The M8 T-handle rods thread through a spider bracket or directly through a counter-hoop to apply tension to the head. 8 rods at equal spacing provide even tension around the head circumference.

Sheet copper (18–22 gauge, dead-soft or 1/4-hard) is the traditional timpani bowl material (modern professional timpani use copper). It can be spun over a wooden mandrel or stretch-formed with a hammer into a parabolic profile.

The tuning system is manual (T-handles only, no pedal/ratchet) — simpler to fabricate, but requires stopping between pitches for adjustment.

Related: [[instruments/compact-drum-kit]] (same rolled CRS shell method for the kit shells).

## Cross-Links

- [[acoustic-classes/tunable-membrane-bowl]]
- [[fabrication/copper-sheet-spinning]]
- [[fabrication/tensioning-hardware]]
- [[instruments/compact-drum-kit]]

## Open Questions

1. How is the 26 in bowl formed — spinning over a wooden mandrel, or hammer/stretch forming?
2. How do the 8 T-handle rods couple to the counter-hoop?
3. What is the target pitch range — typical D2–A2 for a 26 in timpano?
4. Is a pedal/ratchet continuous-tuning mechanism in scope or only manual T-handles?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for bowl geometry and tuning-rod coupling detail. Check Wolfram model for membrane modal analysis.
