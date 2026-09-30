<!-- SPDX-License-Identifier: CC-BY-4.0 -->
---
instrument: Glass Harp
family: idiophone_friction_glass
packet_mode: v5_l2_candidate
authority: concept_only / pending_measurement
readiness: L2 V5 build-packet candidate
---

# Glass Harp Design Study

## Design Thesis

The glass harp is a friction idiophone made from individual wine glasses. The
player wets a finger and circles the rim, causing stick-slip excitation of the
glass. Pitch is selected by the glass and adjusted in practice by water level,
but this packet does not claim any pitch table or fill-height relationship.

The useful first step is not fabricated geometry. It is a disciplined test plan:
choose candidate glasses, label them, measure their dry and filled response,
record water levels consistently, and design a spill-safe playing surface.

## Mechanism

Each glass acts as its own resonator. The player provides a controlled wet
finger contact at the rim. Water changes the effective vibrating system and also
changes playing feel, stability, and spill risk. The setup therefore needs a
layout, labeling method, filling workflow, and measurement log before any
musical scale claim is made.

## Mechanism Analysis

The glass harp has no single body to dimension. Its behavior is the sum of many
individual resonators plus a player's wet-contact technique. The L2 review
therefore treats every glass as an inventory item with its own identity,
condition, dry response, filled response, and handling notes. A future packet
should not group glasses into a scale until the set has been measured.

Water is both a tuning variable and a risk variable. Adding water can shift
response, change onset effort, make the rim harder to excite, and increase spill
risk. The review workflow should separate dry-glass behavior from filled-glass
behavior so a poor response is not misdiagnosed as only a tuning problem.

The support surface is also part of the instrument. A tray or table that damps
the bowls, lets them slide, hides labels, or makes spills hard to control can
make a good glass set unplayable. Early support work should favor reversible
layout mockups and water-safe labeling over permanent fixtures.

## Parametric Intent

Future data tables should separate measured values from choices:

- `glass_id`
- `glass_source_status`
- `rim_condition_status`
- `dry_response_status`
- `filled_response_status`
- `water_level_record_status`
- `onset_effort_status`
- `sustain_status`
- `spill_control_status`
- `layout_ergonomics_status`

All fields are currently `pending_measurement`. This repo does not infer pitch,
diameter, water fill, or tuning behavior from prose, images, or memory.

## Engineering And Acoustic Reasoning

The useful L2 model is relational, not numeric:

- Glass identity, wall profile, rim condition, and material influence dry
  response.
- Water volume, water-level reading method, and evaporation influence filled
  response.
- Finger wetness, rim cleanliness, and hand pressure influence onset and
  sustain.
- Tray material, pad material, and glass spacing influence damping, stability,
  and playability.
- Labeling must survive moisture without becoming a false tuning authority.

No frequencies, fill heights, diameters, wall thicknesses, or scale intervals
are released here. Those belong in a measured glass inventory and validation
log after real candidate glasses exist.

## Materials Reasoning

- Candidate glasses should be selected for intact rims, repeatable response,
  and safe handling before musical role.
- Water-measurement tools should favor repeatability and spill control over
  visual elegance.
- Labels should be removable or replaceable until final glass IDs are stable.
- Tray or pad materials should be tested for damping and slip resistance.
- Towels, wetting vessels, and cleanup materials are part of the playing
  system, not afterthoughts.

## Failure Modes

- A glass chips or cracks during handling or play.
- Similar-looking glasses produce unrelated pitches or response envelopes.
- Water-level readings are not repeatable after draining and refilling.
- Labels loosen, smear, or imply unmeasured pitch authority.
- The tray damps the glass or lets it walk during rim excitation.
- Finger wetness and rim cleanliness dominate the perceived tuning result.
- Session drift from evaporation or splashing invalidates a fill log.

## Tolerances As Questions

- How repeatable is a measured fill after drain/refill cycles?
- How much water-level drift is audible during a session?
- How much tray damping is acceptable before sustain suffers?
- How much glass spacing is needed for hand access without collisions?
- Which label method survives wet handling without touching the rim?

## Authority Boundary

- Concept authority: README, design notes, estimated BOM, and decision record.
- Measurement authority: none yet.
- CAD/DXF authority: none yet.
- Tuning authority: none yet.

Future photos or renders can document layout and playing posture, but they must
not become sources for pitch, fill height, glass dimensions, or fabrication
templates.

## Measurement Gates

Promotion beyond L2 requires:

- A real glass set labeled and measured one glass at a time.
- A repeatable water-level recording method.
- Dry and filled response logs for each candidate glass.
- A safe table or tray layout that controls spills and keeps glasses stable.
- A playability test for onset, sustain, hand spacing, and retuning drift.
- A cleaning and storage plan that preserves labels and measured fill records.

## Risks

- Small changes in water level, rim wetting, or finger pressure may shift
  response.
- Similar-looking glasses may not behave similarly.
- Spill risk can damage labels, surfaces, microphones, or electronics.
- Overconfident scale claims can hide the need for measured tuning logs.
- Glass breakage and sharp edges require a handling and disposal plan.

## L2 Boundary

This file is an L2 review scaffold. It does not provide CAD, DXF, glass
dimensions, water volumes, tuning frequencies, scale layout, tray geometry, or
measured acoustic response.
