# Windows — Logged-On Users and Sessions

**Use case:** triage | response  
**Environment:** windows  
**Risk:** safe

## PowerShell / Windows commands (read-only)

```powershell
whoami /all
quser
Get-CimInstance Win32_LogonSession |
  Select-Object LogonId, LogonType, StartTime |
  Sort-Object StartTime
Get-SmbMapping | Select-Object LocalPath, RemotePath, Status
```

## Expected output
Collector account's current token/groups, interactive or RDP sessions where available, logged-on session records, and mapped SMB paths.

## Collection cautions
`quser` may show only some sessions or return no data; `Win32_LogonSession` includes service/background logons and does not directly identify the person at the keyboard. `Get-SmbMapping` shows the calling context, not every user's mappings. Record command errors and privilege context rather than guessing what absent entries imply.
