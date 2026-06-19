---
title: Bass Surface Drum Blueprint
slug: bass-surface-drum
wiki_type: instrument
status: active
sources:
  - path: ../../../../percussion/bass-surface-drum/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/frame-drum
  - fabrication/rolled-sheet-metal-shell
  - acoustic-classes/large-membrane-bass
open_questions:
  - "What head diameter and membrane tension combination was used to hit the 50 Hz fundamental target — and was this validated with a measurement or only by model?"
  - "Is the shell a rolled ring or a welded cylinder, and what is the head-seat / counter-hoop mounting approach?"
  - "Is this a floor instrument (played lying flat) or an upright frame drum mounted at an angle?"
last_ingest: 2026-06-19
tags: [instrument, drum, frame-drum, bass, large-diameter, sheet-metal, 50hz, steerhide]
---

# Bass Surface Drum Blueprint

## Overview

A very large-diameter frame drum targeting a 50 Hz fundamental — occupying the acoustic niche between a concert bass drum and a floor tom. The shell is a rolled sheet-metal ring 800 mm outer diameter. Steerhide or equivalent heavy head stock provides the mass needed to support 50 Hz membrane resonance.

- **Family:** membranophone / large frame drum
- **Shell OD:** 800 mm (~31.5 in)
- **Target fundamental:** ~50 Hz (low B1 / B♭1 region)
- **Head material:** steerhide or heavy synthetic equivalent
- **Status:** blueprint packet — acoustic model and shell geometry defined; no confirmed prototype

Primary repo links:
- [README](../../../../percussion/bass-surface-drum/README.md)
- [Design notes](../../../../percussion/bass-surface-drum/design.md)

## Current Status

- Release state: blueprint-level packet; no confirmed V5 empirical validation.
- Library family: drum.
- Acoustic class: large membrane / frame drum (bass range).
- CAD state: shell geometry defined; no confirmed `.glb`.

## Source Notes

- [README](../../../../percussion/bass-surface-drum/README.md) — targets (800 mm OD, 50 Hz fundamental, steerhide head), sheet-metal shell method, overview of acoustic design intent.

Artifacts not ingested: `design.md`, `parameters.csv`, `validation.csv`, `bom.csv`.

## Design Knowledge

An 800 mm membrane at low tension can produce fundamentals in the 50–60 Hz range, depending on head mass. Steerhide is preferred because its greater surface density (vs goatskin) lowers the fundamental for a given tension — essential when targeting sub-60 Hz on a flat-tuned frame drum. The shell ring's low depth (relative to the membrane diameter) means body resonance does not dominate; the instrument is a true membrane radiator in this frequency range.

The engineering challenge is head-seat accuracy: a large-diameter ring must be flat and round to within a few mm for the head to seat without wrinkle-induced nodes. Rolled and welded sheet-metal rings can produce adequate roundness with a mandrel-based rolling setup.

## Cross-Links

- [[acoustic-classes/frame-drum]]
- [[acoustic-classes/large-membrane-bass]]
- [[fabrication/rolled-sheet-metal-shell]]

## Open Questions

1. What head diameter and tension was used to hit the 50 Hz fundamental — validated by model or measurement?
2. Is the shell a rolled ring or welded cylinder, and what is the head-seat and counter-hoop mounting approach?
3. Floor instrument or upright frame drum?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for membrane physics model and shell fabrication detail.
