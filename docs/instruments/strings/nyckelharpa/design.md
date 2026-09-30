<!-- SPDX-License-Identifier: CC-BY-4.0 -->
# Nyckelharpa Design Study

## Design Thesis

This concept treats the nyckelharpa as a keyed bowed fiddle where the keyboard
is not decorative hardware; it is the acoustic control surface. The L2 uplift
keeps the instrument in shop-planning authority: it names the assemblies,
interfaces, test rigs, and failure modes that a builder should review before
any measured layout, CAD, DXF, tuning, or string schedule is claimed. The hard
design problem is keeping tangent contact repeatable while the bowed strings
vibrate, the sympathetic strings remain free to ring, and the player can
service the keybox without disturbing the whole setup.

## Mechanism Overview

The player bows the melody strings while the left hand operates keys. Each key
slides in the keybox and carries a wooden tangent. When the key is pressed, the
tangent contacts a melody string from the side and defines a stopped speaking
point. The tangent must meet the string cleanly, avoid dragging during release,
and return without rattling.

Sympathetic strings are not stopped by the main key action. They are routed
below or through the keybox so they can respond to the bowed melody strings.
Their path must preserve clearance from moving keys and tangents, protect the
strings from accidental contact, and leave enough service access for tuning,
replacement, and resonance experiments.

The bridge, nut, tailpiece, keybox, pegbox, and body are coupled. A change in
keybox height, bridge crown, string path, tangent face, or sympathetic-string
clearance changes action feel and tone. This packet therefore records named
setup variables and shop-review fixtures rather than pretending a first-pass
drawing is build authority.

## L2 Assembly Plan

The first physical work should be split into small assemblies before a full
instrument is attempted:

- A bowed-string rail that holds one melody string over adjustable nut, bridge,
  and tail references.
- A removable keybox cassette that can slide one or more keys against the test
  string without being glued into a body.
- A tangent carrier that allows contact-face swaps, height adjustment, and
  release-clearance inspection.
- A sympathetic-string underpass mockup that shows how resonance strings can
  pass below the keybox without being touched by moving keys.
- A body and soundboard planning shell that only tests service access, load
  paths, and mounting order.

Each assembly remains `pending_measurement`. The packet does not choose final
dimensions or release any part as fabrication authority.

## Subsystems

### Bowed String Core

- Melody strings are the directly bowed voices.
- Bow response depends on bridge shape, string path, bow clearance, string
  material, and setup, all pending measurement.
- The L2 shop plan adds a test rail for one bowed string so tangent contact can
  be assessed before a full keybox exists.
- No tuning, string count, string gauges, or scale length are released in this
  packet.

### Keybox And Sliding Keys

- The keybox needs straight, low-friction key travel and a stable reference
  plane.
- Keys need return behavior that is quiet, repeatable, and serviceable.
- Tangents should be individually adjustable during setup.
- Key travel, key spacing, guide material, and return method are all
  `estimate_pending_measurement`.
- The preferred L2 study object is a removable cassette so key friction,
  return, and side-play can be tested outside the body.
- The cassette should include inspection access for the underside and the
  sympathetic-string path rather than trapping those decisions inside the case.

### Tangent Contact

- The tangent face is the pitch-setting contact element.
- Contact should stop the string clearly without crushing, buzzing, or scraping.
- Tangent geometry must allow fine adjustment after the actual string path is
  measured.
- First prototypes should separate tangent-contact tests from full instrument
  body work.
- Contact behavior should be logged as clear stop, muted stop, scrape, buzz,
  double-contact, or missed return.
- The tangent should be replaceable as a small part in the first rig so face
  material and grain orientation can be compared without rebuilding the key.

### Sympathetic String Path

- Sympathetic strings need their own nut, bridge, tail, and tuning access.
- The path must pass near the resonant body while avoiding key and tangent
  interference.
- Resonance is a setup variable, not a guarantee. The first build should log
  which strings respond, which remain weak, and which cause unwanted noise.
- The underpass path should be represented by a serviceable mockup before
  final body closure.
- The path must reserve access for string replacement, tuning hardware,
  damping experiments, and cleaning.

### Body And Service Access

- The body must support bowed-string load, keybox fasteners, bridge load, and
  sympathetic-string routing.
- Removable or inspectable keybox panels are preferred for early prototypes.
- The design should keep tangent adjustment, key cleaning, and sympathetic
  string replacement possible without full disassembly.
- The body plan should identify removable panels, keybox fastener access, and
  non-destructive inspection routes before any exterior form is fixed.
- Glue-ups, closed cavities, and decorative covers should wait until the keybox
  and sympathetic-string service model are reviewed.

## Build Sequence Intent

1. Build the one-string tangent contact rig.
2. Add one sliding key and one adjustable tangent.
3. Add a sympathetic-string clearance mockup below the keybox plane.
4. Add bridge, nut, and tail reference blocks that can be repositioned for
   measurement.
5. Review service access and remove any part that traps tuning or key repairs.
6. Only after those gates pass, draft a measured body/keybox layout for future
   L3 work.

The numbered order is a review sequence, not fabrication instruction.

## Parametric Intent

Future design work should use named parameters before any fabrication file is
created:

- `estimate_body_outline_pending_measurement`
- `estimate_melody_string_count_pending_measurement`
- `estimate_sympathetic_string_count_pending_measurement`
- `estimate_key_count_pending_measurement`
- `estimate_keybox_reference_height_pending_measurement`
- `estimate_key_travel_pending_measurement`
- `estimate_tangent_contact_face_pending_measurement`
- `estimate_bridge_crown_pending_measurement`
- `estimate_string_path_clearance_pending_measurement`

These names are placeholders, not values.

## First Measurement Gates

- Key action: verify smooth travel, return, and side-play on a bench keybox.
- Tangent contact: test one adjustable tangent against one melody string before
  making a full keyboard.
- Clearance: check tangent release and sympathetic-string clearance with a
  transparent or open keybox mockup.
- Bowing: confirm bridge and string path provide playable bow access before
  finalizing body layout.
- Resonance: document sympathetic response only after actual string paths,
  bridge contact, and body coupling are present.
- Serviceability: prove a key, tangent, and sympathetic string can be adjusted
  or replaced without destructive disassembly.
- Assembly order: confirm the keybox, bridge references, and sympathetic path
  can be installed and removed in a repeatable review sequence.
- Documentation: log each failure mode with photos or notes before changing
  tangent face, guide material, or string path.

## L2 Boundary

This file is a concept and shop-planning risk map. It does not provide CAD,
DXF, tooling instructions, dimensions, tuning, string gauges, or a measured
acoustic model. All physical values and future part blanks remain estimates
pending measurement.
