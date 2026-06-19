---
title: Ashiko Drum-Building Workshop
slug: ashiko-drum-workshop
wiki_type: instrument
status: active
sources:
  - path: ../../../../percussion/ashiko-drum-workshop/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/conical-stave-drum
  - fabrication/stave-construction
  - fabrication/jigs-and-fixtures
open_questions:
  - "Workshop tuner readings from 2015 were not recorded — are measured pitch values available anywhere to back-fill validation.csv?"
  - "What is the acoustic difference (empirically) between the ashiko's conical body and the djembe's goblet profile for bass/tone/slap voice?"
  - "Would the same stave-cut jig and lathe-fixture approach scale to a production batch outside a makerspace context?"
last_ingest: 2026-06-19
tags: [instrument, drum, ashiko, stave-built, workshop, L4-validated, goatskin, lathe, jig]
---

# Ashiko Drum-Building Workshop

## Overview

Archive of the engineering and process documentation behind a 2015 workshop where Tony Koop designed and led eight participants — most with no woodworking experience — in building 16 traditional African ashiko hand drums end-to-end: from raw hardwood lumber to a tuneable, laced, goatskin-headed instrument.

The ashiko is a West African hand drum of Yoruba origin; its conical stave-built body sits acoustically between a djembe and a conga. Tony learned the craft at Morgan Drums (St. Paul, MN) before designing a build process robust enough for first-time makers.

- **Family:** membranophone / conical hand drum
- **Status:** L4 V5 empirical packet — validated by the 2015 build of 16 drums
- **Build count:** 16 drums produced in a single workshop
- **Key artifacts:** CAD geometry, compound stave-cut jig, lathe fixture drawings, table-saw sled, BOM, build photos

Primary repo links:
- [README](../../../../percussion/ashiko-drum-workshop/README.md)
- [Design notes](../../../../percussion/ashiko-drum-workshop/design.md)
- [Validation checklist](../../../../percussion/ashiko-drum-workshop/reference/acoustic-validation-checklist.md)
- [Assembly manual](../../../../percussion/ashiko-drum-workshop/assembly-manual.md)

## Current Status

- Release state: L4 V5 empirical packet — process validated by a 16-drum build. `validation.csv` captures nominal shell/head parameters; measured pitch values from 2015 workshop are pending re-measurement (tuner readings not recorded at the time).
- Library family: drum.
- Acoustic class: conical stave drum.
- CAD state: CAD geometry for the goblet-profile shell and compound stave shapes; lathe-fixture drawings present.

## Source Notes

- [README](../../../../percussion/ashiko-drum-workshop/README.md) — workshop context (January 2015, 8 participants, 16 drums, Twin Cities makerspace), background (Morgan Drums craft training), process overview, key engineering contribution (stave-cut jig and process robust enough for first-time makers).

Artifacts not ingested: `design.md`, `validation.csv`, `bom.csv`, `assembly-manual.md`, workshop photo sequence.

## Design Knowledge

The ashiko's body is a conical stave assembly (narrower at the top open end, wider at the head). The engineering challenge is cutting compound-angle staves that assemble into a clean cone without gaps, then gluing, turning on a lathe (using a custom fixture), and lacing a goatskin head. Tony's contribution: a table-saw sled jig for the compound stave cuts that makes the geometry reproducible by a first-time maker with supervision.

The lathe fixture holds the irregular tapered assembly for the final barrel turn and head-seat cut. The process is descended from the same stave-construction discipline as the djembe and dundun repos.

Related: [[instruments/djembe]] (sister project, goblet profile), [[instruments/dundun]] (cylindrical dundun using the same Morgan Drums training lineage).

## Cross-Links

- [[acoustic-classes/conical-stave-drum]]
- [[fabrication/stave-construction]]
- [[fabrication/jigs-and-fixtures]]

## Open Questions

1. Workshop tuner readings from 2015 were not recorded — are measured pitch values available to back-fill `validation.csv`?
2. What is the empirical acoustic difference between the ashiko conical body and the djembe goblet profile for bass/tone/slap voice?
3. Would the same jig approach scale to a production batch outside a makerspace?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for stave geometry math and `reference/acoustic-validation-checklist.md` for pre/post-build gates. Sister repos djembe and dundun are read-eligible for cross-reference.
