---
title: Kora-Inspired 21-String Prototype
slug: kora
wiki_type: instrument
status: active
last_updated: 2026-05-18
source_count: 10
open_questions: 7
tags:
  - instrument
  - string
  - harp-lute
  - private-review
---

# Kora-Inspired 21-String Prototype

## Overview

The `kora` repo is a private-review, root-mode build packet for a 21-string kora-inspired engineering prototype. It is explicitly framed as a hybrid learning prototype, not a traditional-authenticity claim, production-ready commercial instrument, or culturally authoritative kora design.

The project is built around a compact parametric source workbook and a generated shop packet. The technical center of gravity is the coupling between string schedule, tall bridge, membrane-loaded resonator, through-neck load path, tail anchoring, player ergonomics, and cultural provenance review.

Primary repo links:

- [README](../../../../strings/kora/README.md)
- [Design notes](../../../../strings/kora/design.md)
- [Assembly manual](../../../../strings/kora/assembly-manual.md)
- [Risks](../../../../strings/kora/risks.md)
- [Capstone manifest](../../../../strings/kora/capstone-manifest.json)
- [Explorer](../../../../strings/kora/explorer.html)

## Current Status

- Release state: private review.
- Library family: string.
- Acoustic class: harp-lute / arched bridge-harp territory, with a membrane-loaded resonator and split string banks.
- Wolfram state: live in the central library manifest.
- CAD state: no `.glb` detected yet; CAD currently exists as a parametric brief and OpenSCAD placeholder.
- First-build stance: do not string to full target tension until workbook traceability, string safety, bridge/head staged-load testing, neck proof-load, and cultural wording review are complete.

## Source Notes

The first ingest used the text-native sources and linked the binary/generated artifacts without deep extraction:

- [README](../../../../strings/kora/README.md) establishes the packet map, public-release caution, workbook snapshot, and cultural provenance framing.
- [Design notes](../../../../strings/kora/design.md) capture the workbook cell map, governing Mersenne-Taylor string model, segmented bowl assumptions, bridge requirements, and done criteria.
- [Assembly manual](../../../../strings/kora/assembly-manual.md) defines staged prototype build phases and hold points before full tension.
- [Risks](../../../../strings/kora/risks.md) records cultural, string tension, bridge, resonator/head, neck/joint, and ergonomic risks.
- [Validation table](../../../../strings/kora/validation.csv) defines 15 release gates, all open at ingest.
- [Family spec](../../../../strings/kora/family-spec.csv) defines the root prototype, low-tension mule, and partial bridge study.
- [BOM](../../../../strings/kora/bom.csv) captures the segmented bowl, head, neck, tail, bridge, string, electronics, jig, and finish planning assumptions.
- [CAD brief](../../../../strings/kora/cad/kora-parametric-brief.md) states that CAD must make the load path visible and should not treat the shell as the default load-bearing member.
- [CNC plan](../../../../strings/kora/cnc/cnc-plan.md) recommends fixture work before final CNC and defines CNC-ready exit criteria.
- [Wolfram notes](../../../../strings/kora/wolfram/README.md) point to string percent-break plots, low-tension mule schedule, bowl geometry, and measured-vs-predicted charts as future notebook outputs.

Linked artifacts not distilled in this pass:

- [Design workbook](../../../../strings/kora/kora-design-table.xlsx)
- [Capstone deck markdown](../../../../strings/kora/capstone-deck.md)
- [Capstone deck PPTX](../../../../strings/kora/capstone-deck.pptx)
- [Print packet PDF](../../../../strings/kora/print-packet.pdf)
- [Drawings folder](../../../../strings/kora/drawings/)
- [CAD folder](../../../../strings/kora/cad/)
- [Learn-to-play folder](../../../../strings/kora/learn-to-play/)

## Design Knowledge

The workbook snapshot gives the current dimensional anchor:

- Bowl outside diameter: 20.3 in.
- Bowl depth: 9.8 in.
- Neck length: 51.2 in.
- String vibrating lengths: 8.7 to 31.1 in.
- Target string tension ramp: 8 to 14 lbf per string.
- Segmented bowl: 12 segments per ring, 14 rings, 168 total bowl segments.
- Bridge: about 6 in high, with about 0.273 in string spacing by formula.

The governing string model is Mersenne-Taylor:

```text
f = (1 / (2 L)) sqrt(T / mu)
```

The critical limitation is that the current schedule puts several treble strings near or above practical nylon break targets under the idealized round-string model. The design notes call this a safety/readiness issue, not an aesthetic tweak.

The resonator is a segmented wooden bowl replacing a natural calabash form. The wiki should preserve the distinction: this is a practical shop substitute and acoustic study object, not a traditional-material equivalence claim.

## Build And Validation Logic

The assembly plan is intentionally staged:

1. Confirm workbook labels and cell map.
2. Build segmented bowl and rim test rings before committing all segments.
3. Select and test head material before bridge installation.
4. Establish a continuous neck/spine and proof-load the neck/tail path.
5. Prototype the bridge with a broad foot and staged load tests.
6. Use a low-tension mule schedule before full-pitch stringing.
7. Record frequency, head deflection, bridge position, neck deflection, and humidity into `validation.csv`.

The validation table has no passed measurements yet. It should be treated as a release-gate checklist, not evidence of performance.

## Release And Provenance Constraints

This page should keep the kora's cultural context visible. The repo already names the instrument as culturally situated in West African Mande/Mandinka traditions and associated with jali/griot musicianship. Public language should use phrases such as `kora-inspired prototype`, `engineering study`, and `hybrid build packet`.

Avoid:

- authentic
- traditional replica
- master kora
- improved kora
- modernized kora

Public release requires cultural provenance review, safety validation, measured prototype data, and owned or permission-cleared visuals.

## Cross-Links

- [[acoustic-classes/harp-lute]]
- [[fabrication/stave-or-segmented-bowl]]
- [[fabrication/bridge-and-string-layout]]
- [[materials/hide-and-synthetic-heads]]
- [[synthesis/public-release-blockers]]
- [[synthesis/cad-readiness-roadmap]]
- [[synthesis/wolfram-model-patterns]]

## Open Questions

1. Should the first physical build be `KORA-21-MULE` rather than `KORA-21-ROOT` until treble string break margins are fixed?
2. Who should review cultural provenance language before any public-release candidate?
3. Which head material path should be tested first: ethically sourced hide, synthetic membrane, or parallel samples?
4. What real string unit-weight data should replace the current idealized nylon/wound-string assumptions?
5. Should the continuous neck/spine be modeled as a through-neck, an internal spine, or a mechanically backed hybrid?
6. What bridge-foot footprint and pad material should be used for the first staged-load test?
7. Which workbook cells need human-readable labels before CAD/CNC work is allowed to become authoritative?

## Maintenance Notes

Next ingest should extract or summarize the workbook structure, inspect the Wolfram starter file, and decide whether the first synthesis page belongs under `acoustic-classes/harp-lute`, `fabrication/bridge-and-string-layout`, or `synthesis/public-release-blockers`.
