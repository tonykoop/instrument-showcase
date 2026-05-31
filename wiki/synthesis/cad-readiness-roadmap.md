---
title: CAD Readiness Roadmap
slug: cad-readiness-roadmap
wiki_type: synthesis
status: active
sources:
  - path: ../../scripts/generate_library.py
    kind: repo
    last_seen: 2026-05-18
  - path: ../../data/library-manifest.json
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../cajon/capstone-manifest.json
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../cajon/visual-output-register.csv
    kind: repo
    last_seen: 2026-05-18
  - path: ../../../cajon/cad/README.md
    kind: cad
    last_seen: 2026-05-18
  - path: ../../../kora/cad/kora-parametric-brief.md
    kind: cad
    last_seen: 2026-05-18
  - path: ../../../wood-shell-tongue-drum/cad/README.md
    kind: cad
    last_seen: 2026-05-18
  - path: ../../../sambuca/cad/README.md
    kind: cad
    last_seen: 2026-05-18
crosslinks:
  - instruments/cajon
  - instruments/kora
  - instruments/wood-shell-tongue-drum
  - synthesis/public-release-blockers
open_questions:
  - "Should the library manifest grow a separate native CAD authority field, distinct from web-viewer GLB readiness?"
  - "Should generate_library.py scan uppercase CAD folders as well as lowercase cad folders?"
  - "Which repo should be the first repeatable GLB packaging pilot: cajon, tongue-drum, sambuca, or another simple OpenSCAD/SolidWorks asset?"
answers_filed: []
last_ingest: 2026-05-18
last_lint: 2026-05-18
tags:
  - synthesis
  - cad
  - glb
  - library
---

# CAD Readiness Roadmap

## Overview

The library's `cad` field is a web-viewer packaging signal, not a full statement of whether a project has design geometry, fabrication authority, or native CAD work in progress. [scripts/generate_library.py](../../scripts/generate_library.py) currently detects only packaged `.glb` or multi-file `.gltf` assets under a lowercase `cad/` folder and emits one of four values: `inline-glb`, `external-glb`, `gltf`, or `none`.

That distinction matters: the current portfolio has many CAD-adjacent sources - OpenSCAD masters, SolidWorks files, equation blocks, design tables, cut lists, drawing briefs, and deliberate CAD deferrals - while the generated library manifest reports all current entries as `cad: none`.

## Current Status

Snapshot from [data/library-manifest.json](../../data/library-manifest.json), generated `2026-05-18T21:09:42Z`:

| Portfolio signal | Count |
| --- | ---: |
| Total library entries | 50 |
| Entries with explorers | 46 |
| Entries with capstone manifests | 50 |
| Entries with wiki pages | 3 |
| `cad: inline-glb` | 0 |
| `cad: external-glb` | 0 |
| `cad: gltf` | 0 |
| `cad: none` | 50 |

The absence of GLB/glTF packages is therefore portfolio-wide at the library-card level. It should not be read as "no CAD exists." It means no repo currently has a root-level lowercase `cad/*.glb` package or a lowercase `cad/<sub>/*.gltf` package that the generator recognizes.

Examples already in the workspace:

| Repo | Current CAD source state | Library CAD state |
| --- | --- | --- |
| [[instruments/cajon]] | [OpenSCAD master](../../../../percussion/cajon/cad/cajon-master.scad), [CAD README](../../../../percussion/cajon/cad/README.md), design workbooks, SVG drawing set, jig templates, and [visual authority register](../../../../percussion/cajon/visual-output-register.csv). | `none` because no packaged `.glb` or `.gltf` exists. |
| [[instruments/kora]] | [CAD parametric brief](../../../../strings/kora/cad/kora-parametric-brief.md) and placeholder OpenSCAD; CAD must expose the neck/spine/tail load path before becoming authoritative. | `none` because no packaged `.glb` or `.gltf` exists. |
| [[instruments/wood-shell-tongue-drum]] | [CAD intentionally deferred](../../../../idiophones/wood-shell-tongue-drum/cad/README.md) until first-prototype measurements calibrate the workbook; planned SolidWorks assembly and neutral exports are documented. | `none` by design until CAD is produced and packaged. |
| `sambuca` | [SolidWorks design package notes](../../../../strings/sambuca/cad/README.md), [migration checklist](../../../../strings/sambuca/cad/SW-MIGRATION-CHECKLIST.md), equation source, MasterLayout, assembly, and dimensions CSVs. Current notes say inherited kora geometry still needs rebuild. | `none` because native SolidWorks files are not GLB/glTF packages. |
| `tongue-drum` | [SolidWorks master layout and assembly](../../../../idiophones/tongue-drum/cad/) plus dimension extraction macros and generated dimension CSVs. | `none` because no web-viewer package exists. |

## Source Notes

- [generate_library.py](../../scripts/generate_library.py) documents the four CAD categories in its header and sets `INLINE_GLB_THRESHOLD = 5 * 1024 * 1024`.
- The `detect_cad(repo)` resolver looks for `repo / "cad"`, then root-level `*.glb`, then one-level child folders containing `*.gltf`. If none of those checks succeed, it returns `("none", 0)`.
- The library card renderer labels `inline-glb` as an inlined packed asset, `external-glb` as too large to inline, `gltf` as multi-file glTF not yet packed into `.glb`, and `none` as no CAD assets in `cad/` yet.
- The UI exposes the same four values as CAD filters in [site/library.html](../../site/library.html), generated from [generate_library.py](../../scripts/generate_library.py).
- The console summary only counts `inline-glb` as "cad inlined"; it does not summarize `external-glb`, `gltf`, or native CAD source coverage.

## Design Knowledge

### Generator Categories

| Category | What generate_library.py currently means | Operational interpretation |
| --- | --- | --- |
| `inline-glb` | A lowercase `cad/` folder contains one or more root-level `.glb` files; the largest detected `.glb` is 5 MB or smaller. | Best library-card state for lightweight web preview. The asset can be embedded as a data URI, but it is still a preview export, not dimensional authority. |
| `external-glb` | A lowercase `cad/` folder contains a root-level `.glb` larger than 5 MB. | Viewer-ready, but should be referenced externally instead of inlined. Good for detailed assemblies after optimization. |
| `gltf` | No root `.glb` exists, but a child folder under lowercase `cad/` contains at least one `.gltf`. | Multi-file glTF export exists but is not packaged. Next step is usually texture/bin consolidation and `.glb` packing. |
| `none` | No lowercase `cad/` folder, no detected root `.glb`, and no detected child `.gltf`. | No recognized web-viewer package. This may still coexist with authoritative workbooks, OpenSCAD, SolidWorks files, STEP/STL exports, drawings, or an intentional CAD deferral. |

### Authority Vs Preview

Authority is the chain that can support build, review, or release claims. Preview is the chain that can support inspection, communication, or navigation in the library.

CAD authority can come from:

- A parametric workbook, equation file, or design table that is named as source of truth.
- Native CAD source such as OpenSCAD, SolidWorks MasterLayout, or a reviewed assembly that round-trips against the workbook.
- Validated dimension exports, cut lists, drawing packages, scrap-fit tests, measured stock, and prototype measurement rows.
- A register that states which artifacts carry fabrication authority, derived-preview status, or reference-only status.

CAD preview can come from:

- `.glb`, `.gltf`, `.stl`, screenshots, site renders, SVG overviews, exploded views, and generated product images.
- These assets are useful for review and orientation, but should not be used to infer hidden dimensions, tolerances, screw positions, toolpaths, load paths, or acoustic validation unless they explicitly trace back to authority files.

The strongest current example is [[instruments/cajon]]: its [capstone manifest](../../../../percussion/cajon/capstone-manifest.json) names the design table, OpenSCAD source, jig templates, and reviewed drawing set as fabrication authority, while its [visual-output-register.csv](../../../../percussion/cajon/visual-output-register.csv) marks SVGs, jigs, print packet, and placeholder imagery as derived preview or reference-only where appropriate. Its [design notes](../../../../percussion/cajon/design.md) also warn that generated previews and site imagery must not be used to infer fabrication details.

The kora example adds a structural rule: the [CAD parametric brief](../../../../strings/kora/cad/kora-parametric-brief.md) says the workbook remains source of truth and the CAD must make the load path visible, especially the neck/spine and tail anchor. A kora `.glb` that looks good but hides or misroutes the load path would be a preview artifact, not a release authority.

The wood-shell tongue drum example adds a deferral rule: the [CAD README](../../../../idiophones/wood-shell-tongue-drum/cad/README.md) says CAD should wait until first-prototype measurements are folded back into the workbook, because current cut-list geometry is enough for the first build and CAD becomes load-bearing only when it earns its production cost.

## Recommended Next Actions

1. Preserve the four current library categories as web packaging states.
   The generator categories are simple and useful. Do not overload `cad` with native CAD authority unless the manifest grows a second field.

2. Add a separate CAD authority inventory.
   A future manifest field could track `none`, `brief`, `workbook`, `openscad`, `solidworks-in-progress`, `solidworks-verified`, `neutral-export`, and `measured-release`. That would keep fabrication truth separate from GLB packaging truth.

3. Choose one packaging pilot.
   [[instruments/cajon]] is the lowest-friction pilot because its geometry is rectilinear and already has an OpenSCAD master. Export STL or an intermediate mesh, convert to `.glb`, place it at `cajon/cad/cajon.glb`, verify scale/orientation/materials, and rerun `generate_library.py`.

4. Use `gltf` only as a temporary state.
   If a SolidWorks, Blender, or Fusion export produces `cad/<export-name>/scene.gltf` with `.bin` and texture companions, keep it as `gltf` only while reviewing. Pack to `.glb` before considering the library card ready for public browsing.

5. Keep `.glb` files derived and documented.
   Every packaged asset should have a nearby `cad/README.md` note naming the source CAD, export date, scale unit, coordinate convention, hidden/suppressed parts, and whether the file is preview-only or tied to a validated authority chain.

6. Apply the 5 MB split intentionally.
   Aim for `inline-glb` for simple bodies and hero previews. Use `external-glb` for detailed assemblies where simplification would erase important geometry. Do not decimate load-bearing features, joinery, ports, bridges, or tuner geometry just to pass the inline threshold.

7. Decide on folder-case policy.
   The current resolver scans lowercase `cad/` only. Some repos use uppercase `CAD/`; either normalize future instrument repos to lowercase `cad/` or update `generate_library.py` deliberately to scan both without changing existing links.

8. Verify with the library, not only the file system.
   A packaging task is complete only after `python3 scripts/generate_library.py` updates [data/library-manifest.json](../../data/library-manifest.json), the expected `cad` category appears for that slug, and the generated library card/filter behavior matches the package state.

## Cross-Links

- [[instruments/cajon]]
- [[instruments/kora]]
- [[instruments/wood-shell-tongue-drum]]
- [[synthesis/public-release-blockers]]

## Open Questions

1. Should the generated library expose both `cad` and `cad_authority`, or should authority stay wiki-only until the export workflow stabilizes?
2. Should the first pilot target `inline-glb` size from the start, or accept `external-glb` first and optimize later?
3. What is the preferred conversion toolchain for this portfolio: OpenSCAD/STL to Blender GLB, SolidWorks glTF/GLB export, Fusion, or a scripted `gltfpack` step?
4. Should every `.glb` ship with a preview screenshot and a simple scale cube/check fixture for visual QA?
5. Should public release gates require a visual-output register for every instrument that has generated images, drawings, or CAD previews?

## Maintenance Notes

Do not update library counts by hand. The current counts come from [data/library-manifest.json](../../data/library-manifest.json). After the first `.glb` or `.gltf` package lands in an instrument repo, rerun [scripts/generate_library.py](../../scripts/generate_library.py), then update this page with the changed count and a short example note.
