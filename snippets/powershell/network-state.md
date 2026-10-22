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

## Example output — synthetic lab scenario

Example from `Get-NetTCPConnection`, using documentation-only IP addresses:

```text
LocalAddress  LocalPort RemoteAddress  RemotePort State       OwningProcess
------------  --------- -------------  ---------- ----------- -------------
10.20.30.15   49781     203.0.113.44   443        Established 6128
0.0.0.0       3389      0.0.0.0         0          Listen      1324
```

### How to read it

- **LocalAddress / LocalPort:** endpoint and temporary or listening port on the examined system. `49781` is an example ephemeral client port; `3389` is commonly used for RDP, but check service configuration.
- **RemoteAddress / RemotePort:** the opposite endpoint. `203.0.113.44` is an illustrative, reserved documentation address; `443` frequently carries HTTPS/TLS, but the port number **does not establish protocol or content**.
- **State:** `Established` means the TCP session was connected at collection time; `Listen` means the host was awaiting connections.
- **OwningProcess:** the process ID (**PID**) associated with the socket.

### Investigative correlation: PID 6128

To check which **current** process owns a connection:

```powershell
Get-NetTCPConnection -OwningProcess 6128 |
  Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State, OwningProcess

Get-CimInstance Win32_Process -Filter 'ProcessId = 6128' |
  Select-Object ProcessId, ParentProcessId, Name, CreationDate, ExecutablePath, CommandLine
```

For this **hypothetical** incident, PID **6128** could match the PowerShell process in the [process-tree example](processes-services.md). Its PPID may lead back to an application that launched it. Correlate with firewall/proxy/DNS data, logons, EDR and process creation times. A network socket is not proof of exfiltration, and **PID reuse** means timing is essential.

## Collection cautions
Administrator privileges may be needed for complete results. UDP endpoints are not a connection log. DNS caches may be empty; these commands do not prove exfiltration. Record if EDR isolation, VPN changes, or disconnected interfaces occurred before collection.
