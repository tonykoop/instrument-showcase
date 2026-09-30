# Design

## Design Intent

Create an L2 root-mode build packet for a small family of Andean duct flutes
that can be prototyped with PVC before committing to hardwood or bamboo. The
first prototype is a G4 pinkullo-style fipple flute with a removable block so
the windway, window, and labium can be tuned independently from the tube.

This packet supports issue #1 by providing a reviewable shop candidate. It does
not claim L3/build-ready status until the first prototype speaks cleanly and
the tuning rows in `validation.csv` are filled with measured data.

## Governing Model

The starting acoustic model is an open-open pipe:

```text
f = c / (2 * L_eff)
L_eff = L_physical + 2 * 0.6 * radius
c = 13552 in/s at 68 F
```

Tone-hole first pass:

```text
distance_from_foot = acoustic_length * (fundamental_hz / hole_hz)
```

The formula sizes the bore and first-pass holes only. The duct-flute voicing is
empirical: windway height, window length, block fit, labium edge quality, and
breath pressure determine whether the pipe speaks.

## Prototype Family

| Member | Musical role | Fundamental | Bore ID | Physical length | Scale path |
| --- | --- | ---: | ---: | ---: | --- |
| Pinkullo G4 | First prototype | 392.00 Hz | 0.625 in | 16.1 in | pentatonic minor first |
| Tarka A4 | Higher, brighter test | 440.00 Hz | 0.562 in | 14.3 in | pentatonic or hexatonic |
| Small duct flute C5 | Short proof body | 523.25 Hz | 0.500 in | 11.9 in | pentatonic minor |

Physical lengths include first-pass end correction and 0.25 in trimming
allowance. They are deliberately long until measured tuning confirms the
block/window behavior.

## Duct And Window Starter Geometry

| Feature | G4 starter | Validation note |
| --- | ---: | --- |
| Windway height | 0.040 in | Shim down if breath is noisy; open slightly if it chokes |
| Windway width | 0.50 in | About 80% of bore ID |
| Window length | 0.45 in | File after first sound |
| Labium angle | 35 deg | Keep edge crisp and centered |
| Block insertion | 1.00 in | Waxed fit for removable first prototype |
| Window setback from head | 0.75 in | Mark from head datum before cutting |

## Scale Options

Pentatonic minor offsets are the first tuning target: `0, +3, +5, +7, +10,
+12`. A hexatonic/diatonic test can be drilled on a sacrificial PVC body after
the pentatonic body validates the duct geometry. Do not mix scale experiments
with the first voicing validation body.

## Materials

- PVC proof-of-tune: 1/2 in nominal pipe or tube stock with measured actual ID.
- Hardwood follow-up: straight-grain cherry, maple, or walnut blank.
- Bamboo follow-up: only after node spacing and wall thickness are measured.
- Block: cedar, maple, or Delrin insert, fitted airtight but removable.

## SolidWorks/OpenSCAD Handoff

This packet does not include production CAD. The first geometry handoff should
be a simple axisymmetric bore plus rectangular window/block model with named
inputs for bore ID, OD, body length, window length, windway height, and hole
stations. CAD should not be treated as final until the G4 PVC body validates
the windway/window relationship.

## L2 To L3 Gates

- G4 prototype speaks at low and medium breath pressure.
- Fundamental and five tone holes are within +/-15 cents before final tuning.
- Final trim brings the scale within +/-8 cents or records why that target is
not practical.
- Block can be removed and reinstalled without changing pitch by more than
5 cents.
- A hardwood or bamboo body copies only measured PVC geometry, not estimates.
