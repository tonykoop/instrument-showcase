<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Decision Record

## Decisions

- Treat the daxophone as a bowed wooden-tongue friction idiophone with contact
  pickup support.
- Keep the clamp, tongue, dax block, and pickup as separate design subsystems.
- Promote this packet from V5 L1 to L2 planning by adding subsystem shop
  interfaces, a non-dimensional cut/workpiece list, and explicit prototype
  evidence gates.
- Keep the packet below build-ready because no measured tongue blank, clamp
  test, dax-contact test, or pickup test exists.
- Record every artifact as `concept_only` or `pending_measurement`.
- Do not create CAD, DXF, tongue profiles, fret maps, pitch tables, pickup
  placement, or dimensions in this pass.

## Open Questions

- Which real wood blank and grain orientation will define the first prototype?
- What clamp interface holds reliably without crushing the tongue?
- What dax-block face shape and surface finish provide useful expression?
- Where can a contact pickup be mounted without becoming undocumented structure?
- How should bowing response be measured separately from amplifier coloration?
- What safety treatment prevents splinters or sharp bowed edges while preserving
  friction response?

## Promotion Gates

- L2 is satisfied by this planning handoff: subsystem boundaries, BOM classes,
  cut/workpiece categories, and authority constraints are explicit.
- L3 requires reviewed fabrication authority and repeatable prototype response.
- L4 requires empirical playing data, recordings or measurements, and documented
  revisions.

## L2 Evidence Gates

- Measure and photograph the first tongue blank before shaping.
- Log clamp stability, buzz, slip, and fiber damage risk separately from bowing
  behavior.
- Test dax-face contact on a coupon before claiming any contact map or fret-like
  behavior.
- Record pickup mounting reversibility, handling noise, and whether the pickup
  changes the mechanical response.
- Update the authority register before future CAD, DXF, SVG, pickup layout, or
  audio artifacts are treated as anything beyond concept review.
