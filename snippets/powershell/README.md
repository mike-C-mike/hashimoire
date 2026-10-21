# PowerShell — Rapid Windows Collection Snippets

**Use case:** triage | response | validation  
**Environment:** windows  
**Risk:** caution

These are *read-only queries* unless a command explicitly exports a file. Run only on authorized systems. Commands may expose sensitive usernames, paths, IP addresses, and process arguments; save results to approved evidence media.

| Task | Snippet |
| --- | --- |
| Baseline and clock | [System identity and time](system-identity-time.md) |
| Live execution | [Processes and services](processes-services.md) |
| Current network state | [Connections, routes, and caches](network-state.md) |
| Signed-in activity | [Users and sessions](users-sessions.md) |
| Persistent records | [Windows event-log export](event-log-export.md) |
| Evidence integrity | [SHA-256 hashing](sha256-evidence.md) |

Use the [Rapid Evidence Collection Playbook](../../playbooks/acquisition/0-rapid-evidence-collection.md) for authorization, volatility priorities, RAM acquisition, and shutdown decisions. These snippets do **not** replace memory capture or disk imaging.
