# ux-psychology — Claude Code Plugin

106 cognitive biases & UX psychology principles from [Growth.design](https://growth.design/psychology), structured for use during UX design work in Claude Code.

## What it does

- **Auto-activates** when Claude detects UX design work (prototypes, wireframes, user flows, etc.)
- **Command `/ux-psychology`** for on-demand lookups by scenario or principle name
- **Lightweight context**: loads a compact index (~450 words), then fetches only the relevant category on demand

## Structure

```
ux-psychology/
├── .claude-plugin/plugin.json          # Plugin manifest
├── skills/ux-psychology/
│   ├── SKILL.md                        # Skill definition (~450 words)
│   ├── references/
│   │   ├── scenario-index.md           # Scenario → principles lookup (read first)
│   │   ├── information-biases.md       # 29 principles
│   │   ├── meaning-biases.md           # 32 principles
│   │   ├── time-biases.md              # 28 principles
│   │   └── memory-biases.md            # 17 principles
│   └── scripts/
│       └── extract_principles.py       # Regenerate references from JSON source
├── commands/ux-psychology.md           # /ux-psychology command
└── README.md
```

## Categories (based on Buster Benson's Cognitive Bias Codex)

| Category | Count | Focus |
|----------|-------|-------|
| Information | 29 | How users filter and perceive information |
| Meaning | 32 | How users interpret and give meaning to things |
| Time | 28 | How users make quick decisions under pressure |
| Memory | 17 | How users remember (and forget) experiences |

## Usage

```
/ux-psychology                    # Show available scenarios and categories
/ux-psychology onboarding         # Get principles for onboarding flows
/ux-psychology anchoring bias     # Deep dive into a specific principle
/ux-psychology pricing            # Principles for pricing page design
```

## Regenerating references

If the source JSON changes, regenerate the markdown files:

```bash
python3 skills/ux-psychology/scripts/extract_principles.py
```

Source: `../Mystery School - Make art not content/src/output/growth_design_psychology_parsed.json`

## Data source

All 106 principles come from [Growth.design Psychology](https://growth.design/psychology) — a curated collection of cognitive biases applied to product design.
