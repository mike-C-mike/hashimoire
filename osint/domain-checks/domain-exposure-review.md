# Domain Exposure Review — Defensive Workflow

**Use case:** authorized public footprint | DNS | email-domain posture  
**Risk:** caution · **Environment:** browser, Windows PowerShell/CMD, Linux/macOS terminal

## When to use

Use this for **a domain you own or have permission to review**. For unrelated domains, limit activity to ordinary public browsing and genuinely passive information. This is not vulnerability scanning.

## 1. Define scope

```text
Domain: example.org                 # illustrative documentation domain
Owner / authorizing party:
Purpose:
Review time (UTC):
In scope: public DNS, visible web pages, certificate transparency, public documents
Out of scope: login tests, brute force, host discovery scans, restricted resources
```

## 2. Identify public DNS records

Use any *one* of the following approaches. These are lookups, not host scans.

**Windows PowerShell:**

```powershell
Resolve-DnsName example.org -Type A
Resolve-DnsName example.org -Type MX
Resolve-DnsName example.org -Type TXT
Resolve-DnsName _dmarc.example.org -Type TXT
Resolve-DnsName example.org -Type CAA
```

**Linux/macOS (with dig installed):**

```bash
dig example.org A +noall +answer
dig example.org MX +noall +answer
dig example.org TXT +noall +answer
dig _dmarc.example.org TXT +noall +answer
dig example.org CAA +noall +answer
```

### Example output (invented — not a live lookup)

```text
example.org.       300 IN MX 10 mail.example.org.
example.org.       300 IN TXT "v=spf1 include:_spf.example.net -all"
_dmarc.example.org. 300 IN TXT "v=DMARC1; p=reject; rua=mailto:dmarc@example.org"
```

**What you are seeing:** The MX record identifies a nominated mail exchanger; the SPF TXT policy declares permitted sending infrastructure; DMARC sets a policy for mail that fails alignment checks. These are *configuration signals*, **not proof** that a domain cannot be spoofed or that all mail sent from it is legitimate. DKIM selectors cannot reliably be inventoried by guessing a universal selector; check the domain owner's mail-service configuration.

## 3. Review public web and service inventory

- Browse only pages the owner approved (or ordinary public pages if no special permission).
- Record visible contact details, document downloads, outdated services, unnecessary public information, and unwanted subdomain references.
- For **owner-authorized** DNS review, compare the published records with the owner's known-good service inventory. An unusual record is a **lead**; confirm whether it remains needed before recommending removal.
- Public certificate-transparency logs may indicate certificates associated with hostnames, but historical issuance does not establish that a service still exists.

## 4. Check impersonation exposure

- Review **a small set of relevant** visually similar domains or names through public search and appropriate registration information.
- Do not visit suspicious login pages with organizational credentials or submit forms.
- Document exact spelling, URL, visible claim, observation timestamp and why it merits owner review. Similarity alone does not establish malicious intent.

## 5. Create a defensible finding

```text
Finding: Legacy MX record may be unnecessary
Source: public DNS MX query, 2026-10-21 15:00 UTC (synthetic example)
Observed: MX points to mail.example.org
Owner inventory: email service retired; confirmation requested
Risk: potentially confusing or stale mail-routing configuration
Validation needed: verify production mail routing with domain owner
Action: review and remove only after owner approval
Confidence: provisional
```

## Common mistakes and limitations

- DNS caches and TTL values affect what different resolvers see; query time and resolver choice matter.
- SPF, DKIM and DMARC serve different purposes; don't describe them as interchangeable.
- An absent record does not always imply a vulnerability. Confirm service usage, authoritative answers and the owner's policy.
- Avoid treating a cached webpage as the current live version.
- Don't claim a hostname is vulnerable or exposed merely because it has a public DNS entry.

## References

- [Microsoft Resolve-DnsName](https://learn.microsoft.com/en-us/powershell/module/dnsclient/resolve-dnsname)
- [RFC 7489 — DMARC](https://www.rfc-editor.org/rfc/rfc7489)
- [RFC 7208 — SPF](https://www.rfc-editor.org/rfc/rfc7208)

[OSINT home](../README.md) · [Domain category](README.md) · [Safety limits](../safety-notes/osint-safety-boundaries.md)
