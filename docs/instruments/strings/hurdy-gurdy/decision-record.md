<!-- SPDX-License-Identifier: CC-BY-4.0 -->
# Decision Record

## Decisions

- Readiness is `L2 V5 build-packet candidate`; no build-ready language is used.
- The design starts from real hurdy-gurdy mechanics: rosined wheel bow, crank,
  tangent keyboard, melody strings, drones, and trompette buzzing bridge.
- The wheel is treated as the primary risk because trueness, rosin, string
  wrapping, and crank stability affect every voice.
- The trompette bridge is treated as an adjustable experiment instead of a
  fixed part.
- The keyboard is described as a serviceable tangent system; final key count,
  tangent spacing, and pitch layout are not claimed.
- Every artifact in the visual register is marked `concept_only` or
  `pending_measurement`.
- A cut-list scaffold was added as estimated blank families only, not released
  fabrication sizes.
- Engineering review is organized around wheel/string friction, keybox
  repeatability, drone control, and trompette buzz controllability.

## Alternatives Considered

- **Body-first design:** rejected for this uplift because body outline cannot
  validate wheel speech, tangent action, or trompette response by itself.
- **Fixed trompette bridge:** rejected for L2; the bridge must stay adjustable
  until buzz onset and false chatter are tested.
- **Hidden key action:** deferred because visible, serviceable tangents are
  easier to inspect during early setup.
- **Full keyboard prototype first:** deferred in favor of a smaller
  wheel/string/tangent coupon that can isolate friction and return-action
  problems.
- **Publishing estimated sizes:** rejected; all blank sizes remain `TBD` until
  measured or reviewed.

## Open Questions

- What body outline, soundboard structure, and material stack should the first
  prototype use?
- What wheel material and edge treatment can be trued repeatably in Tony's shop?
- What bearing or bushing arrangement gives stable rotation while remaining
  serviceable around rosin dust?
- How should tangents be adjusted and locked without making the keybox fragile?
- How many melody, drone, and trompette strings should a first prototype carry?
- What muting scheme makes drone testing tolerable during setup?
- What trompette bridge adjustment range is needed for controllable buzz?
- Which tests should happen on a wheel-and-string coupon before a full body is
  built?
- What wheel runout, bearing backlash, key side play, and tangent repeatability
  should become measurable acceptance gates?
- Which service operations must be possible without removing strings or the
  keybox?
- How should rosin and string wrapping changes be logged so acoustic changes
  are not attributed to the wrong subsystem?

## Rejected For L2

- No final dimensions.
- No tuning table.
- No string gauges.
- No CAD or DXF geometry.
- No image or render authority.
- No fabrication release claims.
- No fabrication authority in the visual-output register.
