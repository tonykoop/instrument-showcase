# Explorer v2 — template-quality upgrade

Scoped, generator-level improvements to `scripts/generate_explorer_v2.py` so every
per-instrument `explorer.html` gets better **before** we regenerate across all five
families (epic #31). Template-first, then regenerate.

> Why a brief instead of a direct code PR: this was prepared in a Cowork session whose
> shell + folder-mount were blocked by an environment bug, so the generator couldn't be
> run or parse-checked there. Apply these edits locally where the instrument repos are
> cloned (`C:\Users\Tony\Documents\GitHub\instruments`), then verify with the commands at
> the bottom. Every change is additive and progressive-enhancement (no-JS still works).

## What changes and why

1. **FOUC-safe theming + OS preference.** Today the theme is applied by a script at the
   end of `<body>`, so dark-mode users see a white flash on load, and first-time visitors
   always get light even if their OS is dark. Move theme init into `<head>` and honor
   `prefers-color-scheme` when there's no stored choice.
2. **Conditional `model-viewer` load.** The ~heavy model-viewer module is loaded on every
   explorer, but most instruments have no `.glb`. Load it only when `d.glb_rel` is set.
3. **SEO / social metadata.** Add `description`, Open Graph + Twitter card (hero as
   `og:image`), `theme-color`, and minimal JSON-LD — big payoff for a public catalog.
4. **Accessibility.** Skip-to-content link, real gallery `alt` text, `aria-pressed` +
   `aria-label` on the theme button, `aria-label` on the TOC nav, `id="main"` target.
5. **Gallery lightbox (vanilla, progressive).** Click a thumbnail to view inline with
   keyboard nav (← → Esc); falls back to the existing open-in-new-tab when JS is off.

---

## Edit 1 — append to `EXPLORER_CSS` (before the closing `</style>`)

```css
/* ----- accessibility + lightbox + print ----- */
.skip-link{position:absolute;left:8px;top:-44px;z-index:60;background:var(--accent);color:#fff;padding:9px 14px;border-radius:8px;transition:top .15s}
.skip-link:focus{top:8px;color:#fff}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.lb{position:fixed;inset:0;z-index:80;display:none;align-items:center;justify-content:center;background:rgba(8,10,13,.86);padding:28px}
.lb.open{display:flex}
.lb img{max-width:94vw;max-height:90vh;object-fit:contain;border-radius:8px;box-shadow:0 8px 40px rgba(0,0,0,.5)}
.lb-close{position:absolute;top:16px;right:20px;width:42px;height:42px;border:none;border-radius:50%;background:rgba(255,255,255,.12);color:#fff;font-size:22px;cursor:pointer}
.lb-close:hover{background:var(--accent)}
.lb-nav{position:absolute;top:50%;transform:translateY(-50%);width:46px;height:46px;border:none;border-radius:50%;background:rgba(255,255,255,.12);color:#fff;font-size:24px;cursor:pointer}
.lb-nav:hover{background:var(--accent)} .lb-prev{left:18px} .lb-next{right:18px}
@media print{.appbar,.toc,.totop,.pager,.icon-btn,.lb{display:none!important}.app{grid-template-columns:1fr;padding:0}section.card{break-inside:avoid;box-shadow:none}}
```

## Edit 2 — replace the `THEME_SCRIPT` constant with three constants

Delete the existing `THEME_SCRIPT = """..."""` block and add:

```python
# Runs in <head> BEFORE first paint so dark-mode users get no white flash,
# and first-time visitors inherit their OS preference.
HEAD_THEME_INIT = """<script>
(function(){var KEY='hz-theme';try{var s=localStorage.getItem(KEY);
var d=s!==null?s:((window.matchMedia&&window.matchMedia('(prefers-color-scheme: dark)').matches)?'dark':'');
if(d==='dark')document.documentElement.setAttribute('data-theme','dark');}catch(e){}})();
</script>"""

# Toggle handler + broken-image hiding; runs at end of <body>.
THEME_TOGGLE = """<script>
(function(){
  var KEY='hz-theme', b=document.getElementById('theme-toggle');
  function sync(){ if(b) b.setAttribute('aria-pressed', document.documentElement.getAttribute('data-theme')==='dark'); }
  sync();
  if(b) b.addEventListener('click',function(){
    var dark=document.documentElement.getAttribute('data-theme')==='dark';
    if(dark) document.documentElement.removeAttribute('data-theme'); else document.documentElement.setAttribute('data-theme','dark');
    try{localStorage.setItem(KEY,dark?'':'dark');}catch(e){}
    sync();
  });
  document.querySelectorAll('img').forEach(function(im){im.addEventListener('error',function(){var w=this.closest('.hero-cover,.gallery a');if(w)w.style.display='none';});});
})();
</script>"""

# Vanilla, dependency-free gallery lightbox (progressive enhancement: the
# <a href> still points at the file, so no-JS users get open-in-new-tab).
LIGHTBOX_SCRIPT = """<script>
(function(){
  var thumbs=[].slice.call(document.querySelectorAll('.gallery a'));
  if(!thumbs.length) return;
  var lb=document.createElement('div');
  lb.className='lb'; lb.setAttribute('role','dialog'); lb.setAttribute('aria-modal','true'); lb.setAttribute('aria-label','Image viewer');
  lb.innerHTML='<button class="lb-close" aria-label="Close">\\u00d7</button><button class="lb-nav lb-prev" aria-label="Previous">\\u2039</button><img alt=""><button class="lb-nav lb-next" aria-label="Next">\\u203a</button>';
  document.body.appendChild(lb);
  var img=lb.querySelector('img'), i=0;
  function show(n){ i=(n+thumbs.length)%thumbs.length; var a=thumbs[i]; img.src=a.getAttribute('href'); var t=a.querySelector('img'); img.alt=t?t.alt:''; }
  function open(n){ show(n); lb.classList.add('open'); document.body.style.overflow='hidden'; }
  function close(){ lb.classList.remove('open'); document.body.style.overflow=''; }
  thumbs.forEach(function(a,n){ a.addEventListener('click',function(e){ e.preventDefault(); open(n); }); });
  lb.querySelector('.lb-close').addEventListener('click',close);
  lb.querySelector('.lb-prev').addEventListener('click',function(e){ e.stopPropagation(); show(i-1); });
  lb.querySelector('.lb-next').addEventListener('click',function(e){ e.stopPropagation(); show(i+1); });
  lb.addEventListener('click',function(e){ if(e.target===lb) close(); });
  document.addEventListener('keydown',function(e){ if(!lb.classList.contains('open')) return;
    if(e.key==='Escape') close(); else if(e.key==='ArrowLeft') show(i-1); else if(e.key==='ArrowRight') show(i+1); });
})();
</script>"""
```

(`NAV_SCRIPT` is unchanged.)

## Edit 3 — in `render_explorer`, build the head metadata + perf-aware script vars

Insert just before the final `return f"""..."""` (after the `hero_cover = (...)` block):

```python
    # ---- SEO / social metadata + perf-aware head ----
    desc = (f"{d.title} - {d.family_label}"
            + (f" ({d.acoustic_class})" if d.acoustic_class else "")
            + ". Studio explorer with 3D model, render gallery, live Wolfram acoustic "
              "model, bill of materials, and release gates, where present.")
    og_image = f'<meta property="og:image" content="{esc(d.hero_rel)}">' if d.hero_rel else ""
    tw_card = "summary_large_image" if d.hero_rel else "summary"
    ld = json.dumps({
        "@context": "https://schema.org",
        "@type": "CreativeWork",
        "name": d.title,
        "about": d.instrument,
        "genre": d.family_label,
        "creator": {"@type": "Brand", "name": "Heifer Zephyr"},
    }, ensure_ascii=False).replace("<", "\\u003c")
    head_meta = (
        f'<meta name="description" content="{esc(desc)}">'
        f'<meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">'
        f'<meta name="theme-color" content="#0e1116" media="(prefers-color-scheme: dark)">'
        f'<meta property="og:type" content="website">'
        f'<meta property="og:title" content="{esc(d.title)} · Heifer Zephyr">'
        f'<meta property="og:description" content="{esc(desc)}">'
        f'{og_image}'
        f'<meta name="twitter:card" content="{tw_card}">'
        f'<script type="application/ld+json">{ld}</script>'
    )
    mv_script = ('<script type="module" '
                 'src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>'
                 ) if d.glb_rel else ""
```

## Edit 4 — update the returned HTML (`render_explorer` f-string)

- **Head** — replace the always-on model-viewer `<script>` line and inject the new pieces:

  ```html
  <title>{esc(d.title)} · Studio Explorer · Heifer Zephyr</title>
  {head_meta}
  {HEAD_THEME_INIT}
  {mv_script}
  {EXPLORER_CSS}
  </head>
  ```

- **Body open** — add a skip link as the first child of `<body>`:

  ```html
  <body>
  <a class="skip-link" href="#main">Skip to content</a>
  ```

- **Theme button** — add aria:

  ```html
  <button class="icon-btn" id="theme-toggle" type="button" aria-pressed="false" aria-label="Toggle light or dark theme" title="Toggle light / dark">◐ Theme</button>
  ```

- **Main region** — label the TOC nav and give `<main>` the skip target id:

  ```html
  <nav class="toc" aria-label="On this page">{toc_block}</nav>
  <main id="main">
  ```

- **End of body** — swap the script includes:

  ```html
  {THEME_TOGGLE}
  {NAV_SCRIPT}
  {LIGHTBOX_SCRIPT}
  ```

## Edit 5 — gallery `alt` text + decoding hints

Replace the gallery `cells` comprehension:

```python
        cells = "".join(
            f'<a href="{esc(g)}" target="_blank" rel="noopener">'
            f'<img src="{esc(g)}" loading="lazy" decoding="async" '
            f'alt="{esc(d.title)} render {n}"></a>'
            for n, g in enumerate(d.gallery, 1))
```

And the hero cover (add decoding/loading hints):

```python
    hero_cover = (
        f'<div class="hero-cover"><img src="{esc(d.hero_rel)}" alt="{esc(d.title)}" '
        f'loading="eager" decoding="async"></div>'
        if d.hero_rel else
        '<div class="hero-cover"><span class="ph">no hero render yet</span></div>'
    )
```

---

## Verify locally (WSL CLI agent)

```bash
cd ~/Documents/GitHub/instruments/_meta/instrument-showcase   # adjust if path differs
python -c "import ast; ast.parse(open('scripts/generate_explorer_v2.py').read()); print('syntax OK')"
python3 scripts/generate_explorer_v2.py --slug kora --dry-run
python3 scripts/generate_explorer_v2.py --slug kora            # writes explorer.generated.html
# open the generated file and check: no dark-mode flash, OG tags in <head>,
# model-viewer only present when a .glb exists, lightbox opens on a gallery click,
# keyboard nav (Esc / arrows) works, skip-link appears on Tab.
```

Once a single explorer looks right, regenerate the scaffold set:

```bash
python3 scripts/generate_explorer_v2.py --all --only-scaffold --write-explorer
```

Then refresh the library + bundle so the catalog picks up the improved explorers.
