---
title: Public Release Blockers
wiki_type: synthesis
status: active
last_updated: 2026-05-18
source_count: 6
open_questions: 8
tags:
  - synthesis
  - release
  - validation
---

# Public Release Blockers

## Overview

This page tracks recurring reasons an instrument packet should stay private, remain in public review, or avoid production-ready claims. It is the portfolio-level counterweight to enthusiastic explorer pages: the library can be beautiful and still be honest about missing evidence.

## Current Instrument Readout

| Instrument | Current release posture | Main blockers |
| --- | --- | --- |
| [[instruments/kora]] | Private review | Cultural provenance review, unsafe treble string margins, neck/tail proof-load, bridge/head staged-load validation, measured prototype data, owned or permission-cleared visuals |
| [[instruments/sambuca]] | Private review | MULE structural validation, SAM-13 depth/cavity/tuner inconsistencies, inherited kora CAD geometry, musicology/cultural review, release-gate reconciliation |
| [[instruments/cajon]] | Public review / pre-build candidate | Measured CJ-S prototype data, workbook Helmholtz confirmation, snare preload validation, panel thickness and joinery fit, real prototype photos |
| [[instruments/ceramic-hang]] | Explorer-readiness scaffold / not build-ready | Measured clay shrinkage, tone-field coupon evidence, realistic note count, glaze damping, rim/transport protection, fabrication authority |
| [[instruments/ceramic-tongue-drum]] | Private research / prototype planning | Fired ceramic K, same-batch shrinkage, slot survival through firing, glaze mass effects, CTD-M chamber measurement, SVG/CAD/DXF authority |
| [[instruments/wood-shell-tongue-drum]] | L2 root-mode / pre-prototype review | V1 Standard physical tuning data, Padauk K calibration, Helmholtz end correction, rim seal behavior, seasonal joint behavior, CAD/G-code after calibration |

## Blocker Types

### Cultural Or Provenance Review

Use for instruments whose public language could overclaim cultural authority, historical continuity, lineage, or authenticity.

Active example:

- [[instruments/kora]] must remain private until cultural provenance language is reviewed by a knowledgeable player, maker, or advisor.
- [[instruments/sambuca]] needs cultural/musicology review because it is inspired by archaeological/living-history instrument forms and uses visual/provenance claims from Ur-related sources.

### Safety And Load Path

Use when the first build can fail energetically or structurally:

- high string tension
- membrane/head loading
- bridge rocking
- tail or neck proof-load
- seat-load testing
- high-speed lathe or CNC hazards

Active examples:

- [[instruments/kora]] has string break, bridge/head, and neck/tail proof-load gates.
- [[instruments/sambuca]] has curved-neck/string-holder strip validation and a MULE 30-day hold before ROOT geometry can be treated as validated.
- [[instruments/cajon]] has seat-load, joinery, and tapa/screw-boundary gates.
- [[instruments/ceramic-hang]] and [[instruments/ceramic-tongue-drum]] have firing, cracking, shrinkage, glaze, rim, and transport fragility gates.
- [[instruments/wood-shell-tongue-drum]] has lathe-trued shell/rim, stave glue-line, soundboard, and slit-routing gates.

### Predicted Versus Measured Claims

Use whenever an explorer or packet has formulas but no physical prototype measurements.

Active examples:

- [[instruments/cajon]] has predicted plate, Helmholtz, and coupled bass values pending CJ-S measurements.
- [[instruments/ceramic-hang]] has shell/tone-field targets but no fired tone-field evidence yet.
- [[instruments/ceramic-tongue-drum]] has derived ceramic cantilever constants and predicted Helmholtz ratios pending fired CTD-M measurements.
- [[instruments/wood-shell-tongue-drum]] has predicted tongue and cavity values pending V1 Standard measurements.
- [[instruments/sambuca]] has validation language that must be separated into actual measured evidence versus future MULE/ROOT validation intent.
- [[instruments/kora]] has string and resonator models pending safe staged validation.

### Fabrication Authority

Use when drawings, generated images, CAD previews, or concept art could be mistaken for build authority.

Active examples:

- [[instruments/cajon]] explicitly separates design table, OpenSCAD source, jig templates, reviewed drawings, previews, and placeholder images.
- [[instruments/sambuca]] has SolidWorks Pack-and-Go notes but current files still contain inherited kora geometry, so CAD is not build-authoritative.
- [[instruments/ceramic-hang]] and [[instruments/ceramic-tongue-drum]] need measured shrinkage/coupon evidence before CAD/SVG/DXF can be treated as fabrication authority.
- [[instruments/wood-shell-tongue-drum]] defers CAD and G-code until Phase 1 measurements calibrate the acoustic model and hold-down strategy.

### Source And Supplier Freshness

Use when public instructions depend on prices, availability, substitutions, hardware, or material claims that can go stale.

Active examples:

- [[instruments/cajon]] requires supplier price/availability verification before recommending purchases.
- [[instruments/ceramic-hang]] and [[instruments/ceramic-tongue-drum]] require clay body, shrinkage, firing schedule, and glaze compatibility verification before public build instructions.
- [[instruments/wood-shell-tongue-drum]] requires current tonewood stock, Padauk thickness, and substitute checks before buying.

## Suggested Library Status Terms

- `private-review`: do not publish beyond trusted review.
- `public-review`: safe to show as a design packet, but not a measured production build.
- `pre-build-candidate`: complete enough for shop review, not evidence of acoustic performance.
- `measured-prototype`: at least one physical prototype has measurement rows.
- `production-ready`: requires measured prototype, revised docs, authority chain, and release review.

## Open Questions

1. Should `library.html` add a release-evidence filter separate from current release status?
2. Should every public-facing explorer show a predicted-vs-measured badge?
3. Should instrument pages have a standard `release_blockers` frontmatter list for machine-readable rollups?
4. What counts as enough cultural review for culturally situated instruments?
5. Should CAD authority, visual authority, and fabrication authority be separate status axes?
6. Should binary generated artifacts be treated as source, output, or evidence in the wiki manifest?
7. How should measured prototype data be promoted from CSV rows into reusable wiki summaries?
8. Which blockers are Heifer Zephyr brand blockers versus general engineering blockers?

## Maintenance Notes

Update this page after every instrument ingest. It should become the primary portfolio-level checklist for deciding what can move from private review to public review to measured prototype status.
