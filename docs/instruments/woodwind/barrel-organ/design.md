<!-- SPDX-License-Identifier: CC-BY-4.0 -->
---
instrument: Barrel Organ
slug: barrel-organ
family: woodwind
class: hand-cranked mechanical organ with pinned barrel and windchest
readiness: L2 V5 build-packet candidate
authority: concept_only / pending_measurement
---

# Barrel Organ Design

## Design Thesis

A barrel organ is a mechanical wind instrument where a crank links three jobs:
advance the music program, supply wind, and pace the player's performance. The
barrel stores note events as pins or raised features. Followers or trackers read
the program and open pallets in a windchest. Wind from bellows and a possible
reservoir speaks a pipe rank.

This L2 packet deepens the architecture enough for review and mule planning. It
does not define barrel diameter, pin pitch, gear ratio, pallet travel, wind
pressure, pipe scale, pipe length, tuning, or cut geometry.

## Subsystem Plan

### Program Barrel

The barrel program is the mechanical score. The first review should decide
whether the study mule uses a fixed barrel, removable barrel, or replaceable
pinned strip. Each option remains `pending_measurement` because pin retention,
follower wear, indexing, reset-to-start behavior, and timing repeatability have
not been tested.

Planned evidence:

- barrel indexing method chosen and tested;
- follower contact material selected from a wear/noise test;
- tune-start registration checked without pipework;
- pin-retention method reviewed before any drill/CAD/DXF work.

### Crank And Drive Train

The crank must coordinate barrel advance and bellows pumping. A future drive
table should record crank cadence, lost motion, backlash, and reset behavior,
but this packet assigns no ratios or wheel sizes. The first mule should allow
the barrel drive and bellows drive to be isolated so timing and wind faults can
be diagnosed separately.

### Followers, Trackers, And Pallets

The action path is:

```text
barrel pin -> follower -> tracker or lever -> pallet -> pipe channel
```

The review target is a small number of channels with visible motion and easy
adjustment. Authority remains `pending_measurement` until lift, return force,
friction, sealing, and noise are measured.

### Bellows, Reservoir, And Windchest

The bellows and optional reservoir must smooth crank pulses before the windchest
feeds pipe channels. The L2 packet records the need for a wind mule but does
not set pressure, flow, reservoir volume, gasket dimensions, or channel layout.
The windchest should be serviceable: pallet faces, gaskets, springs, and tracker
attachments need access before tonal work starts.

### Pipe Rank Options

The first voice may be flue pipes, reed pipes, or one comparison channel of
each. This packet keeps both families open because package size, voicing effort,
wind demand, and reliability are not yet measured. No pipe pitch, scale, mouth
geometry, reed dimensions, or tuning system is claimed.

### Case And Service Access

The case is treated as an inspection frame rather than finished furniture. It
must expose the barrel, follower row, tracker path, windchest, and bellows for
testing. Handles, enclosure layout, mass, clearances, and access panels remain
`pending_measurement`.

## Parametric Intent

Future tables should use explicit status fields before numbers appear:

- `barrel_program_status`
- `barrel_indexing_status`
- `pin_retention_status`
- `follower_material_status`
- `tracker_motion_status`
- `pallet_seal_status`
- `crank_drive_status`
- `bellows_wind_status`
- `reservoir_need_status`
- `windchest_channel_status`
- `pipe_rank_status`
- `case_access_status`

Numeric fields must be labeled as `estimate_pending_measurement` until they
come from a measured mule, reviewed drawing, supplier specification, or
validated design table.

## L2 Mule Plan

1. Build or mock the crank-to-barrel motion without pipework.
2. Add a follower/tracker/pallet channel and log repeatability.
3. Add bellows and a simple windchest test channel.
4. Compare a flue-pipe and/or reed-pipe response only after wind steadiness and
   pallet sealing are understood.
5. Update `visual-output-register.csv`, `bom.csv`, and `cut-list.csv` before
   any CAD, DXF, or tuning table is introduced.

## Authority Boundary

This is an L2 planning packet. It is not a barrel drilling plan, pinned tune
layout, pipe-scale chart, wind-pressure design, CAD source, DXF release, or
fabrication package. Every artifact remains either `concept_only` or
`pending_measurement`.
