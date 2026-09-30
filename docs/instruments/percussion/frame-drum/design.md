# Frame Drum Design

## Design Intent

This packet defines a public-safe first frame-drum build family centered on a
16 in class single-head drum. The current readiness is `L1_packet`: the repo has
reviewable design tables, starter CAD/vector artifacts, and a measurement plan,
but no built or measured drum. The goal is not to collapse every frame-drum
tradition into one object; it is to create a repeatable engineering baseline
that can branch into bodhran, hand-drum, bendir, pandeiro, and tuned
contemporary variants as real builds are measured.

The baseline build is a shallow hardwood hoop with a natural or synthetic head,
documented across four construction paths:

- Steam-bent hoop for the most traditional continuous rim.
- Stave-built hoop using Tony's existing segmented drum experience.
- Wood-turned hoop for a sculpted profile and clean bearing edge.
- CNC-laminated hoop for repeatability, jigs, and tuner experimentation.

## Governing Model

Frame drums are membrane instruments. A circular tensioned membrane has modal
frequencies approximated by:

```text
f_mn = (alpha_mn / (2*pi*R)) * sqrt(T / sigma)
```

Where:

- `alpha_mn` is the Bessel root for the membrane mode.
- `R` is head radius.
- `T` is membrane tension per unit length.
- `sigma` is membrane area density.

The first useful design pass uses the membrane model for relative scaling, not
final pitch prediction. Real pitch depends on head material, humidity, bearing
edge, hoop stiffness, hand damping, and tensioning method. The packet therefore
ships validation rows for measured fundamental, modal spread, sustain, and
response under different head tensions.

## Baseline Geometry

| Member | Outside diameter | Hoop depth | Wall thickness | Head target |
|---|---:|---:|---:|---|
| FD-14 | 14 in | 2.50 in | 0.375 in | high hand drum / compact bodhran |
| FD-16 | 16 in | 2.75 in | 0.375 in | baseline hand drum |
| FD-18 | 18 in | 3.00 in | 0.500 in | low hand drum / bendir study |

These values are the current design-table authority for the starter model, not
measured fabrication evidence. `family-spec.csv`, `cad/frame_drum_hoop.scad`,
and `drawings/frame-drum-hoop-plan.dxf` must be reconciled after the first
prototype is measured.

## Manufacturing Strategy

The first build should use either steam bending or segmented/stave work because
those paths match Tony's existing shop knowledge and keep the acoustic rim
simple. CNC work is documented as a repeatability and fixture path, not as a
claim that verified G-code exists.

## Assumptions

- Dimensions are derived estimates until the first physical prototype is built.
- Natural hide thickness and moisture response must be measured per head.
- Shell diameter, head material, tensioning method, and safety fixture choices
  remain assumptions until a specific build path is selected and measured.
- Cultural/traditional variants require attribution and tradition-specific
  research before being presented as anything more than engineering studies.
- Feather Song style inflatable tuning is treated as credited inspiration and
  a future experiment, not as an original invention claim here.

## Validation Targets

- Hoop remains round within 1/16 in after head tensioning.
- Bearing edge has no sharp discontinuities that cut the head.
- Fundamental and first strong partials are recorded at low, medium, and high
  tension.
- Head tension can be adjusted or documented repeatably.
- Player ergonomics are checked for hand access, weight, rim comfort, and
  mallet clearance.

See `validation-loop.csv` for the Round 30 measurement loop covering head
tension, resonance, strike response, hoop roundness, and fixture safety.
