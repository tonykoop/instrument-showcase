<!-- SPDX-License-Identifier: CC-BY-4.0 -->
# Music Box Design Study

## Design Thesis

A music box is a timing instrument as much as an idiophone. The sound comes from
steel comb teeth, but the perceived music depends on pin placement, tooth
release, governor stability, escapement behavior, damping, and the stiffness of
the frame that holds the comb and cylinder in alignment.

This L2 packet treats the project as a sequence of coupled mechanisms rather
than a decorative case with a comb inside. The uplift organizes those
mechanisms into reviewable interfaces while preserving the authority boundary:
all numeric design values remain `estimate_pending_measurement` until coupons,
mockups, or reviewed drawings exist.

## Mechanism Overview

A cylinder rotates under controlled drive. Raised pins on the cylinder engage
comb teeth in sequence. Each tooth is lifted, released, and allowed to vibrate.
The comb turns stored mechanical timing into sound. A governor and escapement
control the rate of cylinder rotation so the melody does not speed up or stall.

This packet does not choose final tooth count, pitch set, cylinder diameter,
pin grid, governor type, spring motor, crank drive, case geometry, or resonance
strategy. Those values require measured or reviewed authority before any build
packet can advance.

## L2 Architecture

The build-packet candidate is organized around five authority domains:

- program authority: the cylinder, pins, indexing, and tune encoding;
- comb authority: tooth material, tuning workflow, mounting, and damping;
- release authority: pin-to-tooth lift, release, clearance, and wear;
- speed authority: governor, escapement, drive source, and backlash control;
- frame authority: alignment, resonance path, service access, and noise
  isolation.

Each domain can be prototyped independently before the full instrument is
drawn. That separation is the main L2 improvement over the L1 concept packet.

## Subsystems

### Pinned Cylinder

- The cylinder stores note timing and tooth selection.
- Pin placement must align with comb teeth without side-loading or double
  plucking neighboring teeth.
- Pin height, pin profile, retention, and cylinder material are pending
  measurement.
- A future layout must distinguish musical timing from fabrication coordinates.
- The cylinder needs datum references for start position, row alignment, and
  service removal, but this packet does not assign those datum dimensions.
- A future tune-layout table should distinguish `musical_step_index`,
  `tooth_lane_id`, `event_duration_estimate_pending_measurement`, and
  `pin_authority_status`.

### Steel Comb

- The comb is the primary sound generator.
- Tooth material, profile, root relief, heat treatment, tuning method, and
  mounting stiffness are unresolved.
- Tooth tuning is intentionally not specified here.
- A first test should use a small comb coupon before any full melody cylinder is
  designed.
- The comb coupon should answer whether the shop can make repeatable teeth,
  whether tooth roots crack or fatigue, and how much mount stiffness changes
  sustain.
- Comb authority should eventually come from measured coupons or a reviewed
  commercial comb reference, not from generated calculations in this repo.

### Pluck And Release Interface

- Pins must lift each tooth enough to speak, then release without scraping,
  jamming, or over-bending the tooth.
- The release point controls attack noise and tooth stress.
- Clearance, tooth tip shape, and pin surface finish are first prototype
  questions.
- The mechanism needs a way to test one tooth and one pin before scaling.
- The interface test should log failed releases, double plucks, side loading,
  audible scrape, and permanent tooth set. No pass/fail thresholds are assigned
  until a physical mule exists.

### Governor And Escapement

- The speed-control system prevents runaway and stabilizes tempo.
- Candidate approaches include fan governor, flyball-style governor, friction
  governor, escapement, or hybrid control.
- No speed, torque, spring force, or gear ratio values are claimed here.
- The first prototype should measure speed stability, audible mechanism noise,
  and recovery after load changes.
- The governor should be evaluated separately from comb tone so mechanical
  noise is not mistaken for musical attack. A stethoscope, phone spectrogram,
  or contact mic may be useful later, but this packet records no measurements.

### Drive Train

- A spring motor, hand crank, or weight drive are all concept options.
- Gear train noise, backlash, lubrication, service access, and stop/start
  control are unresolved.
- The drive should be isolated from the comb so gear noise does not dominate the
  tone.
- L2 review should decide whether the first mule is hand-cranked for simplicity
  or spring-driven for realistic speed-control behavior.

### Frame, Case, And Resonance

- The frame must hold the cylinder and comb in stable alignment.
- The case may act as a resonator, protector, and service enclosure.
- Resonance strategy is intentionally unresolved: wood soundboard, box cavity,
  contact pickup, or hybrid amplification all remain concept options.
- Access for tuning, pin service, governor adjustment, and cleaning is a core
  design requirement.
- The case should include removable inspection panels in the eventual design,
  but this packet does not define panel size, hinge geometry, or fasteners.

## Prototype Sequence

1. Comb coupon: one or more test teeth mounted in a small block, used only to
   learn speech, sustain, fatigue, and tuning workflow.
2. Pin-release coupon: one pin, one follower or tooth tip, adjustable lift, and
   repeated cycling to observe scrape and release behavior.
3. Registration mule: a short un-tuned cylinder segment with several lanes,
   used to test lane spacing conceptually without publishing coordinates.
4. Speed-control mule: drive source, governor candidate, and load simulator,
   used to compare noise and steadiness.
5. Integrated bench mule: small cylinder, small comb coupon, temporary frame,
   and rough case only after the prior tests name the missing parameters.

## Acceptance Evidence For L3 Consideration

Before any future L3 claim, the repo should contain measured logs or reviewed
authority for:

- comb tooth material and tuning response;
- cylinder-to-comb registration repeatability;
- pin lift/release wear behavior;
- governor and drive speed stability;
- frame stiffness and service access;
- resonance/noise tradeoff;
- CAD/DXF or reviewed drawings that trace to measured parameters.

## Parametric Intent

Future work should name parameters before assigning values:

- `estimate_tooth_count_pending_measurement`
- `estimate_cylinder_pin_grid_pending_measurement`
- `estimate_comb_material_pending_measurement`
- `estimate_tooth_profile_pending_measurement`
- `estimate_pin_height_pending_measurement`
- `estimate_governor_architecture_pending_measurement`
- `estimate_drive_train_ratio_pending_measurement`
- `estimate_case_resonance_strategy_pending_measurement`

These names are placeholders only. They are not dimensions, tuning values, or
performance targets.

## L2 Packet Interfaces

- `bom.csv` lists the part families and review status.
- `cut-list.csv` lists future cut categories with `estimate_pending_measurement`
  placeholders instead of dimensions.
- `visual-output-register.csv` records the authority of packet files and planned
  future artifacts.
- `decision-record.md` records what was promoted to L2 and what still blocks
  build readiness.

## Measurement Gates

- Comb coupon: verify tooth speech, sustain, stress, and tuning workflow.
- Pin coupon: test lift, release, scraping, and repeatability on one tooth.
- Alignment test: verify cylinder-to-comb registration without side loading.
- Governor test: measure speed stability and mechanical noise under changing
  load.
- Drive test: compare crank, spring, or other drive options before committing
  to a case layout.
- Damping/noise test: separate comb tone from gear, escapement, and case noise.
- Service test: confirm that pins, comb teeth, governor, and drive train can be
  adjusted without destroying the assembly.

## L2 Boundary

This design study is a build-packet candidate only. It does not define a scale,
melody, tuning system, tooth geometry, pin coordinates, governor dimensions,
CAD model, DXF, or fabrication release.
