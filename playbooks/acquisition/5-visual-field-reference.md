# Rapid Collection — Visual Field Reference

**Use case:** triage | acquisition | response  
**Environment:** windows | linux | macos  
**Risk:** caution

> The diagrams illustrate *authorized* collection priorities. They do not override safety, legal scope, containment requirements, or local evidence SOPs.

## Live-to-dead-box flow

```mermaid
flowchart TD
    A["Confirm authority & operational safety"] --> B["Photograph untouched device and record reference time"]
    B --> C{"Containment required immediately?"}
    C -- Yes --> D["Document decision and contain under approved IR procedure"]
    C -- No --> E["Capture prioritized volatile evidence"]
    D --> E
    E --> F["Preserve processes, sessions, network context"]
    F --> G["Export targeted logs and changing artifacts"]
    G --> H["Hash outputs and record collection notes"]
    H --> I{"Keep powered on?"}
    I -- Yes --> J["Transfer live custody and power instructions"]
    I -- No --> K["Review encryption access and shutdown authority"]
    K --> L["Document shutdown and dead-box handoff"]
```

**Interpretation:** Memory capture, live-system queries and containment can change order based on active destructive behavior, hardware stability, encryption, and incident severity. The diagram is not a strict stopwatch.

## Field-to-lab evidence lanes

```mermaid
flowchart LR
    subgraph F["FIELD — collect"]
      A["Photos & field notes"]
      B["Memory image"]
      C["Log / artifact export"]
      D["Disk image"]
    end
    subgraph H["HANDOFF — protect"]
      E["Case ID + tool/version + UTC offset"]
      G["Hashes + restricted storage + custody"]
    end
    subgraph L["LAB — examine copies"]
      I["Validate intake"]
      J["Volatility 3 / MemProcFS"]
      K["EVTX / browser / registry parsers"]
      M["Image mounter / Autopsy"]
    end
    A --> E
    B --> E
    C --> E
    D --> E
    E --> G --> I
    I --> J
    I --> K
    I --> M
```

## Predeployment checks

- [ ] Camera/approved photography method and note forms ready.
- [ ] Separate tool USB and acquisition SSD tested.
- [ ] Power, correct adapters, and spare media accounted for.
- [ ] RAM capture tool works on representative systems; lab can read test output.
- [ ] Encryption/recovery escalation path available if device is unlocked.
- [ ] Collection hashes, errors, and handoff location documented.

## Quick navigation

- [Rapid evidence collection procedure](0-rapid-evidence-collection.md)
- [Collection bag](2-collection-bag-checklist.md)
- [Field-to-lab tool matrix](4-field-to-lab-tool-matrix.md)
- [Windows collection commands](../../snippets/powershell/README.md)
- [Visual style](../../docs/visual-style.md)
