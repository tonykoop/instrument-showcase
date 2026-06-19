---
title: Brass Marine Reed Horn
slug: brass-marine-reed-horn
wiki_type: instrument
status: active
sources:
  - path: ../../../../brass/brass-marine-reed-horn/README.md
    kind: repo
    last_seen: 2026-06-19
  - path: ../../../../brass/brass-marine-reed-horn/design.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/conical-single-reed
  - fabrication/sheet-metal-brass
  - materials/cane-reed
open_questions:
  - "What mouthpiece equivalent length (allotted 126.8 mm) does the actual reed and facing produce? This is the primary calibration risk."
  - "Do tone-hole chimeney diameters and undercutting yield the target D major scale without excessive half-holing?"
  - "Does the two-turn wrap geometry allow comfortable hand position across all 7 holes?"
  - "No capstone-manifest.json — not yet at V5 build-packet gate."
last_ingest: 2026-06-19
tags: [instrument, brass, reed-wind, conical, single-reed, fingering-holes, compact]
---

# Brass Marine Reed Horn

## Overview

A compact conical brass body driven by a standard Bb-clarinet cane reed, coiled into two tight turns and played with seven open finger holes. Target: low D4 fundamental (~294 Hz), D major fingered octave D4–D5. The "marine" framing reflects the intent: compact, robust, and visually akin to a boat horn rather than a delicate orchestral instrument.

- **Family:** conical single-reed wind / brass sheet-metal hybrid
- **Target tuning:** D4 low note (293.665 Hz), D major scale over 7 tone holes
- **Bore:** linear cone 11.94 mm ID → 25.40 mm ID over 457.2 mm centerline
- **Body:** two-turn brass wrap, ~150 × 120 × 70 mm before mouthpiece
- **Materials:** brass sheet, silver-brazed seams; standard Bb-clarinet cane reed
- **Status:** L1 blueprint — parametric starter model present, measurement required

Primary repo links:
- [README](../../../../brass/brass-marine-reed-horn/README.md)
- [Design notes](../../../../brass/brass-marine-reed-horn/design.md)
- [Tuning notes](../../../../brass/brass-marine-reed-horn/tuning-notes.md)
- [Wolfram model](../../../../brass/brass-marine-reed-horn/brass-marine-reed-horn-starter.wl)
- [Fabrication plan](../../../../brass/brass-marine-reed-horn/fabrication-plan.md)

## Current Status

- Release state: L2 V5 build-packet candidate — private blueprint packet, not fabrication-ready.
- Library family: brass (conical single-reed wind).
- Acoustic class: conical open-pipe reed horn (saxophone-family harmonic behavior).
- Wolfram state: `.wl` starter model present; Wolfram Cloud Public-Execute URL available.
- CAD state: SolidWorks plan and flat-pattern checklist written; no confirmed CAD artifacts or `.glb` yet.
- No `capstone-manifest.json`.

## Source Notes

- [README](../../../../brass/brass-marine-reed-horn/README.md) — packet status, family, target tuning, bore lineage (Round 1 Bb cornet conical strake math), body envelope.
- [design.md](../../../../brass/brass-marine-reed-horn/design.md) — acoustic intent (conical open-pipe approximation, effective length derivation), bore geometry (linear cone), two-turn marine wrap rationale, mouthpiece allowance analysis.

Artifacts not ingested: `parameters.csv`, `tuning-notes.md`, `validation.csv`, `bom.csv`, `fabrication-plan.md`.

## Design Knowledge

The bore behaves as a conical open pipe (like a soprano saxophone cousin), not a closed-pipe clarinet, because the cone supports all harmonics. First-order layout uses:

```
effective_length(note) = c / (2 × frequency)
physical_station = effective_length − mouthpiece_equivalent_length
```

| Note | Freq | Effective length |
|---|---|---|
| D4 (all holes closed) | 293.665 Hz | ~584 mm |
| D5 (all holes open) | 587.330 Hz | ~292 mm |

Physical cone centerline is 457.2 mm; the 126.8 mm gap is the acoustic allowance for mouthpiece, bell lip, and tone-hole chimneys — not a claimed physical mouthpiece length. This allowance must be calibrated against a real reed and facing before any build claim.

The body is formed from rolled sheet-metal frusta (linear cone sections) silver-brazed end-to-end and coiled into two turns. Seven tone holes are biased to the outer arc for two-handed reach.

## Cross-Links

- [[acoustic-classes/conical-single-reed]]
- [[fabrication/sheet-metal-brass]]
- [[materials/cane-reed]]

## Open Questions

1. What mouthpiece equivalent length does the actual reed and facing produce? The 126.8 mm allotment is the primary calibration risk.
2. Do tone-hole chimneys and undercutting yield the target D major scale without excessive half-holing?
3. Does the two-turn wrap allow comfortable hand position across all 7 holes?
4. No `capstone-manifest.json` — not yet at V5 build-packet gate.

## Maintenance Notes

First ingest from README and design.md. Next pass: read `tuning-notes.md` for tone-hole derivation details, `parameters.csv` for full bore table, and `validation.csv` for prototype test gates.
