---
title: Dundun (Cylindrical Bass Drum Trio) Blueprint
slug: dundun
wiki_type: instrument
status: active
sources:
  - path: ../../../../percussion/dundun/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/cylindrical-stave-drum
  - fabrication/stave-construction
  - instruments/djembe
  - instruments/ashiko-drum-workshop
open_questions:
  - "What are the diameters and depths of the three dundun sizes (kenkeni / sangban / doundounba) in this design?"
  - "What are the head material and lacing specs — rope/guinea-ring identical to the djembe, or different configuration?"
  - "Is a dundun bell (krinyi) included in the fabrication packet — or only the drum body?"
  - "What is the pitch target for each of the three shells?"
last_ingest: 2026-06-19
tags: [instrument, drum, dundun, kenkeni, sangban, doundounba, cylindrical, stave-built, mande, west-africa, bass-drum]
---

# Dundun — Cylindrical Bass Drum Trio Blueprint

## Overview

A fabrication packet for the dundun (also: doundounba, djun-djun), the family of cylindrical double-headed bass drums used in Mande West African music alongside the djembe. The traditional dundun trio consists of: **kenkeni** (highest, small), **sangban** (mid), and **doundounba** (lowest, large). Each drum is played horizontally or upright by a dedicated player, often with an iron bell (krinyi) mounted on the shell.

- **Family:** membranophone / cylindrical double-headed bass drum
- **Members:** kenkeni (soprano), sangban (mid), doundounba (bass) — trio configuration
- **Construction:** stave-built hardwood cylinder, cowhide heads, rope lacing
- **Origin:** Mande West Africa (Guinea, Mali, Senegal)
- **Status:** blueprint and fabrication packet in the same stave-built research lineage as djembe

Primary repo links:
- [README](../../../../percussion/dundun/README.md)
- [Design notes](../../../../percussion/dundun/design.md)

## Current Status

- Release state: blueprint/fabrication packet; stave-construction lineage from djembe and ashiko projects.
- Library family: drum.
- Acoustic class: cylindrical stave drum (double-headed).
- Wolfram state: acoustic model present; Wolfram Cloud Public-Execute URL available.
- CAD state: shell geometry defined; no confirmed `.glb`.

## Source Notes

- [README](../../../../percussion/dundun/README.md) — instrument overview (Mande origin, trio configuration: kenkeni/sangban/doundounba), construction method (stave-built cylinder, cowhide heads, rope lacing), packet scope.

Artifacts not ingested: `design.md`, `parameters.csv`, `validation.csv`, `bom.csv`.

## Design Knowledge

The dundun shell is a straight cylinder (no goblet waist, no conical taper), making it geometrically simpler than a djembe to stave-build — all staves have the same width and taper angle, and no compound jig routing is required. The difficulty is the double-head design: both ends must have accurate, co-planar bearing edges so two heads can be independently tensioned.

Cowhide heads (thicker, lower-pitched) are traditional and appropriate for the bass register these drums occupy. Rope lacing follows the same vertical + cross-rope pattern as the djembe.

The dundun trio provides harmonic differentiation in Mande ensembles: doundounba holds low-register patterns; sangban plays the mid-range rhythmic call; kenkeni plays faster, higher patterns. All three are typically played with stick beaters on one head while the other head rests on a stand or the player's shoulder.

The krinyi (iron bell) mounted on the shell and played with a metal rod provides the rhythmic anchor for the ensemble — similar in function to the agogô in Candomblé.

Related: [[instruments/djembe]] (goblet companion, same stave lineage and Morgan Drums training), [[instruments/ashiko-drum-workshop]] (conical stave companion).

## Cross-Links

- [[acoustic-classes/cylindrical-stave-drum]]
- [[fabrication/stave-construction]]
- [[instruments/djembe]]
- [[instruments/ashiko-drum-workshop]]

## Open Questions

1. What are the exact shell diameters and depths for kenkeni / sangban / doundounba?
2. Are head material and lacing specs identical to the djembe packet?
3. Is a krinyi (iron bell) included in the fabrication packet?
4. What are the target pitches for each shell?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for stave geometry and `parameters.csv` for the three shell sizes and head specs.
