<!-- SPDX-License-Identifier: CC-BY-4.0 -->
---
instrument: Carillon
slug: carillon
family: idiophone
class: struck tuned bronze bell instrument
readiness: L2 V5 build-packet candidate
authority: concept_only / pending_measurement
---

# Carillon Design

## Concept

A carillon is a keyboard-played set of tuned bells. The player strikes batons with the hands and pedals with the feet; the keyboard motion travels through a mechanical transmission to clappers positioned at the bells. The clappers strike the bells while the bells themselves remain fixed in the tower or frame.

This packet captures the mechanism and L2 review questions only. It does not specify bell sizes, bell profiles, bell weights, casting alloy, partial frequencies, keyboard dimensions, transmission lengths, clapper masses, or tower loads.

## Bell System

The sound source is a set of cast bronze bells, each shaped and tuned so its partials form an intentional musical relationship. Carillon bells are not simple bars or plates; their profiles, wall thickness distribution, crown, waist, sound bow, and lip all influence partials and decay. Final tuning is specialist work after casting and measurement.

This L2 packet treats bell design as a future expert-reviewed authority chain. No bell profile, pitch list, partial target, or bronze specification is asserted here.

## Keyboard And Transmission

The player interface is a baton-and-pedal keyboard. Batons are moved by hand, pedals by foot, and both act through mechanical linkages. A transmission may include wires, trackers, roller boards, guides, return springs, adjusters, and lost-motion compensation. The action should let the player shape dynamics by controlling clapper velocity rather than simply triggering an on/off strike.

Conceptual transmission questions:

- How does baton travel translate into clapper travel?
- Where is adjustability needed to remove slack without holding clappers against bells?
- How are long wire runs guided so they do not bind or rattle?
- How do pedals couple to the largest bells without excessive force?
- What inspection points are needed for maintenance?

## Clapper Mechanics

Each external clapper should strike the bell at a controlled location with repeatable clearance and return. The clapper must not rest against the bell after the strike, and the linkage must allow dynamic control. Clapper material, mass, pivot, spring return, stop position, and adjustment hardware are all pending design and measurement.

The first mule should test motion quality and reset behavior without claiming any musical bell data.

## L2 Action-Mule Plan

| subsystem | L2 candidate direction | authority | promotion evidence needed |
| --- | --- | --- | --- |
| Baton interface | Use a non-sounding baton action mule to study travel feel and rebound. | pending_measurement | Measured travel, return behavior, lost motion, and player-control notes from a mule. |
| Pedal interface | Treat pedal coupling as a separate force/leverage study for larger bells. | pending_measurement | Ergonomic and mechanical review before any load-bearing or bell-specific linkage claim. |
| Transmission routing | Keep wires, trackers, guides, roller boards, and adjusters as layout placeholders. | pending_measurement | Reviewed routing diagram, service access plan, and slack-adjustment method. |
| Clapper assembly | Model clapper control conceptually only; do not assign mass, pivot, strike point, or clearance. | pending_measurement | Expert review plus measured or reviewed clapper geometry for a selected bell. |
| Bell register | Hold bell profiles, partial targets, pitch lists, weights, and foundry specifications outside this packet. | pending_measurement | Foundry or expert-reviewed bell data before any tuning table or casting package. |
| Tower/frame | Treat support structure as an engineering gate, not an instrument-maker estimate. | pending_measurement | Structural review, lifting/service plan, weather exposure plan, and safety gates. |

## Tower And Frame

A full carillon belongs in a tower or engineered frame. The support system must handle bell mass, dynamic strike loads, weather exposure, service access, and safe maintenance routes. This packet makes no structural claim. Tower engineering and lifting plans are out of scope for this L2 candidate.

## Parametric Intent

Future design tables should separate:

- bell identity, casting source, and measured tuning records;
- keyboard batons, pedals, and ergonomic travel;
- transmission path, adjusters, guides, and return components;
- clapper mass, pivot, strike point, clearance, and rebound behavior;
- frame or tower interface, inspection access, and safety gates;
- measured response, decay, tuning, and action feel.

Every numeric field in those future tables should carry provenance: measured bell, foundry record, reviewed drawing, CAD parameter, structural engineering note, or `estimate_pending_measurement`.

## L2 Review Checklist

- Choose the smallest non-sounding action mule that can test baton return, pedal coupling, lost motion, and adjustability without bell data.
- Define what observations belong in a future validation log before claiming action quality.
- Identify which specialist must review bell profiles, partial tuning, foundry data, and tower/frame loads.
- Create CAD only after the action mule or specialist reference supplies controlling inputs.
- Keep every current physical value at `concept_only` or `pending_measurement`.

## V5 Boundary

This is an L2 V5 build-packet candidate. It is not a bell profile design, casting package, tuning plan, tower structure, CAD source, DXF release, or fabrication package.
