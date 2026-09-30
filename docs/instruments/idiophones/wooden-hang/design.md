# Wooden Hang Design

## Design Intent

Design a handpan-inspired wooden idiophone / resonant-vessel hybrid that can be played in a circular lap layout while staying honest about wood behavior. The goal is not to reproduce the PANArt Hang or steel-handpan partial structure. The goal is to discover whether a wooden shell, bowl, or plate system can support musically useful note zones, playable sustain, and enough ergonomic clarity to justify a new instrument family.

The first serious build path is a **top-plate hybrid**: a tuned wooden top plate with isolated note zones over a resonant bowl or cavity. This keeps the handpan-like surface and hand reach while giving the shop more controllable tuning variables than a fully carved monolithic dome.

## Governing Model

Wooden Hang is treated as a coupled plate-and-cavity instrument with possible tongue-like local behavior in the note zones.

First-order plate trend for a locally isolated field:

```text
f_field ~= (kappa / (2*pi)) * (h_local / a_eff^2) * sqrt(E_eff / (rho_eff * (1 - nu^2)))
```

Where:

- `h_local` = local field thickness
- `a_eff` = effective note-field radius or half-axis proxy
- `E_eff` = effective modulus for the chosen species or laminate schedule
- `rho_eff` = effective density
- `nu` = Poisson ratio
- `kappa` = empirical boundary coefficient for the isolation geometry

This is a **derived estimate**, not a final predictor. Wood anisotropy, grain direction, glue lines, bowl coupling, and local slot geometry will move the real pitch.

First-order cavity / gu trend:

```text
f_port = c / (2*pi) * sqrt(A_port / (V_cavity * L_eff))
L_eff ~= t_port + 0.6 * sqrt(A_port / pi)
```

The port is expected to affect warmth, bloom, and low-body response more than exact note tuning. It is included as a controllable resonance variable, not as proof that a handpan-like sound will emerge.

## Design Targets

| Parameter | Target | Status |
| --- | ---: | --- |
| Outer diameter | 18.0 in | design target |
| Playing surface diameter | 15.8 in | derived estimate |
| Overall height | 4.75 in | design target |
| Top-plate thickness | 0.200-0.320 in | experiment range |
| Bowl wall thickness | 0.375-0.500 in | design target |
| Bowl internal depth | 2.25-2.75 in | derived estimate |
| Gu diameter | 2.75-3.50 in | experiment range |
| Rim width | 0.85 in | derived estimate |
| Primary species | hard maple, walnut, or birch laminate | assumption |
| Assembly style | removable or replaceable top during early prototypes | recommended |
| Primary key | G minor 9-note layout | assumption |

## Target Note Layout

| Field | Note | Target Hz | Function | First geometry assumption |
| --- | --- | ---: | --- | --- |
| Ding | G3 | 196.00 | center anchor | 3.90 in major axis, shallow dome or oval field |
| T1 | Bb3 | 233.08 | low outer field | 3.30 in major axis |
| T2 | C4 | 261.63 | outer field | 3.10 in major axis |
| T3 | D4 | 293.66 | outer field | 2.90 in major axis |
| T4 | F4 | 349.23 | outer field | 2.65 in major axis |
| T5 | G4 | 392.00 | outer field | 2.45 in major axis |
| T6 | Bb4 | 466.16 | upper outer field | 2.25 in major axis |
| T7 | C5 | 523.25 | upper outer field | 2.10 in major axis |
| T8 | D5 | 587.33 | upper outer field | 1.95 in major axis |

All note geometries above are **assumption** values sized to create a starting test map. They are not claimed as finished dimensions.

## Construction Branches

### Branch A - Primary: Top-Plate Hybrid

- Thin hardwood or laminated hardwood top plate.
- Note zones formed by underside thinning plus optional relief slots or perimeter scallops.
- Bowl or shell underneath provides air volume and physical support.
- Early prototypes should keep the top replaceable so note geometry can change without rebuilding the whole vessel.

Why this branch leads:

- easiest coupon-to-sector scaling path
- best access to underside tuning cuts
- removable plate lowers rework cost
- allows A/B testing of species, slot geometry, and cavity volume

### Branch B - Secondary: Split-Shell CNC Carved Body

- Laminated blank machined in four operations:
  1. upper inside
  2. lower inside
  3. upper outside
  4. lower outside
- Upper half carries the playing field.
- Lower half carries cavity volume and port.

Benefits:

- clean datum control
- visually closest to a seamless wooden handpan-like shell

Costs:

- more machining time
- harder rework loop
- note-zone behavior still uncertain before committing full shell machining

### Branch C - Secondary: Segmented / Stave Shell

- Stave or ring-built shell with a machined or laminated top.
- Wood-friendly shell construction and repair path.
- Likely strongest if the instrument eventually becomes a wooden resonance vessel with a tuned top rather than a true carved dome.

Costs:

- more glue-line variables
- less visually seamless
- join behavior may influence note uniformity

## Prototype Ladder

| Prototype | Goal | Success criteria |
| --- | --- | --- |
| WHG-P0 coupon set | Test species, thickness, slotting, and finish damping | At least one coupon yields repeatable measurable pitch and useful decay |
| WHG-P1 single field over cavity | Test one ding-like field on a small bowl | Pitch trend follows geometry changes and cavity coupling is audible/measurable |
| WHG-P2 three-note sector | Test realistic hand spacing and interaction | Three notes can coexist without catastrophic cross-talk |
| WHG-P3 five-note subset | First playable subset | Five notes within usable range and ergonomic reach feels promising |
| WHG-P4 full nine-note layout | Full concept evaluation | Layout is playable, structurally stable, and measurement loop suggests a correction path |

## Material Strategy

- Start with stable close-grained species: hard maple, birch plywood/baltic birch laminate, or walnut.
- Avoid very oily species or dramatic open grain in the first acoustic test phase.
- Track moisture content at every measurement session.
- If solid wood proves too anisotropic, pivot to cross-laminated or veneer-laminated top plates.
- Keep finish minimal during acoustic tests: shellac wash, oil-free sealer, or no finish on strike zones.

## Manufacturing Strategy

1. Build coupons from at least two wood systems:
   - solid hardwood along grain
   - laminated or plywood top stock
2. Measure free coupon ring and supported-over-cavity behavior separately.
3. Build a removable-top single-field rig before a full body.
4. Escalate to a 3-note sector with the same datum system planned for the full layout.
5. Only after the sector behaves acceptably should the build commit to a full 9-note layout body.

## Empirical Questions

- Can a wooden top zone ring with enough clarity under hand strike without sounding like a muted tongue drum?
- Does grain direction make note behavior too orientation-sensitive for a circular layout?
- Is the most promising note geometry closer to:
  - isolated plate field
  - slit tongue
  - undercut island
  - hybrid of all three
- What cavity depth and port size support bloom without muddying note attack?
- Does a removable top produce enough structural honesty to justify the rework advantage?
- Should the eventual family be a wooden handpan-like vessel, or a wooden top-plate tonal vessel with its own visual language?

## Assumptions And Unknowns

- The 9-note G minor map is a concept target, not a proven first playable layout.
- The top-plate hybrid is the recommended first prototype because it reduces variables, not because it is already acoustically validated.
- Plate formulas are used as sanity-check tools only.
- No local empirical correction table exists yet for this wooden family.
- The final successful instrument may end up with fewer notes, larger note zones, or a stronger tongue-field identity than the current concept image suggests.
