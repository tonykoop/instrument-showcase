---
title: Copper C Serpent — Sheet-Metal Packet
slug: serpent-sheet-metal-packet
wiki_type: instrument
status: active
sources:
  - path: ../../../../brass/serpent-sheet-metal-packet/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/conical-bore-brass
  - fabrication/sheet-metal-brass
  - fabrication/raised-hammered-shell
open_questions:
  - "What are the measured bore stations from the Lander reference instrument? The packet notes critical dimensions require measured drawings or reviewed CAD before metal is cut."
  - "bom.csv and sourcing.csv are missing — blocking L2 promotion."
  - "How is the double-S body path formed from copper sheet without losing bore continuity at the bends?"
  - "What finger-hole placement (six or seven holes, keys?) does this serpent variant use?"
last_ingest: 2026-06-19
tags: [instrument, brass, serpent, historical, copper, hammer-formed, double-s, finger-holes]
---

# Copper C Serpent — Sheet-Metal Packet

## Overview

A provisional design and fabrication packet for a sheet-metal musical serpent inspired by the William Lander C serpent (ca. 1820–1825). The body follows a double-S path formed from copper raised/hammered shell sections; the bell uses segmented conical sections suited to SolidWorks Lofted Bend. An L1 concept packet — design intent and reference dimensions captured for private review.

- **Family:** conical bore brass / historical woodwind-brass hybrid
- **Reference:** William Lander C serpent, ca. 1820–1825
- **Body:** double-S path, copper raised/hammered shell assembly
- **Bell:** segmented conical sections (lofted-bend approach)
- **Status:** L1 concept packet — not build-certified; critical dimensions require measured drawings

Primary repo links:
- [README](../../../../brass/serpent-sheet-metal-packet/README.md)
- [Design brief](../../../../brass/serpent-sheet-metal-packet/design-brief.md)
- [Fabrication plan](../../../../brass/serpent-sheet-metal-packet/fabrication-plan.md)
- [SolidWorks plan](../../../../brass/serpent-sheet-metal-packet/solidworks-plan.md)
- [Validation checklist](../../../../brass/serpent-sheet-metal-packet/validation-checklist.md)

## Current Status

- Release state: L1 concept packet — private review only; not build-certified, not measurement-verified.
- Library family: brass.
- Wolfram state: Wolfram Cloud Public-Execute URL available.
- CAD state: SolidWorks plan present; no confirmed `.glb`.
- **L2 promotion blockers:** `bom.csv` and `sourcing.csv` are missing.

## Source Notes

- [README](../../../../brass/serpent-sheet-metal-packet/README.md) — packet description, reference instrument (Lander serpent ca. 1820–1825), body form (double-S, copper raised/hammered shell), bell strategy (lofted-bend segmented conical), L2 promotion blockers.

Artifacts not ingested: `design-brief.md`, `parameters.csv`, `fabrication-plan.md`, `validation-checklist.md`.

## Design Knowledge

The serpent is a historical conical-bore wind instrument with a distinctive S-curved wooden body covered in leather, played with a cup mouthpiece. This packet translates the form into copper sheet metal. The Lander reference instrument (ca. 1820–1825) provides the bore and silhouette target.

Key fabrication challenge: the double-S body path requires copper raised/hammered shell sections that maintain bore continuity through two compound bends. The bell uses segmented conical frusta (Lofted Bend approach in SolidWorks) rather than a single lofted surface, which allows each frustum to be flat-patterned independently.

## Cross-Links

- [[acoustic-classes/conical-bore-brass]]
- [[fabrication/sheet-metal-brass]]
- [[fabrication/raised-hammered-shell]]

## Open Questions

1. What are the measured bore stations from the Lander reference instrument? Critical dimensions require measured drawings before metal is cut.
2. `bom.csv` and `sourcing.csv` are missing — blocking L2 promotion.
3. How is the double-S body path formed from copper sheet without losing bore continuity at the bends?
4. What finger-hole placement (six or seven holes, keys?) does this variant use?

## Maintenance Notes

First ingest from README only. Next pass: read `design-brief.md` for bore table and acoustic targets, `fabrication-plan.md` for shell-raising sequence, and `validation-checklist.md` for measurement gates. Add `bom.csv` and `sourcing.csv` to unblock L2 promotion.
