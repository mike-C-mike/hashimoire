# Windows — PowerShell Interactive History

**Use case:** triage | acquisition | validation  
**Environment:** windows  
**Risk:** caution

## Why it matters

PSReadLine history may record commands entered in an interactive console and help reconstruct relevant activity. It is **not a complete PowerShell execution log**.

## Inspect the current user history location

```powershell
(Get-PSReadLineOption).HistorySavePath
```

## Review recent recorded commands (current user only)

```powershell
$HistoryPath = (Get-PSReadLineOption).HistorySavePath
if (Test-Path -LiteralPath $HistoryPath) {
  Get-Content -LiteralPath $HistoryPath -Tail 50
}
```

## Find candidate history files for known profiles

```powershell
Get-ChildItem -Path 'C:\Users\*\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt' -Force -ErrorAction SilentlyContinue |
  Select-Object FullName, Length, LastWriteTimeUtc
```

## Important caveats

- Only interactive sessions with PSReadLine recording enabled are represented. Script and non-interactive execution may not appear.
- History can be incomplete, manipulated, or disabled; some commands may not be saved until session exit.
- History may include passwords or personal data. Avoid `Start-Transcript` or indiscriminate output capture that spreads secrets.
- Preserve the original in-scope history file and metadata to approved evidence media before detailed analysis, with tool and hash records.

## Official reference

[Microsoft — about_PSReadLine](https://learn.microsoft.com/en-us/powershell/module/psreadline/about/about_psreadline)

[Back to Windows snippets](README.md)
