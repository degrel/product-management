# Color & Contrast

> Sources : `skills-main/refactoring-ui/`, `designer-skills-main/ui-design/skills/{color-system,dark-mode-design}/`.

## Construire une palette

### Méthode
1. **Commencer par le neutre** : 9-10 niveaux de gris (50, 100, 200, …, 900). Couvre 80% des besoins UI.
2. **1 primary** : couleur de marque. Décliner en 9-10 niveaux.
3. **1 accent** (souvent = primary ou complémentaire) pour la CTA UNIQUE de l'écran.
4. **Sémantiques figées** : success (green), warning (amber), danger (red), info (blue). Décliner en 3-5 niveaux.

### Stop si…
- 3+ couleurs "de marque"
- Plus de 10 couleurs dans la UI (hors neutres)
- Des teintes "pour ajouter du dynamisme"

## Tokens couleurs recommandés

```yaml
# Global (primitives)
gray-50: #F9FAFB
gray-100: #F3F4F6
gray-200: #E5E7EB
gray-400: #9CA3AF
gray-500: #6B7280
gray-700: #374151
gray-900: #111827
primary-500: #1A4D7A
primary-600: #164263
accent-500: #E6733A
red-500: #DC2626
green-500: #16A34A
amber-500: #D97706
blue-500: #2563EB

# Alias (semantic)
color-surface: gray-50 (light) / gray-900 (dark)
color-surface-elevated: white (light) / gray-800 (dark)
color-text-primary: gray-900 / gray-50
color-text-secondary: gray-600 / gray-400
color-text-muted: gray-500 / gray-500
color-border: gray-200 / gray-700
color-action-primary: primary-500
color-action-primary-hover: primary-600
color-state-success: green-500
color-state-warning: amber-500
color-state-danger: red-500
```

## Contraste WCAG (AA / AAA)

| Texte | AA minimum | AAA |
|---|---|---|
| Normal (< 18pt et < 14pt bold) | 4.5:1 | 7:1 |
| Large (≥ 18pt ou ≥ 14pt bold) | 3:1 | 4.5:1 |
| UI (bordures, icônes porteuses d'info) | 3:1 | — |

Outils :
- **colour-contrast.cc** — web rapide
- **Figma plugin "A11y — Contrast Checker"**
- **DevTools Chrome** → panneau Accessibility sur un élément

### Don'ts contraste

| Problème | Fix |
|---|---|
| Gray-400 sur white | Gray-600+ (4.5:1) |
| Placeholder = vrai texte | Contraste placeholder OK car informatif, pas critique |
| Lien bleu subtil sur bleu clair | Souligner + contraste ≥ 4.5:1 |
| État disabled gris pâle | Maintenir 3:1 minimum pour qu'on voit qu'il existe |

## Dark mode — pas une inversion

Règles :
1. **Fond jamais pur noir**. `#0F172A` (slate-900) ou `#111827` (gray-900). Plus reposant, réduit halation.
2. **Texte jamais pur blanc**. `#E5E7EB` (gray-200) ou équivalent.
3. **Saturation réduite** : couleurs trop saturées vibrent sur fond sombre. Baisser ~10-20%.
4. **Élévation inversée** : en dark, les surfaces ÉLEVÉES sont plus claires (plus proche de la lumière). En light, c'est l'inverse. Utiliser `color-surface-elevated: gray-800` en dark.
5. **Ombres moins utiles** — remplacer par `border` subtile.
6. **Images, illustrations, icônes** : prévoir des variantes dark pour ce qui a du contraste (logos, hero images).

## Daltonisme

- 8% des hommes, 0.5% des femmes sont daltoniens (protanopie, deutéranopie, tritanopie).
- **Jamais rouge/vert seuls** pour signaler succès/échec. Ajouter icône, label, pattern.
- Tester avec **Sim Daltonism** (macOS) ou plugin Figma "Color Blind".

## Palettes data viz

- **Séquentielle** (données ordonnées 0 → max) : une teinte, 5-9 niveaux de clair à sombre. Ex. Blues.
- **Divergente** (écart autour d'une médiane) : 2 teintes avec neutre au milieu. Ex. Red-White-Blue.
- **Catégorielle** (groupes discrets, ≤ 8) : ColorBrewer `Set2`, `Dark2`, `Paired`.
- **Éviter** : arc-en-ciel (pas d'ordre perceptible), palettes trop saturées.

Référence : colorbrewer2.org
