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

## Example output — synthetic lab system

```text
USERNAME      SESSIONNAME  ID  STATE    IDLE TIME  LOGON TIME
labuser       console       1  Active   none       10/21/2026 9:00 AM
responder     rdp-tcp#5     2  Active   none       10/21/2026 10:00 AM
```

### How an examiner reads this

- **SESSIONNAME** can help distinguish an interactive console session from an RDP session.
- **ID** is a Windows *session ID*, **not** the process ID (PID) of a program.
- **STATE** represents status at the time of the query, not who physically used the keyboard.
- **LOGON TIME** is a useful lead for correlating Security 4624 events and other authentication telemetry.

In an intrusion investigation, a session that appears to be remote is a starting point for questions about authorization and logon source; session inventory alone does **not** establish unauthorized access.

## Collection cautions
`quser` may show only some sessions or return no data; `Win32_LogonSession` includes service/background logons and does not directly identify the person at the keyboard. `Get-SmbMapping` shows the calling context, not every user's mappings. Record command errors and privilege context rather than guessing what absent entries imply.
