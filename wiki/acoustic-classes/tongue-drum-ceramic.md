---
title: Ceramic Tongue Drum Acoustic Class
slug: tongue-drum-ceramic
wiki_type: acoustic-class
status: active
sources:
  - path: ../../../ceramic-tongue-drum/README.md
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../ceramic-tongue-drum/design.md
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../ceramic-tongue-drum/family-spec.csv
    kind: spreadsheet
    last_seen: 2026-05-18
  - path: ../../../ceramic-tongue-drum/tongue-spec.csv
    kind: spreadsheet
    last_seen: 2026-05-18
  - path: ../../../ceramic-tongue-drum/validation.csv
    kind: spreadsheet
    last_seen: 2026-05-18
  - path: ../../../ceramic-tongue-drum/risks.md
    kind: repo
    last_seen: 2026-05-18
crosslinks:
  - instruments/ceramic-tongue-drum
  - acoustic-classes/tongue-drum-wood
  - instruments/wood-shell-tongue-drum
  - synthesis/public-release-blockers
open_questions:
  - "Should ceramic tongue drums inherit the wood-shell target of f_H/f_ding around 0.95, or should ceramic Q and inharmonicity move the preferred coupling target?"
  - "How should measured fired ceramic K be stored so later ceramic cantilever instruments can reuse it without overgeneralizing across clay bodies?"
  - "Does a ceramic tongue's higher Q require different strike, sustain, and damping validation rows than wood tongue drums?"
  - "Should CTD-S and CTD-L remain in one acoustic family if their chamber coupling is intentionally outside the warm-coupling band?"
  - "What visual/fabrication authority threshold is required before slit-template drawings become reusable class examples?"
answers_filed: []
last_ingest: 2026-05-18
last_lint: 2026-05-18
review_due: 2026-08-18
tags: [acoustic-class, drum, tongue-drum, ceramic, slip-cast]
---

# Ceramic Tongue Drum Acoustic Class

## Overview

This page tracks slip-cast ceramic slit-tongue instruments where fired-clay tongues behave as fixed-free cantilevers cut into a ceramic top plate, with a vessel shell below acting as a Helmholtz chamber. The first active member is [[instruments/ceramic-tongue-drum]].

This class is the ceramic cousin of [[acoustic-classes/tongue-drum-wood]]. Both use the same cantilever equation and both can couple to an enclosed chamber, but the material/process constraints are different enough to deserve a separate page:

- Wood tongues are cut from dry boards and can often be routed or laser-patterned before final tuning.
- Ceramic tongues are cut at leather-hard greenware, then must survive drying, bisque, glaze, and final fire.
- Wood K values can be species-calibrated; ceramic K depends on clay body, firing schedule, density, moisture, and glaze/mass effects.
- Wood damping supports a warmer, shorter ring; fired stoneware is expected to ring longer with stronger inharmonic partials.

## Current Status

- Active instrument: [[instruments/ceramic-tongue-drum]].
- Evidence state: predicted/prototype planning only; no measured fired CTD-M-P1 data yet.
- Shared release posture: private research until measured prototype data closes ceramic K, shrinkage, slot survival, glaze-bridge, and chamber-response questions.
- Conceptual bridge: use [[acoustic-classes/tongue-drum-wood]] as the closest cantilever/Helmholtz reference, but do not transfer wood material constants or wood fabrication assumptions.

## Source Notes

- [repo] [README](../../../../idiophones/ceramic-tongue-drum/README.md) summarizes the full ceramic packet, release posture, source links, and validation gates.
- [repo] [Design notes](../../../../idiophones/ceramic-tongue-drum/design.md) establish the ceramic cantilever and Helmholtz model, derived Cone-6 stoneware K, inharmonic mode ratios, and guardrails against importing unrelated correction tables.
- [spreadsheet] [Family spec](../../../../idiophones/ceramic-tongue-drum/family-spec.csv) gives CTD-S/M/L shell sizes, gu diameters, predicted chamber frequencies, and coupling ratios.
- [spreadsheet] [Tongue spec](../../../../idiophones/ceramic-tongue-drum/tongue-spec.csv) gives first-order fired tongue lengths for all 27 tongues across the family.
- [spreadsheet] [Validation table](../../../../idiophones/ceramic-tongue-drum/validation.csv) defines the measurement rows this class should expect from ceramic tongue-drum prototypes.
- [repo] [Risks](../../../../idiophones/ceramic-tongue-drum/risks.md) identifies the reusable ceramic-class hazards: derived K, shrinkage variance, slot-end cracks, CTD-L slumping, glaze bridging, and post-fire tuning limits.

## Design Knowledge

The reusable model is:

```text
f = K * t / L^2
L = sqrt(K * t / f)
```

The current ceramic packet uses `K = 33806` for Cone-6 stoneware, `t = 0.197 in`, and a 1 mm slit kerf. That value is a derived estimate, not a measured class constant.

The chamber model is the same family as the wood-shell tongue drum:

```text
f_H = (c / 2 pi) * sqrt(A_port / (V * L_eff))
```

For first-pass warm coupling, the ceramic packet borrows the wood-shell target of roughly `0.85 <= f_H/f_ding <= 1.15`, with the most promising member at 0.94. This borrowed range is an explicit hypothesis. Ceramic Q and inharmonicity may change what players experience as the best coupling point.

Current family behavior:

- CTD-M is the class's first useful calibration build because its predicted chamber ratio is in band.
- CTD-S and CTD-L are useful boundary cases: both fit their tongue lengths, but both are outside the warm-coupling band.
- If S/L are kept, the class may need to distinguish "coupled ceramic tongue drum" from "bare-tongue ceramic vessel drum" as two voicing modes under one process family.

## Fabrication Pattern

Ceramic tongue drums should use a low-force slip-cast workflow:

1. Scale masters from measured same-batch shrinkage, not a generic shrinkage number.
2. Cast a two-piece plaster mold around sealed printed masters.
3. Slip-cast the vessel and demold at leather-hard.
4. Register slit templates mechanically, such as toothpicks or pins, rather than adhesive.
5. Cut slits with a pottery wire while greenware is leather-hard.
6. Add rounded relief holes at slit ends when crack risk matters.
7. Slow-dry and bisque before tuning.
8. Tune with wet abrasive methods only, and only inside a small correction range.
9. Wax-resist tongue tops, slit edges, and gu rim before glaze.
10. Treat fired-slot relocation as destructive test work, not production tuning.

CNC and laser operations may make support tooling, cottles, or chipboard templates. They should not touch greenware, bisque, or final-fired ceramic bodies in the current class pattern.

## Validation Pattern

Reusable validation rows for this class:

- same-batch shrinkage coupon: green, bisque, final-fired dimensions and density
- slot-survival coupon with relief holes
- wall and tongue thickness grid after bisque and final fire
- slit length and kerf verification before firing
- crack inspection under raking light at every slot end and gu rim
- bisque pitch for all tongues
- measured K back-calculation from at least three tongues/coupons
- Helmholtz response with ding damped
- post-tune pitch and material-removal notes
- glaze-bridge inspection and final sustain time
- final-fired pitch/cents error for all tongues
- stand/foot-ring isolation check for large ceramic bodies

## Relationship To Wood Tongue Drums

Use [[acoustic-classes/tongue-drum-wood]] as the closest conceptual sibling:

- Same cantilever pitch equation.
- Same general chamber-coupling intuition.
- Same need for measured-vs-predicted pitch rows.
- Same release blocker around predictions that have not yet been physically measured.

Keep these separate:

- Wood species K tables do not apply to fired stoneware.
- Wood humidity drift is not the same as ceramic shrinkage/firing drift.
- Wood routing/laser workflows do not transfer to greenware slit cutting.
- Wood post-cut tuning latitude is much larger than ceramic post-fire slot correction.
- Ceramic validation must inspect crack, glaze, and silica-dust hazards that do not dominate the wood class.

## Cross-Links

- [[instruments/ceramic-tongue-drum]]
- [[acoustic-classes/tongue-drum-wood]]
- [[instruments/wood-shell-tongue-drum]]
- [[synthesis/public-release-blockers]]

## Open Questions

1. Should ceramic tongue drums inherit the wood-shell target of `f_H/f_ding` around 0.95, or should ceramic Q and inharmonicity move the preferred coupling target?
2. How should measured fired ceramic K be stored so later ceramic cantilever instruments can reuse it without overgeneralizing across clay bodies?
3. Does a ceramic tongue's higher Q require different strike, sustain, and damping validation rows than wood tongue drums?
4. Should CTD-S and CTD-L remain in one acoustic family if their chamber coupling is intentionally outside the warm-coupling band?
5. What visual/fabrication authority threshold is required before slit-template drawings become reusable class examples?

## Maintenance Notes

When CTD-M-P1 measurements exist, update this page with measured K, shrinkage, chamber ratio, sustain, and glaze-bridge results. If the CTD-M data contradicts the borrowed wood-shell coupling target, record that as a ceramic-specific acoustic-class finding rather than silently editing the design assumptions.
