---
title: Jal Tarang Blueprint (Struck Water Bowl Idiophone)
slug: jal-tarang
wiki_type: instrument
status: active
sources:
  - path: ../../../../idiophones/jal-tarang/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/struck-vessel-idiophone
  - instruments/glass-harp
  - instruments/udu
open_questions:
  - "How many bowls are in scope — traditional jal tarang uses 7–22 bowls covering 1–3 octaves?"
  - "What bowl material (porcelain, ceramic, glass, metal) is preferred — and how does this affect tone quality?"
  - "What is the mallet material and hardness for each bowl size?"
  - "What is the tuning workflow — coarse by bowl selection, fine by water fill, verified by tuner?"
last_ingest: 2026-06-19
tags: [instrument, idiophone, jal-tarang, water-bowl, struck, india, porcelain, ceramic, mallets, L2]
---

# Jal Tarang Blueprint — Struck Water Bowl Idiophone

## Overview

A jal tarang: a tuned idiophone made from porcelain, ceramic, glass, or metal bowls partly filled with water and struck with light mallets. Water level changes each bowl's pitch by adding mass to the vibrating membrane/wall. The instrument is a classical Indian percussion instrument used in Hindustani and Carnatic classical music.

- **Family:** idiophone / struck water bowl
- **Materials:** porcelain, ceramic, glass, or metal bowls (material TBD)
- **Tuning method:** bowl selection (dominant) + water fill volume (fine adjustment)
- **Mallets:** light mallets, material TBD
- **Origin:** classical Indian music (Hindustani and Carnatic traditions)
- **Status:** L2 concept/pending-measurement packet — bowl count, material, geometry, water volumes, and pitch values all pending measurement

Primary repo links:
- [README](../../../../idiophones/jal-tarang/README.md)
- [Design study](../../../../idiophones/jal-tarang/design.md)
- [Decision record](../../../../idiophones/jal-tarang/decision-record.md)

## Current Status

- Release state: L2 concept / pending-measurement packet. No CAD, DXF, measured drawing, or acoustic simulation; no bowl dimensions, water volumes, pitch frequencies, tuning table, scale, mallet hardness, or support geometry.
- Library family: idiophone.
- Acoustic class: struck vessel idiophone (water-filled).

## Source Notes

- [README](../../../../idiophones/jal-tarang/README.md) — instrument overview (Hindustani/Carnatic, water-bowl, struck with mallets), core design challenge (stable repeatable tuning workflow: select, fill, measure, play, drain), L2 boundary.

Artifacts not ingested: `design.md`, `bom.csv`, `cut-list.csv`, `decision-record.md`.

## Design Knowledge

The jal tarang works by bowl-resonance modification: a ceramic or porcelain bowl has a characteristic ring pitch when struck dry. Adding water increases the effective mass of the vibrating wall/bottom, lowering the pitch. The pitch shift is approximately monotonic with fill level — more water → lower pitch. This allows one set of bowls to be tuned to different scales by adjusting fill volumes before performance.

The engineering challenge is the tuning workflow: unlike a glockenspiel (where bar lengths are fixed), a jal tarang requires a precise fill-volume protocol for each bowl at each target pitch. Water evaporates and sloshes during performance; the bowl arrangement and access logistics must account for spill management, fill access during a pause, and return-to-pitch repeatability.

Bowl selection strategy (similar to [[instruments/glass-harp]]): measure a pool of bowls (same material, similar size), sort by dry pitch, select the subset that, with fill adjustment, covers the target scale with adequate pitch spacing.

Related: [[instruments/glass-harp]] (wet-finger friction vs mallet-struck, but same water-fill tuning concept), [[instruments/udu]] (struck ceramic vessel, no water fill — different acoustic class).

## Cross-Links

- [[acoustic-classes/struck-vessel-idiophone]]
- [[instruments/glass-harp]]
- [[instruments/udu]]

## Open Questions

1. How many bowls in scope — what range (traditional 7–22 bowls, 1–3 octaves)?
2. What bowl material is preferred — how does it affect tone?
3. What mallet material and hardness for each bowl size?
4. What is the tuning workflow (bowl selection → water fill → tuner verification)?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for bowl selection criteria and fill-volume tuning model.
