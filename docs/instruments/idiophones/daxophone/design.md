<!-- SPDX-License-Identifier: CC-BY-4.0 -->
---
instrument: Daxophone
family: idiophone_friction_wood
packet_mode: v5_l2_planning
authority: concept_only
readiness: L2 planning packet
---

# Daxophone Design Study

## Design Thesis

This V5 L2 packet frames a daxophone as an expressive friction idiophone rather
than a conventional bowed string instrument. The sound source is a wooden tongue
whose outline, grain, clamp condition, and local contact from the dax block all
change the speaking behavior. The contact pickup is part of the instrument
system because it captures details that may be quiet acoustically.

The packet stays non-dimensional. It names the subsystems, shop interfaces,
workpiece categories, and evidence gates needed before any fabrication or
tuning claim can be made.

## Mechanism

The tongue is a shaped wooden cantilever clamped at one end in a block. The bow
excites the free edge. The player's other hand uses a dax block against the
tongue face or edge to alter the active vibrating region and surface contact.
Unlike a fixed fretboard, the dax block is expressive and mobile, so its face
material, contour, grip, and finish matter.

The clamp must hold the tongue without crushing fibers or creating unpredictable
buzz. The contact pickup must sense the tongue or clamp system without becoming
a structural brace that changes the response in an undocumented way.

## L2 Subsystem Plan

| subsystem | L2 responsibility | authority | next evidence |
| --- | --- | --- | --- |
| tongue blank | identify a real wood coupon and track grain/edge preparation | pending_measurement | measured blank record and photos |
| clamp block | hold repeatably without buzz, slip, or fiber damage | pending_measurement | clamp test log |
| dax block | provide expressive contact without undocumented fret geometry | pending_measurement | contact-response notes |
| bow interface | separate bow/rosin behavior from tongue design changes | pending_measurement | bowing test log |
| contact pickup | capture vibration without becoming a structural brace | pending_measurement | reversible pickup mount test |
| output hardware | route signal and strain relief without acoustic shortcuts | pending_measurement | wiring and noise checklist |
| safety finish | remove splinter/sharp-edge risk without muting response | pending_measurement | edge and handling review |

## L2 Workpiece Plan

The first build artifact should be a coupon bench setup, not a finished
performance instrument. `cut-list.csv` names workpiece categories only: tongue
blank coupon, clamp jaw coupon, dax-face coupon, pickup-mount coupon, base
support, edge-finish coupon, cable strain-relief coupon, and test-log template.
None of those entries is a released size, tongue outline, fret/contact map,
pickup coordinate, or tuning prescription.

## Parametric Intent

Future design tables should separate measured data from choices:

- `tongue_blank_id`
- `wood_species_status`
- `grain_orientation_status`
- `tongue_outline_status`
- `edge_finish_status`
- `clamp_interface_status`
- `dax_face_material_status`
- `dax_contact_response_status`
- `pickup_mount_status`
- `bow_response_status`
- `amplified_noise_status`

All fields are currently `pending_measurement`. This repo does not infer
profiles, fret locations, pitch response, or pickup placement from prose,
images, or memory.

## Authority Boundary

- Concept authority: README, design notes, estimated BOM, and decision record.
- Measurement authority: none yet.
- CAD/DXF authority: none yet.
- Tuning authority: none yet.
- Electronics authority: none yet.

Future concept images or sketches may describe mood, ergonomics, or performance
posture, but they must not become sources for tongue profiles, clamp geometry,
dax contact curves, pickup placement, or playable pitch maps.

## Measurement Gates

Promotion beyond L2 requires:

- A real tongue coupon or blank measured and photographed before shaping.
- A clamp test that records stability, buzz, and damage risk.
- A bowing test that separates tongue behavior from pickup and amplifier color.
- A dax-block contact test that documents repeatability and expressive range.
- A pickup mounting test that records noise, handling sensitivity, and
  reversibility.
- A safety review for sharp edges, splinters, clamp force, and bowing posture.
- A traceable authority register entry for any future CAD, DXF, SVG drawing, or
  audio artifact before it can be used outside concept review.

## Risks

- Over-tight clamping can crush wood fibers or mute the tongue.
- Under-tight clamping can buzz, slip, or create false measurement results.
- Bowed-edge preparation affects response and player safety.
- The contact pickup can hide weak acoustic behavior or introduce mechanical
  artifacts.
- Dax-block contact may be expressive but hard to document without a repeatable
  measurement protocol.
