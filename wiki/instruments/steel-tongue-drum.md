---
title: Steel Tongue Drum Blueprint (Tunable Slit Idiophone)
slug: steel-tongue-drum
wiki_type: instrument
status: active
sources:
  - path: ../../../../idiophones/steel-tongue-drum/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/slit-tongue-idiophone
  - fabrication/laser-waterjet-slotting
  - instruments/tongue-drum
  - instruments/handpan
open_questions:
  - "What are the target MIDI notes / tongue lengths for this design — and how many tongues?"
  - "Final pitch depends heavily on batch variation; what is the accepted cents error after tuning?"
  - "Which cutting method (laser / waterjet / CNC) was selected, and what kerf/HAZ measurements exist?"
  - "Has a rough-cut prototype been built and measured, or is validation.csv still empty?"
last_ingest: 2026-06-19
tags: [instrument, drum, idiophone, steel-tongue-drum, slit-tongue, tunable, 12in, empirical, L2]
---

# Steel Tongue Drum Blueprint — Tunable Slit Idiophone

## Overview

A round steel-shell slit-tongue idiophone: a hollow vessel whose top surface carries cut tongue slits, each tongue vibrating as a cantilever beam at its own target pitch when struck by a mallet. A thorough prototype-planning packet derived from an existing design spreadsheet (`steel-tongue-drum-design-table.xlsx`), including the critical caveat that steel tongue drums are empirical instruments — first-pass cantilever predictions must be validated and corrected on the actual prototype.

- **Family:** idiophone / slit-tongue (classified as drum in manifest; lives in idiophones/ directory)
- **Body:** round steel shell, 12 in OD, 6 in height assumption
- **Steel thickness:** 0.079 in (from workbook; actual batch TBD)
- **Slot kerf:** 0.040 in; tongue width 1.0 in (workbook assumptions)
- **Port diameter:** 2.5 in (Helmholtz cavity coupling)
- **Tuning model:** `f = K_steel × t / L²` — first-pass only; final pitch requires prototype trimming
- **Status:** L2 V5 build-packet candidate — private-prototype-ready; no measured data yet

Primary repo links:
- [README](../../../../idiophones/steel-tongue-drum/README.md)
- [Design notes](../../../../idiophones/steel-tongue-drum/design.md)
- [Validation](../../../../idiophones/steel-tongue-drum/validation.csv)

## Current Status

- Release state: L2 V5 build-packet candidate. Design review and sourcing review complete; prototype measurement campaign pending.
- Library family: drum (manifest classification); repo lives in idiophones/ directory.
- Acoustic class: slit-tongue idiophone (circular steel vessel).
- Wolfram state: Wolfram Cloud Public-Execute URL available.
- CAD state: drawing briefs and layout SVG present; no confirmed `.glb`.

## Source Notes

- [README](../../../../idiophones/steel-tongue-drum/README.md) — design baseline (12 in OD, 6 in height, 0.079 in steel, 1.0 in tongue width, 2.5 in port), tuning model, prototype measurement requirements, packet map.

Artifacts not ingested: `design.md`, `validation.csv`, `bom.csv`, `sourcing.csv`, `cut-list.csv`.

## Design Knowledge

Steel tongue drums obey the cantilever frequency formula: `f ≈ K × t / L²`, where `t` is material thickness, `L` is tongue free length, and `K` is a material constant. However, real production deviates from the model due to: steel batch variation in E and density, residual stress from rolling, slot kerf geometry, heat affected zone from laser/plasma cutting, burr mass at slit terminus, mounting isolation stiffness, mallet strike point, and finish coat mass. Each of these is a potential ±20–50 cents error source.

The recommended workflow is:
1. Cut first-pass tongue lengths from the cantilever formula.
2. Strike each tongue, measure Hz with a tuner.
3. Trim (shorten = sharpen, widen = flatten) iteratively until each tongue is within ±5 cents of target.
4. Record trim history in `validation.csv`.

The 2.5 in port provides Helmholtz cavity coupling: the air column inside the vessel resonates near the bass tongue's fundamental, adding sustain and body to the low end.

The packet acknowledges that final tuning is a physical process, not an engineering calculation — so no claim of "tuned" status is made until measured data exists.

Related: [[instruments/tongue-drum]] (wooden box slit-drum; different body material and physics), [[instruments/handpan]] (steel vessel related class).

## Cross-Links

- [[acoustic-classes/slit-tongue-idiophone]]
- [[fabrication/laser-waterjet-slotting]]
- [[instruments/tongue-drum]]
- [[instruments/handpan]]

## Open Questions

1. What are the target MIDI notes and tongue lengths?
2. What is the accepted cents error budget after tuning?
3. Which cutting method (laser / waterjet / CNC) was selected — kerf and HAZ measurements?
4. Has a rough-cut prototype been built and measured, or is `validation.csv` empty?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for tongue-length table and `validation.csv` for prototype strike measurements. Note: family=drum in manifest but repo lives in idiophones/ (this is why the wiki page is in `wiki/instruments/`).
