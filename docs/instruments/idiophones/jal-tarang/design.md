<!-- SPDX-License-Identifier: CC-BY-4.0 -->
---
instrument: Jal Tarang
family: idiophones / tuned vessel percussion
readiness: L2 concept / pending-measurement packet
authority: concept study; pending measurement
---

# Jal Tarang Design Study

## Concept

This packet sketches a jal tarang as an array of tuned bowls partly filled with
water and struck with light mallets. The musical action is simple, but the
setup discipline is not: pitch depends on the bowl, the water volume, the
strike point, the support surface, the mallet, and evaporation or handling
changes during a session.

The design goal is a traceable tuning and staging workflow rather than a
fabrication drawing. A future packet should make each bowl's identity, fill
state, measured pitch, and setup notes easy to record and repeat.

## Mechanism Direction

Candidate design branches:

- Porcelain or ceramic bowls: traditional visual and tactile direction, with
  high variation between individual bowls.
- Metal bowls: potentially durable, but material and rim behavior need
  listening tests before use.
- Graduated bowl set: bowls selected for natural pitch families before adding
  water.
- Uniform bowl family: simpler sourcing and staging, but likely more tuning
  burden from water-volume adjustment.
- Measured fill workflow: future water volumes should be recorded with a
  repeatable vessel or scale, not guessed by eye.
- Support tray or cradle: should keep bowls stable while allowing resonance,
  draining, labeling, and safe transport.

## Parametric Intent

Use named unknowns before any CAD or tuning table:

- `pending_bowl_count`: not specified.
- `pending_bowl_material`: not specified.
- `pending_bowl_diameters`: not specified.
- `pending_bowl_wall_profile`: not specified.
- `pending_target_scale`: not specified.
- `pending_pitch_values`: not specified.
- `pending_water_volume_per_bowl`: not specified.
- `pending_mallet_material`: not specified.
- `pending_support_layout`: not specified.
- `pending_labeling_method`: not specified.

## Prototype Path

The first useful prototype is a measurement session, not a fixture. Select a
small set of candidate bowls, assign temporary IDs, record dry pitch behavior,
add water in controlled increments, and log pitch response after each fill
change. Repeat the same fills after draining and refilling to learn whether
the setup can be reproduced.

Only after that should the packet define a support tray, bowl order, labeling,
water-measurement kit, or performance layout.

## L2 Subsystem Plan

- Bowl inventory: every bowl needs a temporary ID, material note, condition
  note, dry response observation, and handling risk note before tuning work.
- Fill workflow: water should be added, removed, and logged with the same
  repeatable method so later tests can separate bowl behavior from setup error.
- Pitch logging: tuner or recording evidence should be tied to bowl ID and fill
  state, while all pitch values remain pending measurement.
- Mallet testing: strike tools should be compared by attack clarity, rim safety,
  player feel, and noise, not promoted from visual similarity.
- Support and staging: tray or cradle concepts should be tested for stability,
  resonance, drainage, labeling, and safe movement.
- Session drift: evaporation, handling, splashing, and refill/reset behavior
  should be logged before any performance-ready claim.

## Review Tables To Add Later

The next measured packet should add separate tables for bowl inventory,
fill/pitch observations, mallet trials, support behavior, and session drift.
Those tables are not included here because the values do not yet exist.

## Failure Modes

- Bowls ring poorly after water is added or after moving to a different support.
- Fill state cannot be repeated after draining and refilling.
- Labels imply final tuning before measured pitch evidence exists.
- Mallets chip, mute, or overdrive a bowl rim.
- Bowl support is stable but acoustically choking, or resonant but unsafe.
- Evaporation or splashing changes the setup during a session.

## Non-Claims

This packet does not claim traditional repertoire, scale, bowl count, tuning
frequencies, water volumes, bowl dimensions, CAD geometry, DXF coordinates, or
mallet specifications. Those must come from future reference research,
inventory measurement, pitch logging, and player feedback.
