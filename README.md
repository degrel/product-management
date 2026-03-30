# PM Toolkit — Galigeo

Product Management reference files for Galigeo's location intelligence platform.

## Reference Files

| File | Purpose |
|------|---------|
| `discovery.md` | User research, interview synthesis, JTBD, feedback analysis |
| `strategy.md` | Strategy docs, roadmap, scenario modeling |
| `ux-prototyping.md` | Wireframes, UX copy, design review |
| `execution.md` | Specs, acceptance criteria, edge cases |
| `communications.md` | Meeting notes, updates, release notes |
| `data-analytics.md` | SQL queries, data analysis, reports |
| `ai-ux-workflow.md` | AI-driven UX design pipeline (BMAD + /ux) |
| `pm-fundamentals.md` | PM glossary, career progression, tech stack, training resources |

## AI UX Workflow — Quick Start

### Daily use

Starting a new feature:
1. Write a PRD (use the Problem Brief template in Phase 1)
2. Run `/bmad-bmm-create-ux-design` with that PRD → BMAD generates mockups
3. Run `/ux review` on the mockups → catches a11y, touch targets, missing states
4. During implementation, run `/ux <topic>` for component guidance (e.g. `/ux forms` for a login page)
5. Before merge, run `/ux review` on the code → quality gate

### Quick decisions

Check the decision tree first:
- **Reversible** (button color, label)? → Just do it, `/ux topic` if unsure
- **Not reversible** (new navigation, info architecture)? → Full pipeline + user test

### Cheat sheet

| Building… | Run… |
|---|---|
| Forms | `/ux forms` |
| Mobile | `/ux mobile` |
| Components | `/ux components` |
| Navigation | `/ux navigation` |
| Accessibility | `/ux accessibility` |

### Example: login form

1. PRD exists? → check pm/ brief
2. BMAD spec? → `/bmad-bmm-create-ux-design`
3. Review mockup? → `/ux review _bmad-output/design-mockups/login.html`
4. Implementation? → `/ux forms` + `/ux accessibility`
5. Pre-merge? → `/ux review` on the PR files

The templates in each phase section of `ai-ux-workflow.md` are copy-paste ready — fill in the brackets and go.

## Config

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Claude Code project instructions |
| `SKILL.md` | Skill routing and workflow selection |

## Subfolders

| Folder | Purpose |
|--------|---------|
| `_bmad/` | BMAD Method framework (v6.0.0-Beta.8) — agents, templates, slash commands |
| `bmad_output/` | BMAD-generated artifacts (specs, mockups, PRDs) |
| `pm-course/` | Interactive Claude Code course for PMs (separate project) |
| `galigeo/` | Galigeo-specific context and domain files |
