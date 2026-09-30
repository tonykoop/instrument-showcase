# Great Highland Bagpipe Build Packet

## Intent

Build a first-pass engineering packet for a complete Great Highland Bagpipe set
that exposes the system interactions: chanter bore and reed, drones and drone
reeds, bag pressure, stocks, blowpipe valve, tuning slides, sourcing,
maintenance, and validation. The goal is not to claim a finished concert-grade
set from formulas alone; it is to define the measured build loop that gets from
workbook geometry to a playable, serviceable prototype.

## Catalog Metadata

| Field | Value |
| --- | --- |
| Instrument ID | GHB-001 |
| Slug | great-highland-bagpipe |
| Family | reed |
| Pipeline | cnc-lathe |
| Reference workbook | `great-highland-bagpipe-design-table.xlsx` |
| Done-bar family | reed woodwinds, closest local sisters: `chalumeau`, `duduk` |
| Date | 2026-05-08 |

## Design Inputs

| Parameter | Workbook value | Notes |
| --- | ---: | --- |
| Chanter Low A | 480 Hz | Modern GHB pitch, not A440 concert pitch |
| Speed of sound | 13510 in/s | Workbook value, roughly room-temperature air |
| Chanter scale | Mixolydian-like, just intonation | Tuned to drones, not equal temperament |
| Wood reference | African blackwood | Ipe, cocobolo, Delrin, maple, cherry, walnut are prototype alternatives |
| Drone tuning | two A3 tenors, one A2 bass | Tenors one octave below Low A; bass two octaves below |
| Bag pressure | 18-25 inH2O first-pass range | Pressure changes reed pitch and stability |

## Governing Model

The Great Highland Bagpipe is a coupled reed/resonator/reservoir system. The
packet intentionally uses different first-order models for different
subsystems, then validates the coupled result under pressure.

### Chanter

The chanter is a conical bore driven by a double reed. A conical reed pipe
behaves closer to an open-open pipe for pitch than a cylindrical stopped pipe,
but tone holes, reed compliance, and bore taper dominate the final intonation.
The workbook dimensions and measured practice-chanter hole positions are the
starting geometry.

```text
f_chanter ~= c / (2 * L_eff)
L_eff ~= c / (2 * f_target)
c = speed of sound in inches per second
```

Worked example from the workbook:

```text
Low A = 480 Hz
c = 13510 in/s
L_eff = 13510 / (2 * 480) = 14.073 in
Workbook physical full chanter length = 14.5 in
```

The difference between effective and physical length is expected because the
reed seat, conical end behavior, bell flare, and tone-hole network all shift the
effective acoustic length. Final tuning must start with undersize holes and
open them by measurement.

### Drones

The drones are cylindrical single-reed pipes, closed at the reed end and open at
the top. They are first-pass stopped pipes with odd-harmonic emphasis.

```text
f_drone ~= c / (4 * L_eff)
L_eff ~= c / (4 * f_target)
```

Worked examples from the workbook:

```text
Tenor drone A3 = 240 Hz
L_eff = 13510 / (4 * 240) = 14.073 in

Bass drone A2 = 120 Hz
L_eff = 13510 / (4 * 120) = 28.146 in
```

The workbook's physical sections intentionally exceed or subdivide these
effective lengths because tuning chambers, hemped slides, reed seats, and cap
geometry move the acoustic endpoint.

### Bag Pressure And Reeds

The bag is a pressure reservoir, not just a container. The reed only oscillates
inside a stable pressure window. Pressure changes can sharpen or destabilize
the chanter and drones, so every tuning row in `validation.csv` includes
environment and pressure notes.

```text
cents_error = 1200 * log2(measured_hz / target_hz)
pressure_target = 18-25 inH2O for first prototype testing
```

`family-spec.csv` now records the source role for each reed-coupled subsystem.
The chanter is treated as an empirically seeded conical reed pipe for planning
purposes, with final authority coming from purchased double-reed measurements.
The drones are treated as empirically seeded stopped reed pipes, with the
second tenor explicitly blocked from copy status until the first tenor reed,
slide, and pressure response are measured. `reed-pressure-validation.csv`
defines the pressure gates that must be filled before any reed, bore, slide, or
coupled tuning claim can move beyond `measurement_required`.

Do not use the 18-25 inH2O range as measured evidence by itself. It is only the
planned normal-play test window until a manometer log records onset pressure,
normal-play stability, cutoff/choke behavior, reed setting, and cents error for
the selected chanter and drone reeds.

### Empirical Correction Guard

No Native American flute K2 correction is applied here. This packet uses
first-order conical/stopped-pipe estimates plus measured GHB-specific
validation rows. Any future correction must be derived from measured chanter,
drone, reed, and pressure data from this family.

## Chanter Scale Table

| Note | Ratio to Low A | Target Hz at Low A 480 | Model L_eff in | Prototype action |
| --- | ---: | ---: | ---: | --- |
| Low G | 8/9 | 426.67 | 15.832 | Validate as cross/fingering-dependent low note |
| Low A | 1/1 | 480.00 | 14.073 | Establish reed strength and pressure first |
| B | 9/8 | 540.00 | 12.509 | Drill undersize, tape-tune up |
| C written C# | 5/4 | 600.00 | 11.258 | Drill undersize, tune against drones |
| D | 4/3 | 640.00 | 10.555 | Check just fourth against drones |
| E | 3/2 | 720.00 | 9.382 | Watch high hand spacing and hole size |
| F written F# | 5/3 | 800.00 | 8.444 | Small tuning changes are sensitive |
| High G | 7/4 | 840.00 | 8.042 | Treat as cross-fingering/harmonic validation |
| High A | 2/1 | 960.00 | 7.036 | Validate as octave behavior, not a simple hole row |

## Subsystem Interfaces

| Interface | Critical fit | Validation |
| --- | --- | --- |
| Chanter reed to chanter seat | Airtight staple fit, stable blade opening | Reed seats without wobble; Low A speaks at target pressure |
| Chanter stock to bag | Stock tie-in and hemp seal | No bubbles in leak test |
| Drone reed to drone seat | Reed body matches seat diameter | Reed starts, cuts off, and restarts predictably |
| Drone slides | Hemped tenon/socket with tuning travel | Smooth movement, no air loss, no sudden pitch jumps |
| Blowpipe valve | One-way seal | Bag holds pressure when player stops blowing |
| Bag to stocks | Mechanical tie-in | 60-second pressure hold test |

## Hardware Alignment

| Operation | Tooling | Fixture | Notes |
| --- | --- | --- | --- |
| Chanter exterior turning | Lathe roughing/detail tools | Between centers, then chuck/collet | Leave extra length for holding and trimming |
| Chanter conical bore | Step drills plus custom tapered reamer | Headstock-driven deep bore setup | Bore straightness is a high-risk acoustic variable |
| Tone holes | Drill press or mill, undersize bits | V-block indexed to front/back datum | Open by reaming/sanding while measuring pitch |
| Drone cylindrical bores | Long brad-point/twist drills, reamers | Lathe center drilling and steady rest | Build one tenor as process proof |
| Tuning slides | Lathe turning and parting tools | Matched tenon/socket gauges | Hemp clearance must be planned, not guessed |
| Stocks | Lathe boring tools | Batch fixture for repeated stock bodies | Tie-in groove must not cut too deep |
| Mounts/ferrules | Lathe, optional laser engraving | Mandrels for Delrin/ferrule rings | Keep decorative parts removable in prototype |

## Build Strategy

Prototype order is deliberately reeds-first and pressure-first:

1. Buy three chanter reeds and one synthetic drone reed set.
2. Buy a synthetic zipper bag and blowpipe valve before final tuning work.
3. Build a practice/prototype chanter in cherry, walnut, ipe, or Delrin.
4. Validate bore, reed, and hole tuning before building African blackwood.
5. Build one tenor drone, then duplicate it after measured success.
6. Build the bass drone after slide and reed behavior are stable.
7. Tie in stocks, run leakage tests, and maintain a tuning/pressure log.

## Assumptions And Unknowns

| Item | Status | Why it matters |
| --- | --- | --- |
| Chanter bore station table | Derived from workbook and practice measurements | Final intonation needs measured stations, not only a linear cone |
| Reed brand/strength | Unknown until purchased | Reed compliance changes pitch, pressure, and response |
| Bag actual volume | Supplier-dependent | Affects stability and ergonomic squeeze behavior |
| Drone reed seat dimensions | Must match chosen reeds | Synthetic reed body diameters vary |
| Final decorative mount dimensions | Flexible | Do not let ornament drive acoustic or service dimensions |

## Validation Plan

Validation starts with the subsystem, then moves to the coupled system:

1. Bench leak test every stock, reed seat, slide, and bag tie-in.
2. Measure pressure at start, normal play, and cut-off for chanter and drones.
3. Tune drones without the chanter, then add chanter and listen for beating.
4. Record note frequency, cents error, pressure, temperature, humidity, reed,
   and corrective action in `validation.csv`.
5. Repeat after 24 hours to catch hemp compression, bag leakage, and moisture
   effects.
