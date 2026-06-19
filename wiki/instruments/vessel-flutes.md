---
title: Vessel Flutes
slug: vessel-flutes
wiki_type: instrument
status: active
sources:
  - path: ../../../woodwind/vessel-flutes/README.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/vessel-flutes/design.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/vessel-flutes/helmholtz-gates.json
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/helmholtz-vessel-flute
  - fabrication/slip-cast-ceramic
  - fabrication/slab-pinch-prototype
  - synthesis/wolfram-model-patterns
open_questions:
  - "Has the 130 cc ocarina-style lab body been built (slab/pinch) and volume-fill tested?"
  - "Have shrinkage and voicing response measurements been recorded in tuning-log.csv?"
  - "Have helmholtz-gates.json validity boundaries been closed for any prototype?"
  - "Has the hole-area tuning loop been executed (drill undersize, measure pitch, enlarge)?"
  - "Has the slip-cast workflow been validated after shrinkage data is available?"
answers_filed: []
last_ingest: 2026-06-19
last_lint: 2026-06-19
review_due: 2026-09-19
tags:
  - instrument
  - woodwind
  - vessel-flute
  - helmholtz
  - ocarina
  - xun
  - gemshorn
  - ceramic
  - parametric-design
---

# Vessel Flutes

## Overview

The `vessel-flutes` repo is an L2 V5 build-packet candidate for Helmholtz vessel flutes: ocarina, xun, gemshorn-inspired ceramic studies, and quick cavity-volume prototypes. Pitch is governed by cavity volume, voicing aperture area, and effective neck length — not by open-pipe tube length. Not build-ready until volume/voicing measurements close the gates in `helmholtz-gates.json` and `validation.csv`.

Primary repo links:

- [README](../../../../woodwind/vessel-flutes/README.md)
- [Design](../../../../woodwind/vessel-flutes/design.md)
- [Helmholtz gates](../../../../woodwind/vessel-flutes/helmholtz-gates.json)
- [Tuning log](../../../../woodwind/vessel-flutes/tuning-log.csv)

## Current Status

- Release state: L2 V5 build-packet candidate; uncalibrated model; no fired prototype.
- Build target: 130 cc ocarina-style lab body (slab/pinch first; slip-cast after shrinkage data).
- Acoustic class: [[acoustic-classes/helmholtz-vessel-flute]] — Helmholtz resonator.
- Wolfram model: `vessel-flutes-ceramic-vessel-lab-starter.wl` live at Public-Execute cloud URL.
- Release blockers: lab body prototype; volume fill test; voicing response; helmholtz-gates closure.

## Governing Model

Helmholtz resonator:

```
f = c/(2π) · √( A / (V · L_eff) )
```

The model in `design.md` is closed-form and **uncalibrated**. Cavity volume (V), voicing aperture (A), effective neck length (L_eff), wall thickness, and material/fire state are all unknowns until measured on a real prototype.

## Tuning Loop

For vessel flutes, a tone hole increases effective open area — it does not shorten a tube:

1. Measure dry/fired cavity volume
2. Calculate target cumulative open area for each note
3. Drill holes undersize
4. Enlarge holes gradually while measuring pitch
5. Update hole-area curve with real data

`tuning-log.csv` is a header-only stub; rows appended only from real prototype measurements.

## Calibration Gates

`helmholtz-gates.json` records the model's validity boundary, ambient assumptions, and measurement requirements that block L3 promotion. All gates must be closed before any pitch claim is treated as trustworthy.

## Design Overview

| Topic | Packet decision |
|-------|----------------|
| Governing model | Helmholtz: `f = c/(2π)·√(A/(V·L_eff))` |
| First prototype | 130 cc ocarina-style lab body |
| Voicing | Rectangular windway/window with measured effective area |
| Tuning method | Drill holes undersize; track cumulative open area; tune by enlargement |
| Materials | Clay slab/pinch prototype first; slip-cast workflow after shrinkage data |
| Validation | Volume fill test, voicing response, scale tuning, shrinkage log |

## Source Notes

- [repo] [README](../../../../woodwind/vessel-flutes/README.md) — calibration status warning, Helmholtz overview, tuning loop, Refs #1.
- [repo] [design.md](../../../../woodwind/vessel-flutes/design.md) — governing model, first-prototype plan, voicing requirements.
- [repo] [helmholtz-gates.json](../../../../woodwind/vessel-flutes/helmholtz-gates.json) — model validity boundary and L3 promotion blockers.

## Cross-Links

- [[acoustic-classes/helmholtz-vessel-flute]]
- [[fabrication/slip-cast-ceramic]]
- [[fabrication/slab-pinch-prototype]]
- [[synthesis/wolfram-model-patterns]]

## Open Questions

1. Has the 130 cc ocarina-style lab body been built (slab/pinch) and volume-fill tested?
2. Have shrinkage and voicing response measurements been recorded in `tuning-log.csv`?
3. Have `helmholtz-gates.json` validity boundaries been closed for any prototype?
4. Has the hole-area tuning loop been executed (drill undersize, measure pitch, enlarge)?
5. Has the slip-cast workflow been validated after shrinkage data is available?

## Maintenance Notes

Next ingest should pull in lab body build results, volume fill measurements, and hole-area tuning data. Update [[acoustic-classes/helmholtz-vessel-flute]] with empirical voicing-aperture / volume / pitch data.
