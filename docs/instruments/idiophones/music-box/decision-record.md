<!-- SPDX-License-Identifier: CC-BY-4.0 -->
# Decision Record

## Decisions

- Readiness is promoted from `L1 concept packet` to `L2 V5 build-packet candidate`.
- The instrument is treated as a pinned-cylinder steel-comb idiophone with a
  regulated mechanical timing system.
- The first risks are tooth speech, pin release, cylinder-to-comb alignment,
  governor stability, escapement noise, and service access.
- The packet intentionally avoids pitch ranges, tooth geometry, pin
  coordinates, cylinder dimensions, governor dimensions, and CAD/DXF outputs.
- Every authority-bearing packet row is `concept_only` or
  `pending_measurement`; no artifact is fabrication authority.
- L2 adds subsystem interfaces, a fuller BOM, and a planning-only cut list
  without adding dimensions or tuning values.
- Comb, program cylinder, governor, drive, frame, and resonance authority are
  separated so future prototype evidence can promote only the parts that are
  actually measured.

## L2 Uplift Notes

- `README.md` now declares `Status: L2 V5 build-packet candidate`.
- `design.md` now names authority domains, prototype sequence, L3 evidence
  requirements, and packet interfaces.
- `bom.csv` now separates part families, estimate status, review need, and
  subsystem authority.
- `cut-list.csv` was added as a pending-measurement planning surface only.
- The packet still blocks build-ready, CAD, DXF, tuning, and fabrication
  claims.

## Open Questions

- Should the first test be a one-tooth coupon, a small comb coupon, or a simple
  hand-cranked cylinder strip?
- What comb steel and heat treatment can be tuned repeatably in the shop?
- How should pins lift and release teeth without scraping or fatigue damage?
- What governor style is quiet enough for a small acoustic instrument?
- Should the drive be spring-powered, crank-powered, weight-powered, or a bench
  test motor for early measurement only?
- How should the case support resonance without amplifying gear noise?
- What service access is needed for pin replacement and comb retuning?
- What validation log format should capture timing, speed stability, and tooth
  response?
- Which authority source should be accepted for the first full comb: measured
  shop coupon, reviewed commercial comb, or specialist-reviewed drawing?
- Should the first cylinder be a short registration mule or a full tune program
  with most lanes disabled?
- Which speed-control architecture is quiet enough to test before a final case
  resonance path exists?
- What should the future CAD source treat as datum authority: comb mount,
  cylinder bearing axis, or service frame?

## L2 Measurement Plan

- Comb coupon: record speech, sustain, tuning response, stress, and tooth
  fatigue observations.
- Pin coupon: record lift quality, release noise, scrape, double-pluck, and
  permanent set.
- Registration mule: record lane alignment, side loading, follower return, and
  repeatability.
- Governor mule: record speed steadiness and mechanical noise under load
  changes.
- Drive comparison: compare spring, crank, and other drive options before case
  layout.
- Service mockup: verify that pins, comb teeth, governor, and drive components
  can be adjusted without destroying the assembly.

## Rejected For L2

- No dimensions.
- No tuning table.
- No comb tooth lengths or pin coordinates.
- No governor speed targets or gear ratios.
- No CAD, DXF, G-code, or fabrication drawing.
- No claim that the concept is ready to build.
