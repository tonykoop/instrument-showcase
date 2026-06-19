---
title: Disc Trumpet
slug: disc-trumpet
wiki_type: instrument
status: active
sources:
  - path: ../../../../brass/disc-trumpet/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/cylindrical-bore-brass
  - fabrication/sheet-metal-brass
  - fabrication/rectangular-bore-channel
open_questions:
  - "Do rectangular internal bore channels behave acoustically like equivalent-area cylindrical bores, or do corner modes and cross-section discontinuities introduce tonal artifacts?"
  - "How is the four-turn spiral bore path sealed against leaks at the partition strip braze joints?"
  - "Is the rim-exit bell geometry compatible with a standard bell flare acoustic response?"
  - "No capstone-manifest.json — not yet at V5 build-packet gate."
last_ingest: 2026-06-19
tags: [instrument, brass, trumpet, valved, experimental, disc-body, rectangular-bore, compact]
---

# Disc Trumpet

## Overview

A Bb trumpet-length lip-reed brass instrument folded into a 280 mm diameter × 50 mm thick circular "pancake" body. Two circular brass plates and internal partition strips define a four-turn spiral bore path; three chromatic valves protrude from one edge; the bell exits around the rim. Full Bb trumpet acoustic length (1480 mm) and valve intervals in a radically compact envelope.

- **Family:** lip-reed brass / valved trumpet
- **Acoustic length:** 1480 mm open path
- **Pitch target:** open written C5 sounding concert Bb4 (H4 of 1480 mm tube)
- **Valves:** three chromatic, equal-temperament loop lengths
- **Envelope:** 280 mm diameter × 50 mm thick
- **Mass target:** < 0.9 kg
- **Materials:** yellow brass sheet + bought brass valve hardware
- **Status:** L1 blueprint packet — design and review surface only; no prototype

Primary repo links:
- [README](../../../../brass/disc-trumpet/README.md)
- [Design notes](../../../../brass/disc-trumpet/design.md)
- [Wolfram model](../../../../brass/disc-trumpet/disc-trumpet-starter.wl)
- [Risks](../../../../brass/disc-trumpet/risks.md)
- [Fabrication plan](../../../../brass/disc-trumpet/fabrication-plan.md)

## Current Status

- Release state: L1 packet (V5 migration) — review surface only; no CAD/DXF authority, no prototype.
- Library family: brass.
- Acoustic class: cylindrical bore valved brass (trumpet acoustic length).
- Wolfram state: `.wl` acoustic model present; Wolfram Cloud Public-Execute URL available.
- CAD state: SolidWorks plan described; no confirmed CAD artifacts or `.glb`.
- No `capstone-manifest.json`.

## Source Notes

- [README](../../../../brass/disc-trumpet/README.md) — design thesis (preserve trumpet acoustic length in disc body), targets (1480 mm, 280 mm diameter, < 0.9 kg), packet map.

Artifacts not ingested: `design.md`, `parameters.csv`, `risks.md`, `validation.csv`, `tuning-notes.md`.

## Design Knowledge

The disc body replaces round tubing with a sealed sheet-metal sandwich: two circular plates separated by internal partition strips that define the spiral bore path. The four-turn spiral fits 1480 mm of effective acoustic path into a 280 mm disc. Valve block protrudes from the disc edge; bell exits around the rim perimeter.

The rectangular bore channels are the primary acoustic unknown — corners and cross-section shape can introduce mode distortion vs. an equivalent-area cylindrical bore. The Wolfram model (`.wl`) includes rectangular-bore calculations to assess this risk.

Key design choices vs. a standard Bb trumpet:
- Same acoustic length → same pitch and valve intervals
- Rectangular internal channels → fabrication simplicity vs. acoustic risk
- Rim-exit bell → non-standard flare geometry
- Side-mounted valves → ergonomic departure from standard hand position

## Cross-Links

- [[acoustic-classes/cylindrical-bore-brass]]
- [[fabrication/sheet-metal-brass]]
- [[fabrication/rectangular-bore-channel]]

## Open Questions

1. Do rectangular bore channels behave acoustically like equivalent-area cylindrical bores, or do corner modes introduce tonal artifacts?
2. How is the four-turn spiral bore sealed against leaks at partition strip braze joints?
3. Is the rim-exit bell geometry compatible with a standard bell flare acoustic response?
4. No `capstone-manifest.json` — not yet at V5 build-packet gate.

## Maintenance Notes

First ingest from README only — `design.md` and `risks.md` not yet read. Next pass: read `design.md` for rectangular-bore acoustic analysis and `risks.md` for spiral-seal and corner-mode risk details.
