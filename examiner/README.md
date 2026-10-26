# Forensic Examiner Toolkit

**Use case:** acquisition | analysis | verification | response  
**Environment:** windows | linux | macos | mobile  
**Risk:** caution

> **For trained and authorized examiners.** Choose the investigative objective, document authority and scope, and record any unavoidable changes to live evidence.

## Start an examination

<div class="hash-cards">
  <a class="hash-card" href="#/playbooks/acquisition/0-rapid-evidence-collection.md"><span class="hash-card-icon" aria-hidden="true">◇</span><strong>Rapid evidence collection</strong><span>Order of volatility, live capture decisions, encryption considerations, hashing, and handoff.</span><em>Open playbook →</em></a>
  <a class="hash-card" href="#/docs/windows/README.md"><span class="hash-card-icon" aria-hidden="true">▣</span><strong>Windows Execution Investigation</strong><span>Prefetch, Amcache, Security 4688 and Sysmon correlation, with synthetic output, validated tool options, and defensible findings.</span><em>Open Windows examiner →</em></a>
  <a class="hash-card" href="#/snippets/powershell/README.md"><span class="hash-card-icon" aria-hidden="true">⌘</span><strong>Windows quick commands</strong><span>Host baseline, processes, network state, sessions, event-log export, and SHA-256.</span><em>Open snippets →</em></a>
  <a class="hash-card" href="#/playbooks/acquisition/4-field-to-lab-tool-matrix.md"><span class="hash-card-icon" aria-hidden="true">▤</span><strong>Field-to-lab tool matrix</strong><span>Which utilities acquire specific evidence and which lab tools can analyze the result.</span><em>Browse tools →</em></a>
  <a class="hash-card" href="#/playbooks/suspicious-email/phishing-email-investigation.md"><span class="hash-card-icon" aria-hidden="true">✉</span><strong>Phishing investigation</strong><span>User reporting, evidence preservation, header limitations, scope, and containment.</span><em>Open playbook →</em></a>
</div>

**Critical before shutdown:** [BitLocker volume state and existing recovery password reference](../snippets/powershell/bitlocker-recovery-readiness.md). Protect any recovery credential in approved key storage.

## Frequently used references

- [Windows execution evidence and intrusion timeline hub](../docs/windows/README.md)
- [Prefetch / Amcache / execution interpretation](../docs/windows/execution.md)
- [Worked PID-to-network intrusion investigation](../docs/windows/timelines.md)

- [Collection software checklist](../playbooks/acquisition/3-collection-software-checklist.md)
- [Volatility command notes](../docs/tools/volatility/useful-commands.md)
- [FTK Imager from USB](../docs/tools/ftk/ftk-imager-usb-runtime.md)
- [Hashing reference](../docs/hashing/README.md)
- [Acquisition visual workflow](../playbooks/acquisition/5-visual-field-reference.md)
- [Defensive OSINT reference](../osint/README.md)

**Cloud evidence referral:** When a cloud account or provider record is reported, the [Field Collector cloud-preservation guide](../collector/cloud-preservation.md) describes the account identifiers, provider/custodian routing, expiry/renewal tracking and preservation status that should accompany the handoff. Actual acquisition and legal process remain examiner/counsel-controlled.

## A shared evidence journey

If an evidence item arrives from a field collector, review the [collector handoff checklist](../collector/evidence-handoff.md) to understand its original condition, interventions, custody and urgent risks. For storage or video evidence, also review the [removable media preservation guide](../collector/removable-media.md) or [CCTV/cloud-video preservation guide](../collector/video-preservation.md) to understand what the collector was instructed to document.

[← Choose a different role](/)
