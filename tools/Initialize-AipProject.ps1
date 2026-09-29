[CmdletBinding()]
param([Parameter(Mandatory)][string]$ProjectPath, [switch]$Apply)
$ErrorActionPreference = 'Stop'
$workspace = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$target = [IO.Path]::GetFullPath($ProjectPath)
$template = Join-Path $workspace 'templates/project'
if (Test-Path -LiteralPath $target -PathType Leaf) { throw '目标是文件。' }
foreach ($item in @('.ai','AGENTS.md')) {
  if (Test-Path -LiteralPath (Join-Path $target $item)) { throw "已有 $item，拒绝覆盖。请增量合并。" }
}
Write-Output "目标: $target；统一项目模板；新增 .ai/ 与 AGENTS.md。"
if (-not $Apply) { Write-Output '当前为预览；增加 -Apply 执行。'; return }
New-Item -ItemType Directory -Path $target -Force | Out-Null
Copy-Item -LiteralPath (Join-Path $template '.ai') -Destination $target -Recurse
Copy-Item -LiteralPath (Join-Path $template 'AGENTS.md') -Destination $target
$config = Join-Path $target '.ai/project.yaml'
$name = Split-Path $target -Leaf
$body = [IO.File]::ReadAllText($config).Replace('name: UNCONFIGURED', "name: '$($name.Replace("'", "''"))'")
[IO.File]::WriteAllText($config, $body, [Text.UTF8Encoding]::new($false))
Write-Output '初始化完成；核验实际项目路径与命令后填写模型。部分失败时保留现场，不自动覆盖重试。'
