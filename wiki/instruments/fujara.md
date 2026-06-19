---
title: Fujara
slug: fujara
wiki_type: instrument
status: active
sources:
  - path: ../../../woodwind/fujara/README.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/fujara/capstone-manifest.json
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/fujara/validation.csv
    kind: spreadsheet
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/overtone-flute
  - fabrication/stave-construction
  - synthesis/public-release-blockers
  - synthesis/wolfram-model-patterns
open_questions:
  - "Has a physical fujara been built and bore/flue/labium/tuning-response measurements captured?"
  - "Which bore aspect ratio has been selected (45:1, 50:1, 55:1, or 60:1) and validated?"
  - "Has the stave-built construction (glue-up, bore truth, labium cut) been executed and documented?"
  - "Have the three finger-hole positions been verified for harmonic-series intonation?"
  - "Has the side air-tube length been tuned to match the labium position on the main bore?"
answers_filed: []
last_ingest: 2026-06-19
last_lint: 2026-06-19
review_due: 2026-09-19
tags:
  - instrument
  - woodwind
  - overtone-flute
  - fujara
  - stave-built
  - slovak
  - private-review
---

# Fujara

## Overview

The `fujara` repo is a V5 build-packet candidate for engineering documentation of a stave-built fujara — the tall (5–8 ft), three-hole, side-blown Slovak overtone shepherd's flute. The packet contains design-table, SolidWorks, OpenSCAD starter, vector plates, print packet, and validation artifacts but is NOT build-ready until bore, flue/labium, side air-tube, and tuning-response measurements are captured.

UNESCO recognized "Fujara and its music" on the Representative List of Intangible Cultural Heritage in 2008.

Primary repo links:

- [README](../../../../woodwind/fujara/README.md)
- [Capstone manifest](../../../../woodwind/fujara/capstone-manifest.json)
- [Parametric design table](../../../../woodwind/fujara/design-table/fujara-dimensions-parametric.xlsx)

## Current Status

- Release state: private review / V5 design-review build-packet candidate.
- Build target: stave-built fujara; target fundamental D2 to F#3 range.
- Acoustic class: [[acoustic-classes/overtone-flute]] — three-hole side-blown flute; melody from harmonic series (overblowing), not from finger holes.
- CAD/DXF: body, mouthpiece chamber, labium, and jig geometry in SolidWorks + OpenSCAD starter.
- Wolfram model: `fujara_sidebranch_starter.wl` live at Public-Execute cloud URL.
- Release blockers: physical build; bore/flue/labium measurements; tuning-response validation.

## Source Notes

- [repo] [README](../../../../woodwind/fujara/README.md) — parametric design table (D2–F#3, four bore aspect ratios: 45:1/50:1/55:1/60:1); side-blown air path with parallel chamber; stave construction required for 8-ft build lengths; cultural attribution: Slovak pastoral tradition, UNESCO ICH 2008; builder is non-Slovak.

## Design Knowledge

The fujara produces melody from the harmonic series rather than finger holes. The three holes only shift effective air-column length slightly; melody is produced by overblowing:

```text
f_n = n * f_fundamental,  n = 2, 3, 4, 5, 6, 7, 8, ...
```

This gives the lydianic modal scale characteristic of fujara melody (partial 7 is notably flat compared to equal temperament). The player controls partial by breath pressure and embouchure, not by fingering.

The side-blown air path distinguishes the fujara from end-blown flutes: a secondary tube carries breath from the mouthpiece at the top to the labium at the top of the main bore. This allows the player to be 6+ feet away from the bore's open end.

Design table covers D2 (94" blank, bore ~1.25") through F#3 (40" blank, bore ~0.875") at four aspect ratios (bore:length = 45:1, 50:1, 55:1, 60:1). Three finger holes provide fine intonation adjustment across the harmonic series.

Stave construction: glued stave blanks in V-cradle jig; bore drilled on lathe; staves oriented for grain stability. Long bore requires careful setup for straightness.

## Acoustic And Structural Model

The Helmholtz resonance model applies to the stopped-end air column (the bottom end is open, but the top labium acts as the driven end). Overblowing selects successive modes. The side-air-tube length must match the acoustic path to the labium to avoid coupling losses.

## Build And Validation Logic

Build sequence:

1. Select target fundamental and aspect ratio from design table.
2. Glue stave blank; true bore on lathe.
3. Cut and fit side air tube; join to body at labium position.
4. Cut labium (true-sound-hole edge) at correct angle and position.
5. First-sound test: adjust labium angle and flue gap for clean fundamental.
6. Overblow progressively: verify 2nd, 3rd, 4th, 5th partials speak cleanly.
7. Drill three finger holes undersize; tune by enlargement per partial-series intonation.
8. Record all measurements in `validation.csv`.

## Release And Provenance Constraints

This is non-Slovak engineering documentation in respect for a living Slovak cultural tradition. Do not claim authority over traditional construction or imply cultural authenticity. The instruments are "fujara-style" — inspired by, not part of, the Slovak shepherd tradition.

## Cross-Links

- [[acoustic-classes/overtone-flute]]
- [[fabrication/stave-construction]]
- [[fabrication/bore-and-toneholes]]
- [[synthesis/public-release-blockers]]
- [[synthesis/wolfram-model-patterns]]

## Open Questions

1. Has a physical fujara been built and bore/flue/labium measurements recorded?
2. Which bore aspect ratio (45:1/50:1/55:1/60:1) has been selected and validated?
3. Has the side air-tube length been tuned to match the labium position?
4. Have the three finger-hole positions been confirmed for harmonic-series intonation?
5. Has the stave-glue-up and bore trueness been documented?

## Maintenance Notes

Next ingest should pull in first-build measurements, labium geometry, and overblow validation results. Update [[acoustic-classes/overtone-flute]] when tuning-response data exists.
