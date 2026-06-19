---
title: Bowed Frame Drum Blueprint
slug: bowed-frame-drum
wiki_type: instrument
status: active
sources:
  - path: ../../../../percussion/bowed-frame-drum/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/frame-drum
  - fabrication/cr-steel-frame
  - acoustic-classes/bowed-membrane
open_questions:
  - "What is the tone bar material and geometry — is it a steel rod, a brass strip, or a tuned metal bar glued to the head?"
  - "Does bowing the tone bar produce a clean pitched tone, or is it heavily modal and noise-like at 450 mm membrane scale?"
  - "What is the target pitch or tuning spec for the bowed-drone mode?"
  - "Is the head laced, glued, or hoop-tensioned onto the CR-steel frame?"
last_ingest: 2026-06-19
tags: [instrument, drum, frame-drum, bowed, tone-bar, drone, CR-steel, 450mm, bodhran]
---

# Bowed Frame Drum Blueprint

## Overview

A 450 mm bodhran-scale frame drum with a cold-rolled (CR) steel ring shell and an embedded tone bar that can be bowed with a violin bow to produce a sustained drone pitch. The instrument is primarily a hand-played frame drum; the optional bowed mode adds a continuous drone layer analogous to a shruti box.

- **Family:** membranophone / frame drum with bowed-drone feature
- **Shell:** CR-steel ring, ~450 mm OD (bodhran scale)
- **Head:** goatskin or synthetic
- **Tone bar:** metal bar embedded at head center, bowable
- **Status:** blueprint packet — geometry and concept defined; no confirmed prototype

Primary repo links:
- [README](../../../../percussion/bowed-frame-drum/README.md)
- [Design notes](../../../../percussion/bowed-frame-drum/design.md)

## Current Status

- Release state: blueprint packet; no confirmed empirical validation.
- Library family: drum.
- Acoustic class: frame drum / bowed membrane hybrid.
- CAD state: frame ring and tone-bar geometry defined; no confirmed `.glb`.

## Source Notes

- [README](../../../../percussion/bowed-frame-drum/README.md) — overview of the bodhran-scale CR-steel frame, embedded tone bar, and optional bowed-drone mode.

Artifacts not ingested: `design.md`, `parameters.csv`, `bom.csv`.

## Design Knowledge

Cold-rolled steel rings can be bent and welded to very accurate diameters and flatness tolerances, making CR-steel a lower-cost alternative to hardwood hoops for large frame drums. The round-stock or flat-bar CR-steel ring is typically 6–12 mm cross-section for a 450 mm bodhran.

The tone bar is a thin metal strip (steel or brass) bonded across or near the head center. When bowed with a rosined bow, the bar produces a strongly pitched tone sustained for as long as the bow stroke continues — a technique borrowed from hurdy-gurdy and musical-saw practice. The bar's pitch depends on its geometry, mass, and mounting compliance.

The bodhran-scale (450 mm) body makes this portable. The CR-steel frame is lighter than a carved wooden hoop and more dimensionally stable in varying humidity.

## Cross-Links

- [[acoustic-classes/frame-drum]]
- [[acoustic-classes/bowed-membrane]]
- [[fabrication/cr-steel-frame]]

## Open Questions

1. What is the tone bar material and geometry (rod, strip, flat bar)?
2. Does bowing produce a clean pitched tone at this membrane scale?
3. What is the target pitch for the bowed-drone mode?
4. Is the head laced, glued, or hoop-tensioned?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for tone bar physics and attachment method.
