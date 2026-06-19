---
title: Chalumeau Family
slug: chalumeau
wiki_type: instrument
status: active
sources:
  - path: ../../../woodwind/chalumeau/README.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/chalumeau/capstone-manifest.json
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/chalumeau/risks.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/chalumeau/validation.csv
    kind: spreadsheet
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/single-reed-cylindrical
  - fabrication/bore-and-toneholes
  - synthesis/public-release-blockers
  - synthesis/wolfram-model-patterns
open_questions:
  - "Has the CLM-SOP-C4 prototype been built and measured (reed, mouthpiece, bore, tuning, response)?"
  - "What are the measured tone-hole positions and diameters for the soprano member?"
  - "Has a commercial reed and mouthpiece been selected and tested?"
  - "Have the optional two-key levers been designed or tested?"
  - "What SolidWorks design table values have been confirmed from prototype measurements?"
answers_filed: []
last_ingest: 2026-06-19
last_lint: 2026-06-19
review_due: 2026-09-19
tags:
  - instrument
  - woodwind
  - single-reed
  - chalumeau
  - cylindrical-bore
  - private-review
---

# Chalumeau Family

## Overview

The `chalumeau` repo is an L2 V5 build-packet candidate for a family of single-reed chalumeaux: soprano C, alto G, tenor C, and bass F. The design is parametric (body length, bore, tone-hole positions, and optional levers from formulas) with a keyless folk-pipe-simplicity-first approach and an optional two-key metalwork path.

Primary repo links:

- [README](../../../../woodwind/chalumeau/README.md)
- [Risks](../../../../woodwind/chalumeau/risks.md)
- [Capstone manifest](../../../../woodwind/chalumeau/capstone-manifest.json)

## Current Status

- Release state: private review / L2 scaffold.
- Build target: `CLM-SOP-C4` soprano C4 prototype first, keyless; then optional two levers; then scale to alto/tenor/bass.
- Acoustic class: [[acoustic-classes/single-reed-cylindrical]] — cylindrical bore, single reed, effectively stopped pipe (fundamental ~½ wavelength).
- Wolfram model: `chalumeau-packet-starter.wl` live at Public-Execute cloud URL.
- Release blockers: CLM-SOP-C4 prototype measurements (reed, mouthpiece, bore, tuning, tone-hole positions, response).

## Source Notes

- [repo] [README](../../../../woodwind/chalumeau/README.md) — L2 prototype-validation scaffold; parametric design: body length, bore, tone-hole positions, and optional levers from formulas. Reference images: attributed Dudy.eu chalumeau photos (`assets/images/`). Acoustic model sourced from reed/bore lessons in the Great Highland Bagpipe sheet; not copied from Native American flute K2 corrections. First build: CLM-SOP-C4, commercial reed/mouthpiece, no levers.

## Design Knowledge

The chalumeau is a cylindrical, single-reed, effectively stopped pipe. The stopped-pipe acoustic law gives:

```text
f_n = (2n-1) * c / (4 * L_eff),  n = 1, 2, 3, ...
```

This means the fundamental is approximately half the frequency of an open pipe of the same length, and the instrument overblows to the 3rd harmonic (~a 12th, not an octave). This is the key difference from a transverse flute or recorder.

Family plan:

| ID | Variant | Root | Bore ID (in) | Body L (in) |
| --- | --- | --- | --- | --- |
| CLM-SOP-C4 | Soprano C | C4 | 0.500 | 12.672 |
| CLM-ALT-G3 | Alto G | G3 | 0.625 | 16.939 |
| CLM-TEN-C3 | Tenor C | C3 | 0.750 | 25.483 |
| CLM-BAS-F2 | Bass F | F2 | 0.875 | 38.320 |

Build order: soprano first, no levers, commercial reed/mouthpiece; then two optional levers; then scale up to alto, tenor, bass.

## Build And Validation Logic

1. Select commercial reed and mouthpiece for CLM-SOP-C4.
2. Turn/drill soprano body to spec; check bore straightness.
3. First-sound test: record reed, mouthpiece, breath pressure, and fundamental pitch.
4. Drill tone holes undersize; tune by controlled enlargement.
5. Record measured positions and diameters; update design table.
6. Promote to two-lever variant only after soprano speaks cleanly.
7. Scale to alto/tenor/bass only after soprano tone-hole data is validated.

## Release And Provenance Constraints

This is a modern parametric engineering scaffold. The Dudy.eu reference photos are attributed to Petr Skalicky / Dudy.eu; they are design references, not Tony's own build photos. No claim should be made of measured performance until prototype data exists.

## Cross-Links

- [[acoustic-classes/single-reed-cylindrical]]
- [[fabrication/bore-and-toneholes]]
- [[synthesis/public-release-blockers]]
- [[synthesis/wolfram-model-patterns]]

## Open Questions

1. Has CLM-SOP-C4 been built and measured (reed, mouthpiece, bore, tuning, response)?
2. What are the validated tone-hole positions and diameters from the prototype?
3. Has a commercial reed and mouthpiece been selected and sourced?
4. Have the optional two-key levers been designed or prototyped?
5. What SolidWorks design table values have been confirmed from measured prototype data?

## Maintenance Notes

Next ingest should pull in CLM-SOP-C4 prototype measurements and tone-hole data. Update [[acoustic-classes/single-reed-cylindrical]] and [[synthesis/public-release-blockers]] when prototype gates clear.
