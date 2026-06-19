---
title: Sheet-Metal Djembe Blueprint
slug: sheet-metal-djembe
wiki_type: instrument
status: active
sources:
  - path: ../../../../percussion/sheet-metal-djembe/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - instruments/djembe
  - acoustic-classes/goblet-drum
  - fabrication/sheet-metal-spinning
  - fabrication/rolled-sheet-metal-shell
open_questions:
  - "How is the goblet waist achieved in sheet metal — spinning over a form, hydroforming, or sectional roll-and-weld?"
  - "Does the 1.0mm CRS shell produce the same acoustic response as a stave-built hardwood shell — and has this been validated with measurement?"
  - "What is the bearing-edge geometry for the head mounting on a sheet-metal rim?"
  - "How is the guinea-ring rope lacing system adapted for the sheet-metal shell (attachment points for vertical rope anchors)?"
last_ingest: 2026-06-19
tags: [instrument, drum, djembe, sheet-metal, goblet, CRS, spun-steel, rope-lacing, goatskin]
---

# Sheet-Metal Djembe Blueprint

## Overview

A sheet-metal translation of the djembe goblet geometry. The two-piece shell (upper bowl + lower bell) is formed from 1.0 mm cold-rolled steel, preserving the goblet acoustic geometry of the stave-built djembe while enabling sheet-metal sprint fabrication. Head mounting and rope-lacing system follow the traditional djembe method.

- **Family:** membranophone / goblet drum (sheet-metal variant)
- **Shell:** two-piece 1.0 mm CRS — upper bowl + lower open bell, welded at waist
- **Profile:** goblet (preserves djembe head diameter, waist, and bell proportions)
- **Head:** goatskin, rope-and-guinea-ring laced
- **Status:** blueprint packet — geometry translation from stave model; no confirmed prototype

Primary repo links:
- [README](../../../../percussion/sheet-metal-djembe/README.md)
- [Design notes](../../../../percussion/sheet-metal-djembe/design.md)

## Current Status

- Release state: blueprint packet; no confirmed empirical validation.
- Library family: drum.
- Acoustic class: goblet drum (sheet-metal variant).
- CAD state: two-piece shell geometry defined; no confirmed `.glb`.

## Source Notes

- [README](../../../../percussion/sheet-metal-djembe/README.md) — design rationale (sheet-metal sprint methods applied to goblet geometry, 1.0 mm CRS, two-piece construction), head and lacing system.

Artifacts not ingested: `design.md`, `parameters.csv`, `bom.csv`.

## Design Knowledge

The goblet shape cannot be formed as a single rolled cylinder — the waist requires an inward curvature. The design uses a two-piece approach:
- **Upper bowl**: spun or roll-and-weld conical frustum, head diameter down to waist diameter
- **Lower bell**: conical frustum, waist diameter out to open bell

The two are welded at the waist. Waist transition blending is critical for acoustic continuity (no hard bore step) and structural integrity (highest-stress point in the rope-tensioning load path).

1.0 mm CRS is at the lower limit of reasonable structural gauge for a body under rope-lacing tension loads (~800–1200 N). Thicker gauge (1.2 or 1.5 mm) may be needed at the waist and rope-anchor band for durability.

Rope anchor points must be fabricated into the shell — typically a ring of brazed rings or drilled holes reinforced with a heavy collar band — since sheet metal alone cannot carry the rope-point loads without tearing.

The acoustic character of a 1.0 mm CRS shell differs from hardwood: much lower internal damping, so the shell itself rings freely between drum strokes. Players manage this with dampening tape or thicker heads.

Related: [[instruments/djembe]] (stave-built original, same acoustic target), [[fabrication/sheet-metal-spinning]] (spinning method for bowl form).

## Cross-Links

- [[instruments/djembe]]
- [[acoustic-classes/goblet-drum]]
- [[fabrication/sheet-metal-spinning]]
- [[fabrication/rolled-sheet-metal-shell]]

## Open Questions

1. How is the goblet waist achieved — spinning, hydroforming, or sectional roll-and-weld?
2. Does the 1.0 mm CRS shell produce the same acoustic response as stave-built hardwood?
3. What is the bearing-edge geometry for the head on a sheet-metal rim?
4. How are the vertical rope-anchor points fabricated into the metal shell?

## Maintenance Notes

First ingest from README only. Next pass: read `design.md` for two-piece geometry math and structural analysis of the rope-anchor system. Compare `validation.csv` (if present) with djembe measurements.
