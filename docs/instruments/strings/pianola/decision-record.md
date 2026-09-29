<!-- SPDX-License-Identifier: CC-BY-4.0 -->
# Decision Record

## Decisions

- Treat the pianola as a pneumatic player-piano mechanism coupled to an
  existing or representative piano action.
- Uplift readiness to `L2 V5 build-packet candidate` for review and prototype
  planning only.
- Keep all dimensions, roll scales, tracker-bar coordinates, vacuum pressure,
  action travel, tuning data, CAD, and DXF work out of the packet.
- Make the first physical work a single-note pneumatic chain before any full
  tracker bar or keyboard-width assembly.
- Keep expression, sustain, and tempo-control branches separate from the first
  note-actuation proof.
- Add `cut-list.csv` as a coupon and fixture planning register, not as a cut
  geometry release.
- Keep all artifact authority at `concept_only` or `pending_measurement`.

## Assumptions

- A perforated roll passes over a tracker bar.
- Tracker-bar pressure changes operate pouches and valves.
- Pneumatic output actuates a piano action rather than directly sounding a
  separate instrument.
- Timing, leakage, reset, and serviceability are the main early risks.
- L2 can name coupons, fixtures, logs, and sequencing, but cannot promote any
  physical parameter to fabrication authority.

## Open Questions

- Which measured roll/tracker-bar standard or historical player-piano family
  should govern the first L2 parameter set?
- Should the first rig use suction, pressure, or a hybrid representation of the
  pneumatic chain?
- What pouch and valve materials can be tested without overclaiming durability?
- How should expression and sustain coding be introduced after single-note
  response is measured?
- What representative piano action is safe to use for actuation tests?
- What is the safest way to intentionally add controlled leaks for diagnosis?
- What service interval should be simulated before choosing permanent casework?
- Which measurements belong in a future validation table before any L3 claim?

## L2 Prototype Gates

- Select a measured reference frame without copying unreviewed dimensions into
  this packet.
- Build or source one paper-strip coupon and one tracker-bar sensing coupon.
- Bench one pouch/valve pair and log leak behavior, response, reset, and missed
  triggers.
- Couple one pneumatic actuator to a representative piano action or safe action
  load.
- Record serviceability observations for tracker cleaning, pouch replacement,
  valve adjustment, tubing inspection, and paper handling.
- Review whether expression, tempo, sustain, or reroll controls can be added
  without hiding the single-note failure modes.

## Not Accepted As Evidence Yet

- Prose descriptions of historic pianola dimensions.
- Any unmeasured roll scale, tracker-bar layout, vacuum level, or linkage
  geometry.
- CAD, DXF, renders, or photos that do not cite measured or reviewed authority.
- Piano tuning or acoustic claims unrelated to pneumatic actuation.
