---
title: Tongue Drum — Wooden Slit Drum (3-Instrument DoE Study)
slug: tongue-drum
wiki_type: instrument
status: active
sources:
  - path: ../../../../idiophones/tongue-drum/README.md
    kind: repo
    last_seen: 2026-06-19
crosslinks:
  - acoustic-classes/slit-tongue-idiophone
  - acoustic-classes/helmholtz-resonator-drum
  - instruments/steel-tongue-drum
  - instruments/djembe
open_questions:
  - "Has Phase 1 (small/magazine drum, ~486 measurement strikes) been executed — and what was the back-solved effective K for the species tested?"
  - "Has the medium drum (bilateral tongues) been built — and does cross-cavity coupling between the two tongue banks produce measurable pitch coupling?"
  - "What wood species were used in the Phase 1 species sweep (padauk, oak, walnut, hard maple, cherry)?"
  - "What was the Phase 3 prediction accuracy (≤10 cents RMSE target) for the large drum?"
last_ingest: 2026-06-19
tags: [instrument, drum, idiophone, tongue-drum, slit-drum, wooden, DoE, cantilever, helmholtz, 3-drum-series, magazine-plan, WOOD-magazine]
---

# Tongue Drum — Wooden Slit Drum (3-Instrument DoE Study)

## Overview

Engineering documentation for a three-instrument series of wooden tongue drums (slit drums), combined with a rigorous design-of-experiments protocol for predicting each tongue's pitch from geometry, material, and excitation. The three drums span a small magazine-baseline design, a medium original design with bilateral tongues, and a large original design with extended tonal range. Together they constitute a systematic acoustics study of the cantilever-beam slit-drum idiophone.

- **Family:** idiophone / wooden slit drum (classified as drum in manifest; lives in idiophones/ directory)
- **Three drums:**
  - Small: WOOD magazine Oct 2008 plan, 6 tongues, ~7½ × 12 × 6 in body
  - Medium: original design, bilateral tongues (both ends), original question about cross-cavity coupling
  - Large: original design, extended range, wider tongue bank
- **Key physics:** `f₁ ≈ 0.162 × (h/L²) × √(E/ρ)` — cantilever-beam frequency with Helmholtz cavity coupling
- **DoE target:** ≤10 cents RMSE prediction accuracy by Phase 3
- **Status:** L2 V5 build-packet candidate — protocol complete; physical data pending

Primary repo links:
- [README](../../../../idiophones/tongue-drum/README.md)
- [DoE protocol](../../../../idiophones/tongue-drum/docs/study/README.md)
- [Skills index](../../../../idiophones/tongue-drum/docs/SKILLS.md)

## Current Status

- Release state: L2 V5 build-packet candidate. DoE protocol, data schema, and maker research notes complete; physical measurement campaigns pending for all three phases.
- Library family: drum (manifest classification); repo lives in idiophones/ directory.
- Acoustic class: slit-tongue idiophone (wooden box body), Helmholtz cavity coupled.
- CAD state: magazine baseline scanned and attributed; original designs TBD.

## Source Notes

- [README](../../../../idiophones/tongue-drum/README.md) — three-drum series (small/medium/large), DoE protocol (three phases, ~486 strikes phase 1), cantilever formula, Helmholtz cavity coupling, skills index, maker research notes.

Artifacts not ingested: `docs/study/README.md`, `docs/study/data-template.csv`, `docs/research/ikindawannalearn-tongue-drum-notes.md`, CAD/build packets.

## Design Knowledge

Wooden tongue drums are idiophone slit drums: a hollow box body has parallel slits cut in the top panel, leaving tongue-shaped cantilever beams. Each tongue's fundamental frequency follows:

`f₁ ≈ 0.162 × (h/L²) × √(E/ρ)`

where `h` is tongue thickness, `L` is tongue free length, `E` is Young's modulus, and `ρ` is density. This makes `√(E/ρ)` the material-specific stiffness constant — different wood species (padauk, oak, walnut, hard maple, cherry) produce different constants at the same geometry.

The DoE protocol is designed to:
1. Characterize actual vs predicted `f₁` across multiple species (Phase 1 — small magazine drum, ~486 strikes)
2. Test cross-cavity coupling in a bilateral tongue design (Phase 2 — medium drum)
3. Validate predictions on a new geometry before building (Phase 3 — large drum, ≤10 cents RMSE target)

The Helmholtz cavity coupling (shared with [[instruments/djembe]]'s cavity resonance work): the air volume inside the box couples to the open body port, producing a bass resonance that adds sustain to the lowest tongue. Cavity volume and port geometry affect the coupling frequency.

The bilateral design (medium drum) is a novel configuration: tongues extend from both ends, sharing the cavity. If the two banks couple through the air volume, striking one tongue could detectably shift the resonant pitch of the opposing bank — a measurable effect that would distinguish coupled from independent cantilever behavior.

The tongue drum cultural context spans: African log slit drums (lokole, mukoma, ekwe), Mesoamerican teponaztli, steel handpan — but this study focuses on the wooden box-body form for maximum reproducibility in the DoE.

Related: [[instruments/steel-tongue-drum]] (same slit-tongue idiophone, steel body variant), [[instruments/djembe]] (Helmholtz cavity resonator skills originated here).

## Cross-Links

- [[acoustic-classes/slit-tongue-idiophone]]
- [[acoustic-classes/helmholtz-resonator-drum]]
- [[instruments/steel-tongue-drum]]
- [[instruments/djembe]]

## Open Questions

1. Has Phase 1 (~486 strikes on small/magazine drum) been executed — and what was the back-solved effective K per species?
2. Has the medium (bilateral) drum been built — and is cross-cavity coupling measurable?
3. Which species were tested in the Phase 1 species sweep?
4. Did Phase 3 achieve ≤10 cents RMSE prediction accuracy on the large drum?

## Maintenance Notes

First ingest from README only. Next pass: read `docs/study/README.md` for full DoE protocol and `docs/research/ikindawannalearn-tongue-drum-notes.md` for maker research. Check `docs/study/build/data/` for measurement data from any completed phases. Note: family=drum in manifest but repo lives in idiophones/ directory.
