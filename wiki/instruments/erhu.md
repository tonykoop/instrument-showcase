---
title: Erhu
slug: erhu
wiki_type: instrument
status: active
sources:
  - path: ../../../strings/erhu/README.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/erhu/design.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/erhu/capstone-manifest.json
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/erhu/qianjin-measurement-plan.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/erhu/risks.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/erhu/bom.csv
    kind: spreadsheet
    last_seen: 2026-06-19
  - path: ../../../strings/erhu/validation.csv
    kind: spreadsheet
    last_seen: 2026-06-19
  - path: ../../../strings/erhu/wolfram-study-notes.md
    kind: wolfram
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/bowed-string
  - fabrication/membrane-instruments
  - synthesis/public-release-blockers
  - synthesis/wolfram-model-patterns
open_questions:
  - "What are the measured resonator body dimensions (diameter, depth, wall thickness, membrane seat depth)?"
  - "Has the qianjin position been measured per the qianjin-measurement-plan.md protocol on an installed reference instrument?"
  - "What string set has been identified, and have published tensions and bowed response been confirmed?"
  - "Has the membrane bridge-contact geometry been captured per membrane-bridge-contact-capture.csv?"
  - "What V5 MCP artifacts have been completed beyond the qianjin-scale DXF starter?"
  - "Has the neck peg scroll spike geometry been reviewed per neck-peg-bridge-authority-gates.csv?"
answers_filed: []
last_ingest: 2026-06-19
last_lint: 2026-06-19
review_due: 2026-09-19
tags:
  - instrument
  - string
  - bowed-string
  - huqin
  - chinese
  - membrane-resonator
  - private-review
---

# Erhu

## Overview

The `erhu` repo is an L2 V5 build-packet candidate for a 2-string bowed instrument from the huqin family, played throughout Chinese classical and folk music. The packet documents the qianjin-to-bridge setup scale at 380–420 mm (active: 400 mm) and establishes measurement and authority gates before any body or joinery geometry is promoted.

Primary repo links:

- [README](../../../../strings/erhu/README.md)
- [Design notes](../../../../strings/erhu/design.md)
- [Qianjin measurement plan](../../../../strings/erhu/qianjin-measurement-plan.md)
- [Risks](../../../../strings/erhu/risks.md)
- [Capstone manifest](../../../../strings/erhu/capstone-manifest.json)

## Current Status

- Release state: private review / L2 V5 build-packet candidate.
- Build target: qianjin-to-bridge setup-scale prototype; active speaking length 400 mm (range 380–420 mm).
- Acoustic class: [[acoustic-classes/bowed-string]] — 2-string huqin; membrane-covered hexagonal or cylindrical resonator; bridge rests on membrane, not on a wood soundboard.
- Fabrication authority: limited to qianjin-to-bridge scale only. Body, membrane, bridge, neck, peg, scroll, and spike geometry are all blocked behind measurement and review gates.
- DXF: `drawings/erhu-qianjin-scale-starter.dxf` exists for the setup strip only. Body/joinery DXF is not authorized.
- Wolfram model: `erhu-starter.wl` is live; Wolfram Cloud embed now active via Public-Execute URL.
- Release blockers: measured resonator geometry, membrane bridge-contact capture, string-source confirmation, reviewed CAD/DXF, acoustic response.

## Source Notes

- [repo] [README](../../../../strings/erhu/README.md) — L2 V5 candidate; active scale 400 mm; qianjin-to-bridge is the governing measurement; older long-scale assumption is archive-only. Fabrication authority gated behind multiple measurement/review CSV tables. Rounds 21–23 added contact-point measurement protocol and photo evidence registers.
- [repo] [Design notes](../../../../strings/erhu/design.md) — canonical geometry, scope, and non-canonical archive note.
- [repo] [Qianjin measurement plan](../../../../strings/erhu/qianjin-measurement-plan.md) — installed contact-point measurement protocol and anti-violin-scale review rules.
- [spreadsheet] [Resonator authority gates](../../../../strings/erhu/resonator-authority-gates.csv) — blocks resonator body and membrane geometry promotion until measured evidence exists.
- [spreadsheet] [Neck/peg/bridge authority gates](../../../../strings/erhu/neck-peg-bridge-authority-gates.csv) — blocks neck, peg, scroll, spike, bridge-object, and string-spacing geometry until gates clear.
- [spreadsheet] [String source assumptions](../../../../strings/erhu/string-source-assumptions.csv) — blocks pitch, tension, and scale claims until installed string source and bowed response are recorded.
- [wolfram] [Wolfram study notes](../../../../strings/erhu/wolfram-study-notes.md) — source-only computational study notes; Public-Execute cloud URL now live at `wolframcloud.com`.

## Design Knowledge

The erhu is a 2-string bowed instrument. The resonator is a hexagonal or cylindrical wooden box with a python- or synthetic-skin membrane stretched across one face. A snake-wood bridge rests on the membrane; the bow hair passes between the two strings (the bow cannot be removed from the instrument without cutting strings or detuning). This membrane coupling is the key acoustic distinction from Western bowed strings:

```text
f = (1 / (2L)) * sqrt(T / mu)
```

The qianjin is a silk or nylon thread loop clamped around both strings and the neck, acting as a moveable nut to set the active vibrating length. Its exact contact-point position is the primary intonation variable.

Current scale parameters:

| Parameter | Value |
| --- | --- |
| Active speaking length | 400 mm (nominal) |
| Setup range | 380–420 mm |
| Dimension basis | Qianjin-to-bridge contact point |
| Strings | 2 (D4, A4 typical) |

The older long-scale assumption (from Round 8 and earlier) is retained as comparison history in `design.md` but is not canonical geometry for this packet.

## Acoustic And Structural Model

The erhu body is a Helmholtz-like coupling system: the membrane-covered resonator acts as a vibrating plate, and the internal air couples through the open back. Unlike most Western strings, the lack of a wood soundboard means plate stiffness and graduation are replaced by membrane tension as the primary acoustic tuning variable. Membrane material (python skin vs. synthetic) significantly affects tonal quality. The bridge geometry and contact-point load distribution are critical.

The `erhu-starter.wl` Wolfram model covers setup-scale and string tension; full membrane acoustic modeling is documented in `wolfram-study-notes.md` as source-only (not runtime-validated).

## Build And Validation Logic

The validation chain is staged through multiple authority-gate CSV files:

1. Measure installed resonator body: `resonator-photo-measurement-evidence.csv` + `resonator-authority-gates.csv`.
2. Capture membrane and bridge-contact: `membrane-bridge-contact-capture.csv`.
3. Install qianjin per `qianjin-measurement-plan.md`; record contact points.
4. Confirm string source and bowed response: `string-source-assumptions.csv`.
5. Promote geometry to CAD/DXF only after measurement gates clear.
6. V5 MCP artifacts: parametric SCAD master, reviewed DXF, hero render.

## Release And Provenance Constraints

The erhu is a living Chinese musical tradition. The wiki and explorer pages must use careful language. Avoid claiming authority over traditional construction or implying that this packet represents culturally authoritative dimensions. The design notes and risks register include cultural-risk gate entries.

## Cross-Links

- [[acoustic-classes/bowed-string]]
- [[fabrication/membrane-instruments]]
- [[fabrication/bridge-and-string-layout]]
- [[synthesis/public-release-blockers]]
- [[synthesis/wolfram-model-patterns]]

## Open Questions

1. What are the measured resonator dimensions (body diameter, depth, wall thickness, membrane seat depth, sound-hole configuration)?
2. Has the qianjin contact-point position been measured per the installed-measurement protocol on a real reference instrument?
3. What string set has been identified, and have published tensions and bowed response been confirmed at 400 mm scale?
4. Has the membrane bridge-contact geometry been captured per `membrane-bridge-contact-capture.csv`?
5. Which V5 MCP artifacts have been completed beyond the qianjin-scale DXF starter (`erhu-qianjin-scale.scad`, `erhu-qianjin-scale-starter.dxf`)?
6. Has neck/peg/scroll/spike geometry been gate-cleared per `neck-peg-bridge-authority-gates.csv`?

## Maintenance Notes

Next ingest should import resonator measurement evidence, bridge-contact capture, and string-source results. When measured data exists, update [[acoustic-classes/bowed-string]] and [[synthesis/public-release-blockers]] with qianjin-scale confirmation and resonator dimensions.
