# Windows — Live Network State

**Use case:** triage | response  
**Environment:** windows  
**Risk:** safe

## When to use
Before shutdown or network changes where possible, subject to incident containment and authorization.

## PowerShell (read-only)

```powershell
Get-NetIPConfiguration
Get-NetTCPConnection |
  Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State, OwningProcess |
  Sort-Object OwningProcess, LocalAddress, LocalPort
Get-NetUDPEndpoint |
  Select-Object LocalAddress, LocalPort, OwningProcess
Get-NetRoute |
  Select-Object DestinationPrefix, NextHop, InterfaceAlias, RouteMetric
Get-NetNeighbor |
  Select-Object InterfaceAlias, IPAddress, LinkLayerAddress, State
Get-DnsClientCache |
  Select-Object Entry, RecordName, RecordType, Data, Status
```

## Expected output
Current interfaces, TCP connections, UDP listeners, route and neighbor information, and cached DNS entries.

## Collection cautions
Administrator privileges may be needed for complete results. UDP endpoints are not a connection log. DNS caches may be empty; these commands do not prove exfiltration. Record if EDR isolation, VPN changes, or disconnected interfaces occurred before collection.
