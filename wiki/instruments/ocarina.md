---
title: Ocarina
slug: ocarina
wiki_type: instrument
status: active
sources:
  - path: ../../../woodwind/ocarina/README.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/ocarina/design.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/ocarina/validation.csv
    kind: spreadsheet
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/helmholtz-vessel-flute
  - fabrication/slip-cast-ceramic
  - fabrication/3d-printed-master-plaster-mold
  - synthesis/wolfram-model-patterns
open_questions:
  - "Has OCA-P0 (voicing tile / fipple practice cavity) been built and tested?"
  - "Has the clay shrinkage factor been measured from fired test tiles?"
  - "Has the voicing-window labium geometry been empirically tuned for stable tone?"
  - "Has OCA-P1 (Alto C 12-hole) been slip-cast, fired, and first-sound validated?"
  - "Have hole areas been confirmed against the Helmholtz model prediction?"
answers_filed: []
last_ingest: 2026-06-19
last_lint: 2026-06-19
review_due: 2026-09-19
tags:
  - instrument
  - woodwind
  - vessel-flute
  - ocarina
  - helmholtz
  - slip-cast
  - ceramic
  - parametric-design
---

# Ocarina

## Overview

The `ocarina` repo is a V5 explorer/build-packet candidate for a slip-cast ceramic ocarina family — 3D-printed master, plaster mold, Cone-6 stoneware production pipeline. Build-controlling values for chamber volume, voicing geometry, clay shrinkage, and tuning require physical measurement before treated as validated fabrication authority.

Primary repo links:

- [README](../../../../woodwind/ocarina/README.md)
- [Design](../../../../woodwind/ocarina/design.md)
- [Design table](../../../../woodwind/ocarina/ocarina-design-table.xlsx)
- [Validation](../../../../woodwind/ocarina/validation.csv)
- [Family spec](../../../../woodwind/ocarina/family-spec.csv)

## Current Status

- Release state: V5 build-packet candidate; no physical prototype fired.
- Build target: OCA-P1 Alto C 12-hole (low note A4 = 440 Hz, high note F6 ≈ 1397 Hz, chamber ~130 cm³).
- Acoustic class: [[acoustic-classes/helmholtz-vessel-flute]] — pitch set by chamber volume and total open hole area, not tone-hole position along a bore.
- CAD: `cad/ocarina_master.scad` parametric OpenSCAD master; drawing previews in `drawings/`.
- Wolfram model: `ocarina-ceramic-vessel-lab-starter.wl` live at Public-Execute cloud URL.
- Release blockers: OCA-P0 voicing tile; shrinkage measurement; OCA-P1 slip-cast build; tuning loop.

## Acoustic Model

Helmholtz resonator:

```
f = c/(2π) · √( A_open / (V_chamber · L_eff) )
```

`A_open` = cumulative open hole area; `V_chamber` = closed cavity volume; `L_eff = wall_thickness + 0.6·√(A_open/π)` (flanged-port end correction). Hole positions are ergonomic (where fingers reach), not acoustic (where a standing wave wants holes). This gives unusual parametric cleanliness: change volume → whole register transposes; change cumulative area → fingering chart re-tunes.

The burden on voicing/fipple geometry is unusually high — the Helmholtz model says nothing about it and it must be tuned empirically.

## Production Pipeline

3D-printed master → plaster mold → slip casting → bisque fire → glaze → Cone-6 stoneware fire. Master scale factor: `1 / (1 - measured_shrinkage)`. At 12% assumed shrinkage, master scales ~1.136×. Shrinkage must be measured from fired test tiles before production masters are committed.

## Family Targets

First prototype: Alto C 12-hole. Once voicing geometry is stable, the parametric model drives Soprano C / Bass C extensions.

| Prototype | Goal | Success criteria |
|-----------|------|-----------------|
| OCA-P0 voicing tile | Fipple practice cavity | Clear tone on a disposable test cavity |
| OCA-P1 | Alto C 12-hole fired prototype | Pitch within ±25 ¢ at all 12 fingerings |

## Source Notes

- [repo] [README](../../../../woodwind/ocarina/README.md) — background physics, V5 authority map, family targets, production pipeline.
- [repo] [design.md](../../../../woodwind/ocarina/design.md) — full Helmholtz treatment, prototype ladder, voicing-geometry requirements.
- [spreadsheet] [validation.csv](../../../../woodwind/ocarina/validation.csv) — dimensional, pitch, and voicing checks; all rows measurement-required until OCA-P1 build.

## Cross-Links

- [[acoustic-classes/helmholtz-vessel-flute]]
- [[fabrication/slip-cast-ceramic]]
- [[fabrication/3d-printed-master-plaster-mold]]
- [[synthesis/wolfram-model-patterns]]

## Open Questions

1. Has OCA-P0 (voicing tile / fipple practice cavity) been built and tested?
2. Has the clay shrinkage factor been measured from fired test tiles?
3. Has the voicing-window labium geometry been empirically tuned for stable tone?
4. Has OCA-P1 (Alto C 12-hole) been slip-cast, fired, and first-sound validated?
5. Have hole areas been confirmed against the Helmholtz model prediction?

## Maintenance Notes

Next ingest should pull in OCA-P0 voicing results, shrinkage measurement from test tiles, and OCA-P1 first-sound data. Update [[acoustic-classes/helmholtz-vessel-flute]] with any empirical labium-geometry data.
