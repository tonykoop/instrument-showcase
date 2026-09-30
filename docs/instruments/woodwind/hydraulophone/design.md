<!-- SPDX-License-Identifier: CC-BY-4.0 -->
---
instrument: Hydraulophone
family: woodwind_hydraulic
packet_mode: v5_l1_concept
authority: concept_only
readiness: L1 concept packet
---

# Hydraulophone Design Study

## Design Thesis

This V5 L1 packet frames a hydraulophone as a water-driven acoustic instrument,
not as a dry pipe organ or a generic fountain. The sound source is the
interaction between pressurized water jets, player-controlled apertures, and
resonant or radiating structures that convert hydraulic flow into audible
tones.

The first packet stays non-dimensional. It names the subsystems and evidence
gates needed before any fabrication, pressure, tuning, or safety claim can be
made.

## Mechanism

The instrument receives water from a controlled supply. Water exits through a
set of playable jets or finger-hole apertures. The player covers, uncovers,
interrupts, or redirects jets to change the hydraulic state and sound. Future
versions may use a key or valve mechanism, but this L1 packet does not define
keyboard geometry, jet count, pressure range, flow rate, or note layout.

The acoustic mechanism is `pending_measurement`. Candidate behaviors include
flow interruption, water/air cavity excitation, edge interaction, turbulence
noise, and coupled resonators. None is released as a validated model.

## Subsystems

### Water Supply And Pressure Control

- Provides a stable and safe water source.
- Pump, reservoir, regulator, relief, filter, and drain choices are
  `pending_measurement`.
- Pressure and flow values are not released in this packet.

### Jet And Finger-Hole Interface

- Defines where the player interacts with water flow.
- Jet shape, aperture geometry, spacing, guard shape, and tactile surface are
  all `pending_measurement`.
- Any future key mechanism must be treated as a wet mechanism with separate
  safety and maintenance review.

### Acoustic Coupling

- Converts water-flow interaction into audible sound.
- Resonant cavity, tube, edge, baffle, or radiator choices are
  `pending_measurement`.
- This packet does not claim scale, tuning, bore, pitch, or mode behavior.

### Drainage And Splash Control

- Captures water after interaction and returns or drains it safely.
- Drain path, splash guards, sanitation, and floor protection are first-order
  design gates.

### Frame And Service Access

- Supports wet plumbing, playable jets, and any resonator surfaces.
- Must allow inspection, cleaning, drying, and leak checks without destructive
  disassembly.

## Parametric Intent

Future design tables should separate measured values from design choices:

- `water_supply_status`
- `pressure_control_status`
- `jet_interface_status`
- `finger_hole_or_key_status`
- `acoustic_coupling_status`
- `resonator_strategy_status`
- `drainage_status`
- `splash_control_status`
- `sanitation_status`
- `frame_service_status`

All fields are currently `pending_measurement`. This repo does not infer
dimensions, pressure values, flow rates, tuning, or acoustic geometry from
prose, images, memory, or external examples.

## Authority Boundary

- Concept authority: README, design notes, estimated BOM, and decision record.
- Measurement authority: none yet.
- CAD/DXF authority: none yet.
- Hydraulic authority: none yet.
- Tuning/acoustic authority: none yet.
- Safety certification authority: none yet.

Future concept images may describe mood, play posture, or water-flow intent, but
they must not become sources for jet geometry, pressure, flow, hole layout,
resonator geometry, pump selection, drain sizing, or tuning.

## Measurement Gates

Promotion beyond L1 requires:

- A safe water-loop plan with supply, relief, drainage, splash, and sanitation
  controls named before testing.
- A single-jet coupon that records flow behavior without claiming a final note.
- A player-interface test for wet grip, comfort, splash exposure, and control.
- An acoustic coupon that separates water-noise, resonator behavior, and any
  pitched response.
- A maintenance review for cleaning, drying, leak inspection, and storage.
- A safety review for water pressure, slipping, electrical isolation, and public
  interaction.

## Risks

- Water pressure can create unsafe spray, leaks, or unstable handling.
- Wet interfaces can become slippery or unsanitary.
- A visually pleasing fountain-like layout may not produce controlled musical
  sound.
- Drainage and splash control may dominate the mechanical design.
- Any electronics, pumps, sensors, or lights near water require separate safety
  review before inclusion.
