---
title: Electric Violin
slug: electric-violin
wiki_type: instrument
status: active
sources:
  - path: ../../../strings/electric-violin/README.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/electric-violin/design.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/electric-violin/capstone-manifest.json
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/electric-violin/assembly-manual.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/electric-violin/risks.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/electric-violin/bom.csv
    kind: spreadsheet
    last_seen: 2026-06-19
  - path: ../../../strings/electric-violin/validation.csv
    kind: spreadsheet
    last_seen: 2026-06-19
  - path: ../../../strings/electric-violin/electric-violin-starter.wl
    kind: wolfram
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/bowed-string
  - fabrication/electronics-integration
  - synthesis/public-release-blockers
  - synthesis/wolfram-model-patterns
open_questions:
  - "Which V5 MCP artifacts have been completed: OpenSCAD master, SVG/DXF drawings, hero render, print-packet plate?"
  - "What are the 4-string vs 5-string variant dimensions from the design-table authority (electric-violin-design-table.xlsx)?"
  - "What piezo bridge pickup model and wiring scheme have been selected?"
  - "Has ergonomic balance (weight distribution, chin-rest fit, shoulder-rest compatibility) been verified?"
  - "What string set has been chosen and what are its published tension values at 328 mm scale?"
  - "Has electronics path (output jack, preamp, shielding) been validated for hum and ground noise?"
answers_filed: []
last_ingest: 2026-06-19
last_lint: 2026-06-19
review_due: 2026-09-19
tags:
  - instrument
  - string
  - bowed-string
  - violin-family
  - electric
  - private-review
---

# Electric Violin

## Overview

The `electric-violin` repo is an L2 V5 build-packet candidate for a solid-body 4- and 5-string electric violin with piezo bridge pickup integration. It is a modernized interpretation of the acoustic violin form factor, replacing acoustic resonance with a solid body and electronic amplification.

Primary repo links:

- [README](../../../../strings/electric-violin/README.md)
- [Design notes](../../../../strings/electric-violin/design.md)
- [Assembly manual](../../../../strings/electric-violin/assembly-manual.md)
- [Risks](../../../../strings/electric-violin/risks.md)
- [Capstone manifest](../../../../strings/electric-violin/capstone-manifest.json)

## Current Status

- Release state: private review / L2 scaffold.
- V5 status: V4 markdown layer and V5 audit-trail scaffold in place; V5 MCP-produced artifacts (OpenSCAD master, vector plates, hero render, print plate, DXF) remain pending.
- Build target: solid-body electric violin; 4-string baseline at 328 mm scale (G3–D4–A4–E5), with optional 5-string extension.
- Acoustic class: [[acoustic-classes/bowed-string]] — Mersenne-Taylor for open-string pitches; no acoustic body-resonance component; amplification via piezo bridge pickup.
- CAD state: `electric-violin-design-table.xlsx` is the dimension authority. Parametric OpenSCAD master, reviewed DXF, and hero render are V5 gaps (not yet produced).
- Wolfram model: `electric-violin-starter.wl` is local. Live cloud embed now active via `wolframcloud.com` Public-Execute URL.
- Release blockers: V5 MCP artifacts, electronics verification, sourceability check, ergonomic balance, and measured setup data.

## Source Notes

- [repo] [README](../../../../strings/electric-violin/README.md) — L2 V5 candidate status; solid-body 4/5-string design; piezo pickup integration; five pending V5 deliverables (OpenSCAD, SVG/DXF, hero render, print plate, MCP session log row). `electric-violin-design-table.xlsx` is the dimension authority.
- [repo] [Design notes](../../../../strings/electric-violin/design.md) — solid-body assumptions and 4/5-string variant notes; Mersenne-Taylor governing model; body resonance absent; amplification via piezo bridge pickup.
- [spreadsheet] [Family spec](../../../../strings/electric-violin/family-spec.csv) — per-member rows with `acoustic_law`, `end_condition`, `dimension_provenance`; string family is validator-exempt for `validate_acoustic_law.py`; values use `unknown_requires_measurement` until prototype data lands.
- [wolfram] [Wolfram starter](../../../../strings/electric-violin/electric-violin-starter.wl) — open-string acoustic model; Public-Execute cloud URL now live at `wolframcloud.com`.

## Design Knowledge

The electric violin replaces acoustic body resonance with electronic amplification. The governing pitch model remains Mersenne-Taylor:

```text
f = (1 / (2L)) * sqrt(T / mu)
```

Key design differences from acoustic violin:

| Aspect | Acoustic Violin | Electric Violin |
| --- | --- | --- |
| Body | Carved spruce/maple resonator | Solid body (wood or composite) |
| Pickup | None | Piezo bridge transducer |
| Amplification | Acoustic | Electronic (preamp + amp) |
| Body resonance | Critical | Absent / irrelevant |
| Weight distribution | Traditional | Must be verified for ergonomics |

The 4-string baseline at 328 mm scale matches the acoustic violin (G3–D4–A4–E5). A 5-string extension typically adds a low C3 string below G3. Solid-body construction demands intentional weight balancing since there is no hollow body to distribute mass; chin-rest and shoulder-rest compatibility must be verified.

## Acoustic And Structural Model

String tension for 4 strings at 328 mm scale is approximately 45–55 lbf total (depends on string set). The solid body must withstand the neck-pull vector from the neck block and nut to tailpiece without flexing. Electronics integration introduces routing pockets that affect structural cross-section; piezo saddle wiring must be shielded against hum.

## Build And Validation Logic

V5 deliverables required before fabrication-authority review:

1. Parametric OpenSCAD master (`cad/electric-violin.scad`) — from a Claude Desktop MCP session.
2. Reviewed SVG + DXF drawings (`drawings/electric-violin.svg`, `.dxf`).
3. Hero render (`images/hero-render.png`) — Blender or OpenSCAD STL → Blender.
4. Print-packet assembly plate (`print-packet/assembly-plate.pdf`) — callouts referencing design-table cells.
5. ≥ 1 row in `cad/mcp-session-log.md`.

Additional L3 gates: electronics path validation (output jack, preamp, shielding), sourceability date-check, ergonomic balance verification.

## Release And Provenance Constraints

L2 scaffold only; fabrication authority is blocked behind V5 artifacts and measured setup data. `electric-violin-design-table.xlsx` is the dimensional authority; no claim should be made from README or design.md alone until design-table values are locked.

## Cross-Links

- [[acoustic-classes/bowed-string]]
- [[fabrication/electronics-integration]]
- [[fabrication/cnc-routing]]
- [[materials/solid-body-woods]]
- [[synthesis/public-release-blockers]]
- [[synthesis/wolfram-model-patterns]]

## Open Questions

1. Which of the five V5 MCP artifacts have been produced, and which MCP session log rows exist?
2. What are the per-variant dimensions in `electric-violin-design-table.xlsx`?
3. What piezo bridge pickup model and wiring scheme have been selected?
4. Has ergonomic balance been verified for chin-rest/shoulder-rest fit?
5. What string set has been chosen, and what are its published per-string tension values?
6. Has the electronics path (output jack, preamp, shielding) been validated for hum and ground noise?

## Maintenance Notes

Next ingest should pull in V5 artifact status, design-table dimensions, and first electronics-verification results. Update [[acoustic-classes/bowed-string]] and [[synthesis/public-release-blockers]] when L3 gates clear.
