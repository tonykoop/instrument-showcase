# Image-Gen Provenance Sidecar: udu-family-group.png

**Status:** prompt staged — image not yet generated  
**Target:** `examples/catalog-lookbook-pilot/images/udu-family-group.png`  
**Authority:** concept_only  
**Pipeline:** gemini image-gen-2 → Adobe MCP refine (instrument-maker #182)

---

## Prompt

```
Create a high-quality studio photograph showing the complete Udu Drum family:
four ceramic vessels arranged left to right from smallest to largest (S, M, L, XL).

Each udu is a round-bodied ceramic drum with a cylindrical neck at the top and
a smaller side port. The ceramic surface has an earthy terracotta finish with
smooth, slightly textured glaze. All four share the same form but differ in size:
the largest (XL) should be roughly 1.4× the height of the smallest (S).

Camera and lighting:
- Straight-on front view with slight 15° downward angle
- Even soft-box lighting, no harsh shadows between vessels
- White background (#FAFAFA)
- All four instruments in sharp focus

Image specifications:
- Size: 2048 × 1365 pixels, sRGB
- Style: product family photograph

IMPORTANT: This image is a concept visualization only. Do not include ruler
overlays, dimension annotations, size labels, or fabrication specifications.
Scale is approximate and for visual communication only. The image is not
authoritative for any physical build dimension.
```

---

## Adobe MCP Refinement

1. `image_adjust_color_temperature`: +150K for warm terracotta tones
2. `image_adjust_brightness_and_contrast`: brightness=0, contrast=8
3. Save: `images/udu-family-group.png`

---

## visual-output-register.csv Row

```csv
examples/catalog-lookbook-pilot/images/udu-family-group.png, family-shot, concept_only, ai-gen+photoshop-mcp, udu-family-001, 4-member family concept — scale approximate
```
