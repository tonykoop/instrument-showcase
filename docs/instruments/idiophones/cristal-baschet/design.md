<!-- SPDX-License-Identifier: CC-BY-4.0 -->
# Cristal Baschet Design Study

## Design Thesis

This concept treats the Cristal Baschet as a friction-excited transmission and
radiation system rather than a set of decorative sculptures. The playable
surface is the wet-finger glass rod; the engineering core is the chain from rod
contact to threaded stem, movable mass, resonator, and whisker radiator.

## Mechanism Overview

The player wets the fingers and rubs glass rods. Stick-slip motion in the rod
drives a coupled metal stem. The stem carries vibration away from the glass and
into resonating or radiating structures. Threaded hardware and movable masses
allow setup experiments, but this L2 packet does not claim final positions,
pitch values, or measured tuning behavior.

Large cone or flap resonators can emphasize particular voices, while the tall
whisker radiator provides a broad visual and acoustic radiation surface. Both
remain concept mechanisms until their materials, attachment points, stiffness,
and measured response are known.

The design challenge is balancing playability, glass safety, energy transfer,
and serviceability. A beautiful radiator that overloads the glass rod or hides
threaded adjustments is a failed engineering surface. A clean test rig that
lets one rod, one stem, one mass, and one radiator be measured is the right
first artifact.

## Subsystems

### Glass Rod Exciters

- Glass rods are the finger-rubbed excitation surface.
- Rod material, diameter, length, support, and finish are all
  `estimate_pending_measurement`.
- Rod mounting must protect the player from breakage and isolate useful
  vibration from unsafe stress concentration.
- No pitch, tuning, or rod geometry is released in this packet.
- L2 review task: define a one-rod coupon record with stock source, end finish,
  support method, wet-finger playability notes, and breakage/edge observations.

### Threaded Stem Transmission

- Threaded stems carry vibration from the rod into downstream radiators.
- Threads are treated as adjustment and coupling features, not as released
  fabrication specs.
- Stem stiffness, boundary condition, nut stack, washer stack, and mass position
  require bench measurement.
- L2 review task: separate the rod joint, stem, lock hardware, and radiator
  interface in the build log so later changes do not mix causes.

### Movable Mass Tuning

- Movable masses on stems are concept setup controls.
- Future work should log mass position, contact tightness, audible response,
  sustain, and unwanted rattles.
- This packet does not provide mass values, coordinates, or tuning tables.
- L2 review task: create a measurement table before testing that records
  position as `pending_measurement` labels rather than publishing tuned
  coordinates.

### Cone And Flap Resonators

- Cone and flap resonators are candidate radiation surfaces.
- Each resonator must be tested as a replaceable module rather than fixed into
  the first frame.
- Mounting should allow comparison without rebuilding the glass rod assembly.
- Sheet thickness, cone angle, flap outline, and material are pending review.
- L2 review task: keep cone, flap, and neutral reference radiator modules
  swappable from the same stem termination.

### Whisker Radiator

- The whisker radiator is a tall array or bundle-like radiating surface,
  conceptually associated with fiberglass whiskers.
- Safety, splinter control, edge handling, mounting strain, and transport
  protection are first-order design gates.
- Whisker count, length, spacing, and anchoring are not specified in this
  packet.
- L2 review task: treat whisker material and containment as a safety test before
  treating it as a sound-radiation test.

### Frame And Player Interface

- The frame must hold fragile glass, threaded stems, resonators, and radiator
  surfaces without making setup inaccessible.
- The player interface must keep wet-finger access comfortable while isolating
  sharp, brittle, or high-strain regions.
- Cleaning, drying, rod replacement, and resonator swaps should be possible
  without destructive disassembly.
- L2 review task: keep player-wet zones, brittle glass zones, threaded
  adjustment zones, and radiator edges visually and mechanically distinct.

## L2 Shop Interface Plan

| interface | purpose | current authority | next evidence |
| --- | --- | --- | --- |
| rod-to-support | hold glass without unsafe stress concentration | pending_measurement | one-rod coupon support test |
| rod-to-stem | transmit vibration without cracking or buzz | pending_measurement | bench log with inspection photos |
| stem-to-mass | permit controlled adjustment without rattle | pending_measurement | mass sweep protocol, no tuning claims |
| stem-to-radiator | compare radiator modules without rebuilding rod rig | pending_measurement | swappable mounting notes |
| radiator-to-frame | support cone/flap/whisker modules safely | pending_measurement | handling and strain review |
| player-to-instrument | allow wet-finger access and safe maintenance | pending_measurement | ergonomic and cleaning notes |

## L2 Workpiece Plan

The first physical artifact should be a one-rod bench assembly, not the full
sculptural frame. Workpieces are named in `cut-list.csv` as categories only:
glass rod coupon, stem coupon, mass stack, replaceable radiator coupons,
whisker safety coupon, frame rail mockup, guards, and log templates. None of
those entries is a released cut size, rod count, resonator geometry, or tuning
prescription.

## Parametric Intent

Future design work should use named parameters before any fabrication file is
created:

- `estimate_glass_rod_count_pending_measurement`
- `estimate_glass_rod_geometry_pending_measurement`
- `estimate_threaded_stem_family_pending_measurement`
- `estimate_movable_mass_position_pending_measurement`
- `estimate_resonator_family_pending_measurement`
- `estimate_whisker_radiator_layout_pending_measurement`
- `estimate_frame_interface_pending_measurement`
- `estimate_player_clearance_pending_measurement`

These names are placeholders, not values.

## First Measurement Gates

- Excitation: verify one glass rod can be played repeatably with wet fingers
  without unsafe mounting stress.
- Transmission: measure whether one stem carries vibration without loosening,
  rattling, or overloading the rod joint.
- Mass sweep: log audible changes from movable mass position without publishing
  final tuning values.
- Resonator swap: compare one cone-like and one flap-like radiator module with
  the same rod/stem setup.
- Whisker safety: test handling, strain relief, and containment before any
  public-facing radiator claim.
- Serviceability: prove rod, stem, mass, and radiator modules can be inspected
  and replaced independently.

## L2 Boundary

This file is a shop-packet planning handoff. It does not provide CAD, DXF,
tooling instructions, dimensions, tuning, pressure values, resonator
coordinates, or a measured acoustic model. Fabrication remains blocked until
the one-rod rig and radiator coupons produce measured evidence.
