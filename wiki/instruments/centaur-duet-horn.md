---
title: Centaur Duet Horn
slug: centaur-duet-horn
wiki_type: instrument
status: active
sources:
  - path: ../../../../brass/centaur-duet-horn/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/natural-brass-harmonic-series
  - fabrication/sheet-metal-brass
  - fabrication/y-junction-manifold
open_questions:
  - "What is the acoustic impedance discontinuity at the 2-into-1 Y-junction, and does it cause audible reflections or pitch wobble?"
  - "Can two independent lip-reeds synchronize reliably through a shared bore — is the ensemble effect controllable?"
  - "When one mouthpiece is capped, how much drone enhancement does the closed chamber provide and at what frequencies?"
  - "No capstone-manifest.json — not yet at V5 build-packet gate."
last_ingest: 2026-06-19
tags: [instrument, brass, duet, natural-horn, experimental, two-player, y-junction]
---

# Centaur Duet Horn

## Overview

A single-body brass instrument with two mouthpieces converging at a precision-brazed Y-junction into a shared main tube and forward-facing bell. Two players stand side-by-side, each holding one Bach 7C mouthpiece. Playing simultaneously produces chorus and beating effects impossible on a conventional horn. Single-player mode: cap one mouthpiece and use the closed tube as a resonating drone chamber.

- **Family:** brass / natural horn
- **Target tuning:** Bb2 fundamental (116.54 Hz); harmonic series H2–H8 playable
- **Acoustic length:** ~1500 mm (Bb tenor range)
- **Bell:** 5" forward-facing
- **Materials:** 0.030" yellow brass throughout; 0.035" at Y-junction body
- **Status:** L2 planning packet — acoustic notes and fabrication plans reviewable; no CAD, no prototype

Primary repo links:
- [README](../../../../brass/centaur-duet-horn/README.md)
- [Design notes](../../../../brass/centaur-duet-horn/design.md)
- [Wolfram model](../../../../brass/centaur-duet-horn/centaur-duet-horn-starter.wl)
- [Fabrication plan](../../../../brass/centaur-duet-horn/fabrication-plan.md)
- [Risks](../../../../brass/centaur-duet-horn/risks.md)

## Current Status

- Release state: L2 planning packet — design tables and acoustic notes reviewable; no reviewed CAD/DXF or measured validation.
- Library family: brass.
- Acoustic class: natural horn / harmonic-series brass.
- Wolfram state: transfer-matrix acoustic model (`.wl`) present; Wolfram Cloud Public-Execute URL available.
- CAD state: SolidWorks plan and drawings folder present as placeholders; no confirmed `.glb`.
- No `capstone-manifest.json`.

## Source Notes

- [README](../../../../brass/centaur-duet-horn/README.md) — design thesis (two-mouthpiece converging Y-junction, shared bore, forward bell), target tuning, repository layout, V5 readiness statement, ergonomic intent (side-by-side players).

Artifacts not ingested: `design.md`, `parameters.csv`, `validation.csv`, `risks.md`, `tuning-notes.md`, `bom.csv`, `fabrication-plan.md`.

## Design Knowledge

The defining fabrication challenge is the 2-into-1 Y-manifold: a stub-in-cylinder assembly with area-matched bores to minimize acoustic impedance discontinuity at the junction. Both mouthpipe bores enter the manifold and must merge smoothly into the shared main tube bore without an abrupt step.

Two playing modes:
1. **Duet mode** — both players buzz simultaneously; the shared bore mixes the two lip-reed signals. Controlled chorus and beating from small pitch offsets are the intended effect.
2. **Drone mode** — one mouthpiece capped; the closed tube acts as a coupled resonating chamber adding harmonic color to the other player's solo line.

## Cross-Links

- [[acoustic-classes/natural-brass-harmonic-series]]
- [[fabrication/sheet-metal-brass]]
- [[fabrication/y-junction-manifold]]

## Open Questions

1. What is the acoustic impedance discontinuity at the Y-junction, and does it cause audible reflections or pitch wobble?
2. Can two independent lip-reeds synchronize reliably through the shared bore?
3. When one mouthpiece is capped, how much drone enhancement does the closed chamber provide?
4. No `capstone-manifest.json` — not yet at V5 build-packet gate.

## Maintenance Notes

First ingest from README only — design.md, risks.md, and tuning-notes.md not yet read. Next pass: read `design.md` for Y-junction acoustic model and `risks.md` for lip-reed synchronization and junction-leak risk details.
