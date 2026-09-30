<!-- SPDX-License-Identifier: CC-BY-4.0 -->
---
instrument: Octobass
family: strings / bowed bass
readiness: L2 concept / pending-measurement packet
authority: concept study; pending measurement
---

# Octobass Design Study

## Concept

This packet sketches a very large bowed bass in the octobass lineage: a
giant three-string instrument whose strings are too long and too high for
ordinary left-hand stopping. The player bows with the hands while a mechanical
keywork system stops selected string positions.

The engineering center of gravity is not the outline of the body. It is the
translation from a human-scale hand lever or foot pedal into a controlled,
repeatable stop at a giant string. A future build-ready packet must prove that
the stop touches the right string, at the right position, with enough force to
sound cleanly, without crushing the winding, dragging pitch, rattling, or
blocking bow access.

## L2 Subsystem Plan

- String path: define testable string courses, bridge contact, nut or top
  termination, and service access without assigning gauges, pitches, or scale
  length.
- Stop action: compare tangent, padded finger, and backed clamp contacts on a
  one-string rig before choosing a mechanism family.
- Player console: separate hand controls, foot controls, labels, and reset
  feedback so ergonomics can be measured independently from tone.
- Transmission: test cable, rod, and bell-crank paths for backlash, friction,
  noise, return reliability, and adjustment drift.
- Structure: keep body, neck, frame, and mechanism supports in a pending
  structural bucket until string loads and stop forces are measured.
- Safety and service: include string break paths, pinch zones, reset access,
  and maintenance reach in the next prototype review.

## Mechanism Direction

Candidate mechanism families:

- Hand lever bank: large organ-stop-like levers near the player, each linked to
  a selected stopping pad.
- Foot-pedal octave or position bank: pedals select lower-register stops where
  hand reach and force are least practical.
- Remote tangent stops: hard or semi-hard tangents contact the string at
  measured positions, similar in spirit to keyed string instruments but scaled
  for very high string tension.
- Padded clamp stops: paired or backed pads squeeze the string gently against a
  local reference surface, trading tonal clarity against lower damage risk.
- Cable, rod, or bell-crank transmission: a future prototype should compare
  stretch, backlash, friction, reset speed, and serviceability.

## Parametric Intent

Use named parameters before any CAD work:

- `string_count`: prompt-supplied three-string concept constraint.
- `pending_scale_length`: not specified.
- `pending_string_tuning`: not specified.
- `pending_stop_positions`: not specified.
- `pending_stop_force`: not specified.
- `pending_linkage_ratio`: not specified.
- `pending_body_outline`: not specified.
- `pending_bow_clearance`: not specified.
- `pending_service_access`: not specified.
- `pending_console_layout`: not specified.
- `pending_return_reliability`: not specified.
- `pending_string_break_safety`: not specified.

## Prototype Path

The first physical work should not be a full instrument. It should be a
single-string stop-action test rig with adjustable string tension, replaceable
stop pads or tangents, and interchangeable hand/foot inputs. The useful
measurements are actuation force, return reliability, audible rattle, clean
note onset, wear at the string contact, and how much lost motion appears after
repeated cycles.

## L2 Cut-List Intent

The candidate cut-list names parts by subsystem so a future implementer can
replace `pending_measurement` rows with measured or reviewed authority. It is
not a material order, drawing index, or machining plan.

## Non-Claims

This packet does not claim historical octobass measurements, string tuning,
string gauges, bridge geometry, plate design, body volume, linkage dimensions,
or structural sizing. Those must come from future reference research,
measurements, CAD review, and bench tests.
