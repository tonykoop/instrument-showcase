# publish.ps1 - Heifer Zephyr instrument publisher
# One-time setup: install GitHub CLI (https://cli.github.com), then run:  gh auth login
# Then just double-click publish.bat whenever you want to publish.
#
# What it does:
#   1. For every slug in published.txt: make the repo public + enable GitHub Pages
#   2. Regenerate the public instrument library
#   3. Push the refreshed library.html live to tonykoop.github.io
$ErrorActionPreference = "Continue"

$owner     = "tonykoop"
$root      = "C:\Users\Tony\Documents\GitHub"
$showcase  = Join-Path $root "instruments\_meta\instrument-showcase"
$gen       = Join-Path $showcase "scripts\generate_library.py"
$published = Join-Path $showcase "scripts\published.txt"

$py = "python"
if (-not (Get-Command $py -ErrorAction SilentlyContinue)) { $py = "python3" }
if (-not (Get-Command "gh" -ErrorAction SilentlyContinue)) {
  Write-Host "GitHub CLI (gh) not found. Install from https://cli.github.com then run: gh auth login"
  Read-Host "Press Enter to close"; exit 1
}

Write-Host "== Step 1: make repos public + enable Pages =="
Get-Content $published | ForEach-Object {
  $slug = $_.Trim()
  if (-not $slug -or $slug.StartsWith("#")) { return }
  Write-Host "  publishing $slug"
  gh repo edit "$owner/$slug" --visibility public --accept-visibility-change-consequences 2>$null
  gh api -X POST "repos/$owner/$slug/pages" -f "source[branch]=main" -f "source[path]=/" 2>$null | Out-Null
}

Write-Host "== Step 2: regenerate library =="
& $py $gen --workspace $root --base-url "https://tonykoop.github.io" --published $published --output-html "$env:TEMP\hz_library.html" --output-data "$env:TEMP\hz_manifest.json"
if (-not (Test-Path "$env:TEMP\hz_library.html")) { Write-Host "Generation failed."; Read-Host "Press Enter to close"; exit 1 }

Write-Host "== Step 3: push library live (via temp clone, avoids sync lock) =="
$site = Join-Path $env:TEMP "tksite"
if (Test-Path $site) { Remove-Item -Recurse -Force $site }
gh repo clone "$owner/$owner.github.io" $site
Copy-Item "$env:TEMP\hz_library.html" (Join-Path $site "library.html") -Force
Push-Location $site
git add library.html
git commit -m "Refresh instrument library"
git push
Pop-Location
Write-Host ""
Write-Host "Done. Live at https://tonykoop.github.io/library.html in about a minute."
Read-Host "Press Enter to close"
