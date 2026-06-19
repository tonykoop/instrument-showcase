---
title: Conga Drum Blueprint (3-Member Family)
slug: conga
wiki_type: instrument
status: active
sources:
  - path: ../../../../percussion/conga/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/conical-stave-drum
  - fabrication/stave-construction
  - instruments/djembe
  - instruments/ashiko-drum-workshop
open_questions:
  - "What are the exact head diameters for the three members (Quinto / Conga / Tumba) — and what are the target fundamental pitches for each?"
  - "What is the shell taper geometry — are the congas cylindrical, slightly conical, or barrel-shaped cross-sections?"
  - "What is the head-tensioning method — metal lug hardware (traditional Cuban style) or rope lacing?"
  - "What distinguishes the 4 'variants' referenced in the summary — different materials, stave counts, or finish options?"
last_ingest: 2026-06-19
tags: [instrument, drum, conga, stave-built, quinto, tumba, afro-cuban, hand-drum, 3-member-family]
---

# Conga Drum Blueprint — 3-Member Family

## Overview

A 3-member family of hand drums in the conga tradition (quinto, conga, tumba), built using stave construction. Four variants are documented across the family. The conga is an Afro-Cuban hand drum played upright on a stand or between the knees; the three sizes cover soprano (quinto), mid (conga), and bass (tumba) voices in Afro-Cuban ensemble playing.

- **Family:** membranophone / conical stave hand drum
- **Members:** Quinto (soprano), Conga (mid), Tumba (bass) — 3 shells, 4 variants
- **Construction:** stave-built, hardwood
- **Head:** rawhide or treated-skin drum head, lug-and-hoop hardware
- **Status:** v4-era design packet; blueprint and fabrication notes present

Primary repo links:
- [README](../../../../percussion/conga/README.md)
- [Design notes](../../../../percussion/conga/design.md)

## Current Status

- Release state: v4-era packet — one of the older instruments in the library; L-level and V-level explicit from README context.
- Library family: drum.
- Acoustic class: conical stave drum (Afro-Cuban hand drum tradition).
- CAD state: stave geometry defined; no confirmed `.glb`.

## Source Notes

- [README](../../../../percussion/conga/README.md) — 3-member family (Quinto/Conga/Tumba), 4 variants, v4-era context, stave construction, acoustic overview.

Artifacts not ingested: `design.md`, `parameters.csv`, `validation.csv`, `bom.csv`.

## Design Knowledge

Congas differ from djembes in playing technique and head-mounting hardware: traditional Cuban congas use metal lug-and-hoop hardware (identical to drum-kit hardware) rather than rope lacing. The shell is slightly conical (wider at the open bottom) but much less tapered than a djembe. The head is a thick rawhide or buffalo skin mounted over a metal hoop and tensioned by 6–8 tuning lugs.

Stave construction for congas follows the same geometry principles as ashiko and djembe: compound-angle stave cuts, glue-up jig, lathe finish. The three sizes (quinto ~11 in, conga ~12 in, tumba ~14 in head diameter) use the same fabrication process at different scale.

Afro-Cuban conga technique covers: open tone (rim strike), muffled tone (palm across membrane), slap (snapped ring finger near edge), bass (center palm), heel-toe patterns. Shell resonance profile interacts with each voice differently.

Related: [[instruments/djembe]] (goblet profile, rope lacing), [[instruments/ashiko-drum-workshop]] (conical stave, same fabrication lineage).

## Cross-Links

- [[acoustic-classes/conical-stave-drum]]
- [[fabrication/stave-construction]]
- [[instruments/djembe]]
- [[instruments/ashiko-drum-workshop]]

## Open Questions

1. What are the head diameters and target fundamental pitches for the three members?
2. What is the shell taper geometry (cylindrical vs conical vs barrel cross-section)?
3. What is the head-tensioning method — lug hardware or rope lacing?
4. What distinguishes the 4 variants across the family?

## Maintenance Notes

First ingest from README only. v4-era packet; next pass: read `design.md` for stave geometry math and head-diameter specs for all three shell sizes.
