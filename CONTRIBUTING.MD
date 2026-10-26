# Contributing to Hashimoire

Hashimoire is primarily a personal DFIR and defensive security field reference, but corrections, improvements, and defensive-use additions are welcome.

The goal is practical value: notes, workflows, snippets, templates, detections, and scripts that help authorized security and digital evidence work become clearer, safer, and more repeatable.

## Before You Contribute

Please keep the project scope in mind.

Hashimoire is for:

- digital forensics
- defensive security
- evidence workflows
- documentation templates
- tool notes
- triage references
- detection and hunting logic
- defensive OSINT
- repeatable workflows
- small helper scripts

Hashimoire is not for:

- exploit development
- credential theft
- stealth or evasion
- persistence guidance
- unauthorized access
- malware deployment
- destructive activity
- case-specific details
- sensitive internal information

If a contribution would primarily help someone harm people, bypass authorization, misuse access, or evade accountability, it does not belong here.

## Good Contributions

Useful contributions include:

- fixing inaccurate commands
- adding context to a snippet
- documenting expected output
- adding safety or scope warnings
- improving a workflow
- adding a defensive detection note
- adding a template field that improves documentation
- correcting broken links
- clarifying tool version assumptions
- improving readability
- adding evidence-handling considerations

## Terminology and examiner reasoning

Use Hashimoire's [internal writing convention](planning/TERMINOLOGY.md) consistently:

- **Evidence** (capital E): a formally collected/submitted physical item or digital dataset; distinguish the original from forensic images and exports.
- **artifact**: a discovered digital trace (log record, registry entry, message row, file metadata).
- **evidence** (lowercase e): the support that observations provide **for or against** a proposition; it is not automatically conclusive proof or criminal wrongdoing.

An investigation begins with a **question and scope, not the conclusion we hope to prove**. Let artifacts suggest hypotheses, then actively search for competing explanations and disconfirming observations. Record inconclusive or exculpatory results without burying them.

These are editorial conventions—not universally prescribed legal definitions. A digital artifact may itself be evidence under accepted legal and scientific usage. Use the correct statutory/agency terminology where required.

## Quality Bar

A good note should answer as many of these as practical:

- What is this for?
- When would I use it?
- What environment does it apply to?
- What permissions or scope are required?
- What command, query, artifact, or workflow matters?
- What output should I expect?
- What could go wrong?
- What should be documented?

Short contributions are fine. Practical clarity matters more than length.

## Formatting

Use Markdown.

Prefer this basic structure for notes:

```markdown
# Title

## Purpose

What this note helps with.

## Scope

Where this applies and what assumptions it makes.

## Notes / Workflow / Commands

The actual reference material.

## Expected Output

What a user should expect to see, where applicable.

## Cautions

Permissions, impact, limitations, or gotchas.

## Documentation Notes

What should be recorded if this is used in an evidence or security workflow.
```

For analysis pieces, link the [Evidence/artifact/evidence terminology guide](planning/TERMINOLOGY.md) and include a short **alternative explanations / contradictory observations** section when factual interpretation could be contested.
