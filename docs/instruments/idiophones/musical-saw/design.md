<!-- SPDX-License-Identifier: CC-BY-4.0 -->
# Musical Saw Design Study

## Design Thesis

The musical saw is best treated as a controlled-flex idiophone. The sound source
is the saw blade itself, but the playable pitch is shaped by the S-curve bend
and by how the player supports, twists, bows, or strikes the blade. A serious
packet must treat body mechanics, blade safety, and measurement repeatability
as design variables rather than assuming a fixed scale.

## Mechanism Overview

A hand saw blade is held at the handle and flexed into an S curve. A bowed or
struck contact excites a vibrating region of the blade. The player changes pitch
by changing curvature, torsion, support, and contact point. The blade must be
safe to hold and must return predictably enough that a measured exercise can be
repeated.

This L1 packet does not choose final blade geometry, steel alloy, pitch range,
bowing force, strike tool, handle modification, grip fixture, or flex jig. Those
values require measured or reviewed authority before any build packet can
advance.

## Playing Modes

### Bowed Mode

- Bowed playing is the primary concept because it can sustain tone while the
  player changes blade curvature.
- Bow hair, rosin, contact angle, contact pressure, and bow speed are unresolved
  setup variables.
- The bowing surface must be safe and must not depend on unguarded sharp teeth.
- A first test should record whether a stable tone can be started, sustained,
  and stopped without scraping or uncontrolled blade motion.

### Struck Mode

- Struck playing is a secondary concept for transient response and pitch
  exploration.
- The striker material, strike point, rebound, and damping are pending
  measurement.
- Struck tests must account for blade motion, edge safety, and uncontrolled
  overtones.

## Subsystems

### Blade

- Blade material, thickness, taper, tooth condition, edge treatment, and handle
  attachment are pending measurement.
- No blade size, profile, tooth pitch, or steel specification is released.
- A future coupon should log flex behavior, visible damage, audible response,
  and repeatability under gentle test bends.

### Flex Control

- Pitch control depends on S-curve bending, torsion, support, and player
  posture.
- A future guide or jig may help repeat tests, but no jig geometry is claimed in
  this L1 packet.
- Flex limits must be established from safe handling and measured response, not
  from guessed curvature values.

### Contact And Excitation

- Bowing and striking need separate test records because they excite the blade
  differently.
- Bowed tests should log qualitative tone start, sustain, scrape, and release.
- Struck tests should log attack, decay, damping, and repeatability.
- No bowing force, strike force, contact position, or pitch target is specified.

### Handle, Grip, And Safety

- The handle must let the player control bend without sharp-edge exposure or
  hand strain.
- Tooth coverage, blade-tip awareness, and storage/transport protection are
  safety gates.
- Any handle extension or grip aid is pending measurement and safety review.

### Measurement And Documentation

- Future logs should separate blade setup, flex state, contact method, tone
  quality, pitch observation, safety observation, and repeatability.
- Audio or tuner readings, if collected later, must be labeled as measured data
  with date, tool, and setup notes.

## Parametric Intent

Future work should name parameters before assigning values:

- `estimate_blade_family_pending_measurement`
- `estimate_blade_flex_state_pending_measurement`
- `estimate_bow_contact_region_pending_measurement`
- `estimate_strike_contact_region_pending_measurement`
- `estimate_handle_support_method_pending_measurement`
- `estimate_safety_guarding_pending_measurement`
- `estimate_pitch_observation_method_pending_measurement`

These names are placeholders only. They are not dimensions, tuning values, force
values, curvature values, or fabrication targets.

## First Measurement Gates

- Blade survey: document source condition, tooth safety, visible wear, and
  handling hazards.
- Flex test: confirm a repeatable gentle S-curve can be held without unsafe
  motion or visible damage.
- Bow test: verify that a stable tone can be started and stopped safely.
- Strike test: verify transient response and damping without uncontrolled blade
  movement.
- Pitch observation: record measured pitch only after the setup and tool are
  documented.
- Safety review: block any public build guidance until edge protection, posture,
  storage, and transport are addressed.

## L1 Boundary

This design study is a concept map. It does not define a scale, tuning system,
blade geometry, bend geometry, bowing setup, strike setup, CAD model, DXF, or
fabrication release.
