<!-- SPDX-License-Identifier: CC-BY-4.0 -->
# Risks — Tunable Snare Frame Array

## Safety Risks

| Risk | Severity | Probability | Mitigation |
|------|---------|------------|-----------|
| Sharp bearing edge cuts drum head or hand | High | Medium | File/grind 45° chamfer carefully; inspect with finger drag before assembly |
| Weld spatter burns during TIG | Medium | High | Full PPE — gloves, auto-darkening helmet, long sleeves |
| Plasma-cut edge burrs | Medium | High | Deburr all edges before handling; bench-grinder or file |
| Cylinder roll-out injury (blank feeds back) | High | Low | Feed blank slowly; keep hands clear of pinch zone |
| TIG arc flash to bystanders | High | Low | Post "welding in progress" warning; clear 3m radius |

## Ergonomic Risks

| Risk | Severity | Probability | Mitigation |
|------|---------|------------|-----------|
| Frame too wide for single player (550mm) | Medium | Low | Confirmed playable for players with 550mm+ arm span; ok for tabletop |
| Drum heights uneven when frame is angled | Low | Medium | Design for flat tabletop or stand-mount; add leveling feet if needed |
| Head too tight to tune without drum key | Low | Medium | Provide drum key in BOM; wing-nut tension rods as upgrade option |

## Manufacturability Risks

| Risk | Severity | Probability | Mitigation |
|------|---------|------------|-----------|
| Shell OD tolerance vs head counter-hoop fit | High | Medium | Standard drum heads spec ±0.5mm; roll shells to within ±0.5mm; Remo Ambassador is forgiving |
| Cylinder seam misalignment during roll | Medium | High | Tack-weld quickly after rolling; check alignment before full weld |
| Shell C (152mm) too small to roll cleanly | Medium | Medium | Run roll coupon first; watch for creasing near 6in OD; may need to anneal if using harder CRS |
| Frame cut-out diameter wrong (head won't drop in) | High | Low | Add 2mm clearance per side (cut-out = head OD + 4mm); verify on coupon before final plasma |
| Lug ear position mismatch after weld | Medium | Medium | Jig ears before tacking; use a simple 3D-printed or bent-wire locating jig |

## Acoustic Failure Modes

| Risk | Severity | Probability | Mitigation |
|------|---------|------------|-----------|
| Drum B (8in, A3) exceeds Remo head burst tension | High | Low | wolfram model predicts T_required = 2540 N/m vs ~3000 N/m burst; 15% margin; verify with first head |
| Real head σ differs from nominal 0.18 kg/m² | Medium | High | Tune by ear to target frequency; wolfram T values are starting points only |
| Snare wire buzz at low tensions | Low | High | Expected and desirable; adjust with thumb-wheel |
| Frame resonance couples between drums | Medium | Low | Add rubber grommets at shell-to-frame interface; test cross-talk with VAL-018/019 |
| Heads detune with temperature/humidity | Low | High | Normal drum behavior; player re-tunes before each session |

## Notes on Prototype Approach

This is an L0 blueprint — no prototype exists. All targets are model-derived. The highest-risk unknown is shell roll accuracy at 152mm OD (Shell C), because small-radius rolls on 1.0mm CRS are at the limit of typical Maker Nexus slip-roll capacity. Run the Shell C coupon first.
