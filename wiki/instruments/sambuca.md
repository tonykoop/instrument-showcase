---
title: Sambuca Boat-Shaped Arched Harp
slug: sambuca
wiki_type: instrument
status: active
sources:
  - path: ../../../sambuca/README.md
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../sambuca/reverse-engineering.md
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../sambuca/design.md
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../sambuca/assembly-manual.md
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../sambuca/risks.md
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../sambuca/family-spec.csv
    kind: spreadsheet
    last_seen: 2026-05-18
  - path: ../../../sambuca/validation.csv
    kind: spreadsheet
    last_seen: 2026-05-18
  - path: ../../../sambuca/bom.csv
    kind: spreadsheet
    last_seen: 2026-05-18
  - path: ../../../sambuca/cut-list.csv
    kind: spreadsheet
    last_seen: 2026-05-18
  - path: ../../../sambuca/cad/SAM-000_master-equations.txt
    kind: cad
    last_seen: 2026-05-18
  - path: ../../../sambuca/cad/README.md
    kind: cad
    last_seen: 2026-05-18
  - path: ../../../sambuca/cad/SW-MIGRATION-CHECKLIST.md
    kind: cad
    last_seen: 2026-05-18
  - path: ../../../sambuca/cnc/cnc-plan.md
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../sambuca/wolfram/sambuca-acoustics-starter.wl
    kind: wolfram
    last_seen: 2026-05-18
  - path: ../../../sambuca/capstone-manifest.json
    kind: repo
    last_seen: 2026-05-18
crosslinks:
  - acoustic-classes/arched-harp
  - acoustic-classes/harp-lute
  - synthesis/public-release-blockers
  - synthesis/cad-readiness-roadmap
  - synthesis/wolfram-model-patterns
open_questions:
  - "Reconcile SAM-13 body depth and cavity volume: README/design/master equations/family spec use 200 mm depth, while validation/print packet/cut list/Wolfram/capstone artifacts still carry 150 mm or 3.8 L assumptions."
  - "Resolve tuner architecture: current README/equations prefer 6 mm zither pegs, while assembly/BOM/sourcing/drawing/capstone docs still specify hidden geared tuners, PVD gold bulb caps, cord wraps, and 12 mm tuner holes."
  - "Reconcile family pitch ranges and f_max values: some tables say SAM-19 D3-G5 and SAM-25 A2-A5, while CSV/Wolfram values appear one octave higher."
  - "Confirm whether the public-release gate list is the three headline gates or the fuller validation.csv gate set including calibrated ROOT tension, imagery attribution, and etymology review."
  - "Confirm whether the capstone slide claim of MULE acoustic validation is future placeholder text or measured evidence."
  - "Get cultural/musicology advisor review of provenance language before public release."
  - "Request or locate original Woolley field-sketch dimensions if BM 121198 body depth and strip position need tighter anchors."
  - "Run SAM-13-MULE string-holder strip voicing and 30-day neck-deflection hold before treating ROOT geometry as build-validated."
  - "Complete SolidWorks MasterLayout rebuild and regenerate drawings/exported dimensions before CAD becomes authoritative."
answers_filed: []
last_ingest: 2026-05-18
last_lint: 2026-05-18
review_due: 2026-08-18
tags:
  - instrument
  - string
  - arched-harp
  - private-review
---

# Sambuca Boat-Shaped Arched Harp

## Overview

The `sambuca` repo is a private-review v4 build packet for a modern boat-shaped arched harp inspired by British Museum object 121198 from the Royal Cemetery at Ur, c. 2600 BC. The project deliberately treats the original wood form as interpretive: the packet preserves a visual fingerprint from the Ur reconstruction and related references, while modernizing the acoustic geometry, materials, tuning hardware, CNC workflow, validation process, and family scaling.

Primary repo links:

- [README](../../../../strings/sambuca/README.md)
- [Reverse-engineering analysis](../../../../strings/sambuca/reverse-engineering.md)
- [Design notes](../../../../strings/sambuca/design.md)
- [Assembly manual](../../../../strings/sambuca/assembly-manual.md)
- [Risks](../../../../strings/sambuca/risks.md)
- [Capstone manifest](../../../../strings/sambuca/capstone-manifest.json)
- [Print packet](../../../../strings/sambuca/print-packet.md)
- [Build-log site](../../../../strings/sambuca/site/index.html)

## Current Status

- Release state: private review.
- Packet state: `instrument-maker-v4`, generated 2026-05-16.
- Build target: `SAM-13-ROOT`, 13 strings, G-major G3 to E5, 650 mm body length.
- Family: five variants from one MasterLayout concept: `SAM-13-ROOT`, `SAM-19-MID`, `SAM-25-CONCERT`, `SAM-13-AE`, and `SAM-13-MULE`.
- Acoustic class: [[acoustic-classes/arched-harp]], with a boat-shaped resonator, curved cantilever neck, and string-holder strip rather than a separate raised bridge.
- CAD state: Pack-and-Go SolidWorks files exist, but the CAD notes say the internal geometry is still kora-shaped and must be rebuilt from the equations.
- Drawing state: SVG drawings are placeholders until the SolidWorks rebuild clears.
- Validation state: `validation.csv` defines dimensional, tension, structural, acoustic, ergonomic, cultural, and brand checks; no measured validation data was found in the text-native sources.
- Release blockers: at minimum, cultural/musicology review, SAM-13-MULE neck-deflection validation, and Heifer Zephyr brand placement. The detailed validation table marks additional gate-blocking checks.

## Source Notes

The first ingest used text-native sources and linked generated/binary artifacts without deep extraction:

- [repo] [README](../../../../strings/sambuca/README.md) establishes the packet map, private-review status, BM 121198 framing, family variants, headline release gates, dual-license structure, and current high-level design choices.
- [repo] [Reverse-engineering analysis](../../../../strings/sambuca/reverse-engineering.md) locks the taxonomy as boat-shaped arched harp rather than lyre, captures BM card dimensions, distinguishes observed facts from inferred facts, and names remaining measurement needs.
- [repo] [Design notes](../../../../strings/sambuca/design.md) define the design intent, family scaling, keel soundhole strategy, string-holder strip logic, structural joint options, playing position, materials, inlay program, acoustic model, tension calibration plan, and public-release gates.
- [repo] [Assembly manual](../../../../strings/sambuca/assembly-manual.md) gives the 12-stage build sequence, with key hold points before production stock cutting, neck/body joining, MULE voicing, MULE 30-day hold, ROOT stringing, and final documentation.
- [repo] [Risks](../../../../strings/sambuca/risks.md) tracks structural, acoustic, ergonomic, supply, fit/finish, safety, and cultural risks with verification tests.
- [spreadsheet] [Family spec](../../../../strings/sambuca/family-spec.csv) defines five variants and makes `SAM-13-MULE` the reduced-tension validation precursor.
- [spreadsheet] [Validation table](../../../../strings/sambuca/validation.csv) defines the release checks and acceptance criteria, including neck deflection, total tension, soundboard pull-test, acoustic response, provenance review, imagery attribution, and brand placement.
- [spreadsheet] [BOM](../../../../strings/sambuca/bom.csv) and [sourcing](../../../../strings/sambuca/sourcing.csv) capture the walnut/cedar/sapele build slate, string sets, inlay supplies, stand, harness hardware, tooling, jigs, and planning-cost caveats.
- [spreadsheet] [Cut list](../../../../strings/sambuca/cut-list.csv) provides CNC-from-block and stave-laminated hull paths, neck laminates, soundboard, string-holder strip, inlay pockets, stand parts, and reusable fixtures.
- [cad] [Master equations](../../../../strings/sambuca/cad/SAM-000_master-equations.txt) are described as the numeric source of truth for SolidWorks, including 200 mm root body depth, 6 mm zither peg holes, keel port, inlay, and strip dimensions.
- [cad] [CAD README](../../../../strings/sambuca/cad/README.md) and [SW migration checklist](../../../../strings/sambuca/cad/SW-MIGRATION-CHECKLIST.md) warn that the Pack-and-Go files still contain inherited kora geometry and recommend rebuilding a clean sambuca MasterLayout.
- [repo] [CNC plan](../../../../strings/sambuca/cnc/cnc-plan.md) is a pre-CAM operation graph, not G-code; it defines datums, tooling, workholding, and operation-level release checks.
- [wolfram] [Wolfram starter](../../../../strings/sambuca/wolfram/sambuca-acoustics-starter.wl) models hull volume, axial/Helmholtz modes, string tension, soundboard plate mode, coupled cavity-plate response, and family voiced range.
- [repo] [Capstone manifest](../../../../strings/sambuca/capstone-manifest.json) inventories artifacts, records Fall 2026 as the capstone window, and states the dual-license split.

Linked artifacts not distilled in this pass:

- [Capstone deck markdown](../../../../strings/sambuca/capstone-deck.md)
- [Capstone deck PPTX](../../../../strings/sambuca/capstone-deck.pptx)
- [Print packet PDF](../../../../strings/sambuca/print-packet.pdf)
- [Explorer](../../../../strings/sambuca/explorer.html)
- [Generated explorer](../../../../strings/sambuca/explorer.generated.html)
- [Drawings folder](../../../../strings/sambuca/drawings/)
- [CAD folder](../../../../strings/sambuca/cad/)
- [Harness notes](../../../../strings/sambuca/harness/README.md)
- [Learn-to-play folder](../../../../strings/sambuca/learn-to-play/)

## Design Knowledge

The reverse-engineering packet treats BM 121198 as a boat-shaped arched harp, not a lyre. The useful design distinction is topology: a single curved cantilever neck rises from a boat-shaped resonator, and strings fan from the neck to a soundboard string-holder strip. There is no lyre yoke and no separate raised bridge bar.

Current intended SAM-13-ROOT anchors from the README, family spec, and master equations:

- Body length: 650 mm.
- Body width: 150 mm.
- Body depth: 200 mm in the current high-level intent and equations, but older packet surfaces still say 150 mm.
- Instrument height: 810 mm.
- Strings: 13.
- Tuning: G-major, G3 to E5.
- Speaking lengths: about 200 to 580 mm.
- Target total tension: 65 to 80 kgf on ROOT; 40 to 50 kgf or 3.0 to 4.5 kgf/string on MULE depending on source surface.
- Soundhole: single oval keel port, 80 x 50 mm, tilted forward about 15 degrees.
- String termination: glued-on string-holder strip near the bow end, mounted reversibly for MULE voicing before the ROOT position is committed.

The packet frames the visual fingerprint as a set of preserved cues:

- Boat hull with pronounced bow lift.
- Strong J-curve neck.
- Lapis-look multi-strip band along the soundboard/hull seam.
- Rectangular pale bow-end soundboard inlay panel.
- Gold/brass-tone neck-body collar.
- Tuning-peg row along the neck.
- Integral stern stub feet.
- Ornament at the top of the neck, currently proposed as a slip-cast finial in newer notes.

Materials and construction currently target:

- Walnut hull and stand.
- Western red cedar soundboard around 3 mm, with 2.5 to 4.0 mm sweep in the acoustic study.
- Sapele laminated curved neck.
- Walnut or hard maple string-holder strip.
- Brass or bronze neck-body collar.
- Lapis-look dyed veneer plus light spacers for the multi-strip band.
- Fluorocarbon trebles plus wound nylon basses to bring total tension into the target band.

## Acoustic And Structural Model

The core string model is the standard vibrating-string relationship:

```text
f = (1 / 2L) * sqrt(T / mu)
```

The acoustic study then layers hull air modes, keel-port Helmholtz behavior, soundboard plate modes, and a two-coupled-oscillator approximation for cavity plus plate. The intended voicing target is for the coupled cavity/plate pair to support the lower string range rather than leaving the small body quiet in the bass register.

The structural risk center is the neck-to-body joint. The risk register estimates 50 to 65 kgf horizontal pull at a long cantilever arm for the 13-string build and treats the scarf/collar joint as the highest-risk failure point. The design and assembly docs converge on a glued scarf joint reinforced by a brass collar and hidden mechanical pin, with MULE testing before full ROOT tension.

The keel port is intentionally modern. It moves sound radiation forward/downward toward the listener instead of cutting a decorative soundboard rose that would project into the player in the seated-between-thighs posture.

## Build And Validation Logic

The assembly plan is staged around hold points:

1. Review design, risks, master equations, source stock, and fixtures.
2. Mock-fit tuner hardware before cutting production neck stock.
3. Build the hull by CNC-from-block or stave-laminated path.
4. Laminate and CNC-sweep the curved sapele neck.
5. Cut and brace the cedar soundboard, then route inlay pockets.
6. Dry-fit, glue, pin, and inspect the scarf/collar neck-body joint.
7. Glue in the soundboard and inlays.
8. Cut the keel port and make the stand.
9. Install tuners or pegs after the hardware decision is reconciled.
10. Use `SAM-13-MULE` to find the string-holder strip position and run the 30-day neck-deflection hold.
11. Bring `SAM-13-ROOT` to calibrated tension gradually only after MULE passes.
12. Measure acoustic response, Helmholtz behavior, tuning drift, ergonomics, and update documentation.

Important validation rows:

- `V-S-01`: MULE neck deflection at 30-day hold, pass <= 2 mm at the top cap.
- `V-T-02`: ROOT calibrated tension, pass 65 to 80 kgf total.
- `V-S-04`: string-holder strip pull-test on scrap, pass at least 2x service load.
- `V-A-04`: keel-port Helmholtz frequency target around 143 +/- 15 Hz.
- `V-A-05`: string-holder strip position locked after MULE voicing.
- `V-C-01`, `V-C-02`, `V-C-03`: provenance language, imagery attribution, and sambyke etymology review.
- `V-B-01`: Heifer Zephyr brand placement locked.

## Release And Provenance Constraints

This page should use the same cautious language as the repo: `inspired by`, `boat-shaped arched harp`, `Sumerian pattern`, and `modern reinterpretation`.

Avoid claiming:

- reproduction of BM 121198
- recreation of a specific original artifact
- authority over a modern living tradition
- evidence for how the original sounded
- validated acoustic performance
- completed CAD
- completed cultural review

The repo's provenance language argues that the surviving original material is gold tuning pegs and lapis lazuli decoration, while the wooden form is a 1971-72 reconstruction based on seals and excavation sketches. Even with that framing, public release still needs external cultural/musicology review and image-credit audit.

The packet is dual-licensed:

- Design files: CERN-OHL-W-2.0.
- Written content and media: CC-BY-4.0.

## Cross-Links

- [[acoustic-classes/arched-harp]]
- [[acoustic-classes/harp-lute]]
- [[fabrication/cnc-routing]]
- [[fabrication/jigs-and-fixtures]]
- [[fabrication/bridge-and-string-layout]]
- [[materials/cedar]]
- [[materials/walnut]]
- [[materials/sapele]]
- [[synthesis/public-release-blockers]]
- [[synthesis/cad-readiness-roadmap]]
- [[synthesis/wolfram-model-patterns]]

## Open Questions

1. Which SAM-13 body depth is authoritative for public design docs: 200 mm from README/design/master equations/family spec, or 150 mm from validation/print packet/cut list/Wolfram/capstone surfaces?
2. Should the acoustic model be recalculated around the 200 mm depth and about 10.2 L cavity before any claim about Helmholtz frequency, coupled modes, or quiet-instrument mitigation is repeated?
3. Are SAM-13 tuners now zither pegs with 6 mm angled holes, or hidden geared tuners with decorative gold caps, cord wraps, and 12 mm mounting holes?
4. Is the slip-cast finial now locked, or do older gold-cap finial notes still apply to the BM-fingerprint version?
5. Are SAM-19 and SAM-25 `f_max_hz` values in `family-spec.csv` and Wolfram one octave high relative to their stated note names?
6. Does the MULE total-tension target mean 40 to 50 kgf total, 50 kgf total, or 3.0 to 4.5 kgf/string?
7. Which gate list should be treated as release-blocking for the library card: the three headline gates, or all `gate_block: yes` rows in `validation.csv`?
8. Who will perform the cultural/musicology review, and where should written sign-off be stored?
9. Should BM 121198 body depth be confirmed by curator request or Woolley field sketches before CAD rebuild?
10. Should `SAM-13-AE` include a stern eyebolt only for strap/pickup service access, or is that row inherited from larger harness variants?

## Maintenance Notes

Next ingest should reconcile the post-2026-05-16 design updates across README, design notes, master equations, validation, print packet, cut list, Wolfram, and capstone deck. The highest-value cleanup is a single authoritative SAM-13 geometry/tuner table that downstream CAD, CNC, sourcing, drawings, and acoustic models all consume.

When measured data exists, update this page, [[acoustic-classes/arched-harp]], and [[synthesis/public-release-blockers]] with the MULE neck-deflection result, ROOT total tension, acoustic response, and cultural review outcome.
