<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Waterphone Design Study

## Concept

The instrument is a waterphone-style idiophone: a metal resonator bowl partly
filled with water, a central neck or handle, and a ring of vertical rods around
the rim. The player bows or strikes the rods while tilting or rocking the bowl.
The moving water changes coupling, damping, and perceived pitch, creating the
signature bending and shimmering response.

## Mechanism

The bowl acts as a resonant body and water chamber. Rods transfer bowed or
struck energy into the rim and bowl wall. The internal water does not provide a
fixed tuning system; it behaves as a moving load that shifts and smears the
response. The useful design question is therefore not "what exact note does
each rod play?" but "which rod materials, attachment methods, bowl forms, and
water fills produce controllable bends without choking the sound?"

## L2 Subsystem Plan

- Bowl and chamber: keep bowl form, material, seam strategy, fill access, and
  leak control together so water handling is not separated from resonance.
- Neck and handle: treat the neck as both player interface and possible
  service/fill path until tests prove which duties it should carry.
- Rod field: test a small rod-and-rim coupon set before defining a full ring,
  ordering, or pitch map.
- Rod attachment: compare welded, brazed, threaded, clamped, and isolated
  approaches for sustain, serviceability, water safety, and bowing noise.
- Playing response: evaluate bowed, struck, scraped, and hybrid gestures as
  separate response modes.
- Validation: keep leak, corrosion, handling noise, water slosh, rod response,
  and bowl response as separate gates before any CAD/DXF promotion.

## Parametric Intent

The first real design table should vary these parameters only after bench
measurement:

- Bowl material family: stainless, bronze, or another weldable/formable metal.
- Bowl form: shallow, medium, or deep resonator profile.
- Neck design: fill/service access, grip comfort, and seal strategy.
- Rod material family: stainless, bronze, brass, or other bowable metal.
- Rod attachment: welded, brazed, threaded, clamped, or mechanically isolated.
- Rod field: density, ordering, and spacing around the rim.
- Water fill: repeatable fill marks and tilt response.
- Excitation: bow hair/rosin compatibility, striker hardness, and handling
  noise.
- Corrosion and cleanup: water contact, drying path, service access, and
  finish compatibility.
- Attachment service: replacement strategy for failed rods or noisy joints.

No exact dimensions, rod lengths, rod pitches, fill volumes, DXF coordinates,
or acoustic targets are asserted in this L2 packet.

## Measurement Plan

1. Source or form a test bowl and document its dry response with microphone and
   accelerometer recordings.
2. Test a small coupon set of rods with multiple attachment methods before
   committing to a full rim field.
3. Measure dry rod response, wet bowl response, and tilt-bend behavior as
   separate experiments.
4. Record whether bowing, striking, and combined gestures remain controllable.
5. Promote only measured and reviewed data into future CAD, DXF, or tuning
   authority.
6. Tie any future cut-list row to measured bowl, rod, joint, and leak-test
   evidence before material ordering.

## Authority Boundary

This file is concept and pending-measurement authority only. It is suitable for
planning tests and discussing mechanisms. It is not suitable for cutting,
welding, machining, tuning, or purchasing final stock without measurement and
review.
