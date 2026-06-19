---
title: Mute-Tuned Natural Horn
slug: mute-tuned-natural-horn
wiki_type: instrument
status: active
sources:
  - path: ../../../../brass/mute-tuned-natural-horn/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/natural-brass-harmonic-series
  - fabrication/sheet-metal-brass
  - fabrication/hammer-forming
open_questions:
  - "What precision of cone-mute seating is required to achieve ±10 cent pitch accuracy at harmonic 4?"
  - "How are the five mutes (F, E, Eb, D, C) stored and swapped mid-performance without noise or delay?"
  - "What material and surface treatment prevents cone-mute oxidation and maintains consistent seating force?"
  - "No capstone-manifest.json — not yet at V5 build-packet gate."
last_ingest: 2026-06-19
tags: [instrument, brass, natural-horn, mutes, cone-mute, circular-coil, tunable]
---

# Mute-Tuned Natural Horn

## Overview

A compact brass natural horn with a fixed 3700 mm body coiled into a 350 mm OD circular form, retuned via five precisely seated internal bell-throat cone mutes. Each mute is hammer-formed and planished like a small handpan tuning field. Swapping mutes selects among five keys: F, E, Eb, D, and C — the core transpositions of the classical natural horn repertoire.

- **Family:** lip-buzzed brass / natural horn
- **Body:** 3700 mm centerline, 350 mm OD coil, 305 mm bell rim
- **Mutes:** F, E, Eb, D, C (removable cone mutes seated in bell throat)
- **Validation target:** harmonic 4 within ±10 cents per mute
- **Status:** v0.1.0 blueprint — F/E are core targets; Eb/D/C require prototype evidence

Primary repo links:
- [README](../../../../brass/mute-tuned-natural-horn/README.md)
- [Design notes](../../../../brass/mute-tuned-natural-horn/design.md)
- [Fabrication plan](../../../../brass/mute-tuned-natural-horn/fabrication-plan.md)

## Current Status

- Release state: L2 V5 build-packet candidate — v0.1.0 blueprint; F and E mute targets are core, Eb/D/C require measured prototype evidence.
- Library family: brass.
- Wolfram state: Wolfram Cloud Public-Execute URL available.
- CAD state: SolidWorks plan present; no confirmed `.glb`.
- No `capstone-manifest.json`.

## Source Notes

- [README](../../../../brass/mute-tuned-natural-horn/README.md) — thesis (fixed body + five mutes for key retuning), targets (body dimensions, mute keys, ±10 cent validation), packet map.

Artifacts not ingested: `design.md`, `parameters.csv`, `validation.csv`.

## Design Knowledge

The body is a fixed brass coil — once formed, pitch retuning is achieved entirely through the inserted cone mute in the bell throat, not via tuning slides or crooks. Each mute is shaped like a small handpan tuning field: hammer to rough profile, anneal, planish flat, trim the cone, seat in the bell throat, measure harmonic 4, and repeat until within ±10 cents.

The mute shortens the effective acoustic length slightly and adds damping; the precise seating depth determines the pitch offset. Five mutes span the interval from F down to C — roughly four semitones. This covers the core natural horn repertoire keys without full crook sets.

Mute forming procedure (per README): hammer → anneal → planish → trim → seat → measure harmonic 4 → iterate.

## Cross-Links

- [[acoustic-classes/natural-brass-harmonic-series]]
- [[fabrication/sheet-metal-brass]]
- [[fabrication/hammer-forming]]

## Open Questions

1. What cone-mute seating precision is required for ±10 cent pitch accuracy at harmonic 4?
2. How are five mutes stored and swapped mid-performance?
3. What material/surface treatment prevents oxidation and maintains consistent seating force?
4. No `capstone-manifest.json` — not yet at V5 build-packet gate.

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for acoustic mute model and seating geometry, and `validation.csv` for per-mute pitch measurement gates.
