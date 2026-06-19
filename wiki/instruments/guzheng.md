---
title: Guzheng
slug: guzheng
wiki_type: instrument
status: active
sources:
  - path: ../../../strings/guzheng/README.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/guzheng/design.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/guzheng/capstone-manifest.json
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/guzheng/assembly-manual.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/guzheng/risks.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/guzheng/family-spec.csv
    kind: spreadsheet
    last_seen: 2026-06-19
  - path: ../../../strings/guzheng/validation.csv
    kind: spreadsheet
    last_seen: 2026-06-19
  - path: ../../../strings/guzheng/guzheng-starter.wl
    kind: wolfram
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/zither
  - synthesis/public-release-blockers
  - synthesis/wolfram-model-patterns
open_questions:
  - "What measured dimensions exist for GUZ-REF-21 (bridge spacing, soundboard crown, string speaking lengths)?"
  - "Has the soundboard load-spread path been reviewed before any string tensioning?"
  - "What string set has been selected, and have published tensions been verified for GUZ-REF-21?"
  - "Has the CAD gate been opened for guzheng-reference-family.scad with measured parameters?"
  - "Are compact and bass family rows still blocked at allowed_to_build=no_reference_gate_pending?"
  - "Has bridge corridor geometry been reviewed (string spacing, bridge foot footprint, crown curve)?"
answers_filed: []
last_ingest: 2026-06-19
last_lint: 2026-06-19
review_due: 2026-09-19
tags:
  - instrument
  - string
  - zither
  - chinese
  - plucked
  - private-review
---

# Guzheng

## Overview

The `guzheng` repo is an L2 V5 build-packet candidate following a reference-member-first family strategy. The packet treats `GUZ-REF-21` (the 21-string reference member) as the only permitted first build; compact and bass variants inherit no dimensions until the reference member has passed measurement and load gates.

Primary repo links:

- [README](../../../../strings/guzheng/README.md)
- [Design notes](../../../../strings/guzheng/design.md)
- [Assembly manual](../../../../strings/guzheng/assembly-manual.md)
- [Risks](../../../../strings/guzheng/risks.md)
- [Capstone manifest](../../../../strings/guzheng/capstone-manifest.json)

## Current Status

- Release state: private review / L2 V5 build-packet candidate.
- Build target: `GUZ-REF-21` reference member (21-string), then compact and bass variants only after reference-member gate passes.
- Acoustic class: [[acoustic-classes/zither]] — plucked long zither; moveable bridges; soundboard-resonated.
- CAD state: `cad/guzheng-reference-family.scad` exists as a non-rendering gate scaffold; it is NOT fabrication authority until measured parameters are supplied and reviewed.
- Wolfram model: `guzheng-starter.wl` is local. Live cloud embed now active via Public-Execute URL.
- Release blockers: measured GUZ-REF-21 dimensions (bridge spacing, crown, string schedule), load-path review, visual-authority gate, compact/bass variant gates.

## Source Notes

- [repo] [README](../../../../strings/guzheng/README.md) — reference-member-first strategy; GUZ-REF-21 is the only permitted first build; compact and bass rows blocked at `allowed_to_build: no_reference_gate_pending` in `family-spec.csv`. Critical safety gates: do not tension strings until load-spread path is reviewed; do not scale soundboard crown from concept art; do not render or cut from OpenSCAD until measurement gate is deliberately opened.
- [repo] [Design notes](../../../../strings/guzheng/design.md) — packet intent, family split, authority rules, and reference gate.
- [spreadsheet] [Family spec](../../../../strings/guzheng/family-spec.csv) — compact, reference, and bass rows with inheritance blocked by default.
- [spreadsheet] [Validation](../../../../strings/guzheng/validation.csv) — pass/fail gates for crown, creep, bridge corridor, load, string schedule, and visual authority.
- [wolfram] [Wolfram starter](../../../../strings/guzheng/guzheng-starter.wl) — load, crown, and gate-readiness checks; Public-Execute cloud URL now live at `wolframcloud.com`.

## Design Knowledge

The guzheng is a long plucked zither with moveable bridges. Each string has its own moveable bridge (yàn, "goose foot") that sets the speaking length and pitch on the right side (the right side is played); the left side resonates sympathetically. The soundboard arches in a gentle crown; strings press down on the bridge saddle and the soundboard must distribute the combined downward load across all 21 strings.

Key structural observation: the cumulative downforce from 21 strings on a crowned soundboard creates a complex load surface. The bridge corridor geometry (bridge spacing, bridge foot footprint, crown curve, and brace pattern) must be reviewed as a system before tensioning.

Current string schedule: target-only; gauge, tension, source, and measured pitch remain open for GUZ-REF-21.

## Acoustic And Structural Model

The guzheng body is a shallow trapezoidal box resonator with a curved spruce or paulownia soundboard. The Mersenne-Taylor relation governs string pitch:

```text
f = (1 / (2L)) * sqrt(T / mu)
```

The moveable bridge allows pitch adjustment post-build, but bridge foot geometry and soundboard stiffness interact. Excessive crown flattening under string load (creep) is a known risk. The validation table includes crown-creep measurement gates.

## Build And Validation Logic

Reference-member-first gate sequence (from README):

1. Read `design.md` before drafting CAD or cutting stock.
2. Build only `GUZ-REF-21`; compact and bass variants are blocked.
3. Complete all reference-member gates in `validation.csv` (crown, load, bridge corridor, string schedule, visual authority).
4. Only after GUZ-REF-21 passes, revise compact and bass rows in `family-spec.csv`.
5. Use DXF/CAD/reviewed drawings as fabrication authority; generated images are concept-only.

Safety gates:
- Do not tension strings before load-path review.
- Do not scale soundboard crown from concept art.
- Do not render or cut from `guzheng-reference-family.scad` until measurement gate is opened with reviewed parameters.

## Release And Provenance Constraints

The guzheng is a living Chinese musical tradition. Do not claim authority over traditional dimensions or construction. The packet is a modern engineering scaffold for a guzheng-inspired instrument, not a culturally authoritative reproduction.

## Cross-Links

- [[acoustic-classes/zither]]
- [[fabrication/soundboard-bracing]]
- [[fabrication/bridge-and-string-layout]]
- [[materials/paulownia]]
- [[synthesis/public-release-blockers]]
- [[synthesis/wolfram-model-patterns]]

## Open Questions

1. What measured dimensions exist for GUZ-REF-21 (bridge spacing, soundboard crown height, string speaking lengths per position)?
2. Has the soundboard load-spread path been reviewed, including bridge corridor geometry and brace pattern?
3. What string set has been selected and what are its published per-string tension values?
4. Has the OpenSCAD measurement gate been deliberately opened with reviewed parameter values?
5. Are compact and bass family rows still at `allowed_to_build: no_reference_gate_pending` in `family-spec.csv`?
6. Has soundboard crown creep been measured under sustained string load in any test?

## Maintenance Notes

Next ingest should pull in GUZ-REF-21 measurement data, load review, and first validation results. Update [[acoustic-classes/zither]] and [[synthesis/public-release-blockers]] when reference-member gates clear.
