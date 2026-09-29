<!-- SPDX-License-Identifier: CC-BY-4.0 -->
# Decision Record

## qmd Step 0

- Command attempted: `qmd search "musical saw hand saw bowed struck S-curve bending pitch flex control" -c instrument-builds`.
- Result: qmd failed before returning content because sqlite-vec was unavailable
  and the database could not be opened.
- Packet grounding: this L1 packet is grounded in the user prompt and general
  musical-saw mechanism only. It makes no QMD-derived, measured, dimensional,
  tuning, CAD, or fabrication claims.

## Decisions

- Readiness is `L1 concept packet`.
- The instrument is treated as a flexible-blade idiophone played by bowed or
  struck excitation while pitch is changed by S-curve bending.
- Bowed playing is the primary sustained-tone concept; struck playing is a
  secondary response test.
- Blade flex control, edge safety, handle comfort, bow contact, and measurement
  repeatability are the first risks.
- The packet intentionally avoids blade dimensions, tuning values, curvature
  values, bowing force, strike force, handle geometry, CAD, DXF, and fabrication
  outputs.
- Every visual-output register row is `concept_only` or
  `pending_measurement`; no artifact is fabrication authority.

## Open Questions

- Which saw blade family can flex safely and repeatably for a first test?
- How should sharp teeth and blade tip hazards be guarded during bowing?
- What bow and rosin setup starts tone cleanly without excessive scrape?
- What hand posture or temporary guide makes S-curve tests repeatable?
- Should struck tests use a soft striker, fingertip tap, or another safe
  excitation method?
- What measurement log is enough to connect pitch observation to flex state
  without pretending to define a tuning chart?
- What safety checks are required before public build guidance is appropriate?

## Rejected For L1

- No dimensions.
- No tuning table.
- No blade profile, steel specification, curvature value, or pitch range.
- No bowing force, strike force, contact point, or fixture geometry.
- No CAD, DXF, G-code, or fabrication drawing.
- No claim that the concept is ready to build.
