param(
    [ValidateSet('preflight','doctor','query')][string]$Mode = 'preflight',
    [string]$Topic = 'context engineering',
    [string]$PythonPath
)
$ErrorActionPreference = 'Stop'
if (-not $PythonPath) {
    $bundled = Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
    if (Test-Path -LiteralPath $bundled) { $PythonPath = $bundled }
    else {
        $pythonCommand = Get-Command python -ErrorAction SilentlyContinue
        if (-not $pythonCommand) { throw 'Python 3.12+ required; specify -PythonPath.' }
        $PythonPath = $pythonCommand.Source
    }
}
& $PythonPath (Join-Path $PSScriptRoot 'Invoke-RecentSignals.py') --mode $Mode --topic $Topic
if ($LASTEXITCODE -ne 0) { throw "last30days returned $LASTEXITCODE; inspect the printed run directory." }
