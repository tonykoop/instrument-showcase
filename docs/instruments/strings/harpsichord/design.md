<!-- SPDX-License-Identifier: CC-BY-4.0 -->
---
instrument: Harpsichord
family: string_keyboard_plucked
packet_mode: v5_l2_planning
authority: concept_only
readiness: L2 planning packet
---

# Harpsichord Design Study

## Design Thesis

This V5 L2 packet frames a harpsichord as a keyboard-controlled plucked-string
system. The central design problem is not a struck action: each key must raise a
jack so a plectrum plucks the string, then returns quietly while the tongue lets
the plectrum pass back beneath the string. Registers, including 8' and 4'
choirs, are treated as selectable systems whose details remain
`pending_measurement`.

The packet stays non-dimensional. It names subsystems, dependencies, shop
interfaces, workpiece categories, and evidence gates without inventing scale
lengths, string gauges, soundboard geometry, jack dimensions, or tuning.

## Mechanism

The key action lifts a jack in a guided path. The jack carries a tongue and
plectrum that must engage a string on the upward stroke and reset on the return
without re-plucking loudly or hanging. A damper returns with the jack to stop
the string after key release.

Register slides control which jacks are active. In a future design, an 8'
register and a 4' register may be selected independently or coupled, but this
packet does not define choir count, string scale, compass, or stop linkage.

The buff/lute stop is a damping color mechanism. It needs a reversible way to
touch or mute strings consistently without becoming an accidental tuning or
structural authority.

## L2 Subsystem Plan

| subsystem | L2 responsibility | authority | next evidence |
| --- | --- | --- | --- |
| keyboard | define key/action interface without releasing lever geometry | pending_measurement | selected reference or bench action target |
| jack and tongue | prove pluck and quiet reset as a regulated mechanism | pending_measurement | one-jack mockup log |
| plectrum | separate material, cut, and voicing decisions from geometry claims | pending_measurement | plectrum coupon observations |
| registers | keep 8' and 4' concepts selectable without hardcoding spacing | pending_measurement | register-slide mockup notes |
| buff/lute stop | test reversible damping before claiming a stop layout | pending_measurement | contact and release log |
| stringing | block scale, gauge, and tension claims until reference selection | pending_measurement | stringing authority decision |
| soundboard/case | name structure and access concerns before CAD | pending_measurement | risk review and measured target |

## L2 Workpiece Plan

The first physical artifact should be a small action and register bench mockup,
not a full instrument case. `cut-list.csv` names workpiece categories only:
keyboard/action rail coupon, jack coupon, tongue/plectrum coupon, register
slide coupon, buff-stop coupon, stringing authority worksheet, soundboard/case
study coupon, and test-log template. None of those entries is a released size,
string length, jack spacing, register slot, bridge curve, or tuning
prescription.

## Parametric Intent

Future design tables should separate measured values from design choices:

- `keyboard_scope_status`
- `string_scale_status`
- `choir_plan_status`
- `jack_travel_status`
- `plectrum_material_status`
- `tongue_reset_status`
- `register_slide_status`
- `buff_stop_contact_status`
- `damper_behavior_status`
- `soundboard_strategy_status`
- `case_structure_status`

All fields are currently `pending_measurement`. This repo does not infer
dimensions, string tensions, pitch layout, jack spacing, or bridge placement
from historical examples, images, or prose.

## Authority Boundary

- Concept authority: README, design notes, estimated BOM, and decision record.
- Measurement authority: none yet.
- CAD/DXF authority: none yet.
- Stringing authority: none yet.
- Tuning authority: none yet.

Future concept images may describe action layout or visual style, but they must
not become sources for string scale, jack geometry, register spacing, bridge
curves, buff-stop placement, case dimensions, or toolpaths.

## Measurement Gates

Promotion beyond L2 requires:

- A selected historical reference, measured exemplar, or explicit design target
  for keyboard scope and stringing.
- A bench test for jack lift, plectrum release, tongue reset, and damping.
- A register-slide mockup that proves alignment and serviceability.
- A buff-stop test that records contact behavior and reversibility.
- A soundboard and case concept reviewed for structural and acoustic risk.
- A safety and maintenance review for string tension, sharp wire ends, and
  access to regulated action parts.
- A traceable authority register entry for any future CAD, DXF, SVG drawing,
  stringing table, Wolfram model, or audio artifact before it can be used
  outside concept review.

## Risks

- Jack guidance can bind if register and rail relationships are not measured.
- Plectrum voicing may dominate tone and touch more than the first concept
  predicts.
- Register selection can create alignment errors if it is treated as a visual
  layout rather than a regulated mechanism.
- Buff damping can mute unevenly or interfere with normal speaking length if
  not tested.
- Stringing and soundboard choices can create structural loads that are outside
  the authority of an L1 concept packet.
