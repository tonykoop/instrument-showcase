<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Decision Record

## qmd Step 0

- `timeout 30 qmd query "carillon carillon - tuned bronze tower bells played from a baton-and-pedal keyboard via transmission wires to external clappers; bell profile/partials, clapper linkage, transmission geometry"` timed out without usable returned content.
- `qmd search "carillon" -c instrument-builds` failed before returning context because the sqlite-vec extension was unavailable and the database file could not be opened.
- Result: this packet is grounded in the round 7 contract and real carillon mechanics, while keeping all bell, tuning, transmission, and tower claims at concept or pending-measurement authority.

## Key Decisions

- Place the repo at `instruments/idiophones/carillon` because the sound source is struck tuned bells.
- Treat bronze bell founding and tuning as future expert-reviewed authority, not a generated L2 design claim.
- Center the first packet on the real control chain: baton/pedal keyboard, mechanical transmission, external clappers, fixed bells.
- Make action feel and clapper control the first prototype question, before any bell or tower design claim.
- Keep tower/frame engineering out of this L2 packet except as a named safety gate.
- Promote readiness to `L2 V5 build-packet candidate` for review and prototype planning only.
- Add `cut-list.csv` as a pending-measurement planning surface for action mule modules and future artifacts; it does not authorize cutting, casting, or tower fabrication.
- Keep all bell, action, transmission, clapper, tower, CAD, DXF, tuning, acoustic, and pressure/load values at `concept_only` or `pending_measurement`.

## Open Questions

- What is the minimum action mule needed to test baton travel, lost motion, and clapper rebound?
- Which parts of the transmission need adjusters for tuning the feel of the action?
- How should pedal action couple to larger bells while preserving dynamic control?
- What specialist evidence is required before bell profiles or partial targets can enter a design table?
- What structural review is required before a tower or frame can be considered?
- What minimum non-sounding action mule can separate baton feel, pedal leverage, lost motion, and clapper rebound?
- Which observations must be captured before promoting any action design to CAD?
- Which specialist review path owns bell profiles, partial tuning, foundry records, and tower/frame engineering?

## Authority Boundary

No bell dimensions, bell weights, partial targets, tuning values, transmission lengths, clapper masses, tower loads, CAD geometry, DXF coordinates, or measured performance claims are made in this repo. Promotion requires expert-reviewed bell data, measured action behavior, transmission layout review, and structural safety evidence.

## Promotion Gates

- L3 requires expert-reviewed bell/foundry data, reviewed action or measured mule results, reviewed transmission layout, and structural safety evidence.
- L3 CAD/DXF authority must trace to reviewed drawings, measured templates, or specialist-approved parameters.
- L4 requires physical build or mule measurements, action observations, service/safety notes, and any bell/tower validation evidence accepted by the relevant specialist.
