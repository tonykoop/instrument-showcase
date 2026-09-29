# Design

## Design Intent

Create an L2 root-mode build packet for vessel flutes whose pitch behavior is
set by Helmholtz resonance. The first prototype is a 130 cc ceramic ocarina lab
body with a conservative voicing and undersize finger holes. The purpose is to
validate cavity volume, voicing response, cumulative hole area, and shrinkage
before committing to a polished slip-cast family.

This packet supports issue #1 as a reviewable packet candidate. It does not
claim L3/build-ready status until measured cavity volume, shrinkage, and tuner
data are added to `validation.csv`.

## Governing Model

Helmholtz resonance:

```text
f = c / (2*pi) * sqrt(A / (V * L_eff))
L_eff = wall_thickness + end_correction
end_correction ~= 0.6 * sqrt(A/pi)
```

Variables:

- `f`: target frequency in Hz.
- `c`: speed of sound, about 34300 cm/s at 20 C.
- `A`: effective open area in square centimeters.
- `V`: cavity volume in cubic centimeters.
- `L_eff`: effective neck length in centimeters.

For finger-hole notes, `A` is cumulative effective area, not tube length. Hole
interaction and hand coverage require empirical correction.

## Starter Bodies

| Body | Role | Volume | Voicing area | Target | Notes |
| --- | --- | ---: | ---: | ---: | --- |
| VF-130-A4 | First lab body | 130 cc | 0.45 cm2 | A4 | Ocarina-style proof body |
| VF-95-C5 | Smaller response body | 95 cc | 0.35 cm2 | C5 | Tests higher voice and hand size |
| VF-180-G4 | Larger warm body | 180 cc | 0.55 cm2 | G4 | Tests low response and wall stiffness |

## Finger-Hole Area Plan

1. Calculate required cumulative area for each target note.
2. Convert each incremental area into an undersize drill diameter.
3. Drill small, measure, enlarge, and record the final diameter.
4. Update the hole-area curve before copying the body into a mold.

Starter scale for VF-130-A4 is a simple major pentatonic: `A4, B4, C#5, E5,
F#5, A5`. A chromatic fingering chart is out of scope for this L2 pass.

## Ceramic And Prototype Path

- Quick prototype: hand-shaped clay or sealed printed/plaster mockup with
  water-fill volume measurement.
- Ceramic path: slab or pinch body first; slip-cast mold only after shrinkage
  and voicing are measured.
- Mold workflow: preserve the existing `mold-workflow.md` notes and add fired
  shrinkage rows after test tiles.

## SolidWorks/OpenSCAD Handoff

The CAD handoff should expose volume, voicing area, wall thickness, hole
diameters, and mold split line as named inputs. A pretty exterior is secondary
until the Helmholtz measurements agree with the design sheet.

## L2 To L3 Gates

- Actual cavity volume measured within +/-5 cc.
- First sound is stable at low and medium breath pressure.
- Fundamental is within +/-20 cents before tuning holes.
- Tuned pentatonic notes are within +/-10 cents or documented as correction
  data.
- Fired shrinkage is measured before a slip-cast production mold is claimed.
