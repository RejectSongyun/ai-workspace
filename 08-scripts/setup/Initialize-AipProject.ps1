[CmdletBinding()]
param([Parameter(Mandatory)][string]$ProjectPath, [switch]$Apply)
$ErrorActionPreference = 'Stop'
& (Join-Path $PSScriptRoot '../../tools/Initialize-AipProject.ps1') @PSBoundParameters
