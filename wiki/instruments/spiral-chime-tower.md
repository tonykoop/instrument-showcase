---
title: Spiral Chime Tower Blueprint (24-Note Chromatic Fibonacci Helix)
slug: spiral-chime-tower
wiki_type: instrument
status: active
sources:
  - path: ../../../../idiophones/spiral-chime-tower/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/struck-bar-idiophone
  - instruments/tubular-bells
  - instruments/inverted-pan-tower
  - instruments/wind-chimes
open_questions:
  - "How is each brass petal suspended at its nodes — wire through drilled holes, or a washer-stack bracket?"
  - "What is the Fibonacci helix angular step — and how many turns over the 1.2 m spine?"
  - "Have the coupon petals (C4, A4, B5) been formed, mounted, and measured?"
  - "What is the steel spine attachment method for each petal bracket?"
last_ingest: 2026-06-19
tags: [instrument, idiophone, chime, tower, 24-note, chromatic, C4-B5, brass-petal, fibonacci-helix, 1.2m, L2]
---

# Spiral Chime Tower Blueprint — 24-Note Chromatic Fibonacci Helix

## Overview

A Round 4 idiophone blueprint: a 1.2 m vertical chime tower with 24 C26800 brass petals arranged around a 30 mm OD 1018 steel spine in a Fibonacci helix. Each petal is a nodally supported sheet-metal chime targeted to the chromatic 2-octave set C4–B5 (A4 = 440 Hz). An optional 25th crown note (C6) is noted for future extension.

- **Family:** idiophone / vertical chime tower
- **Petals:** 24 C26800 (yellow brass) sheet-metal chimes, 1.5 mm
- **Layout:** Fibonacci helix on 30 mm OD 1018 steel spine, 1.2 m total height
- **Brackets:** 1.5 mm C26800 brass brackets at each spine attachment
- **Range:** chromatic C4–B5 (24 notes, 2 octaves)
- **Tuning model:** free-free metal beam (same as glockenspiel bars)
- **Status:** L2 V5 build-packet candidate — blueprint; coupon validation required before fabrication release

Primary repo links:
- [README](../../../../idiophones/spiral-chime-tower/README.md)
- [Design notes](../../../../idiophones/spiral-chime-tower/design.md)
- [Wolfram starter](../../../../idiophones/spiral-chime-tower/spiral-chime-tower-starter.wl)

## Current Status

- Release state: L2 V5 build-packet candidate. V5 boundary: CAD, DXF, CNC, and tuning authority remain `pending_measurement` until SolidWorks rebuild evidence, coupon measurements, and reviewed exports exist.
- Library family: idiophone.
- Acoustic class: struck-bar idiophone (sheet-metal petal chimes on a tower).
- Wolfram state: first-order free-free brass petal model present; Wolfram Cloud Public-Execute URL available.
- CAD state: SolidWorks plan defined; no confirmed `.glb`.

## Source Notes

- [README](../../../../idiophones/spiral-chime-tower/README.md) — 24 C26800 brass petals, Fibonacci helix on 30 mm steel spine, 1.2 m height, chromatic C4–B5, 1.5 mm brass, coupon sequence (C4, A4, B5 first — full production tower only after corrections).

Artifacts not ingested: `design.md`, `parameters.csv`, `fabrication-plan.md`, `validation.csv`.

## Design Knowledge

The chime petals are free-free metal beams — same physics as glockenspiel bars but in a vertical tower format. Petal shape (rectangular, curved, or trapezoidal) and cross-section determine the frequency; a rectangular petal follows `f ≈ K × t / L²`. The 1.5 mm brass thickness gives good sustain and tone quality in the C4–B5 range.

The Fibonacci helix arrangement provides two aesthetic benefits: (1) no two adjacent angular positions share a petal, so mallet access to any petal is unobstructed from one direction; (2) the spiral phyllotaxis creates the visual signature of the instrument. Each petal is mounted on a bracket bolted to the steel spine at its computed angular position along the helix.

Node-hole suspension: each petal is mounted at its nodes (22.4% and 77.6% of length from each end) using a wire or washer stack — same approach as glockenspiel bars. Rigid mounting at non-node points dramatically damps the fundamental.

The coupon sequence: cut C4, A4, and B5 petals, form to the target curl geometry, mount with the real washer stack, and measure pitch and sustain. Only after corrections validated against the coupon data should production DXFs be treated as fabrication authority.

Related: [[instruments/tubular-bells]] (similar vertical tower format, hollow tube rather than petal), [[instruments/wind-chimes]] (outdoor pentatonic/modal version in the same instrument class), [[instruments/inverted-pan-tower]] (tower format, different pan/note-field idiophone class).

## Cross-Links

- [[acoustic-classes/struck-bar-idiophone]]
- [[instruments/tubular-bells]]
- [[instruments/inverted-pan-tower]]
- [[instruments/wind-chimes]]

## Open Questions

1. How is each brass petal suspended at its nodes?
2. What is the Fibonacci helix angular step — how many turns over 1.2 m?
3. Have the C4, A4, B5 coupon petals been formed, mounted, and measured?
4. What is the steel spine petal-bracket attachment method?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for petal geometry and Fibonacci helix layout, `spiral-chime-tower-starter.wl` for free-free brass petal model.
