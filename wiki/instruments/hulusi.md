---
title: Hulusi
slug: hulusi
wiki_type: instrument
status: active
sources:
  - path: ../../../woodwind/hulusi/README.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/hulusi/design.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/hulusi/validation.csv
    kind: spreadsheet
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/stopped-pipe-free-reed
  - fabrication/lathe-turning-hardwood
  - synthesis/free-reed-pull-down
  - synthesis/wolfram-model-patterns
open_questions:
  - "Has HUL-P0/HUL-P1 (F-key prototype) been built and first-sound validated?"
  - "Have reed pull-down measurements been recorded per reed in validation.csv?"
  - "Has the SolidWorks design-table link been verified bidirectionally against hulusi-design-table.txt globals?"
  - "Have drone pipe lengths been validated against the free-reed pull-down model?"
  - "Has the 2-mode coupling-matrix placeholder in hulusi-starter.wl been fitted against measured HUL-P0 data?"
answers_filed: []
last_ingest: 2026-06-19
last_lint: 2026-06-19
review_due: 2026-09-19
tags:
  - instrument
  - woodwind
  - free-reed
  - hulusi
  - chinese
  - cucurbit
  - parametric-design
  - family-instrument
---

# Hulusi (葫芦丝)

## Overview

The `hulusi` repo is an L2 V5 build-packet candidate for a five-key family (B♭ / C / D / F / G) of wooden hulusi — the Chinese cucurbit free-reed flute. The repo is organized for prototype review and shop planning; HUL-P0/HUL-P1 measurements, production CAD/DXF, reed pull-down calibration, and physical validation remain pending before any L3/build-ready claim.

The v4.1 scaffold upgrades the udu v4 reference with 33 named globals, SolidWorks design-table parity, per-key dimensioned drawings, and a family derivation sheet.

Primary repo links:

- [README](../../../../woodwind/hulusi/README.md)
- [Design](../../../../woodwind/hulusi/design.md)
- [Design table](../../../../woodwind/hulusi/hulusi-design-table.xlsx)
- [Validation](../../../../woodwind/hulusi/validation.csv)
- [Family spec](../../../../woodwind/hulusi/family-spec.csv)

## Current Status

- Release state: L2 V5 build-packet candidate; physical prototype pending.
- Build target: F-key prototype (HUL-P2) first; then B♭/C/D/G from parametric family sheet.
- Acoustic class: [[acoustic-classes/stopped-pipe-free-reed]] — three stopped pipes sharing a hardwood gourd wind chest, each with a brass free reed.
- CAD/DXF: SolidWorks design-table + OpenSCAD; `cad/hulusi-design-table.txt` holds named globals.
- Wolfram model: `hulusi-starter.wl` live at Public-Execute cloud URL.
- Release blockers: HUL-P0/P1 build; reed pull-down measurement; bore tuning loop.

## Acoustic Model

Three independent stopped-pipe + free-reed systems sharing a wind chest:

```text
f_pipe = c / (4 · L_eff)        with  L_eff = L_acoustic + 0.6·r_bore
f_reed = K · t / L_tongue²      (cantilever; brass K ≈ 27,300 imperial)
```

Each reed is cut sharp by `pull_down_cents` (default −30 ¢). The pipe pulls the reed to its resonance (classic free-reed pull-down). The `Master_Inputs` empirical correction loop and `validation.csv` capture actual pull-down per build for tighter reed-cutting on subsequent instruments.

The build replaces the dried gourd with a lathe-turned hardwood gourd and bamboo with pakkawood — same cultural lineage (credited), improved repeatability and bench durability.

## Family Targets

First prototype: F-key (all-holes-closed = F4 = 349 Hz). Once F-key voicing is stable, the parametric model drives B♭/C/D/G via the `Family` sheet in `hulusi-design-table.xlsx`.

- Drone 1: a fifth above tonic (fixed)
- Drone 2: an octave above tonic (waxable — player mutes mid-phrase)
- Melody pipe: 7 finger holes

## Source Notes

- [repo] [README](../../../../woodwind/hulusi/README.md) — 5-key family scope, v4.1 improvements, acoustic model summary, pull-down loop description.
- [repo] [design.md](../../../../woodwind/hulusi/design.md) — full physics treatment, 2-mode coupling-matrix placeholder.
- [spreadsheet] [validation.csv](../../../../woodwind/hulusi/validation.csv) — tuning, pressure, reed, and bore checks; all measurement rows pending until HUL-P0 build.

## Cross-Links

- [[acoustic-classes/stopped-pipe-free-reed]]
- [[fabrication/lathe-turning-hardwood]]
- [[synthesis/free-reed-pull-down]]
- [[synthesis/wolfram-model-patterns]]

## Open Questions

1. Has HUL-P0/HUL-P1 (F-key prototype) been built and first-sound validated?
2. Have reed pull-down measurements been recorded per reed in `validation.csv`?
3. Has the SolidWorks design-table link been verified bidirectionally against `hulusi-design-table.txt` globals?
4. Have drone pipe lengths been validated against the free-reed pull-down model?
5. Has the 2-mode coupling-matrix in `hulusi-starter.wl` been fitted against measured HUL-P0 data?

## Maintenance Notes

Next ingest should pull in HUL-P0 first-sound data, per-reed pull-down measurements, and bore tuning results. Update [[synthesis/free-reed-pull-down]] with empirical correction values when available.
