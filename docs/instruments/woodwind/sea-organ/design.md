<!-- SPDX-License-Identifier: CC-BY-4.0 -->
---
instrument: Sea Organ
slug: sea-organ
family: woodwind / environmental pipe organ
readiness: L1 concept packet
authority: concept_only / pending_measurement
---

# Sea Organ Design Study

## Concept

A sea organ uses wave and tide motion as the air driver for organ-like pipes.
In the envisioned instrument, water movement in or near a seawall compresses
or displaces air through ducts, resonant chambers, or pipe mouths. The result
is a changing, site-responsive sound field rather than a keyboard-controlled
organ.

This packet captures the mechanism families and review gates only. It does not
specify pipe lengths, bore sizes, resonator shapes, chamber volumes, air
pressures, windway geometry, pitch targets, tide ranges, wave loads, drainage
geometry, seawall reinforcement, CAD geometry, or DXF coordinates.

## Mechanism Families

- Wave-air capture: a future system may use water-level changes, wave impact,
  or trapped-air displacement, but the capture geometry is not specified here.
- Air path: ducts, manifolds, valves, and drains are concept-only until site
  measurements and marine engineering review exist.
- Pipe voices: pipes may be organ-pipe-like, whistle-like, or hybrid coastal
  resonators, but tuning and voicing are pending measurement.
- Marine structure: any seawall, breakwater, pier, or shoreline integration
  belongs to civil/marine engineering review before instrument design claims.
- Public setting: sound level, access, maintenance, corrosion, wildlife, and
  safety are first-order design gates, not afterthoughts.

## Pending Parameters

Use named unknowns before any model, CAD, or shop packet:

- `pending_site_tide_range`: not specified.
- `pending_wave_energy_profile`: not specified.
- `pending_air_capture_geometry`: not specified.
- `pending_chamber_volume`: not specified.
- `pending_pipe_count`: not specified.
- `pending_pipe_scale_or_pitch_policy`: not specified.
- `pending_pipe_material`: not specified.
- `pending_drainage_strategy`: not specified.
- `pending_saltwater_corrosion_strategy`: not specified.
- `pending_public_safety_boundary`: not specified.
- `pending_structural_authority`: not specified.

## L1 Prototype Path

The first useful prototype is not a shoreline installation. It should be a
non-structural airflow coupon or benchtop test plan that can compare how
intermittent water motion drives air through one removable pipe or whistle
body. That study should record only qualitative behavior until instruments,
site measurements, and review procedures are selected.

After that, a site-study packet can identify measurement needs for tide/wave
conditions, saltwater durability, drainage, access, public safety, and
permitting. A full V5 shop packet should wait until those evidence gates exist.

## Authority Boundary

This file is `concept_only` and `pending_measurement` authority. It is suitable
for planning research and discussing mechanism tradeoffs. It is not suitable
for cutting pipes, drilling seawalls, specifying materials, selecting tuning,
claiming pressure/flow values, or issuing CAD/DXF files.
