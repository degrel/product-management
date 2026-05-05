# Specs des 4 schémas SVG — Onboarding Christian

**Document associé** : `docs/onboarding-christian-strategy.md`
**Usage** : brief pour la production des SVG (designer ou Greg, indépendamment)
**Format de sortie attendu** : SVG export (intégré dans la page Notion comme image)
**Style général** : épuré, matriciel (format que Christian apprécie), palette Galigéo

---

## Préférences communes aux 4 schémas

- **Hiérarchie visuelle stricte** : 1 idée centrale par schéma, pas de surcharge
- **Pas plus de 3 niveaux** de profondeur visuelle
- **Pas de dégradés**, à-plats ou contours fins seulement
- **Typographie** : 1 police sans-serif, 2 graisses max (bold pour titres, regular pour labels)
- **Légende** : intégrée directement dans le schéma (pas de légende externe)
- **Format Notion** : optimiser pour lecture à 1024px de large dans Notion

---

## Schéma 1 — Vue holistique plateforme (matrice macro)

### Objectif
Donner à Christian une vue 1-page de l'ensemble plateforme + canaux + cas d'usage + personas. **C'est LE schéma de référence** que Christian consultera pendant toute la session.

### Format
- SVG paysage **1600 × 900** (ratio 16:9)
- Lecture en 30 secondes maximum

### Layout

```
┌───────────────────────────────────────────────────────────┐
│  CANAL PLG — Libre-service (free → pro → business)         │
├──────────┬─────────────────────────────────────┬───────────┤
│          │                                     │           │
│ PERSONAS │       PLATEFORME GALIGÉO            │ CAS       │
│  (4-5)   │       (briques techniques)          │ D'USAGE   │
│          │                                     │ (4-5)     │
│          │                                     │           │
├──────────┴─────────────────────────────────────┴───────────┤
│  CANAL SLG — Accompagné (avant-vente → onboarding → enterprise)
└───────────────────────────────────────────────────────────┘
```

### Contenu détaillé

**Centre — Plateforme Galigéo (40 % de la surface)**
Boîte centrale avec 6-8 briques techniques listées en grille :
- Cartographie multi-niveau
- Geocoding multi-pays
- Boundary matching
- Scoring & analyses
- Isochrones
- Cross-filter
- Auth & permissions
- Crédits & rapports

**Bandeau haut — Canal PLG**
- Étiquette « PLG · Libre-service »
- 3 paliers visibles : Free → Pro → Business
- Indicateur visuel : couleur lumineuse / contraste positif

**Bandeau bas — Canal SLG**
- Étiquette « SLG · Accompagné »
- 3 paliers visibles : Avant-vente → Onboarding → Enterprise
- Indicateur visuel : couleur dense / institutionnelle

**Côté gauche — Personas (4-5 cards verticales)**
- C-Level (vision stratégique, ROI)
- Directeurs Développement (études marché, implantation)
- Directeurs Immobilier (portefeuille)
- Data Leaders (analytics, modélisation)
- Network Managers (performance POS)

**Côté droit — Cas d'usage (4-5 cards verticales)**
- Power BI Map (premier cas, V1 commerce)
- Zone Study / Catchment area
- Network Performance
- Expansion / Site selection
- Cannibalisation analysis

### Effet visuel attendu
La plateforme **rayonne** vers les personas (gauche) et les cas d'usage (droite). Les deux canaux **encadrent** l'ensemble.
Christian doit comprendre en 30 secondes : *« Une plateforme, deux canaux, plusieurs cas d'usage activables, plusieurs personas servies. »*

---

## Schéma 2 — Chaîne d'assemblage Factory

### Objectif
Démontrer visuellement le concept Factory : briques techniques → assemblage → cas d'usage. C'est le concept le plus novateur du document, il doit **frapper visuellement**.

### Format
- SVG paysage **1600 × 600**
- Métaphore : chaîne de production / pipeline

### Layout

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  BRIQUES    │ →  │ ASSEMBLAGE  │ →  │ CAS D'USAGE │
│             │    │             │    │             │
│ (8-10)      │    │ (engrenage) │    │ (4-5 cards) │
└─────────────┘    └─────────────┘    └─────────────┘
```

### Contenu détaillé

**Zone gauche — Briques techniques (8-10 rectangles équivalents)**
Chaque brique = rectangle simple avec icône + nom.
Exemples :
- Geocoding
- Boundary matching
- Scoring
- Isochrones
- Cross-filter
- Auth
- Crédits / Rapports
- Tuilage carto
- Data import
- Cartographie multi-niveau

→ Toutes les briques sont **visuellement équivalentes** (même taille, même style). Pas de hiérarchie entre briques.

**Zone milieu — Symbolique d'assemblage**
Métaphore visuelle au choix :
- Engrenages connectés (mécanique)
- Pipeline / chaîne (manufacturing)
- Pattern type Zapier / n8n (modern dev)

→ Doit suggérer un **mouvement** de gauche à droite (flèches subtiles, ou disposition diagonale).

**Zone droite — Cas d'usage outputs (4-5 cards visuelles)**
Chaque card = preview du cas d'usage avec mini-carte ou KPI.
- Power BI Map
- Zone Study
- Network Performance
- Expansion
- Cannibalisation

### Effet visuel attendu
*Manufacturing vibe.* Christian doit comprendre : *« Ces briques + cet assemblage = ce cas d'usage. Et on peut recombiner pour en sortir d'autres. »*

---

## Schéma 3 — Parcours d'achat & activation

### Objectif
Montrer le voyage utilisateur PLG-first sur 5 étapes, avec le ressenti à chaque moment.

### Format
- SVG paysage **1800 × 800** (timeline horizontale)
- 5 étapes équidistantes

### Layout

```
J0          J0+5min      J7           J30          J90
 │            │            │            │            │
 ▼            ▼            ▼            ▼            ▼
[1]──────────[2]──────────[3]──────────[4]──────────[5]
Découverte   Achat 1er    Activation   Upsell       Personnalisation
             cas d'usage              nouveau cas   builder
```

### Contenu détaillé

Pour chaque étape, 4 éléments empilés verticalement :

**(en haut) Icône / illustration** (style line-art ou flat)
- 1. Loupe / page d'accueil
- 2. Panier / paiement
- 3. Carte qui s'affiche (insight)
- 4. Notification / suggestion contextuelle
- 5. Briques d'assemblage (lien avec Schéma 2 et 4)

**(milieu) Maquette annotée** (capture UI placeholder)
- 1. Home page (hero PLG visible + CTA SLG)
- 2. Pricing + checkout simple
- 3. Carte rendue avec données utilisateur
- 4. Pop-up suggestion cas complémentaire
- 5. Interface builder (palette + canvas)

**(milieu bas) Phrase descriptive** (1 ligne courte)
- 1. *« Je découvre Galigéo et son offre PLG »*
- 2. *« J'achète mon premier cas d'usage en quelques clics »*
- 3. *« J'obtiens mon premier insight en moins de 5 minutes »*
- 4. *« Je me vois proposer un cas complémentaire pertinent »*
- 5. *« Je personnalise mes cas et j'assemble mes propres briques »*

**(bas) Indicateur temps**
- J0, J0+5min, J7, J30, J90

### Marquage spécial
Les éléments **désactivables côté SLG** (mécanismes de monétisation immédiate, pop-ups d'achat) doivent être identifiés avec un badge ou icône cadenas. À placer sur les étapes 2 et 4 principalement.

### Effet visuel attendu
Christian doit comprendre : *« L'utilisateur passe de zéro à power user en 90 jours, et chaque étape crée de la valeur (pour lui et pour nous). »*

---

## Schéma 4 — Interface builder (briques pures)

### Objectif
**Prouver que la Factory est tangible** (pas juste un concept marketing). Montrer l'interface builder telle qu'elle sera vécue par un power user.

### Format
- SVG paysage **1400 × 1000**
- Style : capture d'interface annotée

### Layout

```
┌──────────────────────────────────────────────────────┐
│ Header app Galigéo                                   │
├──────────┬─────────────────────────┬─────────────────┤
│          │                         │                 │
│ PALETTE  │   CANVAS D'ASSEMBLAGE   │    PREVIEW      │
│ briques  │   (drag & drop)         │    cas d'usage  │
│          │                         │                 │
│ (liste   │   briques connectées    │    carte +      │
│  10-12)  │   par flèches type      │    KPIs +       │
│          │   Zapier / n8n          │    légende      │
│          │                         │                 │
└──────────┴─────────────────────────┴─────────────────┘
```

### Contenu détaillé

**Zone gauche — Palette de briques (10-12 items)**
Liste verticale. Chaque item :
- Icône
- Nom
- (optionnel) Status d'activation : « Inclus », « Crédits requis », etc.

**Zone centrale — Canvas d'assemblage**
- Briques disposées et connectées par flèches (vibe Zapier / n8n / Make)
- Exemple concret à modéliser : un cas Zone Study qui chaîne Geocoding → Boundary matching → Scoring → Isochrones → Output carte
- Annotations chiffrées **(1)**, **(2)**, **(3)** sur les flèches pour expliquer la séquence

**Zone droite — Preview cas d'usage**
- Mini rendu carte (placeholder réaliste)
- 3-4 KPIs en cards
- Légende cohérente avec la palette

### Annotations
3-4 callouts en marge expliquant :
- **(1)** *« Glissez une brique depuis la palette »*
- **(2)** *« Connectez les briques pour définir le flux »*
- **(3)** *« Le preview se met à jour en live »*

### Effet visuel attendu
*« Ce n'est pas un PowerPoint, c'est un produit. »* Le schéma doit donner l'impression d'une vraie capture, pas d'une illustration abstraite.

---

## Récap pour le designer

| # | Titre | Format | Priorité | Complexité |
|---|-------|--------|----------|------------|
| 1 | Vue holistique plateforme | 1600 × 900 | **Critique** (référence session) | Moyenne |
| 2 | Chaîne d'assemblage Factory | 1600 × 600 | **Critique** (concept central) | Moyenne |
| 3 | Parcours d'achat & activation | 1800 × 800 | Haute | Élevée (5 mockups) |
| 4 | Interface builder | 1400 × 1000 | Moyenne (preuve tangible) | Élevée (mockup détaillé) |

### Si temps limité
**Priorité absolue** : Schémas 1 et 2 (concepts).
**Si temps reste** : Schéma 3 (parcours).
**Optionnel** : Schéma 4 (peut être remplacé par capture Figma existante de l'interface builder).
