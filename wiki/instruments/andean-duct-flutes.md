---
title: Andean Duct Flutes
slug: andean-duct-flutes
wiki_type: instrument
status: active
sources:
  - path: ../../../woodwind/andean-duct-flutes/README.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/andean-duct-flutes/design.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/andean-duct-flutes/capstone-manifest.json
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/andean-duct-flutes/risks.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/andean-duct-flutes/validation.csv
    kind: spreadsheet
    last_seen: 2026-06-19
  - path: ../../../woodwind/andean-duct-flutes/andean-duct-flutes-starter.wl
    kind: wolfram
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/duct-flute
  - fabrication/bore-and-toneholes
  - synthesis/public-release-blockers
  - synthesis/wolfram-model-patterns
open_questions:
  - "Has a G4 pinkullo-style prototype been built and measured for windway, window, breath pressure, and fundamental?"
  - "What are the measured windway height, window length, and labium ramp angle from first-sound tests?"
  - "What tone-hole positions and diameters have been validated on the physical prototype?"
  - "Has the block-to-windway fit been confirmed airtight?"
  - "What material has been used for the prototype body (PVC vs. hardwood vs. bamboo)?"
answers_filed: []
last_ingest: 2026-06-19
last_lint: 2026-06-19
review_due: 2026-09-19
tags:
  - instrument
  - woodwind
  - duct-flute
  - andean
  - fipple-flute
  - private-review
---

# Andean Duct Flutes

## Overview

The `andean-duct-flutes` repo is an L2 V5 build-packet candidate for a small Andean duct-flute family: pinkullo, tarka, and related block-and-window (fipple) flutes. The first build target is a G4 pinkullo-style prototype chosen for its forgiving duct geometry and usefulness as a reference before lower tarka members are attempted.

Primary repo links:

- [README](../../../../woodwind/andean-duct-flutes/README.md)
- [Design notes](../../../../woodwind/andean-duct-flutes/design.md)
- [Risks](../../../../woodwind/andean-duct-flutes/risks.md)
- [Capstone manifest](../../../../woodwind/andean-duct-flutes/capstone-manifest.json)

## Current Status

- Release state: private review / L2 scaffold.
- Build target: G4 pinkullo-style duct flute as first prototype.
- Acoustic class: [[acoustic-classes/duct-flute]] — fipple/block-and-window flute; open-open pipe model; duct/labium voicing.
- Wolfram model: `andean-duct-flutes-starter.wl` is local. Live cloud embed now active via Public-Execute URL.
- Release blockers: prototype windway/window/labium measurements, tone-hole validation, breath-pressure data.

## Source Notes

- [repo] [README](../../../../woodwind/andean-duct-flutes/README.md) — L2 V5 candidate; duct geometry is the center of the packet; tube-length equation sizes the air column but instrument will not speak cleanly without duct+labium tuning together. First prototype: PVC proof-of-tune body; hardwood or bamboo second. Manufacturing path: drill/ream bore, cut fipple window, fit block, drill undersize holes, tune by controlled enlargement.
- [wolfram] [Wolfram starter](../../../../woodwind/andean-duct-flutes/andean-duct-flutes-starter.wl) — L1/L2 validation scaffold; open-open pipe first pass; not a build-ready tuning tool; Public-Execute cloud URL now live.

## Design Knowledge

The governing model is an open-open pipe with end-correction:

```text
f = c / (2 * L_eff)
```

where `L_eff = L_physical + end_corrections`. This gives a first-pass tube length but does NOT determine voicing. The duct and labium interact with the pipe resonance — windway height, window length, labium ramp angle, and block fit must each be measured and adjusted on a physical prototype.

G4 prototype starting parameters (from README):

| Parameter | Start Value |
| --- | --- |
| Windway height | ~0.040 in (adjusted for response) |
| Window length | ~0.45 in (filed after first-sound tests) |
| Labium ramp angle | ~35° (crisp edge, no torn grain) |
| Breath pressure | Logged as low/medium/high until manometer added |

## Acoustic And Structural Model

The duct flute is a resonant air column driven by edge-tone excitation at the labium. Unlike transverse flutes, the air jet is internally guided through a windway block; this removes embouchure technique as a variable but makes the duct geometry critical. The `reference/duct-flute-acoustic-law.md` file documents the boundary conditions, end-correction treatment, and measurement fields that remain unknown.

## Build And Validation Logic

1. Build G4 pinkullo prototype from PVC stock (proof-of-tune body).
2. Fit block; confirm airtight windway seal.
3. First-sound test: adjust windway height for clean fundamental.
4. File window: adjust window length until labium responds at target breath pressure.
5. Drill tone holes undersize; tune by controlled enlargement.
6. Record windway height, window length, ramp angle, and hole positions as measured geometry.
7. Update `validation.csv` with measured values before promoting to hardwood or bamboo.

## Release And Provenance Constraints

The acoustic model is an L1/L2 validation scaffold; it does NOT produce build-ready tuning. Final hole positions and voicing are decided by measurement, not by equations. All visual outputs use `derived_preview` or `pending_measurement` authority.

## Cross-Links

- [[acoustic-classes/duct-flute]]
- [[fabrication/bore-and-toneholes]]
- [[synthesis/public-release-blockers]]
- [[synthesis/wolfram-model-patterns]]

## Open Questions

1. Has a G4 pinkullo prototype been built, and what were the first-sound windway/window/labium measurements?
2. What are the validated tone-hole positions and diameters?
3. Has breath pressure been formally logged (manometer test)?
4. What material was used for the first prototype body (PVC vs. hardwood)?
5. Have lower tarka members been scoped from the reference-member result?

## Maintenance Notes

Next ingest should pull in first-prototype measurement data and tone-hole validation results. Update [[acoustic-classes/duct-flute]] and [[synthesis/public-release-blockers]] when prototype gates clear.
