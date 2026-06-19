---
title: Marimba Blueprint (37-Bar C3–C6, CNC-Cut Padauk)
slug: marimba
wiki_type: instrument
status: active
sources:
  - path: ../../../../idiophones/marimba/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/struck-bar-idiophone
  - instruments/xylophone
  - instruments/glockenspiel
  - instruments/celesta
open_questions:
  - "Have the jig-decision.md fixture gates been validated — specifically which jigs are needed before the full Padauk run?"
  - "What are the measured correction factors for the actual Padauk stock (K, arch depth, node hole spec)?"
  - "What is the resonator tube material — aluminum, PVC, or wood?"
  - "Have pilot bars been cut and measured to validate the workbook K for the actual Padauk lot?"
last_ingest: 2026-06-19
tags: [instrument, idiophone, marimba, 37-bar, C3-C6, padauk, CNC, arch-undercut, resonator, quarter-wave, L2]
---

# Marimba Blueprint — 37-Bar C3–C6, CNC-Cut Padauk

## Overview

A workbook-derived 37-bar C3–C6 marimba packet for CNC-cut Padauk bars with 3D arch undercuts, tuned quarter-wave resonators, and a SolidWorks-ready master-layout handoff. The design turns the existing `marimba-design-table.xlsx` scaffold into a shop-facing documentation set.

- **Family:** idiophone / struck-bar xylophone class
- **Range:** 37 bars, C3 to C6 (3 octaves chromatic)
- **Bars:** African Padauk (primary), arch undercut for partial tuning
- **Resonators:** quarter-wave closed-pipe tubes, one per bar
- **Frame:** CNC-routed, master-layout SolidWorks handoff
- **Model:** `f ≈ K × t / L²` (free-free beam); `L_res ≈ c/(4f) - 0.82 × bore` (quarter-wave resonator)
- **Status:** L2 V5 build-packet candidate — bar schedule, CAD handoffs, and resonator design present; no pilot bars cut yet

Primary repo links:
- [README](../../../../idiophones/marimba/README.md)
- [Design notes](../../../../idiophones/marimba/design.md)
- [Family spec](../../../../idiophones/marimba/family-spec.csv)

## Current Status

- Release state: L2 V5 build-packet candidate. `validation-loop.csv` and `docs/v5-readiness.md` make the V5 promotion boundary explicit. No bar has been cut, struck, mounted, or measured; all pitch values are predictions.
- Library family: idiophone.
- Acoustic class: struck-bar idiophone (orchestral marimba).
- Wolfram state: Wolfram Cloud Public-Execute URL available.
- CAD state: SolidWorks master-layout strategy; `cad/mcp-session-log.md` present. No confirmed `.glb`.

## Source Notes

- [README](../../../../idiophones/marimba/README.md) — 37-bar C3–C6, Padauk bars with arch undercut, quarter-wave resonators, CNC-routed frame, free-free beam model + resonator formula, `jig-decision.md` (fixture gates), pilot-bar protocol.

Artifacts not ingested: `design.md`, `family-spec.csv`, `bom.csv`, `cut-list.csv`, `validation.csv`, `jig-decision.md`.

## Design Knowledge

The marimba bar's arch undercut is the distinguishing feature vs a xylophone: a parabolic or elliptical groove cut into the underside of the bar raises the second mode (first overtone) from its natural ~6.26× ratio to exactly 3× (one octave + fifth) the fundamental. This produces the warm, mellow marimba timbre. The CNC machine's ability to cut a precise arch profile is essential — hand-filing the arch is possible but inconsistent.

Quarter-wave resonators: each bar has a closed-bottom tube (aluminum, PVC, or wood) that reinforces the bar's fundamental by coupling air compression at the tube mouth with the bar's anti-node. Resonator length: `L ≈ c/(4f) - 0.82 × bore`. The resonator does not tune the bar; it adds sustain and loudness by air-coupling.

Padauk (Pterocarpus soyauxii) is preferred for African marimba bars: high specific stiffness (K), good damping ratio, stable grain, attractive orange-red color. However, K varies by stock lot, grain orientation, and moisture content — pilot bars must be cut and measured before the full 37-bar run.

Sister repos: [[instruments/xylophone]] (simpler sibling: no arch undercut, no resonators, higher range), [[instruments/glockenspiel]] (metal bars, no arch undercut, hard mallet).

## Cross-Links

- [[acoustic-classes/struck-bar-idiophone]]
- [[instruments/xylophone]]
- [[instruments/glockenspiel]]
- [[instruments/celesta]]

## Open Questions

1. Have the jig-decision.md fixture gates been validated?
2. What are the measured correction factors for the actual Padauk stock?
3. What resonator tube material — aluminum, PVC, or wood?
4. Have pilot bars been cut and measured to validate workbook K?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for arch-undercut model and `jig-decision.md` for fixture gates. Check `validation.csv` for pilot bar measurement state.
