---
title: Frame Drum (Multi-Tradition R&D)
slug: frame-drum
wiki_type: instrument
status: active
sources:
  - path: ../../../../percussion/frame-drum/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/frame-drum
  - fabrication/bent-wood-hoop
  - instruments/bowed-frame-drum
  - instruments/bass-surface-drum
open_questions:
  - "Which traditions / instruments does this repo cover (bodhran, tar, riq, bendir, pandeiro, shamanic frame drum)?"
  - "What are the distinct design variants — shell material (bent wood, sheet metal, steam-bent), head attachment (laced, glued, hoop), and shell depth?"
  - "Is this an R&D-only structural repo or does it contain buildable designs?"
  - "What is the head-to-shell depth ratio targeted — shallow (bodhran) or medium (pandeiro)?"
last_ingest: 2026-06-19
tags: [instrument, drum, frame-drum, multi-tradition, r-and-d, bodhran, riq, tar, bendir]
---

# Frame Drum — Multi-Tradition R&D

## Overview

A research and development repository covering frame drum designs across multiple world music traditions. Frame drums share a common architectural pattern: a shallow shell (depth much less than head diameter) with a single or double membrane, but differ widely in size, head material, depth ratio, internal jingle or snare fittings, and playing technique.

- **Family:** membranophone / frame drum
- **Scope:** multi-tradition — bodhran, tar, riq, bendir, pandeiro, shamanic and other traditions covered
- **Status:** R&D structural repo; multiple design variants documented

Primary repo links:
- [README](../../../../percussion/frame-drum/README.md)
- [Design notes](../../../../percussion/frame-drum/design.md)

## Current Status

- Release state: R&D packet; tradition coverage and buildable design status TBD on next pass.
- Library family: drum.
- Acoustic class: frame drum (shallow single-headed or double-headed membrane).
- CAD state: geometry variants defined; no confirmed `.glb`.

## Source Notes

- [README](../../../../percussion/frame-drum/README.md) — multi-tradition frame drum scope, design variants (shell material, head attachment, depth), R&D structure.

Artifacts not ingested: `design.md`, any tradition-specific sub-folders, `bom.csv`.

## Design Knowledge

Frame drums are acoustically dominated by the membrane: because the shell is shallow, body resonance contributes little — the drum radiates primarily as a piston membrane. This makes head selection (thickness, surface density, tensioning) the most critical design parameter.

Shell construction varies by tradition:
- **Bent/steam-bent wood hoops**: traditional for bodhran (Irish), tar (Middle Eastern), many shamanic drums
- **Sheet-metal rings**: lower cost, dimensionally stable, suits the sprint-shop method
- **Multi-layer plywood / MDF**: even, smooth bearing edge at low cost

Depth-to-diameter ratio sets the Helmholtz-like body resonance: shallower frames (bodhran-like) produce a drier, more direct membrane tone; medium-depth frames (pandeiro-scale) allow more shell coupling and jingle integration.

Related: [[instruments/bowed-frame-drum]] (CR-steel frame, specialized bowed-drone variant), [[instruments/bass-surface-drum]] (large-diameter extreme of the frame-drum class).

## Cross-Links

- [[acoustic-classes/frame-drum]]
- [[fabrication/bent-wood-hoop]]
- [[instruments/bowed-frame-drum]]
- [[instruments/bass-surface-drum]]

## Open Questions

1. Which specific traditions / instruments are covered in this repo?
2. What are the distinct design variants (shell material, head attachment, depth)?
3. Is this R&D only or does it contain buildable designs?
4. What depth-to-diameter ratios are targeted?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for tradition coverage and variant specifications; check for sub-folders per tradition (bodhran/, tar/, etc.).
