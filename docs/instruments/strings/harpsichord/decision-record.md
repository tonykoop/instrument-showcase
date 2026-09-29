<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Decision Record

## Decisions

- Treat the harpsichord as a keyboard-controlled plucked-string instrument
  centered on jacks, plectra, register slides, and damping.
- Promote this packet from V5 L1 to L2 planning by adding subsystem shop
  interfaces, a non-dimensional cut/workpiece list, and explicit prototype
  evidence gates.
- Include 8' and 4' registers as named concept systems without defining scale,
  stringing, or geometry.
- Include a buff/lute stop as a color mechanism whose contact behavior is
  `pending_measurement`.
- Keep the packet below build-ready because no measured reference, stringing
  design, jack mockup, or register prototype exists.
- Record every artifact as `concept_only` or `pending_measurement`.
- Do not create CAD, DXF, string layouts, tuning tables, jack dimensions,
  plectrum cuts, bridge layouts, or case dimensions in this pass.

## Open Questions

- What historical reference, measured exemplar, or original design target will
  define keyboard scope and stringing?
- How will jack guides, register slides, and jack rail access be arranged for
  regulation?
- What plectrum material and voicing process will be tested first?
- How will 8' and 4' registers be selected, coupled, or intentionally omitted in
  a first prototype?
- What buff-stop material and contact path damp strings without damaging them?
- What soundboard and case strategy can carry string load without unsupported
  assumptions?

## Promotion Gates

- L2 is satisfied by this planning handoff: subsystem boundaries, BOM classes,
  cut/workpiece categories, and authority constraints are explicit.
- L3 requires reviewed fabrication authority and repeatable action/stringing
  validation.
- L4 requires empirical build data, regulation notes, recordings or
  measurements, and documented revisions.

## L2 Evidence Gates

- Select a historical reference, measured exemplar, or explicit design target
  before publishing scale, compass, stringing, or bridge claims.
- Build a one-jack action mockup and log lift, pluck, reset, damping, and
  service access separately.
- Test a register-slide coupon before claiming 8' or 4' alignment geometry.
- Test a buff/lute contact coupon before locating the stop in a full layout.
- Record soundboard, wrestplank, case, and string-load risks before CAD.
- Update the authority register before future CAD, DXF, SVG, stringing tables,
  Wolfram models, or audio artifacts are treated as anything beyond concept
  review.
