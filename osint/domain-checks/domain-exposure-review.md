
```markdown
<!-- osint/domain-checks/domain-exposure-review.md -->

# Domain Exposure Review

## Purpose

This workflow is for reviewing the public exposure of a domain in a defensive, authorized, and low-impact way.

The goal is to understand what is visible from the outside and identify items that may need cleanup, confirmation, or monitoring.

This workflow is useful for:

- personal project domains
- small business domains
- nonprofit domains
- public safety or school-related websites
- professional portfolios
- newly launched websites
- domains being migrated from one platform to another

## Scope Template

Before beginning, document the scope.

```text
Domain:
Organization/project:
Reviewer:
Authorized by:
Date:
Purpose:

In scope:
- Public DNS records
- Public website pages
- Public documents
- Public search engine results
- Basic mail security records
- Known subdomains
- Lookalike domain review

Out of scope:
- Exploitation
- Login testing
- Password reset testing
- Private systems
- Aggressive scanning
- Bypassing access controls
- Contacting third parties without approval

Allowed methods:
- Browser review
- DNS lookup
- Public search
- Public website inspection
- Passive review

Disallowed methods:
- Exploitation
- Credential testing
- Brute force
- Evasion
- Social engineering

A:
Maps a hostname to an IPv4 address.

AAAA:
Maps a hostname to an IPv6 address.

CNAME:
Aliases one hostname to another.

MX:
Identifies mail servers for the domain.

TXT:
Stores text records. Often used for SPF, DKIM, DMARC, verification, and service ownership.

NS:
Identifies authoritative name servers.

CAA:
Identifies which certificate authorities may issue certificates for the domain.

Domain:
Record type:
Name:
Value:
Purpose:
Expected:
Risk:
Recommended action:

Domain: example.org
Record type: TXT
Name: example.org
Value: v=spf1 include:_spf.examplemail.com ~all
Purpose: SPF mail sender policy
Expected: Yes
Risk: Low
Recommended action: Confirm all included senders are still required.