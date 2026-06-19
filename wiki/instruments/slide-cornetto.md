---
title: Slide Cornetto
slug: slide-cornetto
wiki_type: instrument
status: active
sources:
  - path: ../../../../brass/slide-cornetto/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/conical-bore-brass
  - fabrication/sheet-metal-brass
open_questions:
  - "What is the effective acoustic length per slide position, and does the short slide range cover enough semitones for chromatic playing?"
  - "Do the 30 mm smoothing collars at the slide receiver prevent air turbulence at the cylindrical-to-conical bore transition?"
  - "Is bought slide tubing available at the target bore diameter for a conical instrument?"
  - "No capstone-manifest.json — not yet at V5 build-packet gate."
last_ingest: 2026-06-19
tags: [instrument, brass, cornetto, slide, conical-bore, compact, historical-hybrid]
---

# Slide Cornetto

## Overview

A Bb slide cornetto: a conical-bore brass instrument with a short cylindrical trombone-style slide, shallow cornet mouthpiece, 30 mm smoothing collars at the slide receiver, and a compact 4 in bell. Combines the conical bore acoustic character of a cornetto with a slide pitch mechanism instead of finger holes or valves.

- **Family:** brass / conical bore slide instrument
- **Tuning:** Bb
- **Bore:** conical throughout; cylindrical slide section with smoothing collars
- **Slide:** trombone-style short slide for chromatic pitch access
- **Bell:** compact 4 in
- **Mouthpiece:** shallow cornet/cornetto style
- **Status:** L2 V5 blueprint — design and CAD planning authority only; no prototype

Primary repo links:
- [README](../../../../brass/slide-cornetto/README.md)
- [Design notes](../../../../brass/slide-cornetto/design.md)
- [Wolfram model](../../../../brass/slide-cornetto/slide-cornetto-starter.wl)
- [Risks](../../../../brass/slide-cornetto/risks.md)
- [Fabrication plan](../../../../brass/slide-cornetto/fabrication-plan.md)

## Current Status

- Release state: L2 V5 build-packet candidate — design and CAD planning; not fabrication-ready until bought slide tubes, mouthpiece receiver, collars, and bell tooling are measured and CAD/DXF reviewed.
- Library family: brass.
- Wolfram state: first-order acoustic model (`.wl`) present; Wolfram Cloud Public-Execute URL available.
- CAD state: SolidWorks plan described; no confirmed `.glb`.
- No `capstone-manifest.json`.

## Source Notes

- [README](../../../../brass/slide-cornetto/README.md) — instrument description, slide design elements (30 mm smoothing collars, trombone-style), packet map, readiness boundary.

Artifacts not ingested: `design.md`, `parameters.csv`, `risks.md`, `validation.csv`, `tuning-notes.md`.

## Design Knowledge

The instrument is a hybrid: conical bore acoustic character (cornetto/flugelhorn-like mellow response) combined with a slide mechanism for pitch access instead of finger holes or piston valves. The slide section is cylindrical (bought drawn tubing) transitioning to the conical bore via 30 mm smoothing collars — the collars reduce air turbulence at the cylindrical-to-conical transition, which is a known acoustic risk.

The Wolfram model covers first-order acoustic prediction and slide-extension calculations. Validation gates (per `validation-checklist.md`) include measured bore stations, coupon tests, and slide friction checks before any fabrication claim.

## Cross-Links

- [[acoustic-classes/conical-bore-brass]]
- [[fabrication/sheet-metal-brass]]

## Open Questions

1. What is the effective acoustic length per slide position, and does the short slide cover enough semitones for chromatic playing?
2. Do the 30 mm smoothing collars prevent air turbulence at the cylindrical-to-conical bore transition?
3. Is bought slide tubing available at the target bore diameter for a conical instrument?
4. No `capstone-manifest.json` — not yet at V5 build-packet gate.

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for bore station table and slide-position math, `risks.md` for collar-transition risk, and `validation.csv` for slide-friction and pitch measurement gates.
