# OSINT Safety Boundaries — Authorized Public-Source Work

**Use case:** public-source verification | defensive research | incident intake  
**Risk:** caution

## Guiding rule

**Collect only what is necessary to answer an authorized question, from methods the reviewer is allowed to use.** Publicly visible does not always mean appropriate to retain or redistribute.

## 1. Confirm a lawful, proportionate purpose

Before browsing, record the permitted scope, requested output, and any policy/law constraints. For law-enforcement or regulated environments, comply with agency approval, applicable privacy, data handling and disclosure rules. This page is a general reference, not legal advice.

**In-scope examples:** auditing a domain you operate, reviewing public documents your organization released, verifying an organization's public profiles, reducing personal exposure with consent.

**Out-of-scope without additional authority:** accessing restricted accounts, bypassing controls, private-group infiltration, phishing, credential testing, manipulating subjects, or indiscriminate profiling.

## 2. Avoid subject engagement

Ordinary passive/public review is usually safer than attempting contact. Unless separately approved, **do not**:

- Message suspicious users or suspected impersonators.
- Pose as another person or create deceptive accounts.
- Request access to private groups or accounts.
- Attempt password resets or sign-in tests.
- Contact family members, schools, employers, or unrelated third parties.
- Encourage a target to reveal information or click a link.

Engagement can contaminate evidence, signal the investigation, create safety concerns, or exceed scope.

## 3. Data minimization

Record only relevant URLs, times, observations and the least personal detail needed to explain a finding. Avoid copying full personal identifiers into ordinary reports when a partial/redacted description is sufficient. Restrict screenshots and exports according to sensitivity and retention policy.

**Never put** case materials, credentials, personal information, protected student records or CJI in Hashimoire or any public issue tracker.

## 4. Distinguish evidence from inference

| Direct observation | Inference requiring corroboration |
| --- | --- |
| A page states a handle | That a person controls the account |
| A DNS record resolves to an IP | That the current host is owned/operated by the domain owner |
| A document contains an author field | That the named person actually authored the content |
| A matching profile picture appears | That two accounts have the same owner |

Record alternative explanations and confidence; never silently promote a *possible* association to a *confirmed* one.

## 5. Preserve context and avoid overcollection

For a relevant public page, note:

```text
Review ID and authority:
Exact public URL:
Access date/time/timezone:
What was visibly observed:
Whether logged in (and under what authorized account):
Screenshots / saved pages and protected location:
Confidence and alternatives:
Privacy minimization decisions:
Retention or deletion schedule:
```

Web pages and search results change. A saved screenshot shows an observed page state, **not independent authentication of its truth**.

## 6. Stop or escalate

Stop and seek approved direction if the review exposes apparent immediate risk, exploitation involving minors, private credentials, an active safety incident, restricted information, or a requirement for direct engagement. Preserve within authorized channels; do not circulate sensitive material in a public repository.

## 7. Completion check

- [ ] Objective answered or clearly marked unresolved.
- [ ] Sources and observation times retained in approved storage.
- [ ] Findings separate fact, inference, and confidence.
- [ ] Recommendations reduce risk instead of increasing exposure.
- [ ] Personal data retention and handling are justified.

[OSINT home](../README.md) · [Personal exposure workflow](../exposure-checks/personal-exposure-review.md)
