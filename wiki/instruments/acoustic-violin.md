---
title: Acoustic Violin
slug: acoustic-violin
wiki_type: instrument
status: active
sources:
  - path: ../../../strings/acoustic-violin/README.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/acoustic-violin/design.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/acoustic-violin/capstone-manifest.json
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/acoustic-violin/assembly-manual.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/acoustic-violin/risks.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../strings/acoustic-violin/bom.csv
    kind: spreadsheet
    last_seen: 2026-06-19
  - path: ../../../strings/acoustic-violin/validation.csv
    kind: spreadsheet
    last_seen: 2026-06-19
  - path: ../../../strings/acoustic-violin/acoustic-violin-starter.wl
    kind: wolfram
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/bowed-string
  - synthesis/public-release-blockers
  - synthesis/wolfram-model-patterns
open_questions:
  - "Which arching and graduation reference will be selected before plate cutting begins?"
  - "What is the exact body outline, and has a reviewed CAD/DXF been created?"
  - "What are the neck-set projection and action targets, and have they been checked against the bridge line?"
  - "Which string set has been chosen and what are its published tension values?"
  - "Are bridge and soundpost fitting notes with photos available?"
  - "Has open-string pitch stability been measured after 24-hour pitch-up?"
answers_filed: []
last_ingest: 2026-06-19
last_lint: 2026-06-19
review_due: 2026-09-19
tags:
  - instrument
  - string
  - bowed-string
  - violin-family
  - private-review
---

# Acoustic Violin

## Overview

The `acoustic-violin` repo is an L2 V5 build-packet candidate for a 4-string acoustic violin — traditional construction reference and stave-built explorations. It documents the standard setup geometry and engineering gaps for a violin-family instrument, without making fabrication-authority claims until arching, graduation, neck-set, soundpost, and bridge-setup evidence exist.

Primary repo links:

- [README](../../../../strings/acoustic-violin/README.md)
- [Design notes](../../../../strings/acoustic-violin/design.md)
- [Assembly manual](../../../../strings/acoustic-violin/assembly-manual.md)
- [Risks](../../../../strings/acoustic-violin/risks.md)
- [Capstone manifest](../../../../strings/acoustic-violin/capstone-manifest.json)

## Current Status

- Release state: private review / L2 scaffold.
- Packet state: `instrument-maker-v4`, generated 2026-05-09.
- Build target: 4-string acoustic violin reference scaffold (G3–D4–A4–E5, 328 mm vibrating length).
- Acoustic class: [[acoustic-classes/bowed-string]] — standard violin family, Mersenne-Taylor governing model.
- CAD state: placeholder SolidWorks scaffold; arching and graduation not finalized. `acoustic-violin-placeholder.scad` exists. No reviewed DXF.
- Wolfram model: `acoustic-violin-starter.wl` is local. Live cloud embed is now active via `wolframcloud.com` Public-Execute URL.
- Release blockers: arching/graduation reference, neck-set drawing, bridge/soundpost fitting evidence, string-set tension data, open-string pitch stability measurement.

## Source Notes

- [repo] [README](../../../../strings/acoustic-violin/README.md) — establishes L2 V5 status, packet contents, 328 mm scale, G3–E5 tuning, build-review checklist, and validation boundary. Key point: arching, graduation, neck-set, soundpost, bridge setup, CAD, and measured validation are all explicitly incomplete.
- [repo] [Design notes](../../../../strings/acoustic-violin/design.md) — governing model is Mersenne-Taylor open-string equation; body-mode coupling (arching, graduation, bridge, soundpost, air modes) not modeled. Baseline table: 328 mm scale, standard 4-string set, ~356 mm body, spruce/maple construction, neck angle TBD, total tension ~45–55 lbf.
- [repo] [Capstone manifest](../../../../strings/acoustic-violin/capstone-manifest.json) — L2 scaffold readiness; fabrication authority explicitly blocked until reviewed drawings, CAD/DXF, measured setup, and validation evidence exist. Generated and AI-generated images not allowed as authority. Wolfram not allowed as fabrication authority.
- [repo] [Assembly manual](../../../../strings/acoustic-violin/assembly-manual.md) — sequential build steps; critical hold points before bridge/soundpost fitting, neck-set, and pitch-up.
- [repo] [Risks](../../../../strings/acoustic-violin/risks.md) — risk register with mitigations.
- [spreadsheet] [BOM](../../../../strings/acoustic-violin/bom.csv) — bill of materials; sourcing fields are estimated, not date-checked.
- [spreadsheet] [Validation](../../../../strings/acoustic-violin/validation.csv) — validation gates; no measured results present.
- [wolfram] [Wolfram starter](../../../../strings/acoustic-violin/acoustic-violin-starter.wl) — open-string acoustic model; Public-Execute cloud URL now live at `wolframcloud.com`.

## Design Knowledge

The violin family governing model is Mersenne-Taylor:

```text
f = (1 / (2L)) * sqrt(T / mu)
```

Body-mode coupling — arching, graduation, bridge mass, soundpost stiffness, and air/body resonances — is intentionally left outside this packet's scope. The design notes treat it as an empirical question to be answered by a reference arching plan and measured prototype.

Baseline geometry:

| Parameter | Value |
| --- | --- |
| Scale (vibrating length) | 328 mm / 12.91 in |
| Tuning | G3–D4–A4–E5 |
| Body length | ~356 mm (outline TBD) |
| Top | Spruce |
| Back | Maple |
| Target total tension | ~45–55 lbf |
| Neck angle | TBD from setup drawing |

Key build sequence hold points: neck projection and stop-length check before woodwork; bridge-foot and soundpost fitting under low tension; gradual pitch-up; action/stability measurement before L3.

## Acoustic And Structural Model

The violin body radiates through plate-mode coupling: the top plate and back plate have distinct resonance patterns; the air-body mode (A0) couples at roughly 280–290 Hz in a full-size violin body. The soundpost mechanically links top to back, stiffens the treble side, and shifts mode patterns. Graduation (plate thickness profile) tunes the plates. None of this is modeled in the current packet — it must be built, fitted, and measured.

String tension for a standard 4-string violin set is approximately 45–55 lbf total, well within the glued joint tolerance of traditional construction.

## Build And Validation Logic

L3 gates required before claiming build readiness:

1. Select and cite an arching and graduation reference.
2. Create reviewed CAD/DXF or dimensioned drawings for outline, neck set, bridge line, and f-hole placeholders.
3. Verify the selected string set against published tension data before first pitch-up.
4. Record bridge fit, soundpost fit, action, neck projection, and open-string pitch stability.
5. Replace estimated sourcing fields with date-checked supplier evidence before making purchasing claims.

Shop note from README: bring strings up gradually; stop if top, bridge, or soundpost shows unsafe movement. Poorly fitted bridge/soundpost can damage the top even within normal tension range.

## Release And Provenance Constraints

This is a reference scaffold, not a validated build. All fabrication-authority claims remain gated behind reviewed drawings and measured prototype evidence. The packet may be used for design review and prototype planning only.

## Cross-Links

- [[acoustic-classes/bowed-string]]
- [[fabrication/bridge-and-string-layout]]
- [[materials/spruce]]
- [[materials/maple]]
- [[synthesis/public-release-blockers]]
- [[synthesis/wolfram-model-patterns]]

## Open Questions

1. Which arching and graduation reference will be selected, and what dimensions does it specify?
2. Has the neck-set drawing been produced with projection, stop-length, bridge-line, and action targets resolved?
3. Which string set has been chosen, and what are its published per-string tension values?
4. Are bridge-foot fitting and soundpost fitting notes with photos available?
5. Has open-string pitch stability been confirmed after 24-hour pitch-up to final tension?
6. What is the exact CAD/DXF body outline, and has it been reviewed for centerline/bridge-line accuracy?

## Maintenance Notes

Next ingest should pull in arching/graduation selection, neck-set drawing, and first measured setup data. Update [[acoustic-classes/bowed-string]] and [[synthesis/public-release-blockers]] when L3 gates clear.
