---
title: Djembe Blueprint (Stave-Built Research Packet)
slug: djembe
wiki_type: instrument
status: active
sources:
  - path: ../../../../percussion/djembe/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/goblet-drum
  - fabrication/stave-construction
  - fabrication/jigs-and-fixtures
  - instruments/ashiko-drum-workshop
  - instruments/dundun
open_questions:
  - "What is the primary validation data — is it tuner/FFT measurements from a physical drum, or modal analysis from the Wolfram model?"
  - "What is the optimum stave count / stave angle for the goblet waist geometry — and how does waist diameter affect the bass/tone/slap voice separation?"
  - "Are the jig designs in the repo the same jigs used in the ashiko workshop, or are they different fixtures for the goblet profile?"
last_ingest: 2026-06-19
tags: [instrument, drum, djembe, goblet-drum, stave-built, african, acoustic-research, jig, 16-years]
---

# Djembe Blueprint — Stave-Built Research Packet

## Overview

A deep research and fabrication packet for the stave-built djembe — one of Tony's longest-running design projects (16+ years). The djembe is a West African goblet-shaped hand drum with three primary playing voices: bass (full center strike), tone (open ring-finger strike at membrane edge), and slap (snapped strike producing a bright crack). The packet covers CAD geometry, acoustic research (modal analysis, membrane physics), custom jig designs for the goblet shell, and empirical validation.

- **Family:** membranophone / goblet drum (West African tradition)
- **Shell profile:** goblet — wide bowl head, narrow waist, open bell bottom
- **Construction:** stave-built hardwood, rope-and-guinea-ring lacing
- **Head:** goatskin, tensioned by rope lacing
- **Research depth:** 16+ years of continuous refinement across multiple physical builds
- **Status:** deep research packet — acoustic model, CAD, jig designs, empirical data

Primary repo links:
- [README](../../../../percussion/djembe/README.md)
- [Design notes](../../../../percussion/djembe/design.md)
- [Acoustic research](../../../../percussion/djembe/reference/)
- [Jig designs](../../../../percussion/djembe/jigs/)
- [Validation](../../../../percussion/djembe/validation.csv)

## Current Status

- Release state: deep research packet; multiple empirical build cycles.
- Library family: drum.
- Acoustic class: goblet drum (djembe).
- Wolfram state: acoustic/modal model present; Wolfram Cloud Public-Execute URL available.
- CAD state: SolidWorks goblet shell geometry with jig drawings; no confirmed `.glb`.

## Source Notes

- [README](../../../../percussion/djembe/README.md) — project scope (16+ years, acoustic research focus, CAD + jig designs), instrument context (West African goblet drum, three voices), packet map.

Artifacts not ingested: `design.md`, `validation.csv`, `reference/` acoustic papers, `jigs/` fixture drawings.

## Design Knowledge

The djembe's distinctive goblet shape is acoustically significant: the narrow waist acts as a Helmholtz resonator coupling the bowl (membrane chamber) to the open bell, producing the characteristic deep bass voice when the full hand strikes the membrane center. The tone and slap voices are dominated by membrane mode shapes.

The stave construction challenge for the goblet is the double-taper: staves must be compound-cut to form both the inward taper of the bowl and the outward flare of the bell, with the waist formed by the junction. Tony's jig system (descended from and shared with the [[instruments/ashiko-drum-workshop]] project) addresses this by using a sequence of guide templates and lathe fixtures.

Rope-and-guinea-ring lacing provides the tensioning system: goatskin head mounted over a metal ring, vertical tension ropes with horizontal cross-ropes (diamond pattern) allowing progressive tightening. This system is load-bearing and must be designed for the 800–1200 N of rope tension on a 12–14 in head.

Djembe acoustic research (modal analysis) is substantially more advanced in this repo than in any other percussion packet.

Related: [[instruments/ashiko-drum-workshop]] (conical variant, same stave lineage), [[instruments/dundun]] (cylindrical dundun companion drum), [[instruments/sheet-metal-djembe]] (sheet-metal translation of goblet geometry).

## Cross-Links

- [[acoustic-classes/goblet-drum]]
- [[fabrication/stave-construction]]
- [[fabrication/jigs-and-fixtures]]
- [[instruments/ashiko-drum-workshop]]
- [[instruments/dundun]]
- [[instruments/sheet-metal-djembe]]

## Open Questions

1. What is the primary validation data — tuner/FFT measurements from a physical drum, or modal analysis only?
2. What is the optimum stave count / stave angle for the goblet waist — and how does waist diameter affect voice separation?
3. Are the jig designs shared with the ashiko workshop or specific to the goblet profile?

## Maintenance Notes

First ingest from README only. This is the deepest percussion research packet in the library. Next pass: read `design.md`, `reference/` acoustic papers, and `validation.csv` for modal measurement data.
