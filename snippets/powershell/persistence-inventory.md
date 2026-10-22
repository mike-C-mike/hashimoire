# Windows — Startup and Persistence Inventory

**Use case:** triage | response | validation  
**Environment:** windows  
**Risk:** safe

## Why it matters

Scheduled tasks and startup registry keys can identify programs configured to execute at logon or on a schedule. Presence alone is not a maliciousness determination.

## Scheduled task definitions

```powershell
Get-ScheduledTask |
  Select-Object TaskPath, TaskName, State

Get-ScheduledTask |
  Select-Object TaskPath, TaskName, Actions, Triggers
```

## Common startup registry keys

```powershell
$RunLocations = @(
  'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run',
  'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce',
  'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run',
  'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce'
)
foreach ($Path in $RunLocations) {
  if (Test-Path -LiteralPath $Path) {
    Get-ItemProperty -LiteralPath $Path
  }
}
```

## Common startup folder locations

```powershell
Get-ChildItem "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup" -Force -ErrorAction SilentlyContinue
Get-ChildItem "$env:ProgramData\Microsoft\Windows\Start Menu\Programs\Startup" -Force -ErrorAction SilentlyContinue
```

## Cautions

- `HKCU` and `$env:APPDATA` represent the **collector's current account**, not every system user.
- These commands cover **selected persistence surfaces**, not WMI event subscriptions, services, extensions, or all autoruns.
- Task properties can contain arguments/credentials; use approved storage. No entries or denied access do not establish absence of persistence.
- Do not modify, disable, or delete entries during collection unless containment authority requires it.

## Official reference

[Microsoft — Get-ScheduledTask](https://learn.microsoft.com/en-us/powershell/module/scheduledtasks/get-scheduledtask)

[Back to Windows snippets](README.md)
