<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Decision Record

## Decisions

- Use a Franklin-style horizontal spindle with nested graduated glass bowls.
- Treat the instrument as a friction idiophone played by wetted fingers at the
  rims.
- Uplift the packet to V5 L2 because the subsystem plan, BOM, candidate
  cut-list, and promotion gates now identify where future measurements belong.
- Keep all build-critical claims pending because no measured bowl set, spindle
  layout, drive prototype, or tuning evidence exists.
- Record every artifact as `concept_only` or `pending_measurement`.
- Do not create CAD, DXF, renders, pitch tables, dimensions, or drive ratios in
  this pass.

## Open Questions

- What real bowl set, supplier, or custom glass process will define the first
  measured geometry?
- How will the spindle interface support each bowl without point loading the
  glass?
- What bearing and guard layout isolates water from rotating hardware?
- What treadle/flywheel arrangement gives smooth motion without audible
  mechanical noise?
- How much clearance is needed between nested bowls under rotation and player
  touch?
- What validation fixture can measure free-bowl response before mounting and
  mounted response after assembly?
- What minimum service clearance is needed to remove, clean, or replace one
  bowl without disturbing the rest of the stack?
- Which guard elements can be tested on the drive rig before real glass is
  installed?

## Promotion Gates

- L2 records subsystem intent and pending-measurement gates only; it does not
  authorize fabrication.
- L3 requires reviewed fabrication authority and prototype validation.
- L4 requires empirical build data, measured sound response, and documented
  revisions.
