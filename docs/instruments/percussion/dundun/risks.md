# Risks

Status: L2 V5 build-packet candidate.

## Build-Readiness Risks

| Risk | Current State | Required Control |
| --- | --- | --- |
| Reference-only dimensions | Planning pages record useful dimensions, but the packet has not resolved OD, ID, wall thickness, or head-seat basis. | Measurement log plus regenerated CAD/DXF/design-table values. |
| Shell and membrane coupling | Pitch depends on hide mass, head tension, shell volume, and dual-head coupling. | Measured hide data, staged tuning log, and shell tap-tone records. |
| Rope tension and creep | Rope stretch can change pitch and head seating after first tuning. | Rope coupon and 24-hour/post-playing stretch log. |
| Ring roundness and safety | Poor ring welds or wrap thickness can distort heads or abrade rope. | Ring inspection, roundness check, and edge/finish review. |
| Bearing edge and finish | Finish or sharp edges can compromise hide seating and player contact. | Bearing-edge coupon and finish compatibility test. |
| Optional bell hardware | Side bell mount can interfere with rope path or instrument balance. | Mockup/photo check before drilling or mounting. |

## Provenance And Cultural Risks

The dundun family has living Mande cultural context. This repo can document
Tony's Morgan Drums stave-construction work and engineering process, but
public build instructions should keep cultural claims modest until reviewed
against named sources or community/context notes.

Required before L3/L4 promotion:

- Add source notes for terminology, ensemble roles, and regional variation.
- Avoid implying one fixed standard tuning for all dundun traditions.
- Separate Tony's construction method from traditional cultural authorship.

## Stop Conditions

Stop before build-ready release if the only dimension source is a scan/photo,
if Wolfram runtime is claimed without a real run log, or if CAD/DXF output has
no controlling measurement/design-table source.
