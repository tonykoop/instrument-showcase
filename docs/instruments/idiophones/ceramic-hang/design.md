# Ceramic Hang Design

## Design Intent

Design a slip-cast ceramic, handpan-inspired tonal vessel that explores raised/isolated ceramic tone fields on a shallow resonant shell. The project is a research instrument first: the goal is to learn whether molded ceramic tone fields can produce musically useful fundamentals and partials after firing, and what clay body, wall thickness, tone-field geometry, and firing schedule make that repeatable.

The visual target is an approachable 18 inch handpan-like form, but the engineering target is more careful: a ceramic tonal vessel whose final design may diverge from steel handpans if the material asks for a different geometry.

## Governing Model

This instrument is governed by coupled plate/shell vibration plus Helmholtz body resonance.

```text
tone_field_f1 ~= (kappa / (2*pi)) * (h / a^2) * sqrt(E / (rho * (1 - nu^2)))
```

Where `h` is local tone-field thickness, `a` is effective field radius, `E` is Young's modulus, `rho` is density, `nu` is Poisson ratio, and `kappa` is an empirical boundary/shape coefficient. For ceramic this equation is a sanity check, not a final predictor.

```text
f_gu = c/(2*pi) * sqrt(A_gu / (V_shell * L_eff_gu))
L_eff_gu = wall + 0.6 * sqrt(A_gu/pi)
```

The gu/port resonance should be measured as a coupled body mode. It may support warmth and sustain, but it will not tune the tone fields the way hammered steel tuning does.

## Design Targets

| Parameter | Target | Status |
| --- | ---: | --- |
| Outer diameter | 18 in | design target |
| Overall height | 4.5 in | design target |
| Fired wall thickness | 0.22-0.30 in | experiment range |
| Clay shrinkage | 12 percent | assumption until measured |
| Shell volume | 600-850 in3 | derived estimate |
| Gu diameter | 3.5 in | first prototype |
| Clay body | Cone 6 stoneware or porcelain casting slip | TBD |
| Finish | Exterior-only glaze or burnished/oxide surface | TBD |
| Primary key | G minor 9-note layout | assumption |

## Target Note Layout

| Field | Note | Target Hz | Function | First geometry assumption |
| --- | --- | ---: | --- | --- |
| Ding | G3 | 196.00 | center fundamental | 4.0 in raised oval/circle |
| T1 | Bb3 | 233.08 | low outer field | 3.4 in oval |
| T2 | C4 | 261.63 | outer field | 3.2 in oval |
| T3 | D4 | 293.66 | outer field | 3.0 in oval |
| T4 | F4 | 349.23 | outer field | 2.75 in oval |
| T5 | G4 | 392.00 | outer field | 2.55 in oval |
| T6 | Bb4 | 466.16 | outer field | 2.35 in oval |
| T7 | C5 | 523.25 | outer field | 2.20 in oval |
| T8 | D5 | 587.33 | outer field | 2.05 in oval |

The note layout is intentionally marked as an assumption. Ceramic fields may prefer fewer larger notes, different intervals, or a tongue/slit hybrid if isolated plate fields do not ring cleanly.

## Manufacturing Strategy

Use a slip-cast two-shell body:

1. CAD an upper dome with raised tone-field islands and a lower shell with gu port.
2. 3D print master positives oversized by measured clay shrinkage.
3. Make plaster molds with clean registration and no trapped undercuts.
4. Slip cast upper and lower shells separately.
5. Join at leather-hard stage with a reinforced rim/luting band.
6. Bisque fire before any glaze commitment.
7. Measure tone fields, body modes, gu resonance, cracks, and distortion.
8. Iterate field thickness, island geometry, and clay body before decorative finishing.

## Prototype Ladder

| Prototype | Goal | Success criteria |
| --- | --- | --- |
| CHG-P0 tone coupon | Test isolated ceramic field shapes | At least one coupon rings with a clear decay and measurable pitch |
| CHG-P1 mini dome | Test 3 tone fields on a small shell | No cracks; pitch trend follows field size/thickness |
| CHG-P2 18 in blank | Test full shell casting, gu, seam, and body mode | Shell survives drying/bisque and gu resonance is measurable |
| CHG-P3 5-note vessel | First musical layout | Five fields within +/-75 cents after bisque or clear correction path |
| CHG-P4 9-note G minor | Full concept | Playable hand pattern, stable fields, acceptable sustain |

## Empirical Questions

- What clay body gives the longest decay without excessive fragility?
- Do raised tone fields, thinned tone fields, or cut/relief-bounded fields speak best?
- Does glaze damp the fields too much?
- Can tone fields be tuned at greenware/leather-hard stage accurately enough to survive firing?
- Is a 9-note layout realistic in ceramic, or should the first product be 5-7 notes?
- Should the final instrument become a ceramic tongue-handpan hybrid instead of a pure tone-field shell?

## Assumptions And Unknowns

- Elastic properties are derived estimates until test bars are fired and measured.
- No empirical ceramic handpan correction data exists yet in this repo.
- The screenshot reference is visual inspiration only; no supplier dimensions or pricing are used as source data.
- Final tuning may require new mold masters rather than post-fire correction.
- Structural safety matters: the instrument must survive hand strikes, thermal gradients, and transport.

