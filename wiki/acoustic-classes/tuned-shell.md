---
title: Tuned Shell Acoustic Class
slug: tuned-shell
wiki_type: acoustic-class
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
  - path: ../../../ceramic-hang/wolfram-starter.wl
    kind: wolfram
    last_seen: 2026-05-18
  - path: ../../../ceramic-hang/cad/ceramic_hang_master.scad
    kind: cad
    last_seen: 2026-05-18
crosslinks:
  - instruments/ceramic-hang
  - acoustic-classes/box-drum
  - acoustic-classes/tongue-drum-wood
  - synthesis/public-release-blockers
open_questions:
  - "Should this class split into ceramic tuned shells, steel handpan shells, and hybrid tongue-shell instruments after more repos are ingested?"
  - "What minimum coupon matrix is enough before a tuned-shell packet can claim a reusable correction factor?"
  - "How should gu/body resonance be measured consistently across ceramic vessels, handpans, tongue drums, and udu-like forms?"
  - "What public badge should distinguish predicted shell tuning from measured fired-shell tuning?"
  - "Can finish damping be represented as a shared before/after validation row across ceramic shell instruments?"
answers_filed: []
last_ingest: 2026-05-18
last_lint: 2026-05-18
last_updated: 2026-05-18
review_due: 2026-08-18
tags: [acoustic-class, idiophone, shell, ceramic, handpan, helmholtz, validation]
---

# Tuned Shell Acoustic Class

## Overview

This class tracks instruments where localized musical tone fields, tongues, or relief-bounded strike zones are integrated into a curved resonant shell and may couple to an enclosed body or gu/port resonance. The first active wiki member is [[instruments/ceramic-hang]].

The class is useful for ceramic handpan-like vessels now, and may later absorb lessons from steel handpans, ceramic tongue-shell hybrids, udu-adjacent vessels, and other shell idiophones. The shared design problem is not just target pitch; it is how local field geometry, shell stiffness, body air mode, material damping, and fabrication shrinkage produce a playable result.

## Current Status

- Active member: [[instruments/ceramic-hang]].
- Evidence state: predicted and scaffolded, not measured. The current ceramic source packet has no fired tone-field measurements yet.
- Release posture: tuned-shell pages should distinguish design targets from measured acoustic evidence until validation rows exist.
- Nearby classes: [[acoustic-classes/box-drum]] for plate plus cavity instruments, and [[acoustic-classes/tongue-drum-wood]] for cut tongue/cavity idiophones.

## Source Notes

- [repo] [ceramic-hang/design.md](../../../../idiophones/ceramic-hang/design.md) supplies the first class model: coupled plate/shell vibration plus Helmholtz body resonance.
- [repo] [ceramic-hang/assembly-manual.md](../../../../idiophones/ceramic-hang/assembly-manual.md) provides the reusable empirical ladder: shrinkage bars, tone coupons, mini dome, blank shell, musical shell, finish validation.
- [repo] [ceramic-hang/validation.csv](../../../../idiophones/ceramic-hang/validation.csv) defines reusable tuned-shell rows for field geometry, measured pitch, cents error, decay, crack status, body mode, gu response, and result.
- [repo] [ceramic-hang/risks.md](../../../../idiophones/ceramic-hang/risks.md) names the major class risks: poor sustain, model error, cracking, shell slump, fragility, finish damping, shrinkage mismatch, cleanup chipping, and transport damage.
- [wolfram] [ceramic-hang/wolfram-starter.wl](../../../../idiophones/ceramic-hang/ceramic-hang-starter.wl) gives the first reusable plate and Helmholtz calculation scaffold.
- [cad] [ceramic-hang/cad/ceramic_hang_master.scad](../../../../idiophones/ceramic-hang/cad/ceramic_hang_master.scad) shows how shell, gu, shrinkage scale, and field layout can be named parameters while remaining concept-only before measured authority.

## Design Knowledge

The class-level local-field model is:

```text
tone_field_f1 ~= (kappa / (2*pi)) * (h / a^2) * sqrt(E / (rho * (1 - nu^2)))
```

Design readout:

- Increasing local thickness `h` raises the predicted field frequency.
- Increasing effective field radius `a` lowers the predicted field frequency.
- `kappa` is empirical and carries boundary, relief, and shape behavior.
- Ceramic values for `E`, `rho`, `nu`, damping, and shrinkage should be treated as measured build variables, not static catalog truth.

The class-level body/gu model is:

```text
f_gu = c/(2*pi) * sqrt(A_gu / (V_shell * L_eff_gu))
L_eff_gu = wall + 0.6 * sqrt(A_gu/pi)
```

In a tuned-shell instrument, the gu/body resonance can support warmth, air movement, and perceived sustain, but it should not be described as tuning the local tone fields unless measurements show that behavior.

Ceramic and handpan-like shell tuning pattern:

- Start with material truth: fired shrinkage bars and test bars before final master scaling.
- Run a coupon matrix before committing to a full dome. Vary field size, thickness, relief depth, radii, and clay body.
- Separate greenware, bone-dry, bisque, and glaze-fire observations because each stage can move pitch or create cracks.
- Use larger/fewer fields first if sustain or field isolation is weak.
- Treat post-fire grinding as a risk-control operation, not the primary tuning method.
- Keep finish as an acoustic variable. Glaze, oxide, burnish, and unglazed strike zones need before/after pitch and decay comparisons.
- Preserve visual and CAD authority boundaries. Rendered shells and SVG plates are not fabrication authority until tied to measured geometry and released drawings.

## Reusable Validation Pattern

Minimum rows for tuned-shell work:

- build ID and stage
- clay or shell material
- measured shrinkage and master scale factor
- wall thickness and local field thickness
- field major/minor axes or effective radius
- target note and target frequency
- measured frequency and cents error
- decay time and recording setup
- crack status and distortion notes
- body mode and gu/port frequency
- finish state and before/after shift
- handling, rim, stand, and transport notes

Measured data should promote from `validation.csv` into the relevant instrument page only after it is tied to a build ID and stage. Predicted tables remain useful, but they should not be mixed with measured rows in prose.

## Cross-Links

- [[instruments/ceramic-hang]]
- [[acoustic-classes/box-drum]]
- [[acoustic-classes/tongue-drum-wood]]
- [[synthesis/public-release-blockers]]

Potential future source streams:

- [ceramic-tongue-drum](../../../ceramic-tongue-drum)
- [udu](../../../udu)
- [handpan](../../../handpan)

## Open Questions

1. Should this class split into ceramic tuned shells, steel handpan shells, and hybrid tongue-shell instruments after more repos are ingested?
2. What minimum coupon matrix is enough before a tuned-shell packet can claim a reusable correction factor?
3. How should gu/body resonance be measured consistently across ceramic vessels, handpans, tongue drums, and udu-like forms?
4. What public badge should distinguish predicted shell tuning from measured fired-shell tuning?
5. Can finish damping be represented as a shared before/after validation row across ceramic shell instruments?

## Maintenance Notes

Update this page after the first fired ceramic coupon data lands in [[instruments/ceramic-hang]]. If `ceramic-tongue-drum`, `udu`, or `handpan` are ingested later, merge only measured or explicitly labeled design-target facts here, and keep material-specific correction factors separated.
