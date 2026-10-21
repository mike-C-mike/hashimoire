# Windows — Export Relevant Event Logs

**Use case:** response | acquisition  
**Environment:** windows  
**Risk:** caution

## When to use
After preserving higher-volatility state, or earlier if logs may rotate. Set a case-specific, preapproved destination on an **external acquisition SSD** (not the source disk). Coordinate with incident response before touching sensitive logs.

## PowerShell (writes to destination)

```powershell
$Out = 'E:\CASE-EXAMPLE\logs'  # CHANGE to approved evidence destination
New-Item -ItemType Directory -Path $Out -Force | Out-Null

$Channels = @('System', 'Application', 'Security',
              'Microsoft-Windows-PowerShell/Operational')
foreach ($Channel in $Channels) {
    $FileName = ($Channel -replace '[\\/]', '_') + '.evtx'
    wevtutil epl "$Channel" (Join-Path $Out $FileName)
}
Get-ChildItem $Out -Filter '*.evtx' |
  Get-FileHash -Algorithm SHA256 |
  Export-Csv (Join-Path $Out 'event-log-sha256.csv') -NoTypeInformation
```

## Expected output
Exported `.evtx` files and a SHA-256 manifest in the specified evidence directory.

## Collection cautions
The example uses `E:` only as a **placeholder**. Validate drive letter and free space before execution; `New-Item` and exports change the destination. Some channels are absent, inaccessible, or require elevation; errors must be logged, not silently ignored. EVTX exports are a snapshot of available events, not proof all historical events survived retention or tampering. Keep logs restricted because they may contain personal or credential-adjacent data.
