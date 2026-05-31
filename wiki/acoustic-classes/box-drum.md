---
title: Box Drum Acoustic Class
wiki_type: acoustic-class
status: active
last_updated: 2026-05-18
source_count: 1
open_questions: 5
tags:
  - acoustic-class
  - drum
  - box-drum
---

# Box Drum Acoustic Class

## Overview

This page tracks closed-box drums where a thin struck plate couples to an internal cavity. In the current wiki, the first active member is [[instruments/cajon]].

The useful reusable model is plate plus Helmholtz cavity, with practical corrections for panel material, fastener boundary conditions, port end correction, snare preload, and player ergonomics.

## Active Instruments

- [[instruments/cajon]] - three-member cajon family with Compact, Standard, and Bass sizes; first physical prototype is Standard `CJ-S`, V1 finger joint, guitar-string snare.

Potential future members:

- `resonant-box`
- other closed wooden percussion boxes if added to the library

## Governing Model

The cajon page uses two coupled systems:

- A front plate `(1,1)` bending mode.
- A Helmholtz cavity mode through the back port.

Class-level formula:

```text
f_H = (c / 2 pi) * sqrt(A / (V * L_eff))
L_eff = t_back + 1.7 * (d_hole / 2)
```

The first ingest recorded an important correction: the earlier cajon workbook formula used only back-panel thickness for effective neck length. The design notes now use the end-corrected expression; the workbook itself still needs confirmation before it becomes final public authority.

Source: [cajon design notes](../../../../percussion/cajon/design.md)

## Reusable Validation Pattern

Every box-drum packet should distinguish predicted values from measured values:

- Helmholtz cavity frequency
- plate fundamental
- perceived coupled bass
- slap-vs-bass spectral delta
- snare buzz onset, when applicable
- fastener torque or boundary-condition repeatability
- structural load, if the instrument is sat on

For the cajon, all acoustic values remain predictions until the Standard prototype is built and `validation.csv` receives measured rows.

## Design Risks To Watch

- Missing or inconsistent Helmholtz end correction.
- Plate material variability, especially plywood thickness and stiffness.
- Fastener torque changing the plate boundary condition.
- Snare contact pressure being adjusted by ear but not captured as a design variable.
- Placeholder imagery or generated previews being mistaken for fabrication authority.

## Open Questions

1. Should this class require an explicit `predicted` vs `measured` badge in the library or explorer UI?
2. What is the standard measurement workflow for the plate and cavity modes?
3. Should snare preload become a cross-instrument parameter?
4. How should box-drum packets represent player-size ergonomics?
5. Which drawings or CAD files are authoritative before the first measured build?

## Maintenance Notes

When the first cajon prototype is measured, update this page with actual plate/cavity deltas and note whether the corrected Helmholtz model held within the expected tolerance.
