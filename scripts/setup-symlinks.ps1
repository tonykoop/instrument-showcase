# setup-symlinks.ps1
#
# One-time setup. Wires raw-sources/second-brain and raw-sources/obsidian-clips
# into the Obsidian vault so the wiki agent can read tribal-knowledge notes
# without copying or duplicating them.
#
# Run from an elevated PowerShell (Run as Administrator) OR with Windows
# Developer Mode enabled (Settings -> System -> For developers):
#
#   cd C:\Users\Tony\Documents\GitHub\instrument-showcase
#   powershell -ExecutionPolicy Bypass -File .\scripts\setup-symlinks.ps1
#
# Idempotent: re-running is safe. Existing correct links are kept;
# stale or mis-pointed ones are recreated.

param(
    [string]$ShowcaseDir = 'C:\Users\Tony\Documents\GitHub\instrument-showcase',
    [string]$VaultDir    = 'C:\Users\Tony\Documents\Second_Brain',
    [string]$ClipsDir    = 'C:\Users\Tony\Documents\Second_Brain\Clippings'
)

$ErrorActionPreference = 'Stop'

$rawSources = Join-Path $ShowcaseDir 'raw-sources'
$inboxDir   = Join-Path $rawSources  'inbox'
$brainLink  = Join-Path $rawSources  'second-brain'
$clipsLink  = Join-Path $rawSources  'obsidian-clips'
$allowlist  = Join-Path $rawSources  '.ingest-allowlist'

# Ensure raw-sources/ structure exists
if (-not (Test-Path $rawSources)) {
    New-Item -ItemType Directory -Path $rawSources | Out-Null
    Write-Host ('Created: ' + $rawSources) -ForegroundColor Green
}
if (-not (Test-Path $inboxDir)) {
    New-Item -ItemType Directory -Path $inboxDir | Out-Null
    Write-Host ('Created: ' + $inboxDir) -ForegroundColor Green
}

function Set-Symlink {
    param(
        [string]$LinkPath,
        [string]$TargetPath,
        [string]$Label
    )
    if (-not (Test-Path $TargetPath)) {
        Write-Warning ('Target does not exist, skipping {0}: {1}' -f $Label, $TargetPath)
        return
    }
    if (Test-Path $LinkPath) {
        $item = Get-Item $LinkPath -Force
        if ($item.LinkType -eq 'SymbolicLink' -or $item.LinkType -eq 'Junction') {
            $current = $item.Target
            if ($current -is [array]) { $current = $current[0] }
            if ($current -eq $TargetPath) {
                Write-Host ('OK   {0}: {1} -> {2} (already linked)' -f $Label, $LinkPath, $TargetPath) -ForegroundColor Cyan
                return
            }
            Remove-Item $LinkPath -Force
            Write-Host ('Removed stale link: ' + $LinkPath) -ForegroundColor Yellow
        } else {
            Write-Warning ('{0}: {1} exists and is not a symlink. Skipping (move or delete it manually).' -f $Label, $LinkPath)
            return
        }
    }
    try {
        New-Item -ItemType SymbolicLink -Path $LinkPath -Target $TargetPath -ErrorAction Stop | Out-Null
        Write-Host ('Linked {0}: {1} -> {2}' -f $Label, $LinkPath, $TargetPath) -ForegroundColor Green
    } catch {
        Write-Warning 'Symlink failed (need admin or Developer Mode). Falling back to junction.'
        cmd /c mklink /J "$LinkPath" "$TargetPath" | Out-Null
        if (Test-Path $LinkPath) {
            Write-Host ('Junction {0}: {1} -> {2}' -f $Label, $LinkPath, $TargetPath) -ForegroundColor Green
        } else {
            Write-Error ('Could not create ' + $Label + ' link. Run as Administrator or enable Developer Mode.')
        }
    }
}

Set-Symlink -LinkPath $brainLink -TargetPath $VaultDir -Label 'Second_Brain'
Set-Symlink -LinkPath $clipsLink -TargetPath $ClipsDir -Label 'Clippings'

# Verify allowlist is present (created during scaffold pass)
if (-not (Test-Path $allowlist)) {
    Write-Warning ('.ingest-allowlist missing at ' + $allowlist + '. Re-create it from raw-sources/README.md before running the wiki agent.')
} else {
    Write-Host 'OK   .ingest-allowlist present' -ForegroundColor Cyan
}

Write-Host ''
Write-Host ('Done. Next: cd ' + $ShowcaseDir + '; python3 scripts/generate_library.py') -ForegroundColor Green
