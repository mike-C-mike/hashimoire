# Windows — Running Processes and Services

**Use case:** triage | response  
**Environment:** windows  
**Risk:** safe

## When to use
While the endpoint is still live, after confirming scope and deciding whether memory acquisition is warranted. This snapshot is not a RAM image.

## PowerShell (read-only)

```powershell
Get-CimInstance Win32_Process |
  Select-Object ProcessId, ParentProcessId, Name, ExecutablePath, CommandLine, CreationDate |
  Sort-Object ProcessId

Get-CimInstance Win32_Service |
  Select-Object Name, DisplayName, State, StartMode, ProcessId, PathName |
  Sort-Object Name
```

## Expected output
Running process identifiers and parent identifiers; execution paths and command lines when accessible; service status/start behavior and binary paths.

## Collection cautions
Command lines can contain credentials, tokens, and personal information—restrict output access. Missing fields can reflect privileges, protected processes, or provider limitations. Queries may cause minor live-state changes. Note whether PowerShell was elevated and use the same collection window as related network/session snapshots.
