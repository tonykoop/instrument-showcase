---
title: Drone Flutes
slug: drone-flutes
wiki_type: instrument
status: active
sources:
  - path: ../../../woodwind/drone-flutes/README.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/drone-flutes/design.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/drone-flutes/capstone-manifest.json
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/drone-flutes/risks.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/drone-flutes/validation.csv
    kind: spreadsheet
    last_seen: 2026-06-19
  - path: ../../../woodwind/drone-flutes/wolfram-starter.wl
    kind: wolfram
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/native-american-flute
  - fabrication/cnc-routing
  - fabrication/bore-and-toneholes
  - synthesis/wolfram-model-patterns
open_questions:
  - "Have acoustic body and drone-block DXF/CAD exports been produced (DXF-REV-001, FAB-BORE-009)?"
  - "Has a first-article build been completed and melody-tuning validation rows recorded?"
  - "Have the three drone blocks (U/5/8) been turned and fit-tested per 0.005 in slip-fit spec?"
  - "Has the SolidWorks design table been linked to Excel Master_Inputs and configurations exported?"
  - "Have inlay DXFs been validated against the CNC V-Carve workflow for the inlay pockets?"
answers_filed: []
last_ingest: 2026-06-19
last_lint: 2026-06-19
review_due: 2026-09-19
tags:
  - instrument
  - woodwind
  - native-american-flute
  - drone-flute
  - cnc
  - inlay
  - private-review
---

# Drone Flutes

## Overview

The `drone-flutes` repo is an L2 V5 build-packet candidate for a four-member family of Native American style drone flutes: Am, F#m, Em, and Dm. Each flute ships with three swappable drone blocks (unison, fifth-below, octave-below). The bodies use hybrid CNC + lathe + facet construction with Broinwood-style geometric CNC inlay in hard maple over walnut.

Family catalog ID: `DRN-FAM-001`.

Primary repo links:

- [README](../../../../woodwind/drone-flutes/README.md)
- [Design notes](../../../../woodwind/drone-flutes/design.md)
- [DXF shop authority](../../../../woodwind/drone-flutes/dxf-shop-authority.md)
- [Risks](../../../../woodwind/drone-flutes/risks.md)
- [Capstone manifest](../../../../woodwind/drone-flutes/capstone-manifest.json)

## Current Status

- Release state: private review / L2 V5 build-packet candidate.
- Build target: four-member drone-flute family (Am, F#m, Em, Dm); `DRN-FAM-001`.
- Acoustic class: [[acoustic-classes/native-american-flute]] — open-pipe NAF with slow air chamber (SAC), two-chambered flute, using K2 empirical correction from the `flutes` repo (150+ flute dataset).
- DXF authority: acoustic body and drone-block DXF/CAD NOT yet released (DXF-REV-001, FAB-BORE-009 blocked). Only inlay-pattern DXFs (decorative) are present.
- Wolfram model: `wolfram-starter.wl` is live at Public-Execute cloud URL.
- Release blockers: acoustic body/drone-block DXF exports, first-article melody-tuning validation, drone-block fit test.

## Source Notes

- [repo] [README](../../../../woodwind/drone-flutes/README.md) — parametric design pipeline; `Drone-Flutes-Design.xlsx` is the source of truth (284 formulas); SolidWorks linked design table; CNC from V-Carve DXFs. Aesthetic references: Elemental Flutes (drone form) + Broinwood (inlay style). Engineering reference: `flutes` repo for K2 empirical corrections. DXF/shop authority currently gated on acoustic geometry exports.
- [wolfram] [Wolfram starter](../../../../woodwind/drone-flutes/wolfram-starter.wl) — interactive NAF acoustic model; Public-Execute cloud URL now live.

## Design Knowledge

The NAF is a two-chamber open-pipe flute. The slow air chamber (SAC) feeds the flue and splitting-edge (the "bird" block); the melody chamber is the main bore. The K2 empirical correction from 150+ flutes adjusts the pure open-pipe formula for the SAC geometry and splitting-edge effect:

```text
f = c / (2 * (L_bore + K2 * bore_ID))
```

The four family members are tuned to pentatonic minor roots: Am (A4=440), F#m, Em, Dm. The drone side of each flute has three swappable tenon-fit blocks:

| Block | Drone Pitch | Interval Below Tonic |
| --- | --- | --- |
| U (unison) | Same as tonic | 0 |
| 5 (fifth-below) | Perfect 5th below | 7 semitones |
| 8 (octave-below) | Octave below | 12 semitones |

Construction path: Excel → SolidWorks family configurations (Am/F#m/Em/Dm) → V-Carve CNC G-code → lathe bore + faceting → inlay pockets.

## Build And Validation Logic

1. Export acoustic body, bore, SAC, and drone-block DXF/CAD from SolidWorks (DXF-REV-001, FAB-BORE-009).
2. Review DXF against `dxf-shop-authority.md` checklist before cutting.
3. First-article Am flute: CNC bore, SAC, and window; lathe faceting; drill tone holes undersize; tune by enlargement.
4. Record melody-tuning validation rows in `validation.csv`.
5. Turn and fit three drone blocks per 0.005 in slip-fit tolerance.
6. Validate drone tuning and breath response per `shop-validation-gates.csv`.
7. After Am validation, produce remaining three family members.

## Release And Provenance Constraints

The inlay DXFs (decorative, in `inlay-patterns/`) do NOT control tuning, bore, tone holes, or drone-block geometry. The acoustic body DXF/CAD remains blocked until the DXF-REV-001 authority gate is opened. No CNC acoustic geometry should be cut until `dxf-shop-authority.md` checklist is cleared.

## Cross-Links

- [[acoustic-classes/native-american-flute]]
- [[fabrication/cnc-routing]]
- [[fabrication/bore-and-toneholes]]
- [[synthesis/wolfram-model-patterns]]

## Open Questions

1. Have acoustic body and drone-block DXF/CAD exports been produced (DXF-REV-001, FAB-BORE-009)?
2. Has a first-article Am flute been built and melody-tuning validation rows recorded?
3. Have the three drone blocks been turned and tested for 0.005 in slip-fit?
4. Has the SolidWorks design table been linked to Excel and four configurations exported?
5. Have inlay DXFs been validated in V-Carve for the CNC inlay pocket workflow?

## Maintenance Notes

Next ingest should pull in DXF export status, first-article tuning data, and drone-block fit results. Update [[acoustic-classes/native-american-flute]] and [[synthesis/wolfram-model-patterns]] when first-article validation clears.
