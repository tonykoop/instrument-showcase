<!-- SPDX-License-Identifier: CC-BY-4.0 -->
# Wheelharp Design Study

## Design Thesis

The Wheelharp is best treated as a controlled-friction keyboard rather than a
normal plucked or struck string instrument. The player presses keys, but the
sound depends on how each string enters a moving rosined wheel, how quickly it
speaks, how it damps when released, and how consistently the wheel bank runs.

The engineering challenge is not simply adding motors to a keyboard. It is
making a large number of small bowing contacts behave like one playable
instrument.

## Mechanism Overview

A motor drives a bank of wheels. Each wheel presents a rosined edge that can bow
a string when the string is brought into contact. The keyboard maps player
motion into controlled engagement: a key may lift a string toward a wheel, lower
a wheel toward a string, or actuate an intermediate pressure element. This L1
packet does not choose the final linkage.

The instrument needs a note-on path and a note-off path. Note-on requires
repeatable contact pressure, a clean attack, and minimal mechanical noise.
Note-off requires the string to leave the wheel and be damped without bouncing
back into contact. If damping is ignored, the wheel bank can turn every note
into a persistent blur.

The semicircular keyboard can make the instrument visually and physically
distinct, but it also complicates routing. Strings, key levers, dampers, and
wheel-service paths must not fight for the same space.

## Subsystems

### Wheel Bank

- Each wheel edge must run true enough for stable bow contact.
- Wheel material, edge finish, rosin compatibility, cleaning method, and
  replacement method are pending measurement.
- Shared-drive and individual-drive architectures are both open.
- The wheel bank needs guards for fingers, hair, loose clothing, and rosin dust.
- L2 evidence target: a one-wheel coupon with recorded edge material, truing
  method, rosin behavior, noise observations, and service access notes.
- Authority boundary: no wheel count, wheel diameter, axle size, bearing type,
  or spacing is released for fabrication.

### Motor Drive

- Motor type, drive belt, gear train, pulley path, controller, and noise
  isolation are unresolved.
- The drive should support consistent wheel motion before notes engage.
- Electrical isolation and service access should be designed before any powered
  prototype is built.
- No motor speed, torque, current, voltage, or power values are claimed here.
- L2 evidence target: a drive architecture decision comparing shared shaft,
  belt train, and modular motor approaches by safety, noise, serviceability,
  and controllability.
- Authority boundary: powered design remains pending electrical and pinch-point
  review.

### Key-To-String Engagement

- The key action must convert finger motion into controlled bow pressure.
- Candidate actions include lifting the string to the wheel, lowering a pressure
  wheel toward the string, or moving a small shoe that controls contact.
- The action should separate travel feel from final contact pressure so a
  playable key does not automatically imply excessive bow force.
- Key return, bounce, lost motion, and quiet operation are first prototype
  questions.
- L2 evidence target: one removable key-action mule that can test string lift,
  contact shoe, and damper sequencing without committing the whole keyboard.
- Authority boundary: key spacing, lever ratios, pivot positions, and spring
  forces are pending measurement.

### Strings And Damping

- String material, gauge, pitch layout, and tension are pending measurement.
- Idle strings need damping before and after bow engagement.
- String spacing and routing must account for wheel access, rosin maintenance,
  and damping hardware.
- A future test rig should measure attack, release, squeal, chatter, and
  unwanted sympathetic response.
- L2 evidence target: a string/damper test log that records whether release is
  clean before any keyboard layout is scaled up.
- Authority boundary: no tuning table, string scale, gauge, tension, or damper
  material is released.

### Frame, Soundboard, And Resonance

- The frame must hold wheel-bank alignment, keyboard action, string load, and
  motor vibration without turning into a noise source.
- Soundboard or pickup strategy is intentionally unresolved.
- A purely acoustic body, hybrid amplified body, or mostly electric pickup
  architecture are all still concept options.
- L2 evidence target: a structural interface map that separates wheel-bank
  support, string load path, keyboard mounts, service openings, and acoustic or
  pickup provisions.
- Authority boundary: frame stock, body dimensions, bracing, and resonance
  targets remain pending measurement.

### Maintenance And Setup

- Wheel truing, rosin application, string replacement, and damper adjustment
  must be reachable without dismantling the full keyboard.
- Rosin dust and motor debris need containment and cleaning paths.
- A setup log should track wheel condition, string wrapping or surface prep,
  engagement feel, noise, and response.
- L2 evidence target: a service checklist covering wheel replacement, rosin
  cleanup, string replacement, damper adjustment, and guard removal.

## Parametric Intent

Future work should name parameters before assigning values:

- `estimate_key_count_pending_measurement`
- `estimate_wheel_count_pending_measurement`
- `estimate_string_count_pending_measurement`
- `estimate_wheel_edge_material_pending_measurement`
- `estimate_key_travel_pending_measurement`
- `estimate_contact_pressure_pending_measurement`
- `estimate_damper_clearance_pending_measurement`
- `estimate_motor_drive_architecture_pending_measurement`

These are placeholders only. They are not build dimensions or performance
targets.

## First Measurement Gates

- Wheel truing: define a repeatable method to inspect wheel runout and edge
  condition.
- Bow contact: test one string against one wheel before scaling to a bank.
- Damping: verify that release is quiet and complete.
- Drive noise: separate wheel tone from motor and belt noise.
- Rosin management: log dust, buildup, cleaning, and reapplication behavior.
- Keyboard feel: confirm that engagement can be controlled by a player without
  excessive force or bounce.
- Safety: review guarding, electrical isolation, heat, and pinch points before
  powered multi-wheel tests.

## L2 Packet Gates

| Gate | Current authority | Promotion evidence |
| --- | --- | --- |
| Wheel coupon | pending_measurement | One-wheel test with material, edge condition, rosin, noise, and wear notes. |
| Key-action mule | pending_measurement | Bench linkage that proves note-on contact and note-off damping sequence. |
| String setup | pending_measurement | Measured response log with attack, release, squeal, chatter, and sustain observations. |
| Drive safety | pending_measurement | Electrical, guarding, heat, pinch-point, and service-access review. |
| Frame interfaces | pending_measurement | Reviewed layout separating wheel bank, string path, key action, damping, and maintenance access. |
| CAD/drawings | pending_measurement | Reviewed CAD, DXF, or drawing authority after measured parameters exist. |

## L2 Boundary

This design study is a build-packet candidate. It names subsystems, gates, and
planned fabrication classes, but it does not define a scale, tuning system,
wheel size, motor specification, CAD model, DXF, string schedule, or fabrication
release.
