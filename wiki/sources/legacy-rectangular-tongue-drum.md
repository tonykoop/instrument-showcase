---
title: Legacy Rectangular Tongue Drum Source Stream
slug: legacy-rectangular-tongue-drum
wiki_type: source-distillation
status: active
sources:
  - path: ../../../tongue-drum/README.md
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../tongue-drum/docs/study/README.md
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../tongue-drum/docs/study/data-template.csv
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../tongue-drum/docs/research/ikindawannalearn-tongue-drum-notes.md
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../tongue-drum/build/packet/design.md
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../tongue-drum/build/packet/phase1-cad-cnc-tuning-gate-plan.md
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../tongue-drum/build/cad/phase1-dimensions-map.csv
    kind: cad
    last_seen: 2026-05-18
  - path: ../../../tongue-drum/build/packet/phase1-geometry-gates.csv
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../tongue-drum/build/cnc/phase1-cnc-gates.csv
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../tongue-drum/build/packet/phase1-tuning-capture.csv
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../tongue-drum/build/packet/validation.csv
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../tongue-drum/cad/TNG-000_TongueDrum_ALL_CONFIGS_dimensions.csv
    kind: cad
    last_seen: 2026-05-18
crosslinks:
  - acoustic-classes/tongue-drum-wood
  - instruments/wood-shell-tongue-drum
open_questions:
  - "Should the rectangular-box branch eventually get an active instrument page, or remain a source stream until it appears in data/library-manifest.json?"
  - "Which Phase 1 wood species will be built first, and which stock properties should replace catalog density/E values?"
  - "Does the seeded TUNE-001 row represent measured prototype evidence, a template/example row, or an imported planning placeholder?"
  - "What correction factor emerges from measured slit-boundary conditions, end-cap stiffness, kerf width, undercut radius, and removable-bottom state?"
  - "How strongly do opposed tongue banks in the planned medium bilateral design couple through the shared cavity?"
  - "Should the 12-cent sharp-bias / rough-cut-length logic become a shared field in the wood tongue-drum class?"
  - "How should fair-use WOOD magazine plan scans be represented in public wiki/library outputs?"
last_ingest: 2026-05-18
tags: [source, tongue-drum, wood, rectangular, slit-drum, doe, cad-gated]
---

# Legacy Rectangular Tongue Drum Source Stream

## Overview

The local [`tongue-drum`](../../../../idiophones/tongue-drum/README.md) repo is a legacy/source stream for the rectangular-box branch of the wooden tongue drum family. It documents a planned three-phase build and measurement study: a small magazine-plan baseline, a medium original bilateral-tongue design, and a larger extended-range design.

This page is a source distillation rather than an active instrument page. The repo is not currently represented in [`data/library-manifest.json`](../../data/library-manifest.json), and its own status language keeps the first build, medium CAD, large CAD, and Phase 1 measurement data as forthcoming or gated. The active library-linked wooden tongue drum remains [[instruments/wood-shell-tongue-drum]], while this source feeds the broader [[acoustic-classes/tongue-drum-wood]] knowledge base.

Direct source entry points:

- [GitHub repo](https://github.com/tonykoop/tongue-drum)
- [Local README](../../../../idiophones/tongue-drum/README.md)
- [Study protocol](../../../../idiophones/tongue-drum/docs/study/README.md)
- [Maker research notes](../../../../idiophones/tongue-drum/docs/research/ikindawannalearn-tongue-drum-notes.md)
- [Phase 1 CAD/CNC/tuning gate plan](../../../../idiophones/tongue-drum/build/packet/phase1-cad-cnc-tuning-gate-plan.md)
- [Phase 1 dimensions map](../../../../idiophones/tongue-drum/build/cad/phase1-dimensions-map.csv)

## Current Status

- Source status: substantial documentation and scaffolded CAD/CNC/tuning evidence loop, but not a library-manifest instrument.
- Build status in the source repo: small drum first build forthcoming; medium and large CAD forthcoming; Phase 1 measurement data forthcoming.
- Study status in the protocol: documentation only; no completed dataset yet.
- CAD/CNC authority: Phase 1 geometry rows are explicitly `reference_only` and blocked by shop, kerf, workholding, and tuning gates.
- Public source caution: the WOOD magazine plan scans are attributed and framed as fair-use portfolio context in the source repo; do not treat those scans as Tony-authored reusable assets.

## Source Notes

- [repo] [README](../../../../idiophones/tongue-drum/README.md) frames the project as engineering documentation for three planned rectangular tongue drums plus a design-of-experiments protocol for predicting each tongue key from geometry, material, and excitation. The small baseline follows the WOOD magazine October 2008 "Tones-of-Fun Tongue Drum" plan; the medium and large designs are original follow-ons.
- [repo] [Study protocol](../../../../idiophones/tongue-drum/docs/study/README.md) defines the core research questions: wood-property variance, geometric tuning levers, whether the cantilever model can predict fundamentals within +/-10 cents, cavity/radiated-frequency coupling, mallet/strike effects, environmental drift, and bilateral tongue-bank coupling.
- [repo] [Study protocol](../../../../idiophones/tongue-drum/docs/study/README.md) uses the cantilever scaling model `f1 ~= 0.162 * (h / L^2) * sqrt(E / rho)` and treats it as a scaling guide that needs empirical correction for slit boundaries, undercut radius, and panel coupling.
- [repo] [Study protocol](../../../../idiophones/tongue-drum/docs/study/README.md) plans Phase 1 around the small magazine baseline: a deep first-build session of 3 mallet hardnesses x 3 strike forces x 3 strike locations x 3 repeats x 6 tongues, or about 486 strikes, followed by a species sweep.
- [repo] [Study data template](../../../../idiophones/tongue-drum/docs/study/data-template.csv) is a strike-level schema that already includes geometry, species, density, moisture, grain, E reference, cavity variables, mallet variables, strike force/location, fundamentals/overtone peaks, inharmonicity, SPL, decay, spectral centroid, Q, cents error, and notes.
- [repo] [Maker research notes](../../../../idiophones/tongue-drum/docs/research/ikindawannalearn-tongue-drum-notes.md) distill external maker heuristics into repo recommendations: plan playable chord zones, use cantilever calculators over the old 6 percent length rule, rough-cut slightly sharp, tune before permanently closing the box, track end-cap stiffness, treat wood values as priors, and measure with FFT-capable tooling rather than relying on a phone tuner.
- [repo] [Build packet design](../../../../idiophones/tongue-drum/build/packet/design.md) identifies TNG-001 as the small magazine baseline, design stage `Research`, build status `Idea`, priority `High`, CAD design ID `CAD-TONGUE-12`, CNC plan ID `CNC-TONGUE-12`, primary material "Steel or hardwood top", and next step "Decide steel vs hardwood tongue approach; define tuning cuts."
- [cad] [Phase 1 dimensions map](../../../../idiophones/tongue-drum/build/cad/phase1-dimensions-map.csv) transcribes the review geometry for `Small_Baseline_6T`: 18.0 in length, 10.0 in width, 0.5 in top thickness, 5.0 in cavity height, 0.075 in slit kerf, 0.25 in slit-end radius, 0.060 in tongue root gap, and six review tongue lengths ranging from about 5.9 to 8.6 in. All rows are `reference_only`.
- [repo] [Phase 1 gate plan](../../../../idiophones/tongue-drum/build/packet/phase1-cad-cnc-tuning-gate-plan.md), [geometry gates](../../../../idiophones/tongue-drum/build/packet/phase1-geometry-gates.csv), [CNC gates](../../../../idiophones/tongue-drum/build/cnc/phase1-cnc-gates.csv), and [validation loop](../../../../idiophones/tongue-drum/build/packet/validation-loop.csv) define a healthy authority boundary: no CNC slot dimensions from model geometry alone; no tuning claim before strike capture; no full panel CAM release before fixture, datum, kerf, compensation, and first-article checks close.
- [repo] [Phase 1 tuning capture](../../../../idiophones/tongue-drum/build/packet/phase1-tuning-capture.csv) seeds target/capture rows for early C4/D4/D#4 tongue tracking, but most rows are blocked pending capture. Treat this table as an evidence scaffold until the source owner confirms which rows came from physical measurements.
- [cad] [SolidWorks dimension export](../../../../idiophones/tongue-drum/cad/TNG-000_TongueDrum_ALL_CONFIGS_dimensions.csv) includes global equations for body envelope, top/bottom/side/end thicknesses, port diameter, foot geometry, `sharp_bias_cents = 12`, `rough_len_factor`, tongue MIDI notes, bank assignments, tongue widths, and the phase-one tongue-length values.

## Design Knowledge

What this stream contributes to [[acoustic-classes/tongue-drum-wood]]:

- Rectangular-box contrast case. It represents the open/box-style wooden slit-tongue branch, distinct from the enclosed round-body [[instruments/wood-shell-tongue-drum]] branch.
- A stronger empirical plan for flat wooden tongues. The protocol is centered on measured strike data, material density/moisture/grain capture, and predicted-vs-measured tuning error rather than only workbook calculations.
- Shared cantilever vocabulary. Length is the dominant lever through `1 / L^2`; thickness is linear; specific stiffness enters as `sqrt(E / rho)`; slit-boundary details need correction factors.
- Reusable validation schema. The strike-level data template is broader than the current round-body validation rows and could seed class-wide measurement tables for tongue response, mallet response, environmental drift, and spectral quality.
- Shop authority pattern. The Phase 1 gate plan is a useful template for keeping CAD/CNC output at `reference_only` until kerf coupons, fixture registration, first-article cuts, and tuning capture provide evidence.
- Musical-layout lesson. The maker notes argue that target notes should be stored with playable chord zones or scale-degree groupings, not only as isolated target frequencies.
- Practical tuning lesson. Rough cuts should start slightly sharp because lowering a tongue is usually easier than raising it; the CAD export currently encodes a 12-cent sharp-bias concept, but it has not been validated.
- Construction lesson. Tuning access matters. The source notes prefer a removable or clamped bottom during first tuning, plus explicit tracking of bottom state, end-cap stiffness, and slit terminus reference.

## Cross-Links

- [[acoustic-classes/tongue-drum-wood]]
- [[instruments/wood-shell-tongue-drum]]

## Open Questions

1. Should the rectangular-box branch eventually get an active instrument page, or remain a source stream until it appears in `data/library-manifest.json`?
2. Which Phase 1 wood species will be built first, and which measured stock properties should replace catalog density/E values?
3. Does the seeded `TUNE-001` row represent measured prototype evidence, a template/example row, or an imported planning placeholder?
4. What correction factor emerges from measured slit-boundary conditions, end-cap stiffness, kerf width, undercut radius, and removable-bottom state?
5. How strongly do opposed tongue banks in the planned medium bilateral design couple through the shared cavity?
6. Should the 12-cent sharp-bias / rough-cut-length logic become a shared field in the wood tongue-drum class?
7. How should fair-use WOOD magazine plan scans be represented in public wiki/library outputs?

## Maintenance Notes

This source should be re-ingested after any of these events: the first small drum is built, Phase 1 strike data lands, the medium bilateral CAD appears, the large extended-range geometry is defined, or `tongue-drum` is added to `data/library-manifest.json`.

Per the multi-agent ingest scope for this pass, this page was added without editing [[acoustic-classes/tongue-drum-wood]], `wiki/index.md`, `wiki/log.md`, manifests, or generated site files.
