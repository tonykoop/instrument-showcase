<!-- SPDX-License-Identifier: CC-BY-4.0 -->
# Decision Record

## Decisions

- Treat the nyckelharpa as a keyed bowed fiddle, with tangent action as the
  primary engineering risk.
- Keep all dimensions, tuning, string gauges, bridge geometry, tangent layout,
  and CAD/DXF work out of the packet.
- Model the first prototype as separate test rigs before a full instrument:
  one bowed-string/tangent contact rig, one keybox travel rig, and one
  sympathetic-string clearance/resonance rig.
- Prefer serviceable tangent adjustment over hidden precision in the first
  physical study.
- Uplift to L2 by adding shop-planning surfaces, not by promoting any measured
  or fabrication authority.
- Add `cut-list.csv` as a planning ledger for blanks and mockups only; it must
  not be read as a cut-ready part list.
- Keep the keybox removable until tangent contact, sympathetic-string
  clearance, and service access have been reviewed together.

## Assumptions

- Melody strings are bowed directly.
- Wooden tangents stop the melody strings when keys are pressed.
- Sympathetic strings are routed below or through the keybox and are not stopped
  by the main tangent action.
- Key travel, tangent face, bridge, body, and sympathetic path must be adjusted
  together after real measurements.
- The first useful shop artifact is a bench rig, not a complete decorated body.
- A future measured reference tradition or instrument family will be selected
  before any final layout, tuning, or stringing schedule.
- Sympathetic resonance may require damping or isolation experiments; a weak or
  noisy response is not a failure if it is logged honestly.

## L2 Shop-Planning Choices

- Use modular assemblies: one-string rail, keybox cassette, tangent carrier,
  sympathetic underpass, and body planning shell.
- Favor reversible fasteners and removable panels in test rigs.
- Require failure-mode logging before changing multiple variables at once.
- Keep all part quantities as `estimate_pending_measurement`.
- Keep the visual authority register conservative: concept and pending
  measurement only.

## Open Questions

- What reference nyckelharpa family or style should govern the first measured
  packet?
- How many melody, drone, and sympathetic strings should be studied after a
  reference frame is chosen?
- Should the first keybox use sliding wooden keys, hybrid low-friction guides,
  or a removable experimental cassette?
- What tangent adjustment method gives enough setup control without making the
  action fragile?
- How should sympathetic strings be protected while preserving tuning access?
- What guide material and return approach keep keys quiet without excessive
  friction?
- Where should the keybox open for cleaning, tangent replacement, and
  sympathetic-string service?
- What body/soundboard mockup is sufficient to test load paths without
  pretending to be the final resonator?

## Next Work

- Select a reference tradition or measured instrument source.
- Build a one-key tangent test rig before designing a full keyboard.
- Build a sympathetic-string clearance mockup under an open keybox.
- Record measured key travel, tangent contact behavior, buzzing, return noise,
  bow clearance, and sympathetic response before any authority upgrade.
- Populate a future validation table with measured results from the one-key
  rig.
- Update the cut list only after measured reference dimensions or reviewed CAD
  exist.
- Add photos or diagrams only as concept/support visuals unless a reviewed
  dimensional source is also registered.
