---
title: Clarinet Starter Packet
slug: clarinet
wiki_type: instrument
status: active
sources:
  - path: ../../../woodwind/clarinet/README.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/clarinet/capstone-manifest.json
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/clarinet/risks.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../woodwind/clarinet/validation.csv
    kind: spreadsheet
    last_seen: 2026-06-19
  - path: ../../../woodwind/clarinet/measured-bore-tonehole-authority-plan.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/single-reed-cylindrical
  - fabrication/bore-and-toneholes
  - synthesis/public-release-blockers
  - synthesis/wolfram-model-patterns
open_questions:
  - "Have bore stations been measured per bore-station-plan.csv?"
  - "Have tone-hole center, diameter, chimney, and closure been measured per tone-hole-authority-plan.csv?"
  - "Has a reed and mouthpiece been selected and tested per reed-mouthpiece-assumptions.csv?"
  - "Has the leak/pitch validation loop been run per leak-pitch-validation-plan.csv?"
  - "Have CAD/DXF authority gates been opened with measured/reviewed geometry?"
answers_filed: []
last_ingest: 2026-06-19
last_lint: 2026-06-19
review_due: 2026-09-19
tags:
  - instrument
  - woodwind
  - single-reed
  - clarinet
  - cylindrical-bore
  - private-review
---

# Clarinet Starter Packet

## Overview

The `clarinet` repo is an L2 V5 build-packet candidate for a simple cylindrical single-reed clarinet study. The packet has a full V5 surface (OpenSCAD scaffold, MCP session log, visual-output register, measurement authority plan), but all critical dimensions are `pending_measurement` — fabrication authority is blocked until bore stations, tone-hole positions, and mouthpiece geometry are measured and reviewed.

Primary repo links:

- [README](../../../../woodwind/clarinet/README.md)
- [Risks](../../../../woodwind/clarinet/risks.md)
- [Capstone manifest](../../../../woodwind/clarinet/capstone-manifest.json)

## Current Status

- Release state: private review / L1–L2 starter scaffold.
- Build target: keyless-first-prototype single-reed cylindrical clarinet study.
- Acoustic class: [[acoustic-classes/single-reed-cylindrical]] — cylindrical bore, single reed, effectively stopped pipe.
- Fabrication authority: NONE. No measured geometry exists. Do not cut, print, drill, or machine from this repo until the validation loop has bore and tone-hole data.
- Wolfram model: `clarinet-starter.wl` is a source-only quarter-wave check starter. Live cloud embed now active via Public-Execute URL.

## Source Notes

- [repo] [README](../../../../woodwind/clarinet/README.md) — extensive authority-gate chain: bore-station-plan.csv, tone-hole-authority-plan.csv, reed-mouthpiece-assumptions.csv, leak-pitch-validation-plan.csv, cad-dxf-authority-gates.csv; all currently L1 starter (no measured data). Keywork is explicitly out-of-scope for the first prototype; see keywork-scope.md.
- [repo] [Bore + tone-hole authority plan](../../../../woodwind/clarinet/measured-bore-tonehole-authority-plan.md) — B0 evidence plan defining required bore stations, tone holes, reed/mouthpiece setup, leak/pitch validation, and CAD/DXF gates.

## Design Knowledge

The clarinet is a cylindrical, single-reed, effectively stopped pipe. The acoustic law for the stopped pipe gives:

```text
f_n = (2n-1) * c / (4 * L_eff),  n = 1, 2, 3, ...
```

The fundamental is at ~¼ wavelength (the instrument sounds approximately an octave lower than an open pipe of the same length). It overblows to the 3rd harmonic (a 12th), accessed via the register key on a full clarinet. The first prototype is intentionally keyless, meaning only chalumeau register notes are accessible without overblowing.

Key measurement chain: bore diameter → tone-hole positions → tone-hole diameters → chimney height → closure geometry → reed+mouthpiece setup → leak check → pitch validation.

## Build And Validation Logic

Measurement-first sequence:

1. Measure bore stations (bore-station-plan.csv) on a reference instrument or reference source.
2. Measure tone-hole center, diameter, chimney, and closure (tone-hole-authority-plan.csv).
3. Record reed and mouthpiece geometry (reed-mouthpiece-assumptions.csv).
4. Run same-session leak/pitch validation (reed-mouthpiece-leak-capture-session.csv).
5. Record pitch, response, and correction evidence (leak-pitch-validation-plan.csv).
6. Open CAD/DXF gates with reviewed geometry (cad-dxf-authority-gates.csv).

## Release And Provenance Constraints

No fabrication authority exists. All visual outputs are non-dimensional reference images. No cut, print, drill, or machine operation should be executed from this packet until the full authority-gate chain has measured data.

## Cross-Links

- [[acoustic-classes/single-reed-cylindrical]]
- [[fabrication/bore-and-toneholes]]
- [[synthesis/public-release-blockers]]
- [[synthesis/wolfram-model-patterns]]

## Open Questions

1. Have bore stations been measured per `bore-station-plan.csv`?
2. Have tone-hole centers, diameters, chimneys, and closures been measured per `tone-hole-authority-plan.csv`?
3. Has a reed and mouthpiece been selected and characterized per `reed-mouthpiece-assumptions.csv`?
4. Has the same-session leak/pitch validation loop been run?
5. Have CAD/DXF authority gates been opened with reviewed measured geometry?

## Maintenance Notes

Next ingest should import bore measurement data, tone-hole data, and reed/mouthpiece characterization. Update [[acoustic-classes/single-reed-cylindrical]] and [[synthesis/public-release-blockers]] when B0 evidence plan gates clear.
