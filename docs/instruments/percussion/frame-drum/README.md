# Frame Drum — Engineering Documentation Across Methods, Traditions, and Mallets

> *Frame drums across multiple construction methods (stave-built, steam-bent, wood-turned, CNC-machined) and many cultural traditions (Irish bodhrán, Native American hand drum, Middle Eastern daf/riq/bendir, Brazilian pandeiro, Mongolian and Sami shamanic drums). Plus the companion mallets and drumsticks.*

## What this is

Engineering documentation for **frame drum construction** across the full range of methods I want to explore, plus the mallets and sticks that complete the family. The repository is structured around three threads:

At the moment this repo is design intent and research structure rather than a finished build log. Round 30 adds a V5 explorer surface, an explicit visual-authority register, and a validation loop, but it does not promote the packet to measured or build-ready status. Photos, generated renders, MCP-derived art, and per-method documentation will land here as the first drums actually get built.

**Status:** L1 concept packet

## Readiness

L1 concept packet. This repo explicitly frames itself as a V5 **explorer
packet candidate**, not a complete V5 build-packet candidate — see
"V5 explorer packet status" below for the honest accounting of what is
assumption-based vs. what would be required to call this L2 or higher (a
built/measured prototype, sourced supply data, and MCP-derived visual
evidence are all still outstanding).

## Packet Contents

- `design.md` - membrane governing model, baseline FD-14/16/18 geometry, and
  assumptions.
- `bom.csv`, `sourcing.csv`, `cut-list.csv`, `validation.csv`,
  `validation-loop.csv` - first-pass shop packet and measurement-loop tables.
- `assembly-manual.md`, `risks.md`, `photo-shotlist.md` - build flow and
  validation documentation.
- `drawing-brief.md`, `drawings/frame-drum-hoop-plan.dxf` - starter fabrication
  vector artifacts.
- `cad/frame_drum_hoop.scad` - parametric OpenSCAD master driven by
  `family-spec.csv` (FD-14/16/18 rows); authority `pending_measurement`.
- `frame-drum-starter.wl` - Wolfram membrane-mode starter model, embedded live
  in `explorer.html` via Wolfram Cloud; source-only, not executed here.
- `evolution/` - evolution-pipeline Stage 0 intake: master manifest,
  design-intent, and revision register (Gate A not yet run).

1. **Construction methods** — every viable way to build a frame drum, documented as I work through each:
   - **Stave-built** (the technique I learned at Morgan Drums, applied to a thin-shell frame profile)
   - **Steam-bent** (a single thin strip of hardwood bent into a hoop and scarf-joined — the traditional bodhrán approach)
   - **Wood-turned** (segmented or single-piece hoops turned on a lathe)
   - **CNC-machined** (single-piece or multi-segment hoops cut on the [`cnc`](https://github.com/tonykoop/cnc) Haas machines)
   - **Inflatable-tire-tuned** (a contemporary tuning approach pioneered by [Feather Song Drums](https://jourdanneil.wixsite.com/feathersongdrums) in New Zealand — an inflatable inner-tube wrapped around the inside of the rim provides continuously-adjustable head tension)
2. **Cultural traditions** — frame drums span more cultures than almost any other instrument family. Each tradition gets a documented section as I explore it:
   - **Irish bodhrán** — goatskin head, internal cross-brace, played with a tipper (cipín)
   - **Native American hand drum** — single-piece bent hoop, deerskin or elk-skin head, lashed back-strap, beater-style stick
   - **Middle Eastern daf, riq, bendir** — riq with cymbals, daf with internal jingles, bendir with a snare wire across the back
   - **Brazilian pandeiro** — wood frame, tunable head, jingle-platelets in the rim
   - **Mongolian and Sami shamanic drums** — round or oval, decorated head, trance-context drum
   - **(others as the project grows)**
3. **Mallets and sticks** — companion percussion-implement designs. Tony's tipper for bodhrán, beater for hand drum, mallet shafts and head materials for tongue drums and dunduns. **All of Tony's drum-strike-implement design work lives here**, regardless of which sister-repo drum it serves.

Sister repos: [`djembe`](https://github.com/tonykoop/djembe), [`dundun`](https://github.com/tonykoop/dundun), [`tongue-drum`](https://github.com/tonykoop/tongue-drum), [`ashiko-drum-workshop`](https://github.com/tonykoop/ashiko-drum-workshop) — the other percussion repositories whose mallets and sticks may end up documented here.

## Background — why frame drums

A frame drum is the simplest possible drum: a shallow hoop with a stretched membrane on one (sometimes both) faces. Geometrically it's the *limit case* of all the goblet-and-cylinder drums in the rest of my portfolio — what's left when you minimize the body cavity. Acoustically that limit case is interesting: with no significant air-cavity Helmholtz coupling to add bass, the tone comes almost entirely from the **membrane modes** (Bessel modes on a circular tensioned membrane) plus the small-cavity coupling characteristic.

That makes frame drums an excellent platform for studying:

- **Membrane acoustics** in isolation (no big cavity to confound)
- **Tuning mechanisms** — fixed-rim (most traditional), rope-laced, lug-tuned, inflatable-tire-tuned (the Feather Song Drums approach)
- **Hoop construction tradeoffs** — stave, bent, turned, CNC — each affects mass distribution and rim stiffness
- **Skin-prep methodology** — the work that begins long before the drum exists

## Skin preparation

The deerskin-and-stretcher work begins long before the hoop is glued. Photos forthcoming from preparing a deer hide on a stretching frame for use as a head — soaking, scraping, stretching to dimension, drying. This is craft that predates engineering documentation but benefits from it: skin thickness, hair-removal completeness, and stretcher tension all show up later in the drum's tonal character.

*(Skin-prep photos to be added — currently in personal archives.)*

## Construction methods — design intent

### Stave-built frame drum
Thin-shell adaptation of the stave techniques developed for the [`ashiko`](https://github.com/tonykoop/ashiko-drum-workshop) and [`djembe`](https://github.com/tonykoop/djembe) repositories — the same compound-miter math at a much shorter stave height. Trade-off vs. steam-bent: stave seams may be acoustically distinct, but offer wider material options (no need for steam-bendable species).

CAD model in development.

### Steam-bent frame drum
The traditional bodhrán construction: a single thin strip of straight-grained hardwood (ash, oak, cherry) steam-softened, bent around a circular form, scarf-joined at the closure. Visually seamless, acoustically uniform, but limited to species that bend without splitting.

CAD model in development.

### Wood-turned frame drum
A solid-wood ring turned on a lathe from a glued-up blank (segmented turning) or from a sufficiently-large single piece. Most material-wasteful but allows complex profile cross-sections (bevels, beads, internal contours).

### CNC-machined frame drum
A single-piece or multi-segment hoop cut from sheet/plate stock on the Haas VF-2 (or eventually the Maker Nexus ShopBot CNC router for thicker work). Trades the romance of bent wood for repeatability and complex internal profile freedom — internal lugs, tuner mounts, payload pockets all become trivial design moves.

### Inflatable-tire-tuned (Feather Song Drums approach)
[Feather Song Drums](https://feathersongdrums.com/) in New Zealand pioneered using an inflatable bicycle inner-tube wrapped around the inside of the drum rim as a tuning mechanism. Inflate the tube → it presses outward against a movable ring → the ring presses up against the head → continuously-adjustable head tension across a wide range, with no laces or lugs. Brilliant idea worth replicating and documenting.

## Mallets and drumsticks

The mallet/stick design work for **all** my drums lives here, since it crosses repository boundaries cleanly:

- **Bodhrán tipper (cipín)** — small double-headed stick swung between thumb and fingers; head material and balance set the tone
- **Hand-drum beater** — felt or fur-padded head on a wood handle for Native American hand drum playing
- **Tongue-drum mallets** — rubber-ball heads on wood dowels (the magazine plan in [`tongue-drum`](https://github.com/tonykoop/tongue-drum) shows the baseline; alternate head materials are part of the DoE study's mallet-hardness factor)
- **Dundun mallet** — heavy padded stick for bass-drum striking
- **Stick-balance + grip ergonomics** — a cross-cutting design problem worth its own section once data exists

Future skill stub: **`mallet-head-material-vs-tone-spectrum`** — to be extracted when the tongue-drum DoE Phase 1 data starts producing mallet-specific spectral signatures.

## Planned repository structure

As builds begin, this repo will likely grow into:

```
frame-drum/
├── README.md                  ← you are here
├── LICENSE                    ← CC-BY 4.0
├── images/                    ← skin-prep, build photos, finished drums
├── CAD/                       ← per-method body models
│   ├── stave/
│   ├── steam-bent/
│   ├── wood-turned/
│   └── cnc-machined/
├── traditions/                ← per-tradition writeups
├── mallets-and-sticks/        ← cross-drum mallet + stick design work
└── reference/                 ← Feather Song Drums + traditional-construction references
```

## V5 explorer packet status

Current status: `L1 concept packet` / V5 explorer packet candidate (not a
complete V5 build-packet candidate). Fabrication
authority is limited to the assumption-based design table and starter vector
artifacts listed in `visual-output-register.csv`: `family-spec.csv`,
`cad/frame_drum_hoop.scad`, and `drawings/frame-drum-hoop-plan.dxf`. These
files are not measured, runtime-verified, or shop-validated.

Round 30 explorer files:

| File | Role | Authority |
|---|---|---|
| `explorer.html` | Static packet explorer for review | concept/support only |
| `capstone-manifest.json` | Root artifact manifest | metadata |
| `visual-output-register.csv` | Visual authority register | authority map |
| `validation-loop.csv` | Measurement-required validation loop | validation plan |
| `cad/mcp-session-log.md` | MCP provenance status | provenance notes |
| `drawings/frame-drum-hoop-plan.dxf` | FD-16 hoop layout starter | assumption-based fabrication candidate |

Remaining V5 blockers: no physical hoop/head measurements, no selected
tensioning fixture, no recorded resonance or strike-response captures, no
Blender/Illustrator/Photoshop/Adobe/image-generation MCP sessions, no hero
render, no exploded diagram, and no annotated print plate.

## Status

A repository in motion, not a finished portfolio piece. The current packet is
reviewable, but not a complete V5 build-packet candidate.

| Section | Status |
|---|---|
| Repo description, license | ✓ done |
| Construction-method scaffolding | ✓ documented as design intent |
| Cultural-tradition list | ✓ outlined |
| Mallet/stick scope established | ✓ done |
| Hero + skin-prep photos | forthcoming (in personal archives) |
| CAD — stave-built body | forthcoming |
| CAD — steam-bent body | forthcoming |
| CAD — wood-turned body | forthcoming |
| CAD — CNC-machined body | forthcoming |
| Inflatable-tire-tuner concept replication | forthcoming |
| First built drum | forthcoming |

## License

Released under [CC-BY 4.0](LICENSE) — original written content, CAD, photographs, and analysis in this repository are mine, free to reuse and adapt with credit. The traditional frame drum forms documented here originate with the cultures named above and remain culturally significant in their living traditions; the engineering documentation here is my own, free to reuse with attribution. The inflatable-tire tuning concept is credited to **Feather Song Drums** of New Zealand — any replication and documentation here references their innovation.
