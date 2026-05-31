---
title: Slip-Cast Ceramic Tongue Drum Family
slug: ceramic-tongue-drum
wiki_type: instrument
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
  - path: ../../../ceramic-tongue-drum/assembly-manual.md
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../ceramic-tongue-drum/risks.md
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../ceramic-tongue-drum/resources.md
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../ceramic-tongue-drum/jig-decision.md
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../ceramic-tongue-drum/validation-report.md
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../ceramic-tongue-drum/visual-output-register.csv
    kind: spreadsheet
    last_seen: 2026-05-18
  - path: ../../../ceramic-tongue-drum/capstone-manifest.json
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../ceramic-tongue-drum/wolfram-starter.wl
    kind: wolfram
    last_seen: 2026-05-18
crosslinks:
  - acoustic-classes/tongue-drum-ceramic
  - acoustic-classes/tongue-drum-wood
  - instruments/wood-shell-tongue-drum
  - synthesis/public-release-blockers
open_questions:
  - "What measured Cone-6 stoneware K should replace the derived K = 33806 after CTD-M-P1 coupon and tongue tests?"
  - "What same-batch wet-to-bisque and wet-to-final shrinkage should replace the planning 12 percent / 1.136 master scale?"
  - "Do CTD-M-P1 leather-hard 1 mm slits with relief holes survive drying, bisque, glaze fire, and final play without cracks?"
  - "How much pitch drift does glaze mass introduce when tongue tops, slit edges, and gu rim are wax-resisted?"
  - "Does CTD-M's predicted 0.94 Helmholtz-to-ding ratio survive real chamber measurement after firing?"
  - "Should CTD-S and CTD-L be re-ported/re-shaped for stronger chamber coupling, or documented as intentionally more bare-tongue voices?"
  - "When should current SVG slit templates become fabrication authority: after CAD/DXF review, after CTD-M-P1 measured correction, or both?"
  - "Where should the first per-family corrections database results be summarized for the wiki?"
answers_filed: []
last_ingest: 2026-05-18
last_lint: 2026-05-18
review_due: 2026-08-18
tags: [instrument, drum, tongue-drum, ceramic, slip-cast, private-review]
---

# Slip-Cast Ceramic Tongue Drum Family

## Overview

The `ceramic-tongue-drum` repo is a prototype-planning packet for a slip-cast Cone-6 stoneware tongue drum family. It fills the cantilever-idiophone plus slip-cast process cell in the broader instrument-maker catalogue: a fired ceramic top plate is cut into tongues, and the hollow shell underneath provides a Helmholtz chamber through the underside gu.

The family has three members:

- CTD-S: 10 in x 5 in, A-Kurd, A4 ding, 9 tongues total.
- CTD-M: 12 in x 6 in, D-Kurd, D4 ding, 9 tongues total, first production target.
- CTD-L: 14 in x 7 in, G-Kurd, G3 ding, 9 tongues total.

The design intent is not "wood tongue drum in clay." The packet expects fired stoneware to raise the cantilever K constant from the tonewood range into a derived estimate of `K = 33806`, increase Q into the roughly 150-300 range, and produce a brighter, more bell-like inharmonic ring than [[instruments/wood-shell-tongue-drum]].

Primary repo links:

- [README](../../../../idiophones/ceramic-tongue-drum/README.md)
- [Design notes](../../../../idiophones/ceramic-tongue-drum/design.md)
- [Family spec](../../../../idiophones/ceramic-tongue-drum/family-spec.csv)
- [Tongue spec](../../../../idiophones/ceramic-tongue-drum/tongue-spec.csv)
- [Assembly manual](../../../../idiophones/ceramic-tongue-drum/assembly-manual.md)
- [Validation table](../../../../idiophones/ceramic-tongue-drum/validation.csv)
- [Validation report](../../../../idiophones/ceramic-tongue-drum/validation-report.md)
- [Risks](../../../../idiophones/ceramic-tongue-drum/risks.md)
- [Resources](../../../../idiophones/ceramic-tongue-drum/resources.md)
- [Jig decision log](../../../../idiophones/ceramic-tongue-drum/jig-decision.md)
- [Visual authority register](../../../../idiophones/ceramic-tongue-drum/visual-output-register.csv)
- [Capstone manifest](../../../../idiophones/ceramic-tongue-drum/capstone-manifest.json)
- [Wolfram starter](../../../../idiophones/ceramic-tongue-drum/wolfram-starter.wl)

## Current Status

- Release state: private research / prototype planning / V5 explorer readiness.
- Fabrication authority: not build-ready; design tables and reviewed planning sources are authoritative, while current SVGs and explorer visuals are review/support artifacts unless promoted by CAD/DXF/design-table evidence.
- First prototype target: CTD-M-P1, because its predicted Helmholtz-to-ding ratio is 0.94 and it is the workbook standard target.
- Validation state: root-mode validator passed on 2026-05-08 with no findings, but no fired prototype measurements exist yet.
- Public-release gate: keep private until CTD-M-P1 is cast, bisque-fired, glaze-fired, measured, and crack-inspected.
- V5 gap state: OpenSCAD master, DXF exports, Blender renders, exploded diagram, assembly plate, and MCP provenance log remain future work.
- CAD state: `cad/sw-design-table.xlsx` exists for SolidWorks configurations; the packet does not yet contain complete V5 CAD authority.

Do not claim measured acoustic output, validated shrinkage, validated fired ceramic K, validated slot survival, glaze-safe sustained ring, or production-ready dimensions until CTD-M-P1 closes those gates.

## Source Notes

- [repo] [README](../../../../idiophones/ceramic-tongue-drum/README.md) positions the packet as prototype planning, defines CTD-S/M/L, explains the ceramic timbre goal, lists sister slip-cast and cantilever repos, and names CTD-M-P1 as the release-relevant first prototype.
- [repo] [Design notes](../../../../idiophones/ceramic-tongue-drum/design.md) define the coupled cantilever-beam plus Helmholtz model, the derived Cone-6 stoneware K constant, inharmonic mode ratios, family scaling law, process chain, and guardrails against applying wood or NAF corrections.
- [spreadsheet] [Family spec](../../../../idiophones/ceramic-tongue-drum/family-spec.csv) records CTD-S/M/L shell dimensions, gu diameters, chamber volumes, predicted Helmholtz frequencies, coupling ratios, shrinkage assumption, clay body, and per-member notes.
- [spreadsheet] [Tongue spec](../../../../idiophones/ceramic-tongue-drum/tongue-spec.csv) records all 27 tongue targets and first-order fired lengths; all currently fit their member envelopes on paper.
- [spreadsheet] [Validation table](../../../../idiophones/ceramic-tongue-drum/validation.csv) is a planned measurement ledger for coupons, slot survival, greenware, bisque, post-tune, glaze-fire, and final-fired rows. Measurement columns are currently blank.
- [repo] [Assembly manual](../../../../idiophones/ceramic-tongue-drum/assembly-manual.md) defines the shop sequence: master print, plaster mold, slip cast, leather-hard slit cut, slow dry, Cone 06 bisque, bisque tuning, wax-resist glaze, Cone 6 final fire, and small post-glaze wet abrasive correction only.
- [repo] [Risks](../../../../idiophones/ceramic-tongue-drum/risks.md) is the red-team gate. High-severity risks are derived ceramic K, per-batch slip shrinkage, and glaze bridging slit kerfs.
- [repo] [Resources](../../../../idiophones/ceramic-tongue-drum/resources.md) states the private-research release gate and lists the minimum CTD-M-P1 measurements needed before public claims.
- [repo] [Jig decision log](../../../../idiophones/ceramic-tongue-drum/jig-decision.md) selects low-force ceramic jigs only and rejects CNC routing, laser cutting clay, adhesive templates, and post-fire slot relocation as production workflows.
- [repo] [Validation report](../../../../idiophones/ceramic-tongue-drum/validation-report.md) records a clean root-mode packet validator result and restates conservative fired-slot and public-release guidance.
- [spreadsheet] [Visual output register](../../../../idiophones/ceramic-tongue-drum/visual-output-register.csv) separates design-table authority from derived SVG previews and concept-only support images.
- [repo] [Capstone manifest](../../../../idiophones/ceramic-tongue-drum/capstone-manifest.json) gives the current readiness state, V5 gaps, entrypoints, authority files, and validation commands.
- [wolfram] [Wolfram starter](../../../../idiophones/ceramic-tongue-drum/wolfram-starter.wl) reproduces cantilever and Helmholtz predictions, inharmonic spectra, and a Q-based strike synthesis stub.

Linked artifacts not distilled in this pass:

- [Parametric workbook](../../../../idiophones/ceramic-tongue-drum/ceramic-tongue-drum-design-table.xlsx)
- [SolidWorks design table](../../../../idiophones/ceramic-tongue-drum/cad/sw-design-table.xlsx)
- [Explorer](../../../../idiophones/ceramic-tongue-drum/explorer.html)
- [Print packet PDF](../../../../idiophones/ceramic-tongue-drum/print-packet.pdf)
- [Capstone deck](../../../../idiophones/ceramic-tongue-drum/capstone-deck.md)
- [Drawing brief](../../../../idiophones/ceramic-tongue-drum/drawing-brief.md)
- [Supplier RFQ](../../../../idiophones/ceramic-tongue-drum/supplier-rfq.md)
- [Photo shotlist](../../../../idiophones/ceramic-tongue-drum/photo-shotlist.md)

## Design Knowledge

The governing tongue model is the same fixed-free cantilever relationship used by the wood tongue-drum family, but with a different material constant:

```text
f = K * t / L^2
L = sqrt(K * t / f)
```

The current Cone-6 stoneware estimate is:

```text
K_imp = 33806
t = 0.197 in, or 5 mm fired tongue thickness
```

This makes a stoneware tongue shorter than a Padauk tongue at the same pitch and thickness, which is why 5 mm ceramic tongues fit inside 10/12/14 in shells on paper. The packet treats this as a derived estimate until measured CTD-M-P1 coupons and tongues update the correction database.

The chamber model is:

```text
f_H = (c / 2 pi) * sqrt(A_port / (V * L_eff))
L_eff = wall_thickness + 0.6 * sqrt(A_port / pi)
V = (pi / 6) * shell_diameter^2 * shell_height * shape_factor
```

Design assumptions:

- `c = 13510 in/s` at about 68 F.
- Shape factor is 0.70 for the lenticular shell.
- Wall thickness and tongue thickness are both nominally 5 mm fired.
- Warm coupling target is about 0.85-1.15 times the ding, with the wood-shell packet's empirical preference around 0.95.

Family readout from the current table:

| Member | Ding | Shell | Gu | Predicted f_H | Ratio | Readout |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| CTD-S | A4 / 440 Hz | 10 x 5 in | 2.0 in | 314.8 Hz | 0.715 | Outside warm-coupling band; likely more bare-tongue unless re-shaped or re-ported. |
| CTD-M | D4 / 293.66 Hz | 12 x 6 in | 2.5 in | 274.7 Hz | 0.935 | In band; first production target. |
| CTD-L | G3 / 196 Hz | 14 x 7 in | 3.0 in | 243.1 Hz | 1.240 | Outside band; needs smaller port and/or larger chamber if warmth is the target. |

The cantilever overtone series is inharmonic:

```text
mode ratios = 1.000, 6.267, 17.547, 34.386, 56.843
```

That mode-2 ratio is a feature of the intended bell-like ceramic voice, not a defect to tune out.

## Build And Validation Logic

The source packet's first-build logic is coupon-gated:

1. Cast same-batch shrinkage and slot-survival coupons with CTD-M-P1.
2. Verify actual shrinkage before trusting the 12 percent planning value or 1.136 master scale.
3. Cut leather-hard slits with a 1 mm pottery wire using pinned slit-template cards, not adhesive templates.
4. Add relief holes at slit ends to reduce crack concentration.
5. Slow-dry before Cone 06 bisque and inspect all slot ends under raking light.
6. Measure the first bisque strike and back-calculate ceramic K.
7. Tune at bisque with small wet sanding/filing only.
8. Wax-resist tongue tops, slit edges, and gu rim before Cone 6 glaze fire.
9. Measure final pitch, sustain, chamber response, cracks, and glaze bridges before any public claim.

Post-fire slot relocation is not an approved workflow. Fired tuning is limited to small wet abrasive correction on crack-free ceramic, with silica-dust controls.

## Release And Authority Constraints

This page should use [[synthesis/public-release-blockers]] language: the packet is complete enough for research planning, RFQs, and first-build validation, but not enough for public build instructions or product claims.

Current authority split:

- Design dimensions: root workbook, `family-spec.csv`, `tongue-spec.csv`, and SolidWorks design table.
- Visual support: existing SVG drawings, explorer, placeholder images, and site assets.
- Fabrication authority missing: reviewed V5 CAD, DXF exports, measured shrinkage correction, measured fired K correction, and CTD-M-P1 validation data.

The visual-output register explicitly marks SVG previews as derived previews and concept/support images as concept-only. Do not treat the current slit-template SVGs as release-ready fabrication authority without the measured ceramic correction loop.

## Cross-Links

- [[acoustic-classes/tongue-drum-ceramic]]
- [[acoustic-classes/tongue-drum-wood]]
- [[instruments/wood-shell-tongue-drum]]
- [[synthesis/public-release-blockers]]

## Open Questions

1. What measured Cone-6 stoneware K should replace the derived `K = 33806` after CTD-M-P1 coupon and tongue tests?
2. What same-batch wet-to-bisque and wet-to-final shrinkage should replace the planning 12 percent / 1.136 master scale?
3. Do CTD-M-P1 leather-hard 1 mm slits with relief holes survive drying, bisque, glaze fire, and final play without cracks?
4. How much pitch drift does glaze mass introduce when tongue tops, slit edges, and gu rim are wax-resisted?
5. Does CTD-M's predicted 0.94 Helmholtz-to-ding ratio survive real chamber measurement after firing?
6. Should CTD-S and CTD-L be re-ported/re-shaped for stronger chamber coupling, or documented as intentionally more bare-tongue voices?
7. When should current SVG slit templates become fabrication authority: after CAD/DXF review, after CTD-M-P1 measured correction, or both?
8. Where should the first per-family corrections database results be summarized for the wiki?

## Maintenance Notes

Next ingest should happen after CTD-M-P1 has coupon, bisque, post-tune, glaze-fire, and final-fired rows populated in `validation.csv`. Update this page, [[acoustic-classes/tongue-drum-ceramic]], and [[synthesis/public-release-blockers]] with measured-vs-predicted deltas, but do not promote CTD-S/CTD-L claims until CTD-M's ceramic K and shrinkage corrections are applied to those members.
