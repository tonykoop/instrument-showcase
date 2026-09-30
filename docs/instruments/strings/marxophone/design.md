<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Marxophone L2 Design Study

## Concept

The instrument is a Marxophone-inspired fretless zither with spring-mounted
metal hammer arms. Pressing a key or lever brings an arm into contact with a
string course. The spring and arm geometry let the hammer rebound repeatedly,
creating a tremolo-like series of attacks while the player controls onset,
pressure, and duration.

## Mechanism

The main sound source is the string course and soundboard. The hammer system is
an exciter, not a fretting system: it should strike or brush the string without
defining a stopped speaking length. Useful design work therefore lives in the
interaction among string tension, hammer tip material, arm stiffness, spring
return, key feel, bridge coupling, and soundboard response.

The packet does not assert any exact scale length, string gauge, course count,
pitch map, spring rate, hammer mass, key travel, DXF coordinate, or acoustic
target. Those values need bench tests before they can become build authority.

## L2 Subsystem Plan

| subsystem | L2 candidate direction | authority | promotion evidence needed |
| --- | --- | --- | --- |
| String bed | Treat the instrument as a fretless zither-family string bed until measured string response exists. | pending_measurement | String material, course layout, bridge coupling, and tuning policy selected from tests or references. |
| Hammer action | Use replaceable spring-hammer action coupons before full action layout. | pending_measurement | Rebound consistency, noise, wear, and controllability logs from coupon trials. |
| Player interface | Keep keys, tabs, and levers open as interface options. | concept_only | Ergonomic trial notes and selected actuation strategy. |
| Resonator body | Keep soundboard/body construction open until string and hammer load behavior are tested. | pending_measurement | Soundboard coupon response, bridge load review, and body bracing plan. |
| Damping/noise control | Treat damping as an optional branch for controlling mechanism noise. | concept_only | Decision whether damping is needed after hammer-action tests. |
| Documentation | Record every future CAD, DXF, measurement, or render artifact in the authority register. | concept_only | Reviewed source rows and provenance for any promoted artifact. |

## Parametric Intent

Future measured design tables should vary:

- String material family and course layout.
- Soundboard and bridge construction.
- Hammer arm material, stiffness, and pivot strategy.
- Hammer tip material and contact shape.
- Spring return style and adjustment method.
- Key or lever ergonomics.
- Tremolo controllability across soft, medium, and strong attacks.
- Noise separation between useful tremolo and unwanted mechanism rattle.

## Measurement Plan

1. Build a one-course action coupon with interchangeable string, bridge, hammer
   tip, and spring samples.
2. Record dry string response before adding a hammer action.
3. Compare hammer rebound consistency, attack density, decay, rattle, and
   player control across spring and tip options.
4. Add a small multi-course test only after the one-course coupon identifies a
   stable action envelope.
5. Promote only measured and reviewed data into future tuning, CAD, DXF, or
   fabrication authority.

## L2 Review Checklist

- Choose the smallest action coupon that can test hammer tip material, spring
  return, pivot behavior, and player feel without a full instrument layout.
- Separate string-bed tests from hammer-action tests so tuning and tremolo
  behavior are not conflated.
- Decide whether the first interface study uses keys, tabs, levers, or a
  neutral actuator.
- Define the evidence log needed for rebound consistency, action noise, string
  wear, and subjective control before any CAD promotion.
- Keep all current rows at `concept_only` or `pending_measurement` until
  measured templates or reviewed CAD exist.

## Authority Boundary

This file is concept and pending-measurement authority only. It is suitable for
planning experiments and discussing mechanism tradeoffs. It is not suitable for
cutting, drilling, tuning, ordering final strings, specifying springs, or
machining action parts without measurement and review.
