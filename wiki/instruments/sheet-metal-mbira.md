---
title: Sheet-Metal Mbira Blueprint (17-Tine Shona-Inspired)
slug: sheet-metal-mbira
wiki_type: instrument
status: active
sources:
  - path: ../../../../idiophones/sheet-metal-mbira/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/lamellaphone-idiophone
  - instruments/array-mbira
  - fabrication/spring-steel-tongue-welding
open_questions:
  - "How is the tongue-root welding done without top-plate warping — spot weld, tig, or brazing?"
  - "What is the tongue map layout — which notes, which ranks, and what octave range?"
  - "Has the brass buzzer plate been tested — and what buzzing frequency does it produce?"
  - "What is the measured sustain for the 17 tongues — does the 1018 steel box achieve ≥3 s?"
last_ingest: 2026-06-19
tags: [instrument, idiophone, mbira, lamellaphone, 17-tine, spring-steel, 1018-steel-box, buzzer-plate, shona, L2]
---

# Sheet-Metal Mbira Blueprint — 17-Tine Shona-Inspired

## Overview

A Round 4 idiophone blueprint: a 250 × 200 × 80 mm 1018 cold-rolled steel soundbox with 17 spring-steel tongues in three ranks, plus a removable brass buzzer plate. The Shona-inspired seven-degree layout produces a pentatonic-adjacent scale used in traditional Zimbabwean mbira playing. The core engineering challenge is precision tongue-root welding without top-plate warping.

- **Family:** idiophone / lamellaphone (plucked-tine mbira)
- **Soundbox:** 250 × 200 × 80 mm, 1018 CRS, 0.040 in planning thickness
- **Tongues:** 17 spring-steel tongues (0.040 in, 5 mm wide, 60–120 mm rough blanks), three ranks, Shona-inspired 7-degree layout
- **Buzzer plate:** removable brass plate
- **Box resonance:** ~120 Hz (measurement required)
- **Tuning target:** each tongue within ±10 cents; sustain ≥3 s (target 3–6 s)
- **Status:** L2 V5 build-packet candidate — design and CAD planning; precision welding protocol pending

Primary repo links:
- [README](../../../../idiophones/sheet-metal-mbira/README.md)
- [Design notes](../../../../idiophones/sheet-metal-mbira/design.md)
- [Tongue map](../../../../idiophones/sheet-metal-mbira/tongue-map.csv)
- [Wolfram starter](../../../../idiophones/sheet-metal-mbira/sheet-metal-mbira-starter.wl)

## Current Status

- Release state: L2 V5 build-packet candidate. Design and CAD planning authority; no measured tongue data.
- Library family: idiophone.
- Acoustic class: lamellaphone (plucked spring-steel tongue).
- Wolfram state: starter tongue model present; Wolfram Cloud Public-Execute URL available.
- CAD state: SolidWorks plan defined; no confirmed `.glb`.

## Source Notes

- [README](../../../../idiophones/sheet-metal-mbira/README.md) — targets (17 tongues in 3 ranks, Shona 7-degree layout, 1018 steel box 250 × 200 × 80 mm, brass buzzer plate, ±10 cents, ≥3 s sustain), core engineering problem (tongue-root welding without warping).

Artifacts not ingested: `design.md`, `tongue-map.csv`, `validation.csv`, `bom.csv`.

## Design Knowledge

Traditional mbira (Zimbabwean, Shona tradition) uses spring-metal tongues (historically iron, now spring steel or phosphor bronze) mounted over a wooden soundboard. This design replaces the wooden board with a 1018 steel box, which provides a mechanical resonator with a ~120 Hz body mode.

Spring steel tongues obey the cantilever formula: `f = K × t / L²`. Tongue lengths for the Shona 7-degree layout span bass (longer, thicker tongues in the lower rank) through treble (shorter tongues in upper ranks). The three-rank layout (bass/mid/treble) is a traditional mbira configuration — thumbs and forefingers access different ranks simultaneously.

The core engineering problem is tongue-root attachment: welding 0.040 in spring steel to a 0.040 in steel plate without warping the top plate. Options: TIG spot welds with pulse control, resistance spot welding with precise timing, or silver brazing (lower heat input). Any weld that adds mass to the tongue root shifts the pitch down.

The brass buzzer plate (a removable thin brass sheet with small holes) traditionally adds a nasal, buzzing overtone to mbira sound — a culturally significant acoustic feature of Shona mbira.

Related: [[instruments/array-mbira]] (isomorphic chromatic variant with individual resonators under each tine).

## Cross-Links

- [[acoustic-classes/lamellaphone-idiophone]]
- [[instruments/array-mbira]]
- [[fabrication/spring-steel-tongue-welding]]

## Open Questions

1. What tongue-root welding method avoids top-plate warping?
2. What is the tongue map layout (specific notes per rank)?
3. Has the brass buzzer plate been tested acoustically?
4. What is the measured sustain for the 17 tongues?

## Maintenance Notes

First ingest from README only. Next pass: read `tongue-map.csv` for the 17-note layout and `design.md` for welding protocol and box resonance model.
