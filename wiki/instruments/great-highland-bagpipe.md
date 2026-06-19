---
title: Great Highland Bagpipe
slug: great-highland-bagpipe
wiki_type: instrument
status: active
sources:
  - path: ../../../woodwind/great-highland-bagpipe/README.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/great-highland-bagpipe/design.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/great-highland-bagpipe/validation.csv
    kind: spreadsheet
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/conical-double-reed
  - acoustic-classes/cylindrical-drone
  - fabrication/cnc-lathe-turning
  - synthesis/pressure-regulation
  - synthesis/wolfram-model-patterns
open_questions:
  - "Has a practice chanter been turned and first-sound validated with a commercial reed?"
  - "Have tenor drone bores and reed seats been confirmed against manometer pressure data?"
  - "Has the bass drone been built and coupled to the tenor drones in the full pressure loop?"
  - "Have airtightness tests been run with the synthetic bag, stocks, and blowpipe valve?"
  - "Have all chanter note holes been tuned from undersize using tape + incremental enlargement?"
answers_filed: []
last_ingest: 2026-06-19
last_lint: 2026-06-19
review_due: 2026-09-19
tags:
  - instrument
  - woodwind
  - reed-instrument
  - bagpipe
  - great-highland-bagpipe
  - parametric-design
  - system-of-systems
  - cnc-lathe
  - woodturning
---

# Great Highland Bagpipe

## Overview

The `great-highland-bagpipe` repo is an L2/L3-candidate system-of-systems engineering packet for a full GHB set: chanter, tenor drones (×2), bass drone, reeds, bag, stocks, blowpipe, pressure regulation, tuning, sourcing, maintenance, and validation. It treats the GHB as an interacting set of acoustic and mechanical subsystems rather than a single pipe.

Design origin: `great-highland-bagpipe-design-table.xlsx` using a modern GHB Low A of 480 Hz, just-intonation chanter ratios, and first-pass dimensions for a full chanter and drone set. Formula-derived dimensions are first-order estimates until confirmed against a physical reed, bore, and pressure setup.

Primary repo links:

- [README](../../../../woodwind/great-highland-bagpipe/README.md)
- [Design](../../../../woodwind/great-highland-bagpipe/design.md)
- [BOM](../../../../woodwind/great-highland-bagpipe/bom.csv)
- [Assembly manual](../../../../woodwind/great-highland-bagpipe/assembly-manual.md)
- [Validation](../../../../woodwind/great-highland-bagpipe/validation.csv)
- [Reed pressure validation](../../../../woodwind/great-highland-bagpipe/reed-pressure-validation.csv)

## Current Status

- Release state: L2/L3 build-packet candidate; first-order design complete.
- Build target: full GHB set (chanter + tenor×2 + bass drone + bag + stocks + blowpipe).
- Acoustic class: [[acoustic-classes/conical-double-reed]] (chanter) + [[acoustic-classes/cylindrical-drone]] (drones).
- CAD/DXF: parametric OpenSCAD master starter in `cad/`; dimensioned SVG sheets in `drawings/`.
- Wolfram model: `great-highland-bagpipe-starter.wl` live at Public-Execute cloud URL.
- Release blockers: physical build; reed/bore/pressure validation; note hole tuning.

## System Architecture

| Subsystem | Function | First Prototype Decision |
|-----------|----------|--------------------------|
| Chanter | Conical double-reed melody pipe | 14.5 in full-chanter length; tune holes from undersize with commercial reed |
| Tenor drones (×2) | Stopped cylindrical A3 reference pipes | Build both identically; validate one before copying |
| Bass drone | Stopped cylindrical A2 reference pipe | Three sections (bottom/middle/top) with long tuning overlap |
| Reeds | Oscillating valves and pitch drivers | Buy commercial chanter + drone reeds for prototype stability |
| Bag | Pressure reservoir | Synthetic zipper bag for repeatable airtightness |
| Stocks + blowpipe | Airtight mechanical interfaces | Turn as separate service parts; hemp or tied-in seals |
| Maintenance | Keeps system stable | Leakage, hemp, moisture, reed checks every validation pass |

## Build Order

1. Buy reeds and bag first — acoustic system can't be validated without real pressure and reed behavior.
2. Turn a practice/prototype chanter in cherry, walnut, Delrin, or ipe before committing African blackwood.
3. Validate chanter bore and note holes using tape and incremental enlargement.
4. Build one tenor drone; tune reed seat and slide behavior; then duplicate.
5. Build bass drone after tenor tuning and leakage are stable.
6. Turn stocks and blowpipe; tie into bag; run full pressure tests.
7. Final validation: tuning, pressure, leakage, fit, maintenance per `validation.csv`.

## Acoustic Model

The GHB chanter is a conical bore driven by a double reed (cane or synthetic). The cone produces an overblown octave at half the length of a cylindrical pipe of equal fundamental — this enables the bright, penetrating chanter tone despite the instrument's relatively short length.

Drones are closed cylindrical resonators tuned to A. The bass drone sounds A2 (~110 Hz); tenors sound A3 (~220 Hz). Drone reeds must onset below bag pressure and stay stable across the player's pressure variation range. Reed pressure onset/cutoff gates are tracked in `reed-pressure-validation.csv`.

Bag pressure regulation is a coupled system: blow valve prevents back-flow; bag compliance smooths pressure; reed seats set the load. Leakage from any hemp joint or bag seam destabilizes all subsystems simultaneously.

## Source Notes

- [repo] [README](../../../../woodwind/great-highland-bagpipe/README.md) — system map, subsystem table, build order, packet map.
- [repo] [design.md](../../../../woodwind/great-highland-bagpipe/design.md) — governing acoustic model, subsystem interfaces, pressure model.
- [spreadsheet] [validation.csv](../../../../woodwind/great-highland-bagpipe/validation.csv) — tuning, pressure, leakage, fit, and maintenance checks; all rows measurement-required until physical build.
- [spreadsheet] [reed-pressure-validation.csv](../../../../woodwind/great-highland-bagpipe/reed-pressure-validation.csv) — reed source roles, onset/cutoff pressure gates, coupled pressure-response evidence rows.

## Cross-Links

- [[acoustic-classes/conical-double-reed]]
- [[acoustic-classes/cylindrical-drone]]
- [[fabrication/cnc-lathe-turning]]
- [[fabrication/woodturning-conifers]]
- [[synthesis/pressure-regulation]]
- [[synthesis/wolfram-model-patterns]]

## Open Questions

1. Has a practice chanter been turned and first-sound validated with a commercial reed?
2. Have tenor drone bores and reed seats been confirmed against manometer pressure data?
3. Has the bass drone been built and coupled to the tenor drones in the full pressure loop?
4. Have airtightness tests been run with the synthetic bag, stocks, and blowpipe valve?
5. Have all chanter note holes been tuned from undersize using tape + incremental enlargement?

## Maintenance Notes

Next ingest should pull in first-build measurements: chanter bore, note hole sizes and intonation deviations, drone reed onset/cutoff pressures, and bag leakage test results. Update [[acoustic-classes/conical-double-reed]] with any empirical cone-angle vs. tone-quality data.
