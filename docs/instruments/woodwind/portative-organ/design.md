<!-- SPDX-License-Identifier: CC-BY-4.0 -->
---
instrument: Portative Organ
slug: portative-organ
family: woodwind
class: portable flue-pipe aerophone
readiness: L2 V5 build-packet candidate
authority: concept_only / pending_measurement
---

# Portative Organ Design

## Concept

A portative organ is a small portable pipe organ. The player supports the instrument against the body or on the lap, works a bellows with one hand, and plays a short key row with the other. The design goal here is a portable study instrument that demonstrates the historical mechanism honestly before any shop-ready geometry exists.

## Mechanism

The wind path is:

```text
single-hand bellows -> wind reservoir -> windchest -> pallet valves -> flue pipes
```

The bellows is the player's pump. The reservoir smooths the pulses so the pipes receive steadier wind than the bellows alone would provide. The windchest is a sealed box under the pipes. Each key lifts or pulls a pallet valve inside the windchest; when the pallet opens, wind enters the foot of that pipe and the pipe speaks.

This packet assumes a direct mechanical key-to-pallet action for the first study. Linkage ratios, spring return, pallet travel, gasket material, and valve seating pressure are all pending measurement.

## Mechanism Analysis

The instrument is a chain of leaks and delays unless every interface is treated
as a review item. The bellows must move enough air for the intended pipe
behavior, but no pressure or flow target is released here. The reservoir must
smooth hand-pump pulses without becoming too sluggish. The windchest must stay
sealed when no keys are pressed, and each pallet must open cleanly enough that a
pipe can speak without a delayed or noisy onset.

The keyboard is therefore not just an ergonomic surface. Each key is a valve
control. Future design tables should track key travel, pallet lift, seal
material, return method, and windchest access as linked variables. In this L2
packet they remain named questions, not numeric claims.

## Pipes And Ranks

The sound source is a set of flue pipes. A flue pipe speaks when wind is directed through a narrow flue across a mouth toward a lip; the air jet alternates around the lip and excites the air column in the pipe. Mouth cut-up, languid position, flue opening, pipe material, pipe scale, and voicing all affect speech and tone.

Open and stopped pipes are both possible design branches. Open pipes use an open air column and tend to require more physical length for the same pitch family. Stopped pipes use a closed end and can reduce the package size, but they bring different tone color and voicing behavior. No pipe length or tuning value is specified in this L2 packet.

The first concept can support either one rank or a second contrasting rank later. A second rank would add weight, wind demand, and windchest complexity, so the first prototype should prove a single rank and leave a reserved path for expansion.

## Wind System Reasoning

The main design problem is wind stability. A hand bellows naturally produces pulses. The reservoir should buffer those pulses, while the pallets and pipe feet should avoid sudden pressure collapses when multiple keys are played. This packet does not assign wind pressure values; the target is qualitative until a wind mule is measured.

Questions for the mule:

- Does the reservoir keep a pipe speaking during a realistic bellows cadence?
- Does a quick key attack cause a useful speech onset without a choke or chirp?
- Do pallet seals stay quiet and leak-free enough for soft playing?
- Can the player coordinate pumping and keying without the instrument twisting?

## Engineering And Acoustic Reasoning

The acoustic side depends on stable wind and pipe voicing. A pipe that refuses
to speak may indicate a pipe-scale problem, a flue/mouth problem, a windchest
leak, a pallet-opening problem, or an unstable bellows cadence. For that reason,
the first tests should separate the wind mule from any final pipe rank.

The L2 review path should answer these in order:

- Can the bellows and reservoir produce steady enough wind for one test pipe?
- Does opening one pallet collapse the reservoir behavior or produce an
  unwanted attack transient?
- Does a second pallet opening reveal shared-channel limits?
- Can the player pump while pressing keys without twisting the case or changing
  pallet seal behavior?
- Does the chosen pipe branch, open or stopped, fit the portable form without
  inventing pipe lengths?

## Materials Reasoning

- Bellows material must flex repeatedly, seal reliably, and remain repairable.
- Reservoir material must resist leaks while allowing inspection and service.
- Pallet facing material must seal quietly without sticking.
- Windchest body material must hold flat sealing references.
- Pipe material remains open until pipe-scale research and voicing tests exist.
- Case material must balance weight, stiffness, and the need to protect pipes
  while the instrument is carried or supported.

## Failure Modes

- Bellows pulse is too strong for the reservoir to smooth.
- Reservoir response is so slow that pipe attack feels disconnected.
- Pallets leak, stick, slap, or require excessive touch weight.
- Windchest channels couple notes in a way that makes multiple-key behavior
  unstable.
- Pipe feet or mouths are damaged by the portable case layout.
- Player support mode twists the windchest or changes valve sealing.
- A future second rank doubles wind demand before a single-rank mule is proven.

## Tolerances As Questions

- How much reservoir fluctuation is audible on a single test pipe?
- How much pallet leakage can be tolerated before soft playing fails?
- How repeatable must key return be for quiet pallet reseating?
- How much case flex changes windchest sealing?
- What service opening is needed to inspect pallets and gaskets?

## Portable Form

The instrument should read as portable first: case, wind system, key row, and pipes must work as one carried object. The form factor can be strap-supported, lap-supported, or table-supported during early testing. Exact case dimensions, weight, strap geometry, center of gravity, and pipe protection are pending physical mockup.

## Parametric Intent

Future measured tables should separate:

- pipe family and end condition;
- pipe material and wall behavior;
- rank count and stop selection;
- windchest channel layout;
- pallet geometry and sealing material;
- key spacing, touch weight, and return force;
- reservoir volume behavior and bellows cadence;
- case support and handling constraints.

Every numeric field in those future tables should carry provenance: measured mule, reviewed drawing, CAD parameter, or explicit estimate pending measurement.

## V5 Boundary

This L2 packet is a review and prototype-planning scaffold. It is not a pipe-scale chart, tuning design, wind-pressure design, CAD source, DXF release, or fabrication authority.
