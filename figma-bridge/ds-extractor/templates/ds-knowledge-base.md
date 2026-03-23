# Design System: [Nom]

> Source: Figma file `[file_key]` — Extracted [date]

## Color Tokens

| Token | Value | Usage | Context |
|-------|-------|-------|---------|
| primary/500 | #... | CTA buttons, links | Use sparingly |

## Typography Scale

| Style | Font | Size | Weight | Usage |
|-------|------|------|--------|-------|
| heading/h1 | Inter | 32 | Bold | Page titles |

## Spacing Scale

| Token | Value | Usage |
|-------|-------|-------|
| spacing/sm | 8px | Inner padding |

## Components

### Button
- **Variants**: primary, secondary, ghost, danger
- **Required props**: label (string), size (sm | md | lg)
- **Rules**: Max 1 primary button per view
- **Component key**: `abc123`

### Card
- **Variants**: default, elevated, outlined
- **Required props**: title
- **Rules**: Always use within a grid layout
- **Component key**: `def456`

## Layout Patterns

- Grid: 12 columns, 24px gutter
- Max content width: 1200px
- Sidebar width: 280px

## Naming Conventions

- Frames: PascalCase (e.g., `UserProfile`)
- Layers: camelCase (e.g., `headerIcon`)
- Auto-layout frames: suffix with `-row` or `-col`

## Anti-patterns (DO NOT)

- Never use raw hex colors — always use design tokens
- Never nest more than 3 levels of auto-layout
- Never use absolute positioning inside auto-layout frames
- Never create one-off text styles — use the typography scale
