# Typography — Web Typography distillé

> Source : `skills-main/web-typography/SKILL.md` (scale, pairing, loading).

## Règles d'or

1. **1 typeface suffit souvent.** 2 max. Ne jamais 3+.
2. **Stack système par défaut** pour UI pure. Web font justifiée si identité éditoriale.
3. **Échelle finie** : 6-10 tailles. Pas de `17px`, pas de `23px`.
4. **Line-height généreux** : 1.5-1.6 pour body, 1.1-1.2 pour headings.
5. **Measure** : largeur de ligne 45-75 caractères (ch).

## Échelle type recommandée (modular scale ratio ~1.2-1.25)

| Rôle | Size (px) | Line-height | Weight |
|---|---|---|---|
| Display | 48-60 | 1.1 | 600-700 |
| Heading XL | 32-36 | 1.15 | 600 |
| Heading L | 24 | 1.2 | 600 |
| Heading M | 20 | 1.25 | 600 |
| Heading S | 18 | 1.3 | 600 |
| Body L | 18 | 1.55 | 400 |
| Body M | 16 | 1.55 | 400 |
| Body S | 14 | 1.5 | 400 |
| Label | 14 | 1.3 | 500 |
| Caption | 12 | 1.4 | 500 |

## Pairing

Si 2 fonts :
- **Rôles distincts** : 1 pour headings (ex. serif ou display), 1 pour body/UI (sans-serif lisible).
- **Contraste, pas combat** : ne pas pairer deux sans-serif similaires.
- **Exemples éprouvés** : Inter + Source Serif, Space Grotesk + Public Sans, DM Sans + DM Serif.

## Performance & loading

- **`font-display: swap`** : affiche immédiatement avec fallback, échange à l'arrivée. (FOUT > FOIT.)
- **WOFF2 uniquement** (90%+ support, 30-50% plus léger que WOFF).
- **Subsetter** : uniquement les caractères utilisés (`unicode-range`). Typiquement : latin, latin-ext.
- **Max 2 weights par font** (ex. 400 + 600). Chaque weight = fichier séparé.
- **Variable fonts** : 1 fichier pour tous les weights, recommandé dès que 3+ weights.
- **Preload** sur les fonts above-the-fold (`<link rel="preload" as="font">`).

## Anti-patterns

| Anti-pattern | Symptôme | Fix |
|---|---|---|
| 3+ typefaces | Visuel incohérent | Max 2 |
| `font-weight: 300` sur fond clair | Illisible, WCAG fail | Min 400 |
| Line-height 1.0 sur body | Texte dense, difficile | 1.5+ |
| Centered paragraphe long | Fatigue lecture | Align left |
| Tout en MAJ | Illisible > 1 ligne | Réserver aux labels courts |
| FOIT (texte invisible qlqes sec) | Perception de lenteur | `font-display: swap` |

## Réglages micro

- **Letter-spacing** : headings légèrement serrés (`-0.01em` à `-0.02em`), caps legers écartés (`0.04em` à `0.1em`).
- **Font-feature-settings** : activer `'ss01', 'cv11'` pour formes alternatives si la font les supporte (Inter a un "i" sans point en cv11).
- **Ne pas justifier** : texte en FR se justifie très mal sans césure pro.

## Lisibilité et accessibilité

- Contraste body ≥ 4.5:1 (texte normal) / 3:1 (texte large ≥ 18pt / 14pt bold).
- Taille minimum body : 16 px sur desktop, 16 px sur mobile aussi (pas de zoom forcé iOS).
- Respecter `user-scalable`, ne pas bloquer le zoom.
