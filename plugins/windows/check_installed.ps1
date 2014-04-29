<#
  First script argument will be used as the regex matching string to check the DisplayName of an installed component.
#>

if ($args.Count -lt 1) {
    Write-Output "This script requires a regex string argument.
eg.  $($MyInvocation.MyCommand) '^Microsoft.*x64'
"
    exit 3
}

$arg = $args[0]

$items = Get-ChildItem HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall
$hits = $items | Where-Object {$_.GetValueNames().Contains('DisplayName') -and $_.GetValue('DisplayName') -match $arg} | % {$_.GetValue('DisplayName')}
Write-Output $hits
if ($hits.Count -gt 0) {exit 0}
exit 2
