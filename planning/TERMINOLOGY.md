# Editorial Terminology — Evidence Items, Artifacts, and Findings

**Audience:** Hashimoire authors, reviewers, and contributors  
**Purpose:** Consistent internal vocabulary across Field Collector, Examiner, snippets, and worked case examples  
**Adopted:** October 26, 2026  
**Status:** Editorial convention, **not** a new legal or forensic-science definition

> **Our working language:** We call the physical item or formally collected submission **Evidence** (preferably **Evidence Item** for clarity). The traces we discover by examining a device are **artifacts**. An artifact is a clue or observation to interpret and test against other sources—not a conclusion about what someone did. Artifacts help us investigate questions, form and revise hypotheses, and develop defensible findings.

**Important qualification:** This convention is how **Hashimoire writes**, not a claim that artifacts are legally incapable of being evidence. SWGDE defines *digital evidence* broadly as information with probative value in binary form and defines a computer-forensic *artifact* as device-created information/data reflecting past activity. A digital artifact **can have evidentiary value** and may be admitted or described as evidence in legal proceedings. Never state in a report or on the stand that an artifact is categorically “not evidence.” Use the terms below to make our **reasoning** unambiguous, not to override legal definitions.

## Preferred terms

| Use this term | What we mean within Hashimoire | What we avoid assuming |
| --- | --- | --- |
| **Evidence Item** | The **submitted or collected item** under custody: a phone, laptop, USB drive, removable storage device, or another specifically identified source. Also identify native provider productions and other acquired datasets accurately when they are submitted as evidence. | That everything stored on a device has been examined or is relevant. |
| **Acquisition / forensic image / exported dataset** | The collected logical/physical image or provider export, with its own identifier, scope, hash(es), tool/version and custody. This is distinct from the original physical item. | That a verified copy is necessarily complete or that hashing establishes provenance. |
| **Artifact** | Data/trace identified in examination: a Prefetch record, event-log entry, registry value, browser record, message database row, or file metadata. | That its presence alone proves execution, intent, ownership, attribution or another case conclusion. |
| **Observation** | What a specific artifact **actually contains or reports**, including source path, field, raw value, timestamp and the method used to interpret it. | That the reported field is independently true or that a parser is infallible. |
| **Hypothesis** | A **testable explanation or question** raised by observations, the case request or previous examination work. Hypotheses should be compared with alternatives and can change. | That an initial theory is a finding. |
| **Corroboration / contrary indication** | Another sufficiently independent source that supports, qualifies or challenges the proposed explanation. | That two tools reading the **same underlying database** constitute two independent corroborating sources. |
| **Finding** | A documented, reproducible determination **supported by identified observations and stated limits**. Some findings can come from one sufficiently reliable artifact; complex claims generally need more. | That every finding proves a crime or identifies a particular human actor. |
| **Opinion / conclusion** | A reasoned assessment permitted by agency policy, the examiner's expertise and the evidentiary support, including uncertainty/alternatives. | Overclaiming intent, identity, causation or definitive absence of activity. |

Use **record**, **trace**, or **artifact** when describing a specific recovered data element. Use **evidence** where it is appropriate under accepted legal/scientific usage; never rewrite quotations from standards or official evidence forms to match our house terminology.

## The reasoning model

```text
Collected Evidence Item
    ↓ acquisition with recorded scope, custody and integrity
Acquired Data / Working Copy
    ↓ examination and source validation
Artifacts
    ↓ accurately described fields, timestamps and limitations
Observations
    ↓ consider explanations; test, seek counterexamples
Hypothesis ↔ Further Artifacts / Corroboration / Contradictions
    ↓ assess what is actually supported
Finding / Conclusion
    ↓ clear report with source links, method and uncertainty
```

**This is iterative, not a one-way conveyor belt.** An investigative question can exist **before** examination. An artifact can overturn an earlier hypothesis. A single artifact may strongly support a narrow factual observation while remaining insufficient for a larger theory. We don't need to invent multiple artifacts to make a simple finding; we do need to distinguish the **scope of the claim** from the **strength of its support**.

### Worked example — fictional Windows intrusion

| Layer | Example | Appropriate wording |
| --- | --- | --- |
| Evidence Item | Agency-collected laptop, Item 004 | “I examined a forensic working copy acquired from Evidence Item 004.” |
| Artifact A | Security.evtx, Event 4688 | “An event records a PowerShell process created at the specified time.” |
| Artifact B | Sysmon Event 1 | “Sysmon records that process and attributes Word as the parent.” |
| Artifact C | Sysmon Event 3 | “Sysmon records a connection associated with that process's ProcessGuid.” |
| Artifact D | Prefetch entry | “The Prefetch artifact contains launch-related information consistent with PowerShell execution.” |
| Hypothesis | Word-initiated activity resulted in a network connection | “These artifacts raise the question whether document-driven execution caused the observed connection.” |
| Corroboration | ProcessGuid, start times and independent endpoint/network logs if available | “The records are consistent for host, process instance and collection interval.” |
| Finding | Supported process relationship/connection | “The examined records support that a PowerShell process, with Word reported as its parent, initiated a recorded outbound connection.” |
| Not established | Human identity, malicious purpose, data transferred | “These artifacts alone do not establish the operator, intent or exfiltration.” |

The point isn't that each artifact is meaningless in isolation. **Each artifact has a particular evidentiary reach**, and the examiner's reasoning should stay within that reach.

## Writing and courtroom-language examples

**Preferred (physical item):** “Evidence Item 004, a laptop, was submitted for examination. An acquired working copy was verified against the documented image integrity values.”

**Preferred (discovered artifact):** “During examination of Item 004, I identified a Windows Security event-log artifact. The record reports the creation of a process at the specified timestamp.”

**Preferred (hypothesis):** “That observation raised the hypothesis that the document application initiated the scripting process. I examined available process creation, Prefetch and network records to test it.”

**Preferred (finding):** “The available records are consistent with the reported process relationship and outbound connection. The source logs, timestamps and exceptions are identified in the examination notes.”

**Avoid:** “I found an artifact that proves the subject ran malware and stole files.”

**Avoid:** “Artifacts are never evidence in court.” This is scientifically and legally too absolute, and conflicts with established broad definitions of digital evidence.

**Avoid:** “Three tools confirmed it” when they all parsed **the same raw event**. Name the underlying sources, not just the tools.

**Avoid:** “No artifacts were found, therefore the activity did not occur.” Absence may reflect coverage, retention, collection scope, privilege, application configuration, parsing or artifact lifecycle.

## A standard artifact-to-finding note

```text
Evidence Item ID / collected source:
Acquisition/working copy ID, method and hash scope:
Question / scope / initial hypothesis:
Artifact name and exact source path / record identifier:
Original observed data (field names, raw values, native timestamp):
Parser or examination method and tool/version:
Interpretation, with OS/app-version and time-zone assumptions:
Other independent sources checked:
Supporting artifacts or observations:
Conflicting, missing or unavailable material:
Alternative explanations considered:
Hypothesis supported / weakened / unresolved:
Finding (limited to supported facts):
Confidence and known limitations:
Exhibit/output IDs, custody and reviewer:
```

For public examples, all case/item numbers, IDs, account information and outputs must be **synthetic**, explicitly labeled as such.

## Editorial rules for new and revised articles

1. Say **Evidence Item** when referring to the collected/submitted source. Distinguish the physical original from the forensic image and from a derived report.
2. Call individual traces **artifacts** and describe their **observed content** before interpreting what they mean.
3. Organize by **investigative question**, not by a shopping list of artifacts. Each artifact page should specify both useful inferences and unsupported claims.
4. Present hypotheses as **testable and revisable**; include reasonable alternative explanations, contradictions and missing sources.
5. Don't turn a parser field into a courtroom conclusion without addressing source integrity, version, clock, retention, acquisition scope and corroboration.
6. Differentiate **observed**, **consistent with**, **supports**, **cannot determine** and **concluded**; avoid `proves` unless the precise claim and its basis justify it.
7. Acknowledge that **an artifact may be digital evidence** in the established scientific/legal sense. The house distinction clarifies analysis and custody; it **does not** redefine admissibility.
8. Follow agency procedures, current SWGDE best practices and court/jurisdiction terminology where those requirements differ. Do not rewrite statutory terms or standard quotations.

## Published references

- [SWGDE Digital & Multimedia Evidence Glossary, 05-F-001](https://www.swgde.org/documents/published-complete-listing/05-f-001-swgde-digital-multimedia-evidence-glossary/) — official meanings of *artifact*, *digital evidence*, *examination* and related terms. Check the currently published revision before relying on a quoted definition.
- [SWGDE Best Practices for Computer Forensic Examinations, 18-F-001-2.0 (2025)](https://www.swgde.org/documents/published-complete-listing/18-f-001-2/) — data analysis, interpretation of recovered material, reproducible/defensible methods, and conclusions supported by the data.
- [SWGDE Requirements for Report Writing in Digital and Multimedia Forensics, 18-Q-002-1.0 (2018)](https://www.swgde.org/documents/published-complete-listing/18-q-002-swgde-requirements-for-report-writing-in-digital-and-multimedia-forensics/) — clear results, source/item identification, documentation, and bases for included opinions/conclusions.

**Source review date:** October 26, 2026. These sources support disciplined terminology and reporting; the particular **Evidence Item / Artifact** separation in this guide is **Hashimoire's chosen editorial convention**, not a rule SWGDE requires of every examiner.

[Architecture and publication standards](ARCHITECTURE.md) · [Windows investigation example](../docs/windows/timelines.md) · [Examiner Toolkit](../examiner/README.md)
