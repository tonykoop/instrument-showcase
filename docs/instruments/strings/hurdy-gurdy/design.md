<!-- SPDX-License-Identifier: CC-BY-4.0 -->
# Hurdy-Gurdy Design Study

## Design Thesis

This concept treats the hurdy-gurdy as a friction instrument first and a
keyboard instrument second. The wheel, rosin, string wrapping, tangent geometry,
and trompette bridge are coupled setup problems. A successful build packet has
to make those adjustments visible instead of pretending the body outline alone
defines the instrument.

## Mechanism Overview

The player turns a crank that rotates a wheel through an axle. The wheel edge is
rosined and contacts the strings like a continuous bow. Bowing pressure comes
from string height, bridge geometry, cotton wrapping, wheel surface condition,
and the player's crank speed. A wheel cover protects the player's hand and keeps
rosin dust contained while still allowing inspection and service.

Melody strings, often called chanterelles, pass through a keybox. Each key
carries a tangent that stops the melody string at a setup point. The tangents
need lateral position, height, and contact surface adjustment. The key action
must return reliably and avoid rubbing neighboring tangents or strings.

Drone strings bypass the tangent keyboard and speak continuously against the
wheel. They need their own bridge, nut, contact, muting, and setup decisions so
the instrument can shift between full drone, reduced drone, and practice
states.

The trompette is a special drone string that can drive a loose buzzing bridge.
The player can trigger the buzz through crank acceleration. The design problem
is not just making the bridge loose; it is balancing string tension, bridge
mass, wheel friction, and crank impulse so the buzz is controllable instead of
random.

## Subsystems

### Wheel Bow And Crank

- A true wheel is the central fabrication challenge.
- The wheel edge needs a serviceable rosin surface and a way to inspect
  flatness, roundness, wobble, and string contact.
- The crank and axle need low backlash and enough stiffness that crank pulses
  do not create unwanted wheel wobble.
- Bearing, bushing, and wheel-cover choices are pending measurement and
  prototype testing.

### String Contact And Wrapping

- Cotton or similar wrapping on bowed strings is treated as a setup variable,
  not a fixed design fact.
- Contact pressure, rosin loading, string material, wrapping density, and wheel
  condition interact.
- First tests should separate wheel truing from string setup so a bad wheel is
  not misdiagnosed as a bad string choice.

### Tangent Keyboard

- The keybox needs a stable reference plane for keys and tangents.
- Tangents should be adjustable during setup because final speaking points are
  pending measurement.
- The concept favors visible, serviceable tangent attachment over hidden
  mechanisms during the first prototype.
- Key return, lateral play, and tangent clearance are first-order risks.

### Drones

- Drone strings should be laid out as independent voices with their own muting
  and contact setup.
- Drone placement must leave room for wheel service, keybox service, and hand
  clearance at the crank.
- Tuning, string material, and gauge are intentionally not specified in this L1
  packet.

### Trompette And Buzzing Bridge

- The trompette bridge should be designed as an adjustable experiment.
- Setup variables include bridge seating, string break angle, contact point,
  string wrapping, rosin, and crank impulse.
- The first prototype should log when the bridge stays silent, chatters
  controllably, or buzzes continuously.
- The desired behavior is a rhythmic accent under player control, not permanent
  rattling.

### Body, Soundboard, Pegbox, And Tailpiece

- The body and soundboard must support wheel, bridge, keybox, pegbox, and
  tailpiece loads without freezing out service access.
- The pegbox needs enough adjustment range for multiple string families, but no
  final string schedule is claimed here.
- The tailpiece should support separate setup paths for melody, drone, and
  trompette strings.
- Body outline, bracing, soundhole treatment, and material choices are concept
  only until measured or reviewed.

## Parametric Intent

All future dimensions should be named as parameters before fabrication work:

- `estimate_wheel_diameter_pending_measurement`
- `estimate_body_length_pending_measurement`
- `estimate_key_count_pending_measurement`
- `estimate_string_count_pending_measurement`
- `estimate_keybox_reference_height_pending_measurement`
- `estimate_trompette_bridge_mass_pending_measurement`
- `estimate_crank_throw_pending_measurement`

These names are placeholders for future reviewed data. They are not values.

## First Measurement Gates

- Wheel trueness: measure runout before any string setup judgment.
- Wheel surface: record rosin behavior and contact consistency.
- Melody action: verify tangent adjustment, return, and clearance with a test
  string before a full keyboard is built.
- Drone setup: test continuous speech and muting independently of melody keys.
- Trompette response: record crank impulse, buzz onset, controllability, and
  false chatter.
- Service access: confirm wheel, string wrapping, tangents, and bridges can be
  adjusted without disassembling the whole instrument.

## L2 Engineering And Acoustic Reasoning

The acoustic behavior starts at the wheel/string interface. The wheel must
deliver a repeatable stick-slip cycle across melody, drone, and trompette
strings, while the soundboard and bridges convert that friction into useful
motion. For L2 review, the wheel is treated as a controlled surface rather than
as a decorative round part: future work must define truing method, edge
material, rosin behavior, cotton wrapping, and contact-pressure adjustment as
separate parameters.

The tangent keyboard is a pitch-selection mechanism, but no pitch layout is
released here. The L2 model only asserts relationships: key travel must move a
tangent into a repeatable string contact point; tangent lockup must survive
setup changes; return force must clear the string without bouncing; and keybox
geometry must stay stable relative to the melody-string path. Tolerances are
questions to measure, not numbers to invent.

The drone and trompette voices are separate review branches. Drones require
continuous, stable speech and a muting plan. The trompette requires an
adjustable buzzing bridge whose response changes under crank impulse. The
design should therefore separate normal drone testing from trompette testing so
a successful drone setup is not confused with a successful buzzing-bridge
setup.

## Material Reasoning

Candidate material choices remain pending measurement, but the subsystem
requirements are clearer:

- Wheel material must hold a true edge, accept rosin, resist dust loading, and
  be serviceable after wear.
- Keybox and key materials must favor dimensional stability and repairable
  bearing surfaces over decorative complexity.
- Tangent material must be smooth enough not to damage strings while holding a
  repeatable contact shape.
- Bridge and soundboard materials must be selected together because wheel
  friction, drone coupling, and trompette buzz all load the same acoustic
  structure.
- Cotton or equivalent string wrapping is treated as a consumable setup
  material with its own test log.

## Failure Modes To Review

- Wheel runout causes uneven speech or false trompette chatter.
- Rosin dust contaminates bearings, keys, or tangent returns.
- Tangents creep, rotate, or fail to return clear of the melody strings.
- Drone strings overdrive the soundboard or mask melody response.
- Trompette bridge buzz is either absent, continuous, or too sensitive to crank
  motion.
- Crank backlash turns rhythmic accents into wheel wobble.
- Service access requires removing too many coupled setup parts.

## Tolerances As Questions

- How much wheel runout is audible on wrapped strings?
- How much key side play can the tangent tolerate before pitch contact becomes
  unstable?
- How much crank backlash is acceptable before trompette control suffers?
- How repeatable must string wrapping density be for a useful setup log?
- What inspection access is needed to adjust wheel, bridges, tangents, and
  wrapping without resetting the whole instrument?

## L2 Boundary

This file is an L2 engineering-risk map and prototype-planning scaffold. It
does not provide a fabrication drawing, tuning plan, acoustic model, measured
wheel geometry, or measured string schedule.
