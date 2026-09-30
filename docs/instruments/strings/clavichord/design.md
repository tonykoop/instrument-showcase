<!-- SPDX-License-Identifier: CC-BY-4.0 -->
# Clavichord Design Study

## Design Thesis

This concept treats the clavichord as an expressive tangent machine. The key
action is not only a trigger: it controls attack, speaking length, damping,
pressure after contact, and bebung. A credible build packet must therefore
model the key, tangent, string, bridge, hitch, and damping system as one
touch-sensitive mechanism.

## Mechanism Overview

When the player depresses a key, the rear of the key or an attached tangent
lever raises a brass tangent into a string from below. Contact initiates the
sound and defines the active string length. The note continues only while the
key is held because the tangent is part of the sounding boundary. Small changes
in pressure can alter tension and pitch, creating bebung when the action and
string path are stable enough.

In a fretted or listed layout, multiple keys can share one course of strings,
with different tangents defining different speaking lengths. This saves strings
and space but creates musical and mechanical constraints because some related
notes cannot sound independently. In an unfretted layout, each note has its own
course, improving independence at the cost of more strings, more pins, and more
case load.

The first design job is not a full keyboard. It is a small test action that can
compare tangent material, tangent face, key leverage, damping, and bebung
response without pretending that final scale or tuning is known.

## L2 Subsystem Plan

- Key/action coupon: isolate one key lever, balance point, return behavior, and
  tangent lift so touch can be measured before a full keyboard exists.
- Tangent contact: compare candidate brass tangent faces and adjustment methods
  on a single string course before any coordinate table is released.
- String/layout branch: keep fretted/listed and unfretted approaches as
  parallel pending-measurement branches until note-conflict and load evidence
  exists.
- Damping and release: test non-speaking-segment damping with bebung and
  dynamic touch rather than treating damping as a finish detail.
- Case/load path: keep case, bridge, hitch, and tuning-pin fields concept-only
  until string course and load tests establish a reviewed direction.
- Serviceability: require tangent adjustment, key removal, and damper access to
  be demonstrable on the coupon before promoting geometry.

## Subsystems

### Key Action

- Keys must travel smoothly and return quietly.
- The action must allow controllable pressure after tangent contact.
- Leverage, key dip, balance point, and return behavior are all
  `estimate_pending_measurement`.
- No key dimensions or spacing are released in this L2 packet.

### Brass Tangents

- Tangents are the contact, excitation, and pitch-defining surface.
- Tangent face, hardness, angle, polish, and adjustability require bench tests.
- Tangents must avoid scraping, double-striking, buzzing, or unstable bebung.
- Tangent coordinates are not provided here.

### Stringing And Layout

- Fretted/listed and unfretted approaches remain open design branches.
- String count, string material, gauges, course pairing, and tuning are not
  specified at L2.
- Shared-string layouts require an explicit note-conflict map before any L2
  claim.
- Independent-string layouts require a load and tuning-hardware review.

### Damping

- Non-speaking string segments need damping so tangent contact creates a clean
  note rather than sympathetic clutter.
- Damping material, placement, and service access are pending measurement.
- Damping must not prevent bebung or dynamic touch.

### Case, Bridges, And Pins

- The case must carry string load and keep bridge, hitch, and tangent alignment
  stable.
- Bridge placement, hitchpin field, tuning pin field, and soundboard structure
  are concept-only until measured or reviewed.
- The first prototype should separate action testing from full case design.

## Parametric Intent

Future design work should use named parameters before any fabrication file is
created:

- `estimate_keyboard_compass_pending_measurement`
- `estimate_fretted_or_unfretted_layout_pending_measurement`
- `estimate_key_leverage_pending_measurement`
- `estimate_key_dip_pending_measurement`
- `estimate_tangent_face_pending_measurement`
- `estimate_string_course_plan_pending_measurement`
- `estimate_damping_layout_pending_measurement`
- `estimate_bridge_hitchpin_field_pending_measurement`
- `estimate_case_load_path_pending_measurement`
- `estimate_action_coupon_layout_pending_measurement`
- `estimate_note_conflict_map_pending_measurement`
- `estimate_service_clearance_pending_measurement`

These names are placeholders, not values.

## First Measurement Gates

- Tangent contact: test one brass tangent against one string course for attack,
  sustain, buzz, and release.
- Bebung response: log whether pressure modulation is controllable without
  scraping or false pitch jumps.
- Dynamic touch: compare soft and firm attacks without changing released design
  authority.
- Damping: test whether non-speaking segments stay quiet while preserving
  after-contact control.
- Layout branch: compare a small fretted/listed mockup against an unfretted
  mockup before choosing the first L2 direction.
- Serviceability: prove tangent adjustment and key removal can happen without
  destructive disassembly.
- Cut-list promotion: tie each future part class to a measured or reviewed
  source before ordering, cutting, drilling, or laying out tangent positions.

## L2 Boundary

This file is a concept and engineering-risk map. It does not provide CAD,
DXF, tooling instructions, dimensions, tuning, tangent coordinates, string
gauges, pressure values, or a measured acoustic model.
