---
title: Ceramic Hang
slug: ceramic-hang
wiki_type: instrument
status: active
sources:
  - path: ../../../ceramic-hang/README.md
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../ceramic-hang/design.md
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../ceramic-hang/assembly-manual.md
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../ceramic-hang/validation.csv
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../ceramic-hang/risks.md
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../ceramic-hang/family-spec.csv
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../ceramic-hang/bom.csv
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../ceramic-hang/sourcing.csv
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../ceramic-hang/cut-list.csv
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../ceramic-hang/drawing-brief.md
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../ceramic-hang/visual-output-register.csv
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../ceramic-hang/v5-readiness.md
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../ceramic-hang/capstone-manifest.json
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../ceramic-hang/wolfram-starter.wl
    kind: wolfram
    last_seen: 2026-05-18
  - path: ../../../ceramic-hang/cad/ceramic_hang_master.scad
    kind: cad
    last_seen: 2026-05-18
  - path: ../../../ceramic-hang/cnc/setup-sheet.md
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../ceramic-hang/cnc/cnc-plan.json
    kind: repo
    last_seen: 2026-05-18
crosslinks:
  - acoustic-classes/tuned-shell
  - acoustic-classes/tongue-drum-wood
  - acoustic-classes/box-drum
  - instruments/wood-shell-tongue-drum
  - synthesis/public-release-blockers
open_questions:
  - "Which actual clay body and fired shrinkage value should replace the 12 percent assumption?"
  - "Which coupon geometries produce clear pitch, useful decay, and no cracking after bisque and glaze firing?"
  - "Should the musical version remain a pure raised-tone-field shell, or pivot to fewer fields, a relief/slit hybrid, or metal tone elements on a ceramic body?"
  - "Is the 9-note G minor layout feasible in ceramic, or should the first musical target stay at 5-7 notes?"
  - "How much does glaze, oxide, or burnishing shift pitch and damping on matched coupons?"
  - "What rim, cradle, stand, and transport strategy protects the shell without muting it?"
  - "Which CAD, DXF, drawing, or measurement artifact will become fabrication authority after fired evidence exists?"
  - "What measurement workflow should become standard for field pitch, cents error, decay, body mode, and gu response?"
answers_filed: []
last_ingest: 2026-05-18
last_lint: 2026-05-18
last_updated: 2026-05-18
review_due: 2026-08-18
tags: [instrument, idiophone, ceramic, handpan, tuned-shell, explorer-readiness, not-build-ready]
---

# Ceramic Hang

## Overview

The `ceramic-hang` repo is a slip-cast ceramic, handpan-inspired tonal vessel research packet. It asks whether fired ceramic shells can support playable handpan-like tone fields, while staying honest that ceramic is brittle, damped, formulation-dependent, and mostly tuned before firing.

The first serious target is an 18 in diameter, 4.5 in tall shallow vessel in a G minor 9-note layout: G3 ding plus Bb3, C4, D4, F4, G4, Bb4, C5, and D5 outer fields. The manufacturing path is 3D printed master -> plaster mold -> slip-cast upper and lower shells -> bisque measurement -> finish tests -> final validation.

Primary repo links:

- [README](../../../../idiophones/ceramic-hang/README.md)
- [Design notes](../../../../idiophones/ceramic-hang/design.md)
- [Assembly manual](../../../../idiophones/ceramic-hang/assembly-manual.md)
- [Validation table](../../../../idiophones/ceramic-hang/validation.csv)
- [Risk register](../../../../idiophones/ceramic-hang/risks.md)
- [V5 readiness ledger](../../../../idiophones/ceramic-hang/v5-readiness.md)
- [Visual authority register](../../../../idiophones/ceramic-hang/visual-output-register.csv)
- [Capstone manifest](../../../../idiophones/ceramic-hang/capstone-manifest.json)
- [OpenSCAD concept](../../../../idiophones/ceramic-hang/cad/ceramic_hang_master.scad)
- [Wolfram starter](../../../../idiophones/ceramic-hang/ceramic-hang-starter.wl)

## Current Status

- Release state: V5 explorer-readiness scaffold, not a V5 build-packet candidate.
- Fabrication authority: concept CAD and SVG previews only; no registered DXF or measured design-table authority.
- Measurement state: no fired clay-body shrinkage bars, no fired tone-field pitch/decay data, no measured shell geometry, and no strike-zone evidence yet.
- Visual state: existing SVGs and hero artwork are concept/reference artifacts only; the repo is missing a V5 hero render derived from reviewed CAD and an exploded assembly diagram.
- CAD state: [OpenSCAD starter](../../../../idiophones/ceramic-hang/cad/ceramic_hang_master.scad) has named parameters for the shell, gu, shrinkage scale, and field radii, but the file labels itself concept/master geometry rather than production CAD.
- Validation state: [validation.csv](../../../../idiophones/ceramic-hang/validation.csv) defines rows for CHG-P0 through CHG-P3, but measured frequency, cents error, decay, body mode, gu, and result fields are still blank or TBD.
- First-build stance: treat the first physical work as measurement infrastructure, not final tuning. Shrinkage bars and tone coupons come before a full musical shell.

## Source Notes

- [repo] [README](../../../../idiophones/ceramic-hang/README.md) frames the project as an empirical acoustic study first, not a conventional steel handpan clone, and names related repos: `handpan`, `ceramic-tongue-drum`, `udu`, and `tongue-drum`.
- [repo] [design.md](../../../../idiophones/ceramic-hang/design.md) defines the coupled plate/shell plus Helmholtz model, the 18 in target envelope, the G minor 9-note layout, Cone 6 casting-slip assumption, and the CHG-P0 to CHG-P4 prototype ladder.
- [repo] [assembly-manual.md](../../../../idiophones/ceramic-hang/assembly-manual.md) makes shrinkage bars the first shop step, then tone coupons, CAD/master scaling, plaster molds, slip casting, slow drying, bisque measurement, finish tests, and final validation.
- [repo] [validation.csv](../../../../idiophones/ceramic-hang/validation.csv) records the planned measurement schema: build ID, stage, clay body, shrinkage, master scale factor, field geometry, measured pitch, cents error, decay, crack status, body mode, gu, action, result, and notes.
- [repo] [risks.md](../../../../idiophones/ceramic-hang/risks.md) highlights acoustic sustain uncertainty, first-order model error, field cracking, large-dome slump/warp, lap-playing fragility, glaze damping, shrinkage mismatch, fired cleanup chipping, and transport damage.
- [repo] [family-spec.csv](../../../../idiophones/ceramic-hang/family-spec.csv) defines CHG-P1 mini 3-field dome, CHG-P2 full blank body, CHG-P3 five-note vessel, and CHG-P4 nine-note G minor target.
- [repo] [bom.csv](../../../../idiophones/ceramic-hang/bom.csv), [sourcing.csv](../../../../idiophones/ceramic-hang/sourcing.csv), and [cut-list.csv](../../../../idiophones/ceramic-hang/cut-list.csv) identify Cone 6 casting slip, #1 pottery plaster, 3D printed masters, drying cradle, firing support ring, measurement tools, finish tests, rim protection, and transport case as the practical bill of work.
- [repo] [drawing-brief.md](../../../../idiophones/ceramic-hang/drawing-brief.md) requires top, section, tone-field detail, bottom, mold split, and firing support views, while warning that dimensions must distinguish fired dimensions from master dimensions.
- [repo] [visual-output-register.csv](../../../../idiophones/ceramic-hang/visual-output-register.csv) marks the OpenSCAD file, SVG layout, SVG section, tone-field detail, and hero artwork as `concept_only`, with no fabrication-required authority.
- [repo] [v5-readiness.md](../../../../idiophones/ceramic-hang/v5-readiness.md) lists partial CAD/vector/print-packet evidence and missing V5 render, exploded diagram, measured geometry, tuning behavior, and media/export chain.
- [repo] [capstone-manifest.json](../../../../idiophones/ceramic-hang/capstone-manifest.json) repeats the readiness posture: fabrication authority is not build-ready, measurement evidence remains required, and all concept visuals must remain non-authoritative unless tied to named fabrication authority.
- [wolfram] [wolfram-starter.wl](../../../../idiophones/ceramic-hang/ceramic-hang-starter.wl) contains first-order ceramic material placeholders, a tone-field plate formula, a Helmholtz estimate for a 3.5 in gu and 700 in3 body, and G minor target rows.
- [cad] [cad/ceramic_hang_master.scad](../../../../idiophones/ceramic-hang/cad/ceramic_hang_master.scad) defines an 18 in OD, 4.5 in high, 0.25 in wall concept with 12 percent shrinkage and `master_scale_factor = 1 / (1 - shrinkage)`.
- [repo] [cnc/setup-sheet.md](../../../../idiophones/ceramic-hang/cnc/setup-sheet.md) and [cnc-plan.json](../../../../idiophones/ceramic-hang/cnc/cnc-plan.json) are pre-CAM plans for master prints and optional cottle/cradle templates, not G-code.

Linked artifacts not deeply extracted in this pass:

- [Ceramic-Hang-Design.xlsx](../../../../idiophones/ceramic-hang/Ceramic-Hang-Design.xlsx)
- [Print packet markdown](../../../../idiophones/ceramic-hang/print-packet.md)
- [Print packet PDF](../../../../idiophones/ceramic-hang/print-packet.pdf)
- [Capstone deck markdown](../../../../idiophones/ceramic-hang/capstone-deck.md)
- [Capstone deck PPTX](../../../../idiophones/ceramic-hang/capstone-deck.pptx)
- [Explorer](../../../../idiophones/ceramic-hang/explorer.html)
- [Site page](../../../../idiophones/ceramic-hang/site/index.html)

## Design Knowledge

The acoustic model combines local tone-field plate/shell behavior with a body/gu resonance:

```text
tone_field_f1 ~= (kappa / (2*pi)) * (h / a^2) * sqrt(E / (rho * (1 - nu^2)))
```

For the gu:

```text
f_gu = c/(2*pi) * sqrt(A_gu / (V_shell * L_eff_gu))
L_eff_gu = wall + 0.6 * sqrt(A_gu/pi)
```

The repo treats the tone-field equation as a sanity check, not a predictor. Ceramic material constants, boundary behavior, firing shrinkage, and damping must be replaced by test-bar and coupon measurements.

Target dimensions and assumptions:

- Outer diameter: 18 in.
- Overall height: 4.5 in.
- Fired wall thickness experiment range: 0.22-0.30 in.
- Shrinkage: 12 percent assumption until measured.
- Shell volume estimate: 600-850 in3.
- Gu diameter: 3.5 in for the first full-size prototypes.
- Clay body: Cone 6 stoneware or porcelain casting slip, not yet selected.
- Finish path: exterior-only glaze, burnish, or oxide surface, all TBD until coupon tests.

Target field layout:

| Field | Note | Target Hz | First geometry assumption |
| --- | --- | ---: | --- |
| Ding | G3 | 196.00 | 4.0 in raised oval/circle |
| T1 | Bb3 | 233.08 | 3.4 in oval |
| T2 | C4 | 261.63 | 3.2 in oval |
| T3 | D4 | 293.66 | 3.0 in oval |
| T4 | F4 | 349.23 | 2.75 in oval |
| T5 | G4 | 392.00 | 2.55 in oval |
| T6 | Bb4 | 466.16 | 2.35 in oval |
| T7 | C5 | 523.25 | 2.20 in oval |
| T8 | D5 | 587.33 | 2.05 in oval |

Prototype ladder:

- CHG-P0 tone coupons: find at least one isolated ceramic field with clear decay and measurable pitch.
- CHG-P1 mini dome: test three fields on a small shell; success means no cracks and a pitch trend that follows size/thickness.
- CHG-P2 full blank body: test full shell casting, drying, firing, seam, gu, and body mode without musical-field promises.
- CHG-P3 five-note vessel: first musical shell; success target is five fields within +/-75 cents after bisque or a clear correction path.
- CHG-P4 nine-note G minor: full handpan-inspired concept with playable hand pattern, stable fields, and acceptable sustain.

The repo's most important design rule is data closure: every prototype gets a build ID and a measured record. Ceramic handpan-like tuning only becomes predictable if fired pitch, decay, cracking, shrinkage, and shell distortion feed the next mold and thickness revision.

## Release And Authority Constraints

This packet is suitable for studio review, research planning, and coupon-stage prototyping. It is not suitable for production-ready, build-ready, or measured-performance claims.

Do not claim:

- measured tone-field tuning or sustain
- validated 12 percent shrinkage
- selected clay-body acoustic constants
- verified gu/body resonance
- build-ready CAD, DXF, G-code, or drawings
- authoritative strike-zone geometry
- real prototype photos, audio, or finished-instrument visuals

Public-facing pages should keep the distinction between steel handpan methods and this ceramic research path. Steel handpans depend on plastic forming, hammer tuning, and elastic steel plates; this ceramic packet depends on mold geometry, clay formulation, firing behavior, and pre-fire empirical correction.

## Cross-Links

- [[acoustic-classes/tuned-shell]]
- [[acoustic-classes/tongue-drum-wood]]
- [[acoustic-classes/box-drum]]
- [[instruments/wood-shell-tongue-drum]]
- [[synthesis/public-release-blockers]]

Related repo links for a future ingest:

- [handpan](../../../handpan)
- [ceramic-tongue-drum](../../../ceramic-tongue-drum)
- [udu](../../../udu)
- [tongue-drum](../../../tongue-drum)

## Open Questions

1. Which actual clay body and fired shrinkage value should replace the 12 percent assumption?
2. Which coupon geometries produce clear pitch, useful decay, and no cracking after bisque and glaze firing?
3. Should the musical version remain a pure raised-tone-field shell, or pivot to fewer fields, a relief/slit hybrid, or metal tone elements on a ceramic body?
4. Is the 9-note G minor layout feasible in ceramic, or should the first musical target stay at 5-7 notes?
5. How much does glaze, oxide, or burnishing shift pitch and damping on matched coupons?
6. What rim, cradle, stand, and transport strategy protects the shell without muting it?
7. Which CAD, DXF, drawing, or measurement artifact will become fabrication authority after fired evidence exists?
8. What measurement workflow should become standard for field pitch, cents error, decay, body mode, and gu response?

## Maintenance Notes

Next ingest should extract the workbook structure, inspect any new validation rows, and update [[acoustic-classes/tuned-shell]] with measured ceramic correction patterns. Keep [visual-output-register.csv](../../../../idiophones/ceramic-hang/visual-output-register.csv) aligned with any new CAD, render, image-generation, OpenSCAD, Blender, Illustrator, or DXF outputs.

This multi-agent round intentionally did not update `index.md`, `log.md`, manifests, generated site files, or `library.html`.
