---
title: Glockenspiel Blueprint (25-Bar Chromatic C5–C7)
slug: glockenspiel
wiki_type: instrument
status: active
sources:
  - path: ../../../../idiophones/glockenspiel/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/struck-bar-idiophone
  - instruments/xylophone
  - instruments/marimba
  - instruments/tubular-bells
open_questions:
  - "What are the three pilot bar results (C5, A5, C7) — has the effective K been back-solved from real stock?"
  - "What grommet durometer was selected for the cord/grommet node suspension?"
  - "Has a 10-bar pentatonic art-fair variant been built and demonstrated?"
  - "What mallet hardness is recommended for the C5–C7 aluminum bar set?"
last_ingest: 2026-06-19
tags: [instrument, idiophone, glockenspiel, metallophone, 25-bar, chromatic, C5-C7, aluminum, walnut-frame, L2]
---

# Glockenspiel Blueprint — 25-Bar Chromatic C5–C7

## Overview

A V5 L2 build-packet candidate for a 25-bar chromatic glockenspiel (metallophone), C5 to C7, in 6061-T6 aluminum flat bars on a CNC-routed walnut frame with cord-and-grommet free-free suspension. A 10-bar C-major pentatonic art-fair variant is included for short workshop or retail builds.

- **Family:** idiophone / struck-bar metallophone
- **Range:** 25 chromatic bars, C5 to C7; 10-bar pentatonic variant (C-major)
- **Bars:** 6061-T6 aluminum, 0.250 in × 1.000 in cross-section
- **Frame:** CNC-routed black walnut, piano-keyboard layout (naturals forward, sharps raised)
- **Suspension:** cord/paracord + rubber grommets at node points (22.4% and 77.6% of bar length)
- **Model:** `f ≈ K × t / L²` (free-free beam, first flexural mode)
- **Status:** L2 V5 build-packet candidate — bar schedule, frame plan, and CAD handoffs present; no pilot bars cut or measured yet

Primary repo links:
- [README](../../../../idiophones/glockenspiel/README.md)
- [Design notes](../../../../idiophones/glockenspiel/design.md)

## Current Status

- Release state: L2 V5 build-packet candidate. First physical pass: cut 3 pilot bars (C5, A5, C7) to back-solve effective K for the actual stock lot.
- Library family: idiophone.
- Acoustic class: struck-bar idiophone (metallophone — aluminum bars).
- Wolfram state: Wolfram Cloud Public-Execute URL available.
- CAD state: SolidWorks/CNC frame plan; `capstone-manifest.json` present; no confirmed `.glb`.

## Source Notes

- [README](../../../../idiophones/glockenspiel/README.md) — 25-bar C5–C7 + 10-bar pentatonic variant, aluminum bars (0.25 × 1 in), walnut frame (piano layout), node suspension, free-free beam model, pilot-bar protocol (C5, A5, C7 first; measure; update full family schedule).

Artifacts not ingested: `design.md`, `family-spec.csv`, `bom.csv`, `cut-list.csv`, `validation.csv`.

## Design Knowledge

The glockenspiel bar obeys the free-free Euler-Bernoulli beam formula: `f ≈ K × t / L²`. Length is the dominant pitch variable; thickness is a secondary lever and also affects loudness and tone character. Node holes at 22.4% and 77.6% of bar length allow mounting without acoustic damping of the fundamental.

Glockenspiel bars have no undercut (unlike marimba bars which have a parabolic arch undercut to tune the second mode). The second mode is left to speak naturally — its ~6.26× relationship to the fundamental is audible as a high partial and characteristic of the glockenspiel's bright timbre.

Aluminum is lighter and cheaper than brass for this range (C5–C7); at shorter lengths the bars are easily handled and tuned. 6061-T6 has a consistent E and density, making the K value more predictable than softer alloys. The pilot-bar protocol (cut 3 bars, measure Hz, back-solve effective K for the actual stock lot) is the correct way to account for stock-lot variation before cutting all 25 bars.

Sister repos: [[instruments/xylophone]] (same physics, wooden bars, no resonators), [[instruments/marimba]] (wooden bars with parabolic undercut and matched resonators), [[instruments/tubular-bells]] (same chromatic target range approach, hollow tube geometry).

## Cross-Links

- [[acoustic-classes/struck-bar-idiophone]]
- [[instruments/xylophone]]
- [[instruments/marimba]]
- [[instruments/tubular-bells]]

## Open Questions

1. Have the three pilot bars (C5, A5, C7) been cut and measured — and what was the back-solved K?
2. What grommet durometer was selected?
3. Has the 10-bar pentatonic art-fair variant been built?
4. What mallet hardness is recommended?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for bar schedule and `family-spec.csv` for the full 25-bar table. Check `validation.csv` for pilot bar measurements.
