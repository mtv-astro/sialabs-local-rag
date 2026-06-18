Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$env:UV_DEFAULT_INDEX = "https://pypi.org/simple"
$env:NPM_CONFIG_REGISTRY = "https://registry.npmjs.org/"

function Invoke-Checked {
  param(
    [Parameter(Mandatory=$true)][string]$Name,
    [Parameter(Mandatory=$true)][string]$WorkingDirectory,
    [Parameter(Mandatory=$true)][string]$Command,
    [string[]]$Arguments = @()
  )

  Write-Host ""
  Write-Host "==> $Name"

  Push-Location $WorkingDirectory
  try {
    & $Command @Arguments
    $exitCode = $LASTEXITCODE
  }
  finally {
    Pop-Location
  }

  if ($null -ne $exitCode -and $exitCode -ne 0) {
    throw "$Name failed with exit code $exitCode"
  }
}

if (!(Test-Path ".env") -and (Test-Path ".env.example")) {
  Copy-Item ".env.example" ".env" -Force
  Write-Host "Created local .env from .env.example for validation. Do not commit .env."
}

Invoke-Checked "backend: uv lock" "backend" "uv" @("lock", "--refresh")
Invoke-Checked "backend: uv sync" "backend" "uv" @("sync", "--dev")
Invoke-Checked "backend: ruff fix" "backend" "uv" @("run", "ruff", "check", ".", "--fix")
Invoke-Checked "backend: ruff check" "backend" "uv" @("run", "ruff", "check", ".")
Invoke-Checked "backend: pytest" "backend" "uv" @("run", "pytest")
Invoke-Checked "backend: mypy" "backend" "uv" @("run", "mypy", "src")

if (Test-Path "frontend/package-lock.json") {
  Invoke-Checked "frontend: npm ci" "frontend" "npm" @("ci")
} else {
  Invoke-Checked "frontend: npm install" "frontend" "npm" @("install")
}

Invoke-Checked "frontend: typecheck" "frontend" "npm" @("run", "typecheck")
Invoke-Checked "frontend: build" "frontend" "npm" @("run", "build")

if (Get-Command docker -ErrorAction SilentlyContinue) {
  Invoke-Checked "docker compose config" "." "docker" @("compose", "config")
} else {
  Write-Host "Docker not found; skipping docker compose config."
}

Write-Host ""
Write-Host "Validation finished successfully. Review git status and diff before committing."
git status --short
git diff --stat
