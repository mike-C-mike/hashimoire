<!-- osint/domain-checks/README.md -->

# Domain Checks

This folder contains defensive domain and website exposure review notes.

Domain checks help identify public-facing configuration, ownership signals, DNS records, mail security posture, exposed public documents, stale subdomains, impersonation risk, and other public information that may create security, privacy, or trust issues.

This is not a penetration testing folder.

The focus is public, passive, authorized review.

## Purpose

Domain checks help answer questions like:

- What public DNS records exist for this domain?
- Are old or unused records still visible?
- Are mail security records configured?
- Are unnecessary subdomains exposed?
- Are public documents revealing too much?
- Are website pages exposing avoidable contact, staff, or technical information?
- Are there lookalike domains that could support phishing or impersonation?
- Does the domain support trust and verification?

## Appropriate Use Cases

Appropriate use cases include:

- reviewing your own website
- checking a project domain before launch
- reviewing a small business or nonprofit domain
- checking basic email authentication posture
- identifying stale DNS records
- reviewing public website exposure
- checking for obvious impersonation or lookalike domains
- documenting external footprint for an authorized security review

## Out of Scope

Do not use this folder for:

- unauthorized scanning
- exploitation
- brute forcing
- bypassing authentication
- accessing restricted paths
- vulnerability exploitation
- credential testing
- phishing
- harassment
- targeting unrelated domains

If the domain owner has not authorized the review, keep the work limited to ordinary public visibility checks.

## Folder Contents

- `domain-exposure-review.md`  
  A detailed workflow for reviewing public DNS, mail security records, website exposure, public documents, subdomains, and lookalike domain risk.

## Documentation Standard

For each domain review, capture:

```text
Domain:
Organization/project:
Reviewer:
Authorized by:
Date:
Purpose:
In scope:
Out of scope:
Allowed methods:
Disallowed methods:
Summary:
Findings:
Recommended actions:
Limitations: