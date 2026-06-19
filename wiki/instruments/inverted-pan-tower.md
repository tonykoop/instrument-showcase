---
title: Inverted Steel Pan Tower Blueprint
slug: inverted-pan-tower
wiki_type: instrument
status: active
sources:
  - path: ../../../../idiophones/inverted-pan-tower/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - instruments/steel-pan
  - acoustic-classes/tuned-shell-idiophone
  - instruments/spiral-chime-tower
open_questions:
  - "What is the note layout across the 45 tone fields on 5 pans — and is it chromatic, pentatonic, or a custom scale?"
  - "How does the shared interior cavity contribute to bass coupling — Helmholtz mode or something else?"
  - "What is the one-pan mule design — single inverted pan standing alone, with how many note fields?"
  - "How are the 5 pans structurally connected to form a stable 1.2 m tower?"
last_ingest: 2026-06-19
tags: [instrument, idiophone, steel-pan, inverted, tower, 5-pan, 45-note-fields, 1.2m, shared-cavity, L2]
---

# Inverted Steel Pan Tower Blueprint

## Overview

A greenfield idiophone: five inverted 550 mm steel pans stacked into a 1.2 m hollow tower, with 45 tuned note fields across the 5 pans and a shared interior cavity intended to add measurable bass coupling. An inverted pan places the note fields on the concave (inner) face facing downward — playing technique and mallet access differ from conventional steel pan.

- **Family:** idiophone / inverted tuned steel pan tower
- **Pans:** 5, each 550 mm diameter, stacked vertically
- **Note fields:** 45 across the 5 pans
- **Tower height:** 1.2 m
- **Shared cavity:** hollow tower interior — bass coupling hypothesis
- **Status:** L2 V5 build-packet candidate — design and CAD planning only; one-pan mule, rim-flange coupon, nitriding pitch-shift coupon, tower stability test, and spectrum validation all pending

Primary repo links:
- [README](../../../../idiophones/inverted-pan-tower/README.md)
- [Design notes](../../../../idiophones/inverted-pan-tower/design.md)
- [Parameters](../../../../idiophones/inverted-pan-tower/parameters.csv)
- [Wolfram starter](../../../../idiophones/inverted-pan-tower/inverted-pan-tower-starter.wl)

## Current Status

- Release state: L2 V5 build-packet candidate — v0.1.0 blueprint. Not fabrication-ready until one-pan mule, rim-flange coupon, nitriding pitch-shift coupon, tower stability test, and spectrum validation pass.
- Library family: idiophone.
- Acoustic class: tuned shell idiophone (inverted steel pan tower).
- Wolfram state: first-order plate/cavity calculations (`.wl`) present; Wolfram Cloud Public-Execute URL available.
- CAD state: SolidWorks plan defined; no confirmed `.glb`.

## Source Notes

- [README](../../../../idiophones/inverted-pan-tower/README.md) — instrument concept (5 inverted 550 mm pans, 45 note fields, 1.2 m tower, shared cavity), validation gates (one-pan mule first), packet map.

Artifacts not ingested: `design.md`, `parameters.csv`, `fabrication-plan.md`, `validation.csv`, `risks.md`.

## Design Knowledge

The inverted pan configuration: instead of playing on the convex top surface (conventional steel pan), the pans are flipped so the note fields are on the concave side facing upward (or inward in the tower). Inverted pans produce a different radiation pattern — the concave surface focuses sound slightly inward rather than outward.

The shared interior cavity is a novel design element: the hollow tower formed by the stacked pans may function as a coupled acoustic resonator for the lower note fields, similar to the Gu port on a handpan. Whether this produces measurable pitch enhancement or bass warmth is an empirical question (a tower stability and spectrum validation gate).

45 note fields across 5 pans averages 9 fields per pan — a full steel-pan density. The note layout must account for cross-field coupling (adjacent tone fields on the same pan should be non-adjacent in pitch to minimize sympathetic resonance).

Related: [[instruments/steel-pan]] (conventional upright steel pan, same tuned-dimple idiophone class), [[instruments/spiral-chime-tower]] (different tower format, brass chime petals on a 1.2 m spine).

## Cross-Links

- [[instruments/steel-pan]]
- [[acoustic-classes/tuned-shell-idiophone]]
- [[instruments/spiral-chime-tower]]

## Open Questions

1. What is the 45-note field layout across 5 pans — chromatic, pentatonic, or custom scale?
2. How does the shared interior cavity contribute to bass coupling?
3. What is the one-pan mule design?
4. How are the 5 pans structurally connected for a stable 1.2 m tower?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for note layout and cavity coupling model, `inverted-pan-tower-starter.wl` for plate/cavity calculations.
