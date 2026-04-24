# PM Toolkit

Product Management knowledge base and portable skills for Claude Code.

## Project Structure

```
product-management/
├── CLAUDE.md                          # Project identity & Galigeo context
├── README.md                          # This file
│
├── .claude/skills/                    # All skills (auto-routed by Claude Code)
│   ├── pm-help/                       # List skills, orient user
│   ├── pm-discovery/                  # Interview synthesis, JTBD, feedback
│   ├── pm-strategy/                   # Strategy, roadmap, ROI, PRDs
│   ├── pm-execution/                  # Specs, acceptance criteria, handoff
│   ├── pm-communications/             # Meetings, updates, release notes
│   ├── pm-data-analytics/             # SQL, reports, dashboards
│   ├── pm-revenue/                    # Revenue architecture, PLG↔SLG, bowtie WbD
│   ├── design-sprint/                 # Multi-day design workflow, framing
│   ├── design-ia/                     # IA, flows, mental models, hiérarchie
│   ├── design-craft/                  # Visual craft: typo, color, spacing, motion
│   ├── design-system/                 # Tokens, components, DESIGN.md, handoff
│   ├── design-review/                 # Critique, heuristic eval, a11y, quality gate
│   ├── design-psychology/             # 106 biais, Hook Model, persuasion éthique
│   ├── bmad-*/                        # BMAD framework skills
│   └── figma-use/                     # Figma MCP integration
│
├── knowledge/                         # Deep reference, loaded on demand
│   ├── design/                        # 15 fiches distillées + 5 fiches biais
│   │   └── psychology/                # Growth.design biases (info/meaning/time/memory)
│   ├── pm-course/                     # PM training modules (Carl Vellotti)
│   └── revenue/                       # Leadership du revenu (Collective Impact)
│
├── galigeo/                           # Company-specific context
├── docs/                              # Project documents & feature specs
├── _bmad/                             # BMAD framework (v6.3.0)
├── figma-bridge/                      # Figma MCP server & plugin
└── bmad_output/                       # BMAD-generated artifacts
```

## Architecture

```
┌─────────────────────────────────────────────────┐
│  CLAUDE.md — Context Layer                      │
│  Company identity, personas, glossary           │
│  Project-specific, not portable                 │
├─────────────────────────────────────────────────┤
│  .claude/skills/{pm,design}-* — Action Layer    │
│  Templates, workflows, slash commands           │
│  Portable: symlinked to ~/.claude/skills/       │
├─────────────────────────────────────────────────┤
│  knowledge/design/ — Depth Layer                │
│  15 distilled design fiches + 106 biases        │
│  Loaded on demand by skills                     │
└─────────────────────────────────────────────────┘
```

## PM Skills

Run `/pm-help` to see all skills and the decision tree.

| Command | Purpose |
|---------|---------|
| `/pm-help` | List all skills, orient on which to use |
| `/pm-discovery` | Interview synthesis, JTBD, feedback triage |
| `/pm-strategy` | Strategy docs, roadmap, ROI, PRDs, KPIs |
| `/pm-execution` | Feature specs, acceptance criteria, engineering handoff |
| `/pm-communications` | Meetings, updates, release notes, soft skills |
| `/pm-data-analytics` | SQL queries, reports, dashboards, data quality |
| `/pm-revenue` | Revenue architecture: PLG↔SLG, bowtie CR1-CR8, LTV/CAC/NRR, SPICED |

## Design Skills

6 skills ciblés pour un PM qui fait des maquettes et collabore avec un designer.

| Command | Purpose |
|---------|---------|
| `/design-sprint` | Cadrer plusieurs jours de design (framing → diverge → decide → prototype → test) + orchestration BMAD/ux |
| `/design-ia` | Information architecture, user flows, navigation, mental models, Nielsen heuristics |
| `/design-craft` | Visual craft : typo, color, spacing, hiérarchie visuelle, microinteractions, responsive |
| `/design-system` | Tokens, composants, naming, DESIGN.md handoff, versioning |
| `/design-review` | Heuristic evaluation, audit a11y, critique, pre-merge quality gate, tests légers |
| `/design-psychology` | 106 biais cognitifs, Hook Model, Fogg, persuasion éthique |

## BMAD Framework (v6.3.0)

Structured workflows for ideation, review, and document management.

| Command | Purpose |
|---------|---------|
| `/bmad-help` | Workflow guidance, next steps |
| `/bmad-brainstorming` | Interactive ideation sessions |
| `/bmad-party-mode` | Multi-agent discussions |
| `/bmad-editorial-review-prose` | Review text for clarity and tone |
| `/bmad-editorial-review-structure` | Propose document reorganization |
| `/bmad-review-adversarial-general` | Critical quality review |
| `/bmad-review-edge-case-hunter` | Exhaustive edge-case analysis |
| `/bmad-shard-doc` | Split large docs into smaller files |
| `/bmad-index-docs` | Generate doc index |
| `/bmad-distillator` | Lossless document compression |
| `/bmad-advanced-elicitation` | Deep critique (socratic, red team, etc.) |
| `/bmad-init` | Initialize/configure BMAD project |

Update: `npx bmad-method@next install`

## Using skills in another project

The PM + design skills are symlinked globally to `~/.claude/skills/` — they work in every project automatically.

To install manually in a specific project:

```bash
# Symlink all PM + design skills
for skill in /path/to/product-management/.claude/skills/{pm-*,design-*}; do
  ln -s "$skill" .claude/skills/$(basename "$skill")
done

# Optionally link the design knowledge base
ln -s /path/to/product-management/knowledge knowledge
```

Chaque skill est self-contained. Le `CLAUDE.md` du projet fournit le contexte métier — les skills sont de la méthodologie générique qui s'adapte à n'importe quel domaine.

## Figma Integration

Figma Bridge MCP server in `figma-bridge/`. Use `/figma-use` skill before any `use_figma` tool call.
