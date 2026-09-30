# Steel Tongue Drum Design

Generated: 2026-05-08

## Intent

Create a traceable root-mode packet for a tuned steel tongue drum. The packet documents the first-pass geometry from `steel-tongue-drum-design-table.xlsx`, the manufacturing assumptions that can move pitch, and the validation workflow needed to turn estimates into a tuned instrument.

This design is intentionally conservative about claims. The workbook formulas size tongues from a cantilever model, but the final instrument must be tuned by measured cutting and strike tests.

## Source Artifacts

| Source | Role | Status |
| --- | --- | --- |
| `steel-tongue-drum-design-table.xlsx` | Design table and first-pass geometry | Present |
| `README.md` | Root repo overview | Expanded in this packet |
| `instrument-maker-v4` references | Physics, sourcing, print packet, validator | Applied |
| Measured prototype data | Required for final tuning confidence | Not present |

## Workbook Inputs Used

| Parameter | Value | Unit | Source / confidence |
| --- | ---: | --- | --- |
| Shell outside diameter | 12.000 | in | workbook input, assumption |
| Shell height | 6.000 | in | workbook input, assumption |
| Steel thickness | 0.079 | in | workbook input, verify with calipers |
| Kerf width | 0.040 | in | workbook input, process-dependent |
| Tongue count | 11 | count | workbook note rows include bass row plus 10 numbered rows |
| Tongue width | 1.000 | in | workbook input, derived estimate |
| Port diameter | 2.500 | in | workbook input, derived estimate |
| Tuning standard | 440 | Hz | A4 reference |
| Selected K constant | 32098 | imperial | workbook steel table, first-pass only |

## Governing Model

Use the cantilever beam model only as an initial layout estimate:

```text
f = K_steel * t / L^2
L = sqrt(K_steel * t / f)
```

Where:

- `f` is target frequency in Hz.
- `K_steel` is the workbook steel constant, currently 32098 for the selected steel row.
- `t` is steel thickness in inches.
- `L` is free tongue length in inches.

The model assumes an ideal fixed-free tongue. A real steel tongue drum departs from that ideal because the tongue remains part of a stressed plate/shell, is cut by a finite kerf, may be heat affected, may retain burrs, and is coupled to the vessel body and support system.

## Target Tongue Table

The values below are first-pass estimates from the workbook formula family. Treat every length as a starting cut length with trim allowance, not a final tuned dimension.

| Tongue | MIDI | Note | Target Hz | Derived length in | Derived length mm | Status |
| ---: | ---: | --- | ---: | ---: | ---: | --- |
| Bass | 50 | D3 | 146.83 | 4.16 | 105.6 | derived estimate |
| 1 | 57 | A3 | 220.00 | 3.39 | 86.2 | derived estimate |
| 2 | 58 | A#3/Bb3 | 233.08 | 3.30 | 83.7 | derived estimate |
| 3 | 60 | C4 | 261.63 | 3.11 | 79.0 | derived estimate |
| 4 | 62 | D4 | 293.66 | 2.94 | 74.6 | derived estimate |
| 5 | 64 | E4 | 329.63 | 2.77 | 70.4 | derived estimate |
| 6 | 65 | F4 | 349.23 | 2.69 | 68.4 | derived estimate |
| 7 | 67 | G4 | 392.00 | 2.54 | 64.5 | derived estimate |
| 8 | 69 | A4 | 440.00 | 2.40 | 60.9 | derived estimate |
| 9 | 72 | C5 | 523.25 | 2.20 | 55.9 | derived estimate |
| 10 | 74 | D5 | 587.33 | 2.08 | 52.8 | derived estimate |

## Shell / Helmholtz Estimate

The workbook includes a first-pass vessel estimate using a 12 in diameter, 6 in high partial volume assumption and a 2.5 in port. This is useful for checking whether the shell may reinforce or color the tongue field, but it should not be treated as a final resonator design.

For this packet, the shell resonance is documented as a support variable:

- Verify actual internal volume after forming, welding, or purchased shell selection.
- Measure the port diameter after deburring and finish.
- Compare struck tongue spectra mounted and unmounted.
- Record whether final mounting shifts pitch or sustain.

## Empirical Tuning Workflow

1. Rough-cut the tongues long or conservative, with rounded stress-relief termini.
2. Deburr both sides without thinning the root unpredictably.
3. Strike each tongue with the same mallet and support condition.
4. Log measured Hz and cents error in `validation.csv`.
5. Remove material in controlled passes, favoring tip/length correction first.
6. Re-measure after each tuning pass and after final mounting.
7. Re-check drift after finish cure and 24-72 hours of rest.

## Manufacturing Assumptions

- Steel grade is not locked. Mild low-carbon sheet is the default planning case; stainless is acceptable only after revisiting K, cutting method, corrosion plan, and work hardening behavior.
- Thickness must be measured at the actual blank, not assumed from nominal sheet gauge.
- Laser cutting is fast but risks heat affected zones and local stress changes.
- Waterjet cutting reduces heat risk but can leave taper, abrasive edge texture, and local burrs.
- CNC milling can control slot geometry but needs serious fixturing and coolant/chip planning on thin steel.
- Every inside slot end needs a smooth radius to reduce crack initiation.

## Unresolved Tuning Assumptions

- Actual steel grade, modulus, density, hardness, and residual stress.
- Actual kerf after the chosen cutting process.
- Whether the blank is flat sheet, preformed shell, salvaged vessel, or welded assembly.
- Final support/isolation scheme.
- Mallet hardness and strike point standard.
- Finish mass and corrosion-protection method.
- Whether the bass tongue and high tongues remain balanced in volume and sustain after final trimming.

## Acceptance Criteria

The packet becomes public-review ready only after:

- Each tongue has target Hz, measured Hz, cents error, mallet condition, support condition, and environment logged.
- Rough-cut, deburr, first strike, tuning pass, final mount, and drift check rows are complete.
- At least one process note records actual kerf, burr condition, and heat/warp observations.
- `validation-report.md` is updated from measured data rather than assumptions.
