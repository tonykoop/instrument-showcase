# Ocarina Build Packet

## Source

- Design table: `docs/Ocarina.xlsx`
- Sheet: `Ocarina`
- Inspected range: `A1:H141`
- Workbook content observed: design inputs, size library, Helmholtz calculator, 12-hole fingering chart, ceramic workflow, BOM, design notes, and Wolfram notebook notes.

## Design Intent

Build a slip-cast ceramic Alto C 12-hole ocarina using a 3D-printed master and plaster mold workflow. The current table is focused on the standard "sweet potato" vessel-flute form, but the same model can be used as the baseline for sculptural vessel flutes.

## Governing Model

Ocarinas behave primarily as Helmholtz resonators:

```text
f = c/(2*pi) * sqrt(A_open/(V_chamber * L_eff))
```

Unlike a transverse flute or Native American style flute, pitch is driven by chamber volume and total open-hole area, not tone-hole distance along a bore. Hole position is still important for ergonomics, grip, and fingering logic.

## Current Workbook Inputs

| Field | Current value |
| --- | --- |
| Ocarina type | Alto C, 12-hole |
| Chamber volume | 130 cm3 |
| Wall thickness | 0.4 cm |
| Voicing window width | 0.9 cm |
| Voicing window height | 0.5 cm |
| Speed of sound | 34300 cm/s |
| Clay body | Cone 6 stoneware |
| Shrinkage | 12 percent |
| Target low note | A4, 440 Hz |
| Target high note | F6, 1397 Hz |

## Critical Design Features

- Chamber volume is the master tuning input. Measure it by water fill after CAD, master print, greenware, bisque, and glaze fire.
- Voicing window area sets the all-closed low-note behavior along with volume and effective neck length.
- Fipple geometry is the playability bottleneck: windway gap, labium angle, channel smoothness, and edge sharpness should be treated as first-class dimensions.
- Finger holes should start undersized. Enlarge to sharpen; flattening after over-enlarging is possible but slower and less clean.
- Exterior-only glazing is preferred for tuning stability and acoustic response. Mask the fipple, holes, and chamber interior.

## Workbook Improvement Notes

During inspection, rows 39-42 of the 12-hole fingering chart contain formulas for hole area, cumulative open area, and calculated frequency. Rows 43-51 currently show placeholder `=` cells instead of filled formulas. Recommended next workbook cleanup:

1. Copy the area formula pattern from `D40:D42` through `D51`.
2. Copy the cumulative area pattern from `E40:E42` through `E51`.
3. Copy the frequency formula pattern from `F40:F42` through `F51`.
4. Add measured frequency, cents error, and tuning action columns.
5. Add a note that hole combinations can be cross-fingered if total open area is equivalent.
6. Verify the size-library `Length (in)` column. Inspection showed serial-like values such as `46180`, so those cells may have been formatted or entered incorrectly.

## Mold Strategy

Use a 2-piece plaster mold for the main body. The first prototype can use a press-molded body to speed iteration, but production should move toward slip casting once the fipple and chamber volume are stable.

Recommended mold/CAD features:

- Split line around the widest body perimeter.
- Positive registration keys that do not trap clay.
- Pour/drain path or assembly opening appropriate to the chosen casting workflow.
- Removable or cleanable fipple detail. If the fipple is too delicate for the mold, cast a blank and hand-cut the voicing at leather-hard stage.
- Master scale factor: `1/(1 - shrinkage)`; for 12 percent shrinkage this is about `1.136`.

## Prototype Ladder

| Prototype | Goal | Success criteria |
| --- | --- | --- |
| OCA-P0 voicing tile | Practice windway/labium only | Clear tone on a disposable test cavity |
| OCA-P1 closed vessel | Verify chamber volume and fipple | Stable A4-ish all-closed tone before finger holes |
| OCA-P2 4-hole | Prove tuning workflow | Four tuned notes within +/-25 cents after bisque |
| OCA-P3 12-hole | Full range test | Chromatic pattern playable, no blocked grip |
| OCA-P4 matched set | Soprano C, Alto C, Bass C | Shared mold logic and glaze family |

## Open Assumptions

- Pricing in the workbook is an estimate and has not been date-checked.
- Clay shrinkage must be measured for Tony's actual slip, not assumed from supplier average.
- The fipple may need empirical iteration beyond the Helmholtz model.
- Exact ergonomics depend on hand span and final sculptural body shape.
