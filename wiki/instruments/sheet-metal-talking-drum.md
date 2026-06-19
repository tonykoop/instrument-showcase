---
title: Sheet-Metal Talking Drum Blueprint
slug: sheet-metal-talking-drum
wiki_type: instrument
status: active
sources:
  - path: ../../../../percussion/sheet-metal-talking-drum/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/pressure-tuned-drum
  - fabrication/sheet-metal-spinning
  - fabrication/rolled-sheet-metal-shell
open_questions:
  - "How are the two mirror-cone halves joined at the waist — welded seam, or a slip-fit pressure ring?"
  - "What is the precise pitch range specified — G3→D5 is approximately a minor 7th; how many distinct pitches are controllable by elbow squeeze?"
  - "What is the rawhide tension-ladder geometry (number of ropes, crossing pattern, squeeze-to-pitch mapping)?"
  - "What are the cone dimensions (head diameter, cone height, waist diameter) for the two halves?"
last_ingest: 2026-06-19
tags: [instrument, drum, talking-drum, hourglass, pressure-tuned, sheet-metal, G3, D5, rawhide, squeeze]
---

# Sheet-Metal Talking Drum Blueprint

## Overview

A sheet-metal translation of the hourglass-shaped talking drum (like the Yoruba dùndún, not to be confused with the Mande dundun bass drum). The shell is an hourglass formed by two mirror-image conical frustums joined at the waist. Rawhide heads on both ends are connected by a tension rope ladder. Squeezing the ropes with the elbow while striking with a curved stick bends the membrane pitch from G3 to D5 — approximately a minor 7th range — allowing melodic speech-tone patterns.

- **Family:** membranophone / pressure-tuned hourglass drum
- **Shell:** two mirror-image conical frustums, sheet-metal, joined at waist
- **Heads:** rawhide (both ends)
- **Tensioning:** rawhide rope tension ladder connecting both heads
- **Pitch range:** G3→D5 by elbow-squeeze variation of rope tension
- **Status:** blueprint packet — geometry and tension model defined; no confirmed prototype

Primary repo links:
- [README](../../../../percussion/sheet-metal-talking-drum/README.md)
- [Design notes](../../../../percussion/sheet-metal-talking-drum/design.md)

## Current Status

- Release state: blueprint packet; no confirmed empirical validation.
- Library family: drum.
- Acoustic class: pressure-tuned hourglass drum.
- CAD state: hourglass shell geometry defined; no confirmed `.glb`.

## Source Notes

- [README](../../../../percussion/sheet-metal-talking-drum/README.md) — hourglass shell (two mirror cones), rawhide tension ladder, elbow-squeeze pitch control, G3→D5 range.

Artifacts not ingested: `design.md`, `parameters.csv`, `bom.csv`.

## Design Knowledge

The talking drum's distinctive property is continuously variable pitch during a stroke: the elbow squeezes the lateral rope ladder, increasing tension on both heads simultaneously, raising the membrane fundamental. Release of squeeze lowers the pitch. This produces the speech-like gliding tones characteristic of Yoruba tonal language communication.

The G3→D5 range (roughly a 10-semitone minor 7th) is typical for the kalangu/dùndún family. The sheet-metal translation must preserve this: the cones must be thin enough (1.0–1.2 mm) that the shell does not damp membrane vibration, and the waist junction must not block rope-tension transmission between the two heads.

The hourglass shell geometry: each half is a conical frustum (wide at the head, narrow at the waist), mirror-imaged. The waist diameter and half-angle determine the overall ergonomics (elbow grip width) and the shell's mechanical compliance under squeeze load.

Rawhide (untreated skin) is preferred for the rope ladder because it provides consistent stiffness after initial conditioning. Tension rope pattern: typically 8–12 vertical ropes in a zigzag ladder between the two head rings.

Related to, but distinct from, [[instruments/dundun]] (Mande cylindrical bass drum with same name but different instrument class and origin).

## Cross-Links

- [[acoustic-classes/pressure-tuned-drum]]
- [[fabrication/sheet-metal-spinning]]
- [[fabrication/rolled-sheet-metal-shell]]

## Open Questions

1. How are the two mirror-cone halves joined at the waist — welded seam or slip-fit pressure ring?
2. How many distinct controllable pitches exist in the G3→D5 elbow-squeeze range?
3. What is the rawhide tension-ladder geometry (rope count, crossing pattern)?
4. What are the cone dimensions (head diameter, cone height, waist diameter)?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for cone geometry math and rope-tension model. Note instrument is unrelated to the Mande dundun (cylindrical bass drum) despite similar names.
