# Image-Gen Provenance Sidecar: ocarina-hero.png

**Status:** prompt staged — image not yet generated  
**Target:** `examples/catalog-lookbook-pilot/images/ocarina-hero.png`  
**Authority:** concept_only  
**Pipeline:** gemini image-gen-2 → Adobe MCP refine (instrument-maker #182)

---

## Prompt

```
Create a high-quality studio photograph of a slip-cast ceramic ocarina in Alto C.

The ocarina is a transverse vessel flute: oval body with a small mouthpiece at
one end and tone holes across the top surface. The ceramic surface has a smooth
matte white glaze with subtle warm undertones from the firing process.

Camera and lighting:
- 3/4 view: 45° azimuth, 30° elevation above table level
- Studio HDRI lighting: neutral soft-box key light at front-left, fill at right
- Clean neutral grey background (#E0E0E0)
- Shallow depth of field: ocarina sharp, background soft

Image specifications:
- Size: 2048 × 1536 pixels, sRGB
- Style: product photography, editorial quality

IMPORTANT: This image is a concept visualization only. Do not include dimension
lines, measurements, ruler overlays, tone-hole dimensions, or fabrication
specifications. The image is not authoritative for any physical build dimension.
The number and placement of tone holes shown is approximate and for visual
communication only.
```

---

## Adobe MCP Refinement Steps (after generation)

1. `image_remove_background` → neutral grey (#E0E0E0)
2. `image_adjust_brightness_and_contrast`: brightness=5, contrast=10
3. `image_apply_lens_blur`: focal_distance=0.5, radius=8
4. Save: `images/ocarina-hero.png` (overwrite seed)
5. Move seed to: `images/.seeds/ocarina-hero-seed-YYYYMMDD.png`

---

## visual-output-register.csv Row

```csv
examples/catalog-lookbook-pilot/images/ocarina-hero.png, render, concept_only, ai-gen+photoshop-mcp, ocarina-hero-001, studio hero concept — not dimensional
```

## mcp-session-log.md Row

```
| ocarina-hero-001 | YYYY-MM-DD | gemini-imagen (#182) | templates/image-prompts/hero.md | examples/catalog-lookbook-pilot/images/ocarina-hero.png | studio hero concept | concept_only; seed archived |
```
