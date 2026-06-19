---
title: Bell-Stack Chord Horn
slug: bell-stack-chord-horn
wiki_type: instrument
status: active
sources:
  - path: ../../../../brass/bell-stack-chord-horn/README.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../../brass/bell-stack-chord-horn/design.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../../brass/bell-stack-chord-horn/risks.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/bessel-flare-horn
  - synthesis/chord-radiation-brass
  - fabrication/sheet-metal-brass
open_questions:
  - "Does the three-bell nested configuration actually produce three discrete spectral peaks, or does inter-bell cross-talk smear them into a thick timbre? (Risk A-1)"
  - "Can a standard lip-reed drive the modified three-bell impedance profile? (Risk A-2)"
  - "Do the DXF flat patterns account for the compound-curvature seams on nested Bessel bells?"
  - "No capstone-manifest.json present — has the repo reached V5 build-packet gate yet?"
last_ingest: 2026-06-19
tags: [instrument, brass, experimental, chord-horn, bessel-flare, no-valves]
---

# Bell-Stack Chord Horn

## Overview

An experimental single-mouthpiece brass instrument that radiates a **Bb major triad from a single buzzed note** by stacking three concentric Bessel-flare bells along the same axis. Each bell is tuned (via its Bessel γ exponent) to selectively reinforce one harmonic of the pedal Bb2 fundamental: H1 (Bb root), H3 (F perfect 12th = 5th pitch-class), H5 (D major 17th = 3rd pitch-class). The result is a wide-voicing Bb–F–D chord audible from one embouchure, no valves, no ensemble.

- **Family:** brass (single-mouthpiece, no valves)
- **Tuning:** A4 = 440 Hz; pedal Bb2 = 116.54 Hz; playable register Bb3
- **Acoustic length:** 1500 mm (Bb tenor scale)
- **Bells:** 4" / 5" / 6" mouths; Bessel γ = 0.85 / 0.55 / 0.35
- **Materials:** yellow brass CDA 260, silver-brazed seams
- **Status:** v0.1.0-blueprint — first-principles design, no prototype built

Primary repo links:
- [README](../../../../brass/bell-stack-chord-horn/README.md)
- [Design notes](../../../../brass/bell-stack-chord-horn/design.md)
- [Risks](../../../../brass/bell-stack-chord-horn/risks.md)
- [Fabrication plan](../../../../brass/bell-stack-chord-horn/fabrication-plan.md)
- [Assembly manual](../../../../brass/bell-stack-chord-horn/assembly-manual.md)
- [Wolfram model](../../../../brass/bell-stack-chord-horn/bell-stack-chord-horn-starter.wl)

## Current Status

- Release state: v0.1.0-blueprint — no prototype built, all acoustic values are predictions.
- Library family: brass.
- Acoustic class: Bessel-flare multi-bell chord horn.
- Wolfram state: `.wl` first-principles impedance model present; Wolfram Cloud Public-Execute URL available.
- CAD state: SolidWorks plan and DXF flat-pattern checklist written; no confirmed CAD artifacts or `.glb` yet.
- No `capstone-manifest.json` — not yet at V5 build-packet gate.

## Source Notes

- [README](../../../../brass/bell-stack-chord-horn/README.md) — overview, design thesis, file map, quickstart for a builder, BOM cost estimate (~$437).
- [design.md](../../../../brass/bell-stack-chord-horn/design.md) — parametric model: Bessel horn cutoff derivation, harmonic series table, nested-bell geometry, γ-value selection rationale, inter-bell annular-gap coupling analysis.
- [risks.md](../../../../brass/bell-stack-chord-horn/risks.md) — failure modes across acoustic, structural, ergonomic, supply, and manufacturability categories; each risk has a verification test attached.

Artifacts not ingested in this pass:
- `parameters.csv`, `bend-table.csv`, `cut-list.csv`, `bom.csv`, `sourcing.csv`
- `bell-stack-chord-horn-starter.wl` (Wolfram impedance model)
- `solidworks-plan.md`, `flat-pattern-checklist.md`
- `fabrication-plan.md`, `assembly-manual.md`
- `tuning-notes.md`, `validation.csv`

## Design Knowledge

The bore runs: cylindrical leadpipe → conical main tube → 3 nested Bessel-flare bells at the terminus. The acoustic standing-wave harmonics fall at:

| Harmonic | Frequency | Note | Bell target |
|---|---|---|---|
| H1 | 116.54 Hz | Bb2 (pedal) | 6" bell, γ = 0.35 |
| H2 | 233.08 Hz | Bb3 (normal register) | reflected / suppressed |
| H3 | 349.62 Hz | F4 | 5" bell, γ = 0.55 |
| H4 | 466.16 Hz | Bb4 | reflected / suppressed |
| H5 | 582.70 Hz | D5 | 4" bell, γ = 0.85 |

Each Bessel bell has a cutoff frequency `f_c ≈ (c / 2π) · γ / r_mouth`. Above cutoff the bell radiates; below it reflects. Setting the three bells' cutoffs to bracket H1, H3, H5 respectively should suppress the intermediate even harmonics and make the chord audible.

The instrument is valveless — the player gets one chord (and its register variants by embouchure). It is an acoustic-exploration instrument, not a chromatic brass for repertoire.

## Fabrication Path

Brass CDA 260 sheet metal, silver-brazed seams. Each bell's curved surface requires a lofted flat pattern developed via DXF export from SolidWorks. The nested assembly requires careful inter-bell spacing to minimize acoustic cross-talk (risk A-1). A CNC plasma nesting plan is in `cnc/`. Coupon bend tests (per `flat-pattern-checklist.md`) are required before production cutting.

## Risks And Release Constraints

Three highest-leverage risks:
1. **A-1 Spectral smear** — nested bells may not produce three discrete radiated peaks; inter-bell cross-talk could blend harmonics. Mitigation: felt/O-ring gaskets at annular gaps, or γ re-tuning.
2. **A-2 Lip-reed coupling** — the modified impedance may lack sufficient peak Q for the player's lip-reed to lock onto. Verification: sustained pedal Bb2, on-axis spectrum, peaks ≥ 6 dB above adjacent harmonics.
3. **M-x Nested-bell assembly tolerance** — three concentric bells with brazed seams require tight coaxial alignment. Tolerance stack-up plan needed before first braze.

## Cross-Links

- [[acoustic-classes/bessel-flare-horn]]
- [[synthesis/chord-radiation-brass]]
- [[fabrication/sheet-metal-brass]]

## Open Questions

1. Does the three-bell nested configuration produce three discrete spectral peaks, or does inter-bell cross-talk smear them into a thick timbre? (Risk A-1)
2. Can a standard lip-reed drive the modified three-bell impedance profile reliably? (Risk A-2)
3. Do the DXF flat patterns account for compound-curvature seams on nested Bessel bells?
4. No `capstone-manifest.json` present — has the repo reached V5 build-packet gate?

## Maintenance Notes

First ingest from README, design.md, risks.md. Next pass: read `parameters.csv`, `validation.csv`, `solidworks-plan.md`, and the `.wl` Wolfram model for deeper acoustic parameter extraction. After first prototype, update status and file actual spectral measurements.
