---
title: Wood Shell Tongue Drum
slug: wood-shell-tongue-drum
wiki_type: instrument
status: active
last_updated: 2026-05-18
source_count: 12
open_questions: 8
tags:
  - instrument
  - drum
  - tongue-drum-wood
  - pre-prototype
---

# Wood Shell Tongue Drum

## Overview

The `wood-shell-tongue-drum` repo is an L2 root-mode packet for a round-body wood slit-tongue idiophone with an enclosed resonator. It is positioned as the round-body counterpart to Tony's rectangular-prism wooden tongue drum work, but with an added Helmholtz cavity under the tongue field.

The packet defines four geometric variants across three size envelopes, all driven by a single parametric design table. The recommended first prototype is V1 Cylinder + Flat Top, Standard 16 in, A Kurd, A3 ding, 11 tongues.

Primary repo links:

- [README](../../../../idiophones/wood-shell-tongue-drum/README.md)
- [Design notes](../../../../idiophones/wood-shell-tongue-drum/design.md)
- [Assembly manual](../../../../idiophones/wood-shell-tongue-drum/assembly-manual.md)
- [Validation report](../../../../idiophones/wood-shell-tongue-drum/validation-report.md)
- [Risks](../../../../idiophones/wood-shell-tongue-drum/risks.md)
- [Joinery matrix](../../../../idiophones/wood-shell-tongue-drum/joinery-configuration-matrix.md)
- [Capstone manifest](../../../../idiophones/wood-shell-tongue-drum/capstone-manifest.json)

## Current Status

- Release state: L2 root-mode packet / pre-prototype review.
- Library family: drum.
- Acoustic class: wood tongue drum with enclosed Helmholtz cavity.
- Wolfram state: owner-only in the central library manifest.
- Explorer state: awaiting explorer generation in the central library manifest.
- CAD state: no `.glb` detected yet; CAD and G-code are intentionally deferred until Phase 1 measurements calibrate Padauk K, rim seal behavior, Helmholtz end correction, and hold-down strategy.
- First-build stance: V1 Standard 16 in prototype should populate `validation.csv` and `validation-report.md` before the packet claims build-ready evidence.

## Source Notes

The first ingest used text-native sources and linked binary/generated artifacts without deep extraction:

- [README](../../../../idiophones/wood-shell-tongue-drum/README.md) gives the concept, variant matrix, first-prototype recommendation, acoustic one-paragraph model, build status, sister repos, and highest-risk unknowns.
- [Design notes](../../../../idiophones/wood-shell-tongue-drum/design.md) define the four variants, size presets, tongue equations, Helmholtz model, computed coupling ratios, tongue-fit caps, prototype configuration, and build phase sequence.
- [Assembly manual](../../../../idiophones/wood-shell-tongue-drum/assembly-manual.md) defines the V1/V2 cylinder path, V3/V4 hemisphere path, soundboard workflows, gu-port tuning, tongue tuning, validation, and finish.
- [Validation report](../../../../idiophones/wood-shell-tongue-drum/validation-report.md) records clean packet checks and human-owned remaining actions from the 2026-05-08 public-readiness pass.
- [Risks](../../../../idiophones/wood-shell-tongue-drum/risks.md) tracks 16 risks across acoustic, structural, ergonomic, supply, and fit/finish categories.
- [Family spec](../../../../idiophones/wood-shell-tongue-drum/family-spec.csv) defines all 12 variant/size cells and computed Helmholtz ratios.
- [Validation table](../../../../idiophones/wood-shell-tongue-drum/validation.csv) defines predicted tongue/cavity values and measurement rows. At ingest, measured values are blank.
- [Joinery matrix](../../../../idiophones/wood-shell-tongue-drum/joinery-configuration-matrix.md) separates shell construction from soundboard capture and recommends a stave/segmented shell plus rabbeted top capture.
- [Jig and template plan](../../../../idiophones/wood-shell-tongue-drum/cnc/jig-and-template-plan.md) defines first-prototype fixture choices, laser outputs, and CAM readiness gates.
- [Capstone manifest](../../../../idiophones/wood-shell-tongue-drum/capstone-manifest.json) lists the packet files and generated output state.
- [Wolfram starter](../../../../idiophones/wood-shell-tongue-drum/wolfram-starter.wl) is the future 3-DOF coupled oscillator starting point.
- [Legacy rectangular tongue-drum repo](../../../../idiophones/tongue-drum/README.md) is a likely future source stream but was not ingested deeply in this pass.

Linked artifacts not distilled in this pass:

- [Parametric workbook](../../../../idiophones/wood-shell-tongue-drum/wood-shell-tongue-drum-design-table.xlsx)
- [Capstone deck markdown](../../../../idiophones/wood-shell-tongue-drum/capstone-deck.md)
- [Capstone deck PPTX](../../../../idiophones/wood-shell-tongue-drum/capstone-deck.pptx)
- [Print packet PDF](../../../../idiophones/wood-shell-tongue-drum/print-packet.pdf)
- [Hero drawing](../../../../idiophones/wood-shell-tongue-drum/drawings/00-hero-v1-standard.svg)
- [Concept sheet](../../../../idiophones/wood-shell-tongue-drum/concepts/round-body-variants_concept-sheet.png)
- [Learn-to-play folder](../../../../idiophones/wood-shell-tongue-drum/learn-to-play/)

## Design Knowledge

The design matrix combines:

- V1: cylinder body, flat soundboard.
- V2: cylinder body, domed soundboard.
- V3: hemisphere bowl, flat soundboard.
- V4: hemisphere bowl, domed soundboard.

Sizes:

- Travel 12 in OD.
- Standard 16 in OD.
- Floor Pouf 20 in OD.

The recommended first prototype is V1 Standard 16 in because it has the lowest piece count, most predictable flat-cantilever physics, a coupled Helmholtz ratio on paper, and the fewest unknowns before calibration.

Core tongue model:

```text
f = K * t / L^2
L = sqrt(K * t / f)
```

For the default Padauk soundboard, the design uses K = 24438. This value needs calibration against actual stock.

Core cavity model:

```text
f_H = (c / 2 pi) * sqrt(A_port / (V * L_neck))
```

Design target:

```text
0.80 <= f_H / f_ding <= 1.20
```

For V1 Standard, the predicted values are A3 ding at 220 Hz and Helmholtz `f_H` around 194.6 Hz, ratio 0.88.

## Family Matrix Readout

Promising cells from the current design table:

- V1 Standard: ratio 0.88, recommended first build.
- V1 Floor Pouf: ratio 0.99, but the D3 ding tongue does not fit the current radial cap without mitigation.
- V3 Standard: ratio 1.08, likely a good second-phase build after flat/cylinder lessons.

Cells needing caution:

- V2 Standard and V4 Standard are under-coupled at current gu-port presets.
- Floor Pouf variants have tongue-fit and ergonomics risks.
- Domed variants depend on an unmeasured curved-cantilever multiplier.

## Build And Validation Logic

The Phase 1 V1 Standard build should answer the questions needed before later variants:

1. Can the 16-stave Black Walnut cylinder close, glue, and lathe-true within tolerance?
2. Does the rabbeted soundboard joint hold an airtight seal?
3. Does the actual Padauk stock match the K constant closely enough?
4. Does the gu-port tuning curve place `f_H/f_ding` inside the coupled regime?
5. Do the slit kerf, tongue lengths, and post-finish behavior keep all tongues within tuning tolerance?
6. Does the round-body form create acceptable weight, reach, and playability?

The validation report says the packet passes clean file-presence and readiness checks, but measured prototype data is not yet available.

## Release And Authority Constraints

This packet is suitable for design review and first-prototype planning. It is not yet L3/build-ready evidence.

Do not claim:

- measured acoustic performance
- validated Padauk K for Tony's actual stock
- validated Helmholtz end correction
- build-ready CAD or G-code
- real photos/audio until the prototype exists

The public-readiness pass already fixed the gu-port tuning direction across several files: increasing port area raises Helmholtz frequency.

## Cross-Links

- [[acoustic-classes/tongue-drum-wood]]
- [[synthesis/public-release-blockers]]
- [[synthesis/cad-readiness-roadmap]]
- [[synthesis/wolfram-model-patterns]]
- [[fabrication/jigs-and-fixtures]]
- [[fabrication/cnc-routing]]
- [[materials/padauk]]
- [[materials/walnut]]

## Open Questions

1. Should the first wiki distillation of the legacy rectangular `tongue-drum` repo be folded into [[acoustic-classes/tongue-drum-wood]] before more wood-shell work?
2. What measured Padauk K should replace the library value after the first A4 calibration tongue?
3. What measured Helmholtz end-correction should be added to the workbook if V1 Standard deviates by more than 10 percent?
4. Which rim seal strategy should become default if the rabbet joint leaks: lap step, cork gasket, or revised machining tolerance?
5. When should CAD/G-code become public: after poplar test disc, after first Padauk soundboard, or after full finished prototype?
6. Should Floor Pouf be redesigned around Cedar, a thinner soundboard, or a raised ding?
7. How should gu-port tuning logs be stored: `validation.csv`, a dedicated data folder, or a source summary page?
8. Should the concept sheet be preserved as ideation only, or routed into a visual/reference source summary?

## Maintenance Notes

Next ingest should inspect the workbook, Wolfram starter, and `visual-output-register` if one is added. After V1 measurements exist, update this page, [[acoustic-classes/tongue-drum-wood]], and [[synthesis/public-release-blockers]] with measured-vs-predicted deltas.
