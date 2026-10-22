# Domain Checks — Public-Facing Exposure

**Purpose:** Review an authorized domain's public DNS, email authentication, public web footprint and impersonation exposure without testing private systems.

## Start the review

**[Open the complete Domain Exposure Review →](domain-exposure-review.md)**

You will learn how to:

1. Set the exact authorized domain and permitted methods.
2. Query common DNS records with `Resolve-DnsName` or `dig`.
3. Recognize public MX, SPF, DMARC and CAA records and their limits.
4. Compare public records with the owner's intended service inventory.
5. Record an observation, supporting timestamp and concrete remediation question.

### A quick example

```powershell
Resolve-DnsName example.org -Type MX
Resolve-DnsName _dmarc.example.org -Type TXT
```

**What it establishes:** what DNS data a resolver returned at collection time. It does **not** prove that mail service is secure or that all published endpoints are still in use.

**Output:** a scoped inventory and owner-confirmed action list, not a vulnerability-scan report.

[OSINT home](../README.md) · [Safety boundaries](../safety-notes/osint-safety-boundaries.md)
