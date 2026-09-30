<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Decision Record

## qmd Step 0

- `timeout 30 qmd query "barrel organ hand-cranked pinned barrel pallets flue reed organ pipes bellows windchest"` started, expanded search variants, searched, began reranking, and timed out without usable returned content.
- Result: this packet is grounded in the user request and real barrel-organ mechanics, while keeping all dimensions, tuning, wind, barrel-program, and pipe claims at concept or pending-measurement authority.

## L2 Uplift Decision

Promote the packet from L1 concept to L2 V5 build-packet candidate because the
repo now has a subsystem plan, expanded estimated BOM, and cut-list scaffold for
review. This is not a readiness promotion to build-ready status. All physical
specifications remain `pending_measurement`.

## Family Placement

The repo remains at `instruments/woodwind/barrel-organ` because the sounding
elements are organ pipes: air-column flue pipes and/or reed pipes. The
instrument also has a strong mechanical-program component, but current workspace
taxonomy places pipe-organ aerophones under woodwind-style folders.

## Key Decisions

- Treat the crank as driving both musical program advance and wind production.
- Use a pinned barrel or equivalent raised-feature carrier as tune storage.
- Keep fixed barrel, removable barrel, and replaceable strip options open until
  a mechanism mule clarifies indexing and wear.
- Use followers or trackers from the barrel to open windchest pallets.
- Separate action-mule, wind-mule, and pipe-mule evidence so failures can be
  diagnosed without guessing.
- Keep both flue and reed pipes as possible voice families until wind demand,
  package size, and voicing complexity are reviewed.
- Make the first prototype a mechanism and wind mule, not a tuned musical
  instrument.

## Open Questions

- Should the first barrel be fixed, removable, or represented by a replaceable pinned strip?
- How should crank motion divide between barrel rotation and bellows pumping?
- What follower material and spring return avoid noisy or sticky tracking?
- How will start-of-tune indexing reset without damaging followers or pins?
- Is a reservoir needed for steady speech, or can a simple bellows satisfy the first demo?
- Should the first musical rank use flue pipes, reed pipes, or one of each as a comparison?
- What service openings are required before the case becomes a finished enclosure?
- What evidence should promote this packet to L3: reviewed action drawings, measured wind stability, pipe response, or all three?

## L2 Acceptance Checks

- README uses an L2 status while preserving non-build-ready language.
- `design.md` names subsystem gates without adding dimensions or tuning values.
- `bom.csv` and `cut-list.csv` are complete enough for review but keep every
  physical value `pending_measurement`.
- `visual-output-register.csv` continues to classify artifacts only as
  `concept_only` or `pending_measurement`.

## Authority Boundary

No dimensions, pin spacing, barrel scale, pipe lengths, tuning values,
wind-pressure values, CAD geometry, DXF coordinates, or measured performance
claims are made in this repo. Promotion requires measured action behavior, wind
stability, pallet sealing, pipe response, and reviewed design tables.
