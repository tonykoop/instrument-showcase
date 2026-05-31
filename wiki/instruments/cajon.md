---
title: Cajon Family Public-Review Prototype
slug: cajon
wiki_type: instrument
status: active
last_updated: 2026-05-18
source_count: 11
open_questions: 6
tags:
  - instrument
  - drum
  - box-drum
  - public-review
---

# Cajon Family Public-Review Prototype

## Overview

The `cajon` repo is a pre-build V5 build-packet candidate for a parametric three-member cajon family. It treats the cajon as a coordinated box-drum system rather than a single fixed box: Compact, Standard, and Bass members share a geometric law, multiple joinery paths, and optional snare lineages.

The first physical prototype is the Standard `CJ-S`, V1 finger-joint shell, with snare option B using guitar strings.

Primary repo links:

- [README](../../../../percussion/cajon/README.md)
- [Design notes](../../../../percussion/cajon/design.md)
- [Assembly manual](../../../../percussion/cajon/assembly-manual.md)
- [Validation report](../../../../percussion/cajon/validation-report.md)
- [Risks](../../../../percussion/cajon/risks.md)
- [Capstone manifest](../../../../percussion/cajon/capstone-manifest.json)
- [Explorer](../../../../percussion/cajon/explorer.html)

## Current Status

- Release state: public-review prototype / pre-build V5 candidate.
- Library family: drum.
- Acoustic class: box drum, coupled plate-and-Helmholtz system.
- Wolfram state: owner-only in the central library manifest.
- CAD state: no `.glb` detected yet; OpenSCAD source, SVG drawings, jig templates, and a visual authority register exist.
- Fabrication authority: design table, OpenSCAD source, jig templates, and reviewed drawing set. Measurement-gated before production-release claims.

## Source Notes

The first ingest used the text-native sources and linked the binary/generated artifacts without deep extraction:

- [README](../../../../percussion/cajon/README.md) gives the family overview, authority status, physics summary, first prototype, file map, and roadmap.
- [Design notes](../../../../percussion/cajon/design.md) explain the family scaling law, plate model, corrected Helmholtz formula, snare strategy, joinery variants, CNC inlay strategy, and open assumptions.
- [Assembly manual](../../../../percussion/cajon/assembly-manual.md) defines the build sequence for inlay, joinery, sound hole, glue blocks, snare, box glue-up, tapa attachment, tuning, finish, and inspection.
- [Validation report](../../../../percussion/cajon/validation-report.md) records pre-build validation status, acceptance gates, test sequence, and release checklist.
- [Risks](../../../../percussion/cajon/risks.md) tracks 17 acoustic, structural, ergonomic, supply, and fit/finish risks.
- [Family spec](../../../../percussion/cajon/family-spec.csv) defines Compact, Standard, and Bass dimensions and predicted acoustic targets.
- [Validation table](../../../../percussion/cajon/validation.csv) holds predicted-vs-measured rows. At ingest, measured values are still blank.
- [Capstone manifest](../../../../percussion/cajon/capstone-manifest.json) identifies the prototype, authority boundary, core files, directories, and public-release concerns.
- [Build instructions](../../../../percussion/cajon/BUILD.md) explain binary deliverable generation and clarify markdown/CSV as source of truth for regenerated binaries.
- [Jig decision](../../../../percussion/cajon/jig-decision.md) and [resources](../../../../percussion/cajon/resources.md) should be read in the next deeper fabrication pass.
- [Visual output register](../../../../percussion/cajon/visual-output-register.csv) controls visual/CAD authority.

Linked artifacts not distilled in this pass:

- [Reference workbook](../../../../percussion/cajon/cajon-design-table.xlsx)
- [Generated design workbook](../../../../percussion/cajon/Cajon-Family-Design.xlsx)
- [Capstone deck PPTX](../../../../percussion/cajon/Cajon-Family-Capstone.pptx)
- [Print packet PDF](../../../../percussion/cajon/Cajon-Family-Print-Packet.pdf)
- [Drawings folder](../../../../percussion/cajon/drawings/)
- [CAD folder](../../../../percussion/cajon/cad/)
- [Jigs folder](../../../../percussion/cajon/jigs/)
- [Learn-to-play folder](../../../../percussion/cajon/learn-to-play/)

## Design Knowledge

The cajon bass voice is governed by two coupled systems:

- Front-plate `(1,1)` bending mode of the 3 mm Baltic-birch tapa.
- Helmholtz cavity mode of the closed box and circular back port.

The corrected Helmholtz model is:

```text
f_H = (c / 2 pi) sqrt(A / (V L_eff))
L_eff = t_back + 1.7 * (d_hole / 2)
```

The repo flags an important correction: the original workbook used only back-panel thickness for `L_eff`, missing the end correction. The design notes now use the corrected expression; workbook formula revision remains a release concern.

Family targets:

| Member | Size | Sound hole | Predicted f_H | Predicted plate | Voice |
| --- | --- | --- | --- | --- | --- |
| Compact `CJ-C` | 15 x 11 x 11 in | 4.0 in | 107 Hz | 107 Hz | bright A2/G#2 |
| Standard `CJ-S` | 18 x 12 x 12 in | 4.5 in | 96 Hz | 84 Hz | balanced G2 |
| Bass `CJ-B` | 22 x 14 x 14 in | 5.0 in | 77 Hz | 60 Hz | deep E2/D#2 |

The Standard is the first prototype because it is the family tonal center and can calibrate the family law before Compact and Bass builds.

## Build And Validation Logic

The build plan emphasizes repeatability and measurement:

1. Acclimate and mill stock.
2. Route inlay before assembly.
3. Cut V1 finger joints for the first prototype.
4. Cut and deburr the back-panel sound hole.
5. Glue internal corner blocks.
6. Mount the guitar-string snare system after the shell plan is stable.
7. Glue and square the box.
8. Attach the tapa with the top 4 to 5 in slap-zone relief.
9. Tune snare onset by ear, then record Helmholtz, plate, slap, and sustain measurements.

The validation report says measured prototype data is not yet available. All acoustic values remain predictions until `validation.csv` has measured values and dates.

## Risks And Release Constraints

The risk register identifies 17 open risks across five categories. Highest-leverage concerns for first prototype:

- Helmholtz/plate mismatch if the corrected model or material assumptions are wrong.
- The historical workbook formula missing Helmholtz end correction.
- Tapa screw torque non-uniformity changing plate boundary behavior.
- Supplier variation in 3 mm Baltic-birch tapa thickness.
- Snare preload not represented as a parametric workbook value.
- Inlay press-fit and panel routing risk before assembly.

Public-release concerns in the manifest include replacing placeholder visuals with real build photos, verifying supplier pricing, confirming workbook Helmholtz cells, preserving predicted-vs-measured language, and validating snare preload, panel thickness, joinery fit, and strike response.

## Cross-Links

- [[acoustic-classes/box-drum]]
- [[fabrication/cnc-inlay]]
- [[fabrication/jigs-and-fixtures]]
- [[materials/baltic-birch]]
- [[materials/walnut]]
- [[synthesis/public-release-blockers]]
- [[synthesis/cad-readiness-roadmap]]
- [[synthesis/wolfram-model-patterns]]

## Open Questions

1. Has `cajon-design-table.xlsx` itself been updated to use the corrected Helmholtz end correction, or only the generated workbook/design notes?
2. Should `snare contact preload` become a workbook parameter after the first CJ-S build?
3. What measurement setup will be used for REW/tap tests, and where should first-build spectral data land under `data/`?
4. Which SVG drawings are authoritative enough for shop work before CAD-exported drawings replace them?
5. Should the library card eventually show visual-authority status in addition to CAD/Wolfram/wiki status?
6. When measured values arrive, should the wiki split a reusable [[acoustic-classes/box-drum]] page from this instrument page?

## Maintenance Notes

Next ingest should inspect `visual-output-register.csv`, `jig-decision.md`, `resources.md`, and the OpenSCAD master. After first-build measurements exist, update this page and create a cross-instrument `box-drum` acoustic-class page.
