# Onboarding Christian — Stratégie produit Galigéo

**Date** : 2026-05-04
**Auteur** : Greg (Product Management)
**Contexte** : Session 1h pour onboarder Christian sur le naming, le packaging, le découpage besoins/cas d'usage et la priorisation Power BI V1
**Format** : Document Notion (lecture autonome + support discussion)
**Status** : Draft pour relecture interne

---

## 0. TL;DR — En 30 secondes

> **Vision** : Galigéo devient une plateforme location intelligence ouverte, vendue sous deux canaux qui cohabitent — **PLG** (libre-service) et **SLG** (accompagné) — avec une activation par **cas d'usage prédéfinis**.
>
> **Le shift** : on garde la marque **Galigéo**, on adopte un positionnement *English first*, et on structure l'offre autour de **briques techniques assemblées en cas d'usage** — la *Factory*.
>
> **Ce qu'on demande à Christian** :
> 1. Validation de la **cohabitation PLG/SLG** comme architecture cible
> 2. Validation du **modèle de licences** (crédits + rapports, montants par offre)
> 3. Validation de la **priorisation Power BI V1** (commerce, axe « carte juste du premier coup »)

---

## 1. Vision & ambition

### Pourquoi maintenant
- Le marché location intelligence se polarise : outils GIS lourds (ArcGIS) vs visuels BI faibles (Azure Maps, Icon Map). Aucun acteur ne couvre les deux.
- Galigéo a un asset rare : boundaries FR/EU OOTB, expertise zones, base installée enterprise déjà on-prem.
- **Sans shift PLG**, on reste un acteur SLG niche. **Avec PLG**, on capture l'audience BI mondiale au moment où elle abandonne sa carte.

### Ambition
> **Galigéo, le standard location intelligence pour les organisations qui décident sur la carte — accessible au premier essai, puissant à l'usage continu.**

### Architecture cible : PLG ↔ SLG cohabitent
La home porte d'abord le **SLG** (canal historique, générateur de CA), avec une option **PLG** visible partout (gratuit → trial → paid).
Les deux canaux partagent **la même plateforme**. Différences : pricing, accompagnement, activation des mécanismes de monétisation immédiate (désactivables côté SLG).

> **[ SCHÉMA 1 — Vue holistique plateforme ]** *(image à insérer)*
> Macro-schéma matriciel 1 page : plateforme au centre, canaux PLG/SLG en bandeaux, cas d'usage à droite, personas à gauche. Specs détaillées en annexe C.

---

## 2. Concept Factory — Briques → Cas d'usage

### Le principe
La plateforme = des **briques techniques** (cartographie, geocoding, boundary matching, scoring, isochrones, cross-filter, etc.). Ces briques sont **assemblées** pour produire des **cas d'usage prédéfinis** que l'utilisateur active depuis son interface.

> **[ SCHÉMA 2 — Chaîne d'assemblage Factory ]** *(image à insérer)*
> Flux gauche → droite : briques techniques → assemblage → cas d'usage outputs. Specs détaillées en annexe C.

### Pourquoi ce modèle gagne

| Avantage | Pour qui |
|----------|----------|
| Activation immédiate sans formation | PLG / Self-serve |
| Personnalisation et builder à la demande | Power users / SLG |
| Logique d'upsell claire (1 cas → N cas) | Croissance net revenue |
| Mutualisation des briques techniques | R&D / Coût de build |

### Trois niveaux d'usage
1. **Niveau 1 — PLG** : activation cas d'usage prédéfini, paramètres simples, premier insight en < 5 min
2. **Niveau 2 — Modification** : ajustement des paramètres, ajout de variables, sans toucher l'assemblage
3. **Niveau 3 — Builder** : assemblage propre des briques (interface builder, voir schéma 4)

---

## 3. Packaging & naming

### Stratégie naming — simplicité assumée
- **Marque conservée** : Galigéo
- **Positionnement externe** : *English first* pour conquérir l'international
- **Offres métier** : Galigéo + descriptif (pas de sous-marques)
  - Exemples : Galigéo *Reach*, Galigéo *Network*, Galigéo *Expansion*

### Modèle de licence
Une licence = **modalité d'accès** (places, niveau de support).
Sur cette licence, on **active des cas d'usage**. Limites d'usage = enveloppe de **crédits + rapports** montant selon l'offre.

| Niveau | Cible | Support | Crédits / Rapports |
|--------|-------|---------|--------------------|
| **Free** | Découverte / trial | Self-serve | Limité |
| **Pro** | PME / Builder solo | Email | Modéré |
| **Business** | Équipes | Onboarding inclus | Élevé |
| **Enterprise** | Grands comptes | Dédié + on-prem possible | Custom |

→ Détail complet et limites par cas d'usage en **annexe A** (à compléter après validation D2).

---

## 4. Power BI — Le premier cas d'usage PLG concret

Power BI plug-in est le **premier cas d'usage activé sur la Factory**. Périmètre V1 validé techniquement (Patrick) et globalement (Aurélien) le 2026-04-03. Orientation **100% PLG**, focus retail/commerce.

### Argument V1
> ***« Sortez la même carte, sans Excel intermédiaire, du premier coup — en France et partout en Europe. »***

### Trois axes différenciateurs V1

| Axe | Pain résolu | Concurrence |
|-----|-------------|-------------|
| **Geocoding correct multi-pays** | Carte fausse → utilisateur abandonne pour un treemap | Azure Maps, ArcGIS structurellement faibles |
| **Polygones illimités + boundaries FR/EU** | Limite 32K caractères Power Query → JSON cassé | Icon Map plafonné, Esri pas de boundaries OOTB |
| **EU data sovereignty + on-prem** | Compliance banque/santé/défense (Schrems II, DORA) | Tous concurrents = US cloud |

### Roadmap (1-liner par phase)
- **V1 — Q3 2026** *« Sortez la carte juste, du premier coup. »* — Persona Sophie (Builder retail/public FR/EU)
- **V2 — Q1 2027** *« Explorez votre carte. »* — Ajouts : H3 hexagones, lasso, Microsoft Cert Tier 1
- **V3 — H2 2027** *« Décidez sur la carte. »* — Ajouts : spatial intersect, multi-couche, data hub

### Table stakes (à prouver visuellement en démo, pas axes différenciateurs)
- Performance 30K-70K points fluide (deck.gl WebGL)
- Cross-filter sans friction (DataView API native)
- Format Pane natif Power BI

→ Détail des **12 leviers candidats** + scoring conviction + sourcing verbatims en **annexe B**.

---

## 5. Parcours utilisateur (maquettes)

> **[ SCHÉMA 3 — Parcours d'achat & activation ]** *(image à insérer)*
> Timeline horizontale 5 étapes avec maquettes annotées. Specs détaillées en annexe C.

### Les 5 moments clés
1. **Découverte** — home page (SLG mis en avant, PLG visible partout)
2. **Achat 1ᵉʳ cas d'usage** — friction minimale, pricing transparent (mode PLG)
3. **Activation** — cas prêt à l'emploi, premier insight en < 5 min
4. **Upsell** — suggestion d'un cas complémentaire au moment opportun
5. **Personnalisation** — passage progressif au builder pour les power users

### Comportement PLG vs SLG
- **Mécanismes d'engagement** (suggestions, contextual help, onboarding tour) → **partagés** dans tous les modes.
- **Mécanismes de monétisation immédiate** (pop-ups d'achat, paywalls) → **désactivables côté SLG** (post-avant-vente, formation).

> **[ SCHÉMA 4 — Interface builder (briques pures) ]** *(image à insérer)*
> Capture annotée : palette de briques + canvas d'assemblage + preview. Specs détaillées en annexe C.

---

## 6. Validations demandées & prochaines étapes

### Décisions à valider (3)

| # | Décision | Rationale |
|---|----------|-----------|
| **D1** | Cohabitation **PLG / SLG** comme architecture cible | Conserve le canal CA historique tout en capturant l'audience BI internationale |
| **D2** | Modèle licence = **crédits + rapports** montants par offre | Pricing simple côté PLG, flexible côté Enterprise |
| **D3** | Power BI V1 priorité **« carte juste du premier coup »** (axes L1+L2+L3+L6) | Pain validé sur 100% personas / forums ; concurrence structurellement faible sur ces axes |

### Trade-offs à arbitrer (en réunion ou follow-up)

| # | Question | Notre proposition | À débattre |
|---|----------|-------------------|------------|
| **T1** | Microsoft Cert Tier 1 maintenant ou différé ? | Différé V2 | Si < 20 % marché régulé visé : on garde V2. Si ≥ 30 % : on bifurque archi V1 |
| **T2** | Drive-time / isochrones en V2 ou V3 ? | V3 (silence forums = signal) | Customer interviews 5-7 clients à planifier avant fin mai |
| **T3** | Logo Galigéo permanent en V1 ? | Oui (consensus actuel) | Risque « marque blanche » à arbitrer |

### Questions ouvertes (sujets en cours, avec délais)

| Sujet | Owner | Délai |
|-------|-------|-------|
| Critères pricing personnalisables (restitution visuelle site) | À assigner | Fin mai |
| Limites d'usage exactes (cartes / rapports / crédits) par cas d'usage | À assigner | Mi-mai |
| Plan marketing associé à la sortie V1 Power BI | À assigner | Avant lancement |
| Format de restitution interne secondaire (Notion vs cloud design) | Greg | Cette semaine |
| Découpage précis licence / builder / viewer / contraintes | À assigner | Avant V1 |

### Prochaines étapes après validation
1. **D1 validé** → finalisation maquette home + V0 site
2. **D2 validé** → spec licences finalisée + intégration pricing
3. **D3 validé** → kickoff dev V1 Power BI, planification customer interviews drive-time

---

## Annexes

### Annexe A — Détails des plans

À compléter après validation D2. Doit contenir :
- Tableau plans × fonctionnalités (matrice)
- Limites d'usage exactes par plan (cartes / rapports / crédits)
- Cas d'usage activables par plan
- Règles d'upsell entre plans

### Annexe B — Power BI : 12 leviers candidats

Source : `[A décider] Power BI plug-in — Différenciateurs V1 / V2 / V3`

#### Tableau de conviction

| Levier | Pain | Concurrence | Phase | Capacité Galigéo |
|--------|------|-------------|-------|-------------------|
| L1 — Geocoding correct multi-pays ⭐ | 🔴🔴🔴 | 🟢 vide | **V1** | 🟢 (E16) |
| L2 — Polygones illimités (boundaries serveur) ⭐ | 🔴🔴🔴 | 🟢 vide | **V1** | 🟢 (déjà spec) |
| L3 — Boundaries FR/EU OOTB ⭐ | 🔴🔴 | 🟢 vide | **V1** | 🟢 (E15-S7) |
| L4 — Performance 30K-70K points | 🔴🔴 | 🟡 (Icon Map) | V1 (table stake) | 🟢 (validé proto) |
| L5 — Cross-filter sans friction | 🔴🔴 | 🟡 | V1 (table stake) | 🟢 (DataView) |
| L6 — EU data sovereignty + on-prem ⭐ | 🔴🔴 | 🟢 vide | **V1** | 🟢 (architecture) |
| L7 — Lasso / polygon select | 🔴 | 🟡 | V2 | 🟢 (deck.gl) |
| L8 — H3 hexagones + 3D extrude | 🔴 | 🟡 (Icon Map Pro) | V2 | 🟢 (déjà spec V2) |
| L9 — Drive-time / isochrones | 🔴🔴 silencieux | 🟢 vide | V2/V3 | 🟡 (E17, ext API) |
| L10 — Microsoft Cert Tier 1 | 🔴🔴 gatekeeper | 🟡 (ArcGIS) | V2 | 🟡 |
| L11 — Spatial intersect / buffer | 🔴 | 🟡 (ArcGIS+) | V3 | 🟡 (E17) |
| L12 — Multi-couche + per-user visibility | 🔴 | 🟡 (Icon Map Pro) | V3 | 🟡 |

#### Verbatims clés (V1)

- *« St Helens (UK) mapped to Cambodia; Rivers State, Nigeria appeared in Canada. »* — British Red Cross
- *« Map and Filled Map only seem to reliably work for North America and Western Europe. »* — Power BI community
- *« Icon Map has a character limitation of around 32K, and some polygons may have 70K character length. »* — Microsoft Fabric community
- *« Around 4k postal codes. I ended up solving this by downloading a public table of all postal codes in Norway. »* — r/PowerBI 2026-03-25

#### Argument anti-substitution (le plus fort)
Quand le geocoding échoue, l'utilisateur **ne change pas de visuel — il abandonne la carte pour un treemap**. C'est le finding le plus grave et notre cible la plus directe.

→ Détail complet (qualitatif + quantitatif + sourcing par levier) : voir document source.

### Annexe C — Specs des 4 schémas SVG

Voir document séparé : `docs/onboarding-christian-schemas-specs.md`
