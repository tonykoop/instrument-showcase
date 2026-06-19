---
title: Floor Harp
slug: floor-harp
wiki_type: instrument
status: active
sources:
  - path: ../../../strings/floor-harp/README.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/floor-harp/design.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/floor-harp/capstone-manifest.json
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/floor-harp/assembly-manual.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/floor-harp/risks.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/floor-harp/string-schedule.csv
    kind: spreadsheet
    last_seen: 2026-06-19
  - path: ../../../strings/floor-harp/bom.csv
    kind: spreadsheet
    last_seen: 2026-06-19
  - path: ../../../strings/floor-harp/validation.csv
    kind: spreadsheet
    last_seen: 2026-06-19
  - path: ../../../strings/floor-harp/floor-harp-starter.wl
    kind: wolfram
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/floor-harp
  - fabrication/frame-load-analysis
  - synthesis/public-release-blockers
  - synthesis/wolfram-model-patterns
open_questions:
  - "Has a source-backed 22-string note/gauge/tension schedule been obtained from a supplier?"
  - "What is the total estimated string load and has the neck/pillar/base structure been reviewed for that load?"
  - "Has a tuning-pin scrap test been run (pilot size, torque, holding power)?"
  - "Has a staged pitch-up log with frame movement measurements been recorded?"
  - "What CAD has been produced beyond the design intent: dimensioned drawings for string paths, neck, pillar, base?"
  - "Has tip stability and playing-position ergonomics been verified?"
answers_filed: []
last_ingest: 2026-06-19
last_lint: 2026-06-19
review_due: 2026-09-19
tags:
  - instrument
  - string
  - harp
  - pedal-style
  - private-review
---

# Floor Harp

## Overview

The `floor-harp` repo is an L2 V5 build-packet candidate for a small floor-standing concert-style harp. It documents a 22-string C3–C6 diatonic design and establishes the frame-load review, string schedule validation, and staged pitch-up protocol as prerequisites for L3 promotion.

Primary repo links:

- [README](../../../../strings/floor-harp/README.md)
- [Design notes](../../../../strings/floor-harp/design.md)
- [Assembly manual](../../../../strings/floor-harp/assembly-manual.md)
- [Risks](../../../../strings/floor-harp/risks.md)
- [Capstone manifest](../../../../strings/floor-harp/capstone-manifest.json)

## Current Status

- Release state: private review / L2 scaffold.
- Build target: 22-string floor harp, C3–C6 diatonic.
- Acoustic class: [[acoustic-classes/floor-harp]] — plucked string / pillar-frame resonator.
- String schedule: target-only 22-string C3–C6 schedule in `string-schedule.csv`; gauge, tension, source, and measured pitch fields remain open.
- CAD state: design-intent only; dimensioned neck, pillar, and base drawings not yet produced.
- Wolfram model: `floor-harp-starter.wl` is local. Live cloud embed now active via Public-Execute URL.
- Release blockers: source-backed string schedule, total-load frame review, tuning-pin scrap test, staged pitch-up log, sourceability check for strings and long clear hardwood.

## Source Notes

- [repo] [README](../../../../strings/floor-harp/README.md) — L2 V5 candidate; 22-string C3–C6 diatonic; speaking lengths graduated ~42 in (bass) to ~13 in (treble); nylon/fluorocarbon/wound bass strings. Frame-load path must be reviewed before any string-up. Critical shop note: detune and revise if neck, pillar, or base joint shows permanent movement.
- [repo] [Design notes](../../../../strings/floor-harp/design.md) — design basis, string schedule assumptions, and structural gaps.
- [spreadsheet] [String schedule](../../../../strings/floor-harp/string-schedule.csv) — target-only 22-string schedule; not a source-backed gauge or tension chart.
- [wolfram] [Wolfram starter](../../../../strings/floor-harp/floor-harp-starter.wl) — acoustic/tension model; Public-Execute cloud URL now live at `wolframcloud.com`.

## Design Knowledge

The floor harp carries substantial sustained string load through neck, pillar, and base to soundboard. The governing string model is Mersenne-Taylor:

```text
f = (1 / (2L)) * sqrt(T / mu)
```

For a 22-string diatonic C3–C6 harp with graduated speaking lengths (~13–42 in), total string load is in the range of 300–500 lbf depending on string gauge selection. The structural path runs from soundboard (where strings terminate at pins) through the body/resonator, upward through the curved neck (which resists the string-pull cantilever moment), and down through the pillar to the base.

Key design decisions still open:

| Decision | Status |
| --- | --- |
| String set (gauge, material, maker) | Target-only; no source confirmation |
| Per-string tension schedule | Not yet backed by supplier data |
| Neck cross-section and lamination | Pending load review |
| Pillar angle and section | Pending load review |
| Tuning-pin bore and spacing | Pending scrap test |
| Soundboard material and graduation | TBD |

## Acoustic And Structural Model

The soundboard is the primary radiator; the hollow body (box resonator) couples the air volume for bass reinforcement. Soundboard graduation, bridge curve geometry, and string termination geometry are all interrelated. The structural model must size the neck cantilever and pillar compression before choosing materials — laminated hardwood or solid hardwood are typical for the neck; pillar is usually solid hardwood or metal tube.

## Build And Validation Logic

L3 gates (per README):

1. Source-backed 22-string gauge/tension schedule from supplier data.
2. Total string load estimate + structural review of neck, pillar, and base joint.
3. Tuning-pin scrap test (pilot size, torque, holding power).
4. Staged pitch-up log with frame deflection measurements after each stage.
5. Tip-stability and playing-position photos.
6. Sourceability check for harp strings, pins, and long clear hardwood.

Shop protocol: tune in stages, measure frame after each stage, keep people out of the string plane. Detune and revise if permanent joint movement is observed.

## Release And Provenance Constraints

L2 scaffold only. The current string schedule is a design target, not a fabrication authority. No frame geometry should be cut from this packet alone — it requires a reviewed load-path side elevation, dimensioned cross-sections, and sourced string data.

## Cross-Links

- [[acoustic-classes/floor-harp]]
- [[fabrication/frame-load-analysis]]
- [[fabrication/bridge-and-string-layout]]
- [[materials/hardwood-frame]]
- [[synthesis/public-release-blockers]]
- [[synthesis/wolfram-model-patterns]]

## Open Questions

1. What string set (maker, gauge, material per note) has been identified, and what are its published tension values?
2. What is the estimated total string load, and has the neck/pillar/base load path been reviewed for that load?
3. Has a tuning-pin scrap test been conducted (pilot bore, torque, holding power)?
4. Has a staged pitch-up log been started?
5. What CAD has been produced beyond the design intent? Has a dimensioned side elevation been drawn?
6. Has tip stability and playing-position ergonomics been checked?

## Maintenance Notes

Next ingest should pull in the string schedule from supplier data, load review results, and first pitch-up log. When measured data exists, update [[acoustic-classes/floor-harp]] and [[synthesis/public-release-blockers]].
