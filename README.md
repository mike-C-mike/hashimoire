# Hashimoire

**Hashimoire** is a practical DFIR and defensive security field reference for tool notes, playbooks, artifact paths, snippets, detections, templates, scripts, and repeatable workflows.

It is not meant to be a polished textbook or a copy of tool `--help` output. It is a working knowledge base for the commands, procedures, reminders, and documentation habits that are useful when time matters.

The name is intentionally a little weird.

A grimoire is a book of collected knowledge, formulas, instructions, and working notes. Hashimoire applies that idea to digital forensics and defensive security: hashes, artifacts, commands, triage notes, tool references, detections, templates, and field-tested reminders.

## What This Is

Hashimoire is a living reference for authorized defensive work, including:

- DFIR triage notes
- Evidence handling habits
- Tool installation and usage notes
- Common command patterns
- Hashing references
- Windows, Linux, and macOS notes
- Detection and hunting queries
- SIEM-focused tuning notes
- Defensive OSINT and exposure checks
- Templates and checklists
- Repeatable workflows
- Scripts and small helpers

The goal is to build something practical enough to use, not something that only looks impressive in a README.

## What This Is Not

Hashimoire is not a hacking tutorial.

It is not:

- exploit development
- credential theft
- stealth guidance
- evasion guidance
- persistence guidance
- unauthorized access guidance
- “how to break in” material
- case-specific or sensitive content

This repo does not contain client data, internal system details, confidential case information, protected personal information, or anything that would be inappropriate to publish.

The working rule is simple:

> If a note would primarily help someone harm people, bypass authorization, misuse access, or evade accountability, it does not belong here.

This project is for authorized, legal, ethical, defensive work.

## Core Principles

Hashimoire follows a few simple rules:

- Practical beats exhaustive.
- Notes should explain why a step matters, not just what to type.
- Commands should include context, assumptions, and expected output where possible.
- Evidence-related workflows should include documentation considerations.
- Dangerous techniques are framed defensively or excluded.
- Templates should make work more consistent, not create paperwork theater.
- If a workflow affects evidence, the documentation path matters as much as the tool output.

## How to Use This Repo

Use the repo by task type:

- Start with **snippets** for quick command refreshers.
- Use **playbooks** for repeatable workflows under time pressure.
- Use **docs** for deeper notes, install steps, gotchas, and artifact references.
- Use **detections** for hunting logic, SIEM queries, and tuning notes.
- Use **templates** for repeatable documentation and review checklists.
- Use **scripts** for small helpers that reduce repetitive work.

## Repo Structure

```text
hashimoire/
├─ docs/
│  ├─ evidence-workflows/
│  ├─ hashing/
│  ├─ tools/
│  ├─ windows/
│  ├─ linux/
│  ├─ macos/
│  ├─ mobile/
│  ├─ networking/
│  ├─ storage/
│  └─ reporting/
│
├─ playbooks/
│  ├─ triage/
│  ├─ acquisition/
│  ├─ suspicious-email/
│  ├─ endpoint-review/
│  ├─ account-compromise/
│  ├─ lost-device/
│  └─ evidence-handoff/
│
├─ snippets/
│  ├─ powershell/
│  ├─ bash/
│  ├─ python/
│  ├─ sqlite/
│  ├─ yara/
│  ├─ sigma/
│  └─ kql/
│
├─ detections/
│  ├─ sigma/
│  ├─ yara/
│  ├─ kql/
│  ├─ splunk/
│  └─ notes/
│
├─ osint/
│  ├─ exposure-checks/
│  ├─ username-checks/
│  ├─ domain-checks/
│  ├─ metadata-checks/
│  └─ safety-notes/
│
├─ templates/
│  ├─ acquisition/
│  ├─ chain-of-custody/
│  ├─ reporting/
│  ├─ intake/
│  └─ review-checklists/
│
├─ scripts/
│  ├─ hash-manifests/
│  ├─ folder-setup/
│  ├─ file-inventory/
│  └─ log-parsing/
│
└─ lab-notes/
   ├─ tool-installs/
   ├─ test-data/
   └─ validation-notes/

## Start here: acquisition and live-response reference

- [Acquisition playbooks](playbooks/acquisition/README.md) — collection sequence, field bag, software readiness and lab follow-on.
- [Windows collection snippets](snippets/powershell/README.md) — small, reusable PowerShell command references, with scope and output cautions.
