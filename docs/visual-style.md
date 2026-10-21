# Hashimoire Visual Style

**Use case:** documentation | navigation  
**Environment:** github markdown  
**Risk:** safe

Hashimoire's visual identity is inspired by its existing **black, forest-green, emerald glow, and antique-gold grimoire artwork**. Use visuals to explain investigation workflows—not merely decorate pages.

## Working palette

| Role | Hex | Use |
| --- | --- | --- |
| Obsidian | `#0B0F0B` | Dark illustration backgrounds |
| Forest | `#14241A` | Diagram panels |
| Emerald | `#315D36` | Paths and accents |
| Arcane glow | `#78A65D` | Active/high-priority nodes |
| Antique gold | `#C8B88A` | Evidence milestones and headings |
| Off-white | `#F4F2E8` | Dark-background label text |

These are *working approximations* based on the current artwork, not a brand-standard color extraction.

## GitHub-specific rules

- Use **Mermaid** for editable process and decision diagrams; GitHub renders it natively.
- Favor GitHub's theme-aware Mermaid defaults over hard-coded dark backgrounds so diagrams remain readable in light and dark modes.
- For PNG/SVG illustrations, ensure text contrast, use descriptive alt text, and keep file sizes moderate.
- Keep command reference pages predominantly text and code. Diagrams belong near workflow decision points.
- Do not place real case identifiers, sensitive screens, keys, or evidentiary material in public illustrations.
- Prefer relative links and repository-hosted media over brittle third-party image URLs.

## Visual hierarchy

1. Section title and use-case tags.
2. One purposeful diagram or field reference when it reduces ambiguity.
3. Operational checklist and precise commands.
4. Validation / limitations / links to the next action.

The existing website hero image is the primary artistic reference; this document governs supporting Markdown visuals.
