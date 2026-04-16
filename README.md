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
│   ├── pm-ux/                         # Flows, wireframes, UX copy, review
│   ├── pm-communications/             # Meetings, updates, release notes
│   ├── pm-data-analytics/             # SQL, reports, dashboards
│   ├── pm-ai-ux/                      # AI-driven UX pipeline (BMAD + /ux)
│   ├── bmad-*/                        # BMAD framework skills (12 skills)
│   └── figma-use/                     # Figma MCP integration
│
├── knowledge/                         # Deep reference, loaded on demand
│   ├── ux-design/                     # UX psychology (106 biases), articles
│   │   ├── ux-psychology/             # Growth.design cognitive biases
│   │   └── ...                        # Progressive disclosure, etc.
│   └── pm-course/                     # PM training modules (Carl Vellotti)
│       └── course-materials/          # PRD writing, data analysis, strategy
│
├── references/                        # Quick-lookup files
│   ├── pm-fundamentals.md             # PM glossary, career, tech stack
│   └── claude-power-user-checklist.md # Claude Code power user checklist
│
├── galigeo/                           # Company-specific context
│   ├── 1-PLG.md                       # Product-led growth strategy
│   ├── Product-manager-Galigeo.md     # PM role at Galigeo
│   └── Produits et ICP.md             # Products & ideal customer profiles
│
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
│  .claude/skills/pm-* — Action Layer             │
│  Templates, workflows, slash commands           │
│  Portable: symlinked to ~/.claude/skills/       │
├─────────────────────────────────────────────────┤
│  knowledge/ — Depth Layer                       │
│  UX psychology, PM course, articles             │
│  Loaded on demand by skills                     │
├─────────────────────────────────────────────────┤
│  references/ — Quick Lookup Layer               │
│  Glossary, checklists                           │
│  Loaded on demand                               │
└─────────────────────────────────────────────────┘
```

## PM Skills

Run `/pm-help` to see all skills and a decision tree for which to use.

| Command | Purpose |
|---------|---------|
| `/pm-help` | List all PM skills, orient on which to use |
| `/pm-discovery` | Interview synthesis, JTBD, feedback triage |
| `/pm-strategy` | Strategy docs, roadmap, ROI, PRDs, KPIs |
| `/pm-execution` | Feature specs, acceptance criteria, engineering handoff |
| `/pm-ux` | User flows, wireframes, UX copy, design review, cognitive biases |
| `/pm-communications` | Meetings, updates, release notes, soft skills |
| `/pm-data-analytics` | SQL queries, reports, dashboards, data quality |
| `/pm-ai-ux` | AI-driven UX pipeline (BMAD + /ux), quality gates |

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

## Using PM skills in another project

The PM skills are already symlinked globally to `~/.claude/skills/` — they work in every project automatically.

To install manually in a specific project:

```bash
# Symlink all PM skills
for skill in /path/to/product-management/.claude/skills/pm-*; do
  ln -s "$skill" .claude/skills/$(basename "$skill")
done

# Optionally, link the knowledge base (for ux-psychology, pm-course refs)
ln -s /path/to/product-management/knowledge knowledge
```

Each skill is self-contained. Your project's own `CLAUDE.md` provides company context — the skills are generic PM methodology that adapts to any domain.

## Figma Integration

Figma Bridge MCP server in `figma-bridge/`. Use `/figma-use` skill before any `use_figma` tool call.
