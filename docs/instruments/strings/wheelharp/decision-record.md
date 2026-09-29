<!-- SPDX-License-Identifier: CC-BY-4.0 -->
# Decision Record

## Decisions

- Readiness is `L2 V5 build-packet candidate`.
- The instrument is modeled as a keyboard-controlled rosined wheel bank, not as
  a conventional plucked, struck, or single-wheel hurdy-gurdy.
- The first technical risk is controlled friction: wheel truing, rosin, string
  contact, damping, and mechanical noise.
- The motor drive is treated as an unresolved subsystem, with no performance
  numbers claimed.
- The key action is intentionally left open between string-moving, wheel-moving,
  and pressure-shoe approaches.
- L2 scope is limited to naming review surfaces, fixture classes, authority
  boundaries, and measurement gates.
- Visual-output register rows may be `concept_only` or `pending_measurement`;
  no artifact is fabrication authority.
- The first promotion artifact should be a one-wheel coupon plus a key-action
  mule, not a full semicircular keyboard.

## L2 Promotion Gates

- Wheel coupon proves contact stability, truing method, rosin management, and
  service access.
- Key-action mule proves note-on contact and note-off damping sequence.
- String/damper test log records attack, release, chatter, squeal, sustain, and
  unwanted sympathetic response.
- Drive safety review covers guarding, heat, electrical isolation, pinch points,
  and emergency stop behavior before powered multi-wheel tests.
- Frame interface map separates wheel bank, string path, key action, damping,
  guard removal, and maintenance access.
- CAD, DXF, or drawings remain blocked until measured or reviewed parameters
  exist.

## Open Questions

- Should the wheel bank use one shared drive path or many independently driven
  wheels?
- Should each key move the string, the wheel, or an intermediate contact shoe?
- How can the design damp strings cleanly at release without making the key
  feel heavy?
- What wheel material and rosin combination gives stable tone with tolerable
  dust and wear?
- How should the semicircular keyboard route strings and linkages without
  blocking wheel maintenance?
- Should the first prototype be acoustic, amplified, or a bench test rig with
  pickups?
- What guarding is needed around continuously spinning rosined wheels?
- What must be tested in a one-wheel coupon before scaling to a wheel bank?

## Rejected From The Packet

- No dimensions.
- No tuning table.
- No string gauges.
- No wheel diameter or motor speed targets.
- No CAD, DXF, G-code, or fabrication drawing.
- No claim that the concept is ready to build.

## Still Rejected For L2

- Full keyboard scale, note count, or tuning release.
- Wheel diameter, motor speed, torque, voltage, or power claims.
- String gauge, tension, pitch layout, or scale length claims.
- CAD, DXF, G-code, or fabrication drawing authority.
- Any L3/build-ready language.
