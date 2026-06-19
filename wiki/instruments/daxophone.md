---
title: Daxophone Blueprint (Bowed Wooden Tongue)
slug: daxophone
wiki_type: instrument
status: active
sources:
  - path: ../../../../idiophones/daxophone/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/friction-idiophone
  - instruments/musical-saw
  - instruments/bowed-dish
open_questions:
  - "What tongue wood species — and how does grain direction affect bowing response?"
  - "What is the clamp design — pressure, compliance, and resonance of the clamp block?"
  - "What contact pickup (piezo disk, condenser, transducer) and placement?"
  - "What dax block face geometry produces the most vocal tonal range?"
last_ingest: 2026-06-19
tags: [instrument, idiophone, daxophone, bowed, wooden-tongue, dax-block, contact-pickup, hans-reichel, L2]
---

# Daxophone Blueprint — Bowed Wooden Tongue

## Overview

A daxophone: a bowed wooden tongue clamped in a stable block, excited along its edge with a bow, shaped and stopped with a hand-held "dax" block to produce continuously variable, vocal, speech-like tones. A contact pickup captures the tongue vibration for amplification or recording. Invented by Hans Reichel; this packet is a design study for building one from scratch.

- **Family:** idiophone / bowed wooden tongue (with contact pickup)
- **Excitation:** bow along edge of wooden tongue
- **Pitch control:** dax block pressed against tongue to change effective vibrating shape
- **Amplification:** contact pickup (piezo or transducer)
- **Status:** L2 planning packet — not fabrication-ready; all tongue/clamp/dax/pickup dimensions pending measurement

Primary repo links:
- [README](../../../../idiophones/daxophone/README.md)
- [Design notes](../../../../idiophones/daxophone/design.md)
- [Decision record](../../../../idiophones/daxophone/decision-record.md)

## Current Status

- Release state: L2 planning packet — design study only. Tongue material, grain direction, clamp pressure, dax-face geometry, and pickup placement all pending measurement.
- Library family: idiophone.
- Acoustic class: friction idiophone (bowed wood).

## Source Notes

- [README](../../../../idiophones/daxophone/README.md) — mechanism (bowed tongue edge, dax block stops for pitch/shape control, contact pickup for amplification), engineering focus (repeatable clamping, expressive dax contact, low-noise pickup mounting, safe edge preparation).

Artifacts not ingested: `design.md`, `bom.csv`, `cut-list.csv`, `decision-record.md`.

## Design Knowledge

The daxophone tongue is typically a thin, flexible wooden blade (similar to a wooden tongue-drum tongue in cross-section), clamped horizontally in a solid block at one end and free at the other. Bowing along the edge excites bending vibration in the free region — similar to a musical saw, but wooden and clamped at one end (cantilever rather than S-curve bending).

The dax block is a hand-held piece of wood with a shaped face. Pressing the dax face against the tongue at different points along its length changes the effective vibrating segment — shortening the free length raises the apparent pitch, and the varied contact produces vocal, nasal, or horn-like formants. This technique was developed by Hans Reichel and produces extremely expressive speech-like tones.

The contact pickup (typically a piezo disk or similar transducer) must be mounted on the clamp or tongue base where it captures structural vibration without adding mechanical mass to the free tongue region.

Key engineering problems: consistent clamp repeatability (so the tongue returns to the same position), expressive but controllable dax contact, low-noise pickup mounting.

Related: [[instruments/musical-saw]] (flexible blade, continuous pitch by bending — same bowed-flexible-plate class), [[instruments/bowed-dish]] (bowed rod → dish, different radiator approach).

## Cross-Links

- [[acoustic-classes/friction-idiophone]]
- [[instruments/musical-saw]]
- [[instruments/bowed-dish]]

## Open Questions

1. What wood species and grain direction for the tongue?
2. What is the clamp design (pressure, compliance, resonance of clamp block)?
3. What contact pickup type and placement?
4. What dax block face geometry produces the most expressive vocal range?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for tongue geometry and dax-block mechanics.
