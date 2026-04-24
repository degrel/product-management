# Design Tokens

Les design tokens sont les valeurs atomiques (couleurs, espacements, typo, etc.) partagées entre design et dev.

## Architecture à 3 niveaux

```
┌─ Component tokens (usage scopé)
│   button-primary-bg
│   ↓
├─ Alias tokens (sémantique)
│   color-action-primary
│   ↓
└─ Global tokens (primitives)
    blue-500: #3B82F6
```

| Tier | Rôle | Qui le modifie |
|---|---|---|
| **Global** | Palette complète, valeurs brutes | Équipe DS uniquement |
| **Alias** | Sens métier | Équipe DS |
| **Component** | Usage précis dans un composant | Équipe DS, parfois équipe feature |

**Règle absolue** : aucun composant ne référence un global directement. Tout passe par un alias.

## Catégories

### Color
```yaml
# Global
gray-{50,100,200,300,400,500,600,700,800,900}
primary-{50..900}
red-{500,600}, green-{500,600}, amber-{500,600}, blue-{500,600}

# Alias
color-surface            # fond principal
color-surface-elevated   # cartes, modals
color-surface-alt        # banded rows, sections
color-text-primary
color-text-secondary
color-text-muted
color-text-on-primary    # sur fond primary
color-border
color-border-subtle
color-action-primary
color-action-primary-hover
color-state-success / warning / danger / info
color-focus-ring
```

### Spacing (base 4 px)
```yaml
space-{xs,sm,md,lg,xl,2xl,3xl,4xl}
# = 4, 8, 12, 16, 24, 32, 48, 64

# Alias sémantiques (Lyft-style)
space-inset-{sm,md,lg}      # padding interne
space-stack-{sm,md,lg}      # margin entre items empilés
space-inline-{sm,md,lg}     # gap horizontal
```

### Typography
```yaml
font-family-base: Inter, -apple-system, sans-serif
font-family-display: Inter
font-family-mono: ui-monospace, monospace

font-size-{xs,sm,base,lg,xl,2xl,3xl,4xl,5xl}
# = 12, 14, 16, 18, 20, 24, 30, 36, 48

font-weight-{regular,medium,semibold,bold}
# = 400, 500, 600, 700

line-height-{tight,normal,relaxed}
# = 1.2, 1.5, 1.75

letter-spacing-{tight,normal,wide}
```

### Radius
```yaml
radius-none: 0
radius-sm: 4
radius-md: 8
radius-lg: 12
radius-xl: 16
radius-full: 9999
```

### Elevation (shadow)
```yaml
elevation-0: none
elevation-1: 0 1px 2px rgba(0,0,0,0.05)
elevation-2: 0 2px 6px rgba(0,0,0,0.08)
elevation-3: 0 8px 16px rgba(0,0,0,0.10)
elevation-4: 0 16px 32px rgba(0,0,0,0.12)
z-index-{dropdown,sticky,overlay,modal,toast,tooltip}
```

### Motion
```yaml
duration-fast: 150ms
duration-normal: 200ms
duration-slow: 300ms
easing-ease-out: cubic-bezier(0, 0, 0.2, 1)
easing-ease-in-out: cubic-bezier(0.4, 0, 0.2, 1)
```

### Border
```yaml
border-width-{0,1,2,4}
border-style-{solid,dashed}
```

## Naming convention

Pattern : `{category}-{property}-{variant}-{state}`

Règles :
- **kebab-case** (cross-platform)
- **Ordre général → spécifique** (gauche → droite)
- **Pas de valeurs dans le nom d'un alias** (`color-blue-500` = global, `color-action-primary` = alias)
- **État en dernier** : `default, hover, active, focus, disabled`
- **Plateforme** en suffixe si besoin : `button-padding-mobile`

### Exemples bons / mauvais

✅ `color-action-primary-hover`
✅ `space-inset-md`
✅ `button-padding-md`
❌ `blueHoverColor` (camelCase, contient la valeur)
❌ `main-button-bg` (vague, pas hiérarchique)
❌ `btn1Color` (arbitraire)

## Theming (light ↔ dark)

Seuls les **alias** changent entre thèmes. Les globaux restent figés.

```yaml
# Light
color-surface: gray-50
color-text-primary: gray-900
color-border: gray-200

# Dark
color-surface: gray-900
color-text-primary: gray-50
color-border: gray-700
```

Les composants (`button-primary-bg`) référencent `color-action-primary` → aucune modification nécessaire pour supporter le dark mode.

## Formats standards

- **W3C Design Tokens Format** (émergent) : JSON avec `$value`, `$type`, `$description`.
- **Style Dictionary** (Amazon) : transforme un JSON source en CSS/iOS/Android/...
- **DTCG** (designtokens.org) : groupe de travail, format JSON canonique.

Figma Variables (2023+) exporte nativement vers ces formats.

## Audit des tokens

Signes de dérive :
- Tokens non-utilisés (morts)
- Valeurs hardcodées dans les composants (`#3B82F6` au lieu de `color-action-primary`)
- Aliases manquants pour un besoin métier récurrent
- Valeurs presque identiques (`gray-500: #6B7280` et `gray-550: #6A7380`)

Audit minimal :

```markdown
## Token audit — [date]

### Usage
- Globals utilisés / définis : X/Y
- Aliases utilisés / définis : X/Y
- Tokens à supprimer : [liste]

### Hardcodes (valeurs brutes dans composants)
- Fichier : valeur → token proposé
- `Button.tsx:42` : `#3B82F6` → `color-action-primary`

### Gaps
- Nouveau pattern qui manque de token : [description]
- Proposition : nouveau token `X`, valeur `Y`
```
