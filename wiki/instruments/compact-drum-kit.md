---
title: Compact Sheet-Metal Drum Kit Blueprint
slug: compact-drum-kit
wiki_type: instrument
status: active
sources:
  - path: ../../../../percussion/compact-drum-kit/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/cylindrical-shell-drum
  - fabrication/rolled-sheet-metal-shell
  - instruments/timpani-sheetmetal
open_questions:
  - "What are the exact shell diameters and depths for each of the 5 pieces (kick, snare, rack toms ×2, floor tom)?"
  - "How are the shells tensioned — tension rods / T-bolts into a counter-hoop, or lug-and-rod hardware?"
  - "What head stock is specified for the snare drum to achieve appropriate snare response with a sheet-metal shell?"
  - "Are the hardware mounting brackets (tom arms, cymbal stands) bought or fabricated?"
last_ingest: 2026-06-19
tags: [instrument, drum, drum-kit, sheet-metal, 5-piece, snare, kick, rack-tom, floor-tom, CRS]
---

# Compact Sheet-Metal Drum Kit Blueprint

## Overview

A 5-piece drum kit — kick, snare, two rack toms, and a floor tom — with shells fabricated from rolled cold-rolled steel (CRS) cylinders and bought hardware. The design prioritizes sheet-metal sprint methods: rolled and seam-welded shell cylinders, bought counter-hoops and tension hardware, bought drum heads.

- **Family:** membranophone / drum kit
- **Pieces:** kick, snare, 2 rack toms, floor tom (5-piece configuration)
- **Shell material:** rolled CRS, seam-welded cylinder
- **Hardware:** bought (tension rods, lugs, counter-hoops, tom arms, bass drum spurs)
- **Status:** blueprint packet — shell geometry and fabrication approach defined; no confirmed prototype

Primary repo links:
- [README](../../../../percussion/compact-drum-kit/README.md)
- [Design notes](../../../../percussion/compact-drum-kit/design.md)
- [BOM](../../../../percussion/compact-drum-kit/bom.csv)

## Current Status

- Release state: blueprint packet; no confirmed empirical validation.
- Library family: drum.
- Acoustic class: cylindrical-shell drum set.
- CAD state: shell geometry defined; no confirmed `.glb`.

## Source Notes

- [README](../../../../percussion/compact-drum-kit/README.md) — overview of the 5-piece configuration (kick/snare/2 rack toms/floor tom), rolled CRS cylinder shell method, bought hardware list.

Artifacts not ingested: `design.md`, `parameters.csv`, `bom.csv`, `validation.csv`.

## Design Knowledge

Drum kit shells are among the simplest acoustic shell forms — open cylinders with two tensioned heads. CRS rolled cylinders are straightforward to fabricate: roll sheet to diameter, tack and seam-weld, true on a lathe chuck if needed, then deburr and sand the bearing edges. The critical spec is bearing edge geometry (typically 30°–45° inner chamfer + sharp outer crown) — it determines head seating, resonance coupling, and overtone character.

Sheet-metal shells produce a bright, direct sound different from maple or birch. Lower internal absorption means attack transients are sharper; the shell's own ring can be audible until damped by Evans Hydraulic / Remo Controlled Sound heads or muffling rings.

Bought hardware (tension rods, lugs, hoops) is the correct buy-vs-build decision for a small-batch sprint kit; casting and machining lugs is not economic at one-off volumes.

Related: [[instruments/timpani-sheetmetal]] (same CRS shell method, tunable timpani variant).

## Cross-Links

- [[acoustic-classes/cylindrical-shell-drum]]
- [[fabrication/rolled-sheet-metal-shell]]
- [[instruments/timpani-sheetmetal]]

## Open Questions

1. What are the shell diameters and depths for each of the 5 pieces?
2. How are the shells tensioned — tension rods / T-bolts, or lug hardware?
3. What head stock for the snare drum?
4. Are tom arms and cymbal stands bought or fabricated?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for shell specifications and `bom.csv` for hardware sourcing.
