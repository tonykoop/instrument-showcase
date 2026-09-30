<!-- SPDX-License-Identifier: CC-BY-4.0 -->
# Pianola Design Study

## Design Thesis

This concept treats the pianola as a pneumatic control instrument coupled to a
piano action. The core engineering problem is not the piano scale; it is the
chain from perforated roll to tracker-bar sensing, pouch/valve amplification,
action actuation, timing, and repeatable reset.

The L2 uplift turns the initial concept into a reviewable prototype plan. It
still does not release fabrication geometry. The packet now separates the
subsystems that must be measured before a complete player mechanism is drawn:
paper transport, tracker-bar sensing, pilot pneumatics, actuator output, action
interface, control branches, and service access.

## Mechanism Overview

A perforated roll passes across a tracker bar. When a hole in the roll exposes
a tracker-bar port, the local pressure state changes. That small signal is
routed to a pouch or valve system, which amplifies the event and admits or
releases vacuum/air to a pneumatic actuator. The actuator then moves part of
the piano action so a hammer can strike a string through the normal action
chain.

The design problem is a timing and leakage problem as much as a force problem.
The tracker bar must sense holes cleanly, the roll must track without tearing
or wandering, pouches must respond quickly without sticking, valves must seal
and vent predictably, and the action must return before the next event.

Expression controls, sustain, reroll, tempo, and dynamic response remain named
branches. This L2 packet focuses on a single-note pneumatic chain plus enough
supporting structure to review how that chain could scale later.

## Subsystems

### Roll Transport

- The roll transport must keep paper aligned across the tracker bar.
- Roll drive, rewind, take-up, tension, edge guidance, and paper support are all
  `estimate_pending_measurement`.
- The first rig should let a short test strip move across one sensing port with
  adjustable support pressure and visible paper tracking.
- The transport should record whether false triggering comes from the sensing
  system or from paper wander.
- No roll scale, hole geometry, tempo range, or spool dimensions are released
  in this L2 packet.

### Tracker Bar

- The tracker bar is the sensing surface.
- Port layout, sealing surface, paper contact, and cleaning access are pending
  measured reference or prototype work.
- First tests should use a small transparent or inspectable tracker-bar section.
- The first section should include a way to isolate one port, intentionally
  introduce a leak, and clean the sensing face without losing alignment.
- Multi-note tracker-bar layout is explicitly out of scope until the one-port
  chain is measured.

### Pneumatic Signal Chain

- Tracker-bar pressure changes should operate a pouch or pilot valve.
- Pouch material, valve seat, venting path, and leakage tolerance require bench
  testing.
- Vacuum level and airflow are not specified at L2.
- The pouch/valve module should be removable so material and seat experiments
  do not force a full tracker-bar rebuild.
- Every pressure, volume, pouch area, and response-time value remains
  `estimate_pending_measurement`.

### Action Actuation

- Pneumatic output must interface with a piano key/action or a representative
  action test rig.
- The actuator should move enough to test timing and repeatability without
  claiming final strike force or tone.
- Lost motion, reset speed, and regulation are first-order risks.
- The L2 target is a repeatable bench coupling, not finished piano touch.
- The actuator path should be documented as a mechanical interface with
  pending travel, force, leverage, and reset measurements.

### Expression And Controls

- Sustain, soft/loud response, tempo, reroll, and expression coding are future
  branches.
- The first packet should not mix expressive control claims with the basic
  note-actuation proof.
- Expression claims require measured timing and action response.
- Tempo and reroll controls may be represented as placeholders in the cut list,
  but they remain concept-only until the single-note chain is stable.

### Service And Failure Modes

- Tracker-bar cleaning, paper replacement, pouch replacement, valve adjustment,
  and tubing inspection must be reachable in any future layout.
- Early tests should log common failure modes: missed trigger, false trigger,
  slow reset, pouch sticking, valve hiss, paper snag, action under-travel, and
  action over-travel.
- Any layout that hides pouches or valves behind permanent casework should be
  rejected until a measured maintenance cycle exists.

## L2 Prototype Sequence

1. Bench one tracker-bar port with a hand-moved test strip.
2. Add one pouch and pilot valve, still without a piano action.
3. Add one actuator and a representative action load.
4. Log leak, response, reset, and missed-trigger behavior.
5. Only after the single-note chain is repeatable, evaluate paired-note spacing
   and expression/control branches.

Each step is a measurement gate, not a fabrication release.

## Parametric Intent

Future design work should use named parameters before any fabrication file is
created:

- `estimate_roll_scale_pending_measurement`
- `estimate_tracker_bar_port_layout_pending_measurement`
- `estimate_pouch_area_pending_measurement`
- `estimate_valve_seat_geometry_pending_measurement`
- `estimate_vacuum_level_pending_measurement`
- `estimate_tube_routing_pending_measurement`
- `estimate_action_travel_pending_measurement`
- `estimate_repeat_rate_pending_measurement`
- `estimate_expression_control_path_pending_measurement`

These names are placeholders, not values. Any future numeric value using these
names must be marked as an estimate until measured or reviewed.

## First Measurement Gates

- Tracker sensing: verify a single roll hole can produce a clean signal without
  paper snagging or false triggering.
- Pouch response: measure whether one pouch/valve pair opens and resets
  repeatably without sticking.
- Leak behavior: record leak paths before scaling to many notes.
- Actuation: drive one action or representative key mechanism and log travel,
  reset, and missed notes.
- Timing: compare roll event timing to action event timing on a small test rig.
- Serviceability: prove tracker-bar cleaning, pouch replacement, and valve
  adjustment can happen without destructive disassembly.
- Authority review: verify that `bom.csv`, `cut-list.csv`, and future CAD or
  visual artifacts do not turn placeholder names into released dimensions.

## L2 Boundary

This file is a prototype-planning map. It does not provide CAD, DXF, tooling
instructions, dimensions, roll-hole coordinates, vacuum pressure, tuning,
strike-force values, or a measured acoustic/action model.
