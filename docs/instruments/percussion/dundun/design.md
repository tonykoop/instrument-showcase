# Dundun Trio V5 Starter Design

Current status: L2 V5 build-packet candidate.

Fabrication authority: not build-ready. The existing scanned planning pages
and build photos are preserved as reference evidence. Future DXF, CAD, design
tables, or measured templates must control shop dimensions.

## Intent

This packet frames a three-drum stave-built dundun family:

- Kenkeni: small/high voice and timekeeping pulse.
- Sangban: middle voice and melodic/harmonic lead.
- Doundounba: large/low voice and bass anchor.

The design target is a coherent trio rather than three isolated drums. Shell
diameter, shell depth, hide mass, rope tension, and dual-head coupling all need
to be measured together before CAD can be released.

## Planning-Derived Shell Assumptions

The main dimensional evidence is the scanned planning sheet
`drawings/img20260426_00504715.png`. It records these starter targets:

| Voice | Planning target | Stave options shown | Current authority |
| --- | --- | --- | --- |
| Doundounba | 17 in diameter x 27.5 in long | 24 staves at 2.219 in width and 7.5 deg bevel; 18 staves at 2.952 in width and 10 deg bevel | reference only |
| Sangban | 14 in diameter x 22.65 in long | 24 staves at 1.827 in width and 7.5 deg bevel; 18 staves at 2.431 in width and 10 deg bevel | reference only |
| Kenkeni | 11 in diameter x 17.35 in long | 24 staves at 1.436 in width and 7.5 deg bevel; 18 staves at 1.91 in width and 10 deg bevel | reference only |

These are useful planning dimensions, but they need confirmation against
available lumber, finished wall thickness, head seating diameter, ring stock,
and ergonomic handling before they become fabrication geometry.

## Head And Rope System

Assumed construction is a two-headed cowhide dundun with top and bottom hoop
assemblies linked by vertical rope. Tension diamonds or similar rope pulls
raise both heads together, so the instrument should be treated as a coupled
membrane-shell system rather than a single isolated head.

Open head measurements:

- Cowhide thickness and mass per unit area.
- Wet-stretch allowance from rawhide to seated dry head.
- Bearing-edge radius and final head clear diameter.
- Hoop/ring outside diameter, ring material, and wrap thickness.
- Rope diameter, rope fiber, stretch under load, and knot/diamond spacing.
- Whether each drum gets side bell mounting hardware and where that hardware
  lands relative to rope paths.

## Acoustic Model

The first-order model has three interacting parts:

- Tensioned circular membrane modes set by head radius, hide mass, and tension.
- Cylindrical air volume and shell resonance set by length, diameter, wall
  thickness, and wood stiffness.
- Dual-head coupling through the enclosed air and shared rope tension.

Target pitch relationship is approximately a fourth between adjacent voices,
with doundounba lowest, sangban in the middle, and kenkeni highest. Exact Hz
targets are measurement-required because traditional dundun tunings vary by
ensemble, hide, and playing style.

## Decisions To Make Before CAD Release

- Choose 18 or 24 staves for each voice. The 24-stave option gives a rounder
  shell; the 18-stave option uses wider staves and may simplify stock yield.
- Confirm whether shell dimensions are inside diameter, outside diameter, or
  finished head-seat diameter in each historical drawing note.
- Define wall thickness and bearing-edge profile.
- Define ring diameter offsets and rope clearance.
- Decide whether all three drums share a common stave count and jig setup.
- Decide finish and moisture-sealing requirements for cowhide seating areas.

See `shell-head-tension-validation-plan.md` for the gate-by-gate plan that
turns these decisions into measured shell, head, rope, and family evidence
without claiming build-ready authority.

## Unknowns Requiring Measurement

- Actual dimensions from any surviving physical drums or templates.
- Finished shell roundness tolerance after glue-up and sanding.
- Shell resonance and tap tone before heading.
- Head seating diameter after hide dries.
- Rope stretch after initial tuning, after 24 hours, and after a playing cycle.
- Ergonomic carry and playing height with strap, stand, or floor position.
- Whether side-bell hardware changes balance or creates rope interference.

## Readiness Label

This is an L2 V5 build-packet candidate. It is suitable for planning,
measurement capture, and future CAD/DXF drafting. It is not suitable for
cutting staves, ordering all materials, or releasing a shop packet without the
validation gates in `validation.csv`, `validation-loop.csv`, and
`v5-material-measurement-gates.md`.
