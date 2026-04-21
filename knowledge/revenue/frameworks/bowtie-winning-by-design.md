---
name: Bowtie (Nœud papillon) — Winning by Design
type: framework
sources:
  - Session 1 (Business Models) — slides 81-108
  - Session 2 (Mesurer et analyser la performance) — slides 5-18, 29-38, 43
  - Session 3 (PLG to SLG) — slides 3-5
---

# Bowtie (Nœud papillon) — Winning by Design

## Definition

Le **Bowtie** (nœud papillon) est le nouveau funnel des revenus récurrents, développé par Winning by Design pour remplacer l'entonnoir classique (qui ne modélisait que l'acquisition). Il est **symétrique autour de l'Engagement Mutuel** et couvre 7 étapes : **Awareness → Education → Selection → Engagement Mutuel → Onboard → Adoption → Expansion**. Le closing n'est plus une ligne d'arrivée mais un point central où les deux parties s'engagent mutuellement. La croissance vient **à la fois de l'acquisition (gauche) et de l'expansion (droite)**.

## Pourquoi c'est important

Pour un PM, le Bowtie est la carte unique qui permet de :
- Cesser de traiter le produit comme un outil uniquement d'acquisition (feature → deal signé) et l'inscrire dans un parcours qui inclut Onboard, Adoption, Expansion.
- Mesurer la performance end-to-end avec un modèle de données partagé par Marketing, Sales, CS et Produit (langage commun).
- Arbitrer la roadmap en fonction de l'étape la plus faible du bowtie (ex : feature de découverte vs feature d'adoption).
- Comprendre que **Valeur (impact promis, côté gauche) et Impact (valeur réalisée, côté droit) sont symétriques** : si ce qu'on promet en vente n'est pas délivré en CS, tout l'édifice LTV s'effondre.

## Le framework en détail

### Les 7 étapes

| # | Étape | Question du client |
|---|---|---|
| 1 | Awareness | "Est-ce qu'il y a un problème ?" |
| 2 | Education | "Suis-je intéressé par leur solution ?" |
| 3 | Selection | "Est-ce que je suis mieux ailleurs ?" |
| 4 | Engagement Mutuel | "Qui a besoin de ça pour qu'on puisse réussir ensemble ?" |
| 5 | Onboard | "Comment prouver qu'on a raison d'y aller ?" |
| 6 | Adoption | "Je continue ou j'arrête ?" |
| 7 | Expansion | "Qu'est-ce qu'on peut faire d'autre ?" |

### Modèle de données standardisé : VM, CR, T

**3 grands types de métriques** transversales : Volumes / Taux de conversion / Durées.

**Volumes (VM1 → VM8)** — combien de clients/prospects à chaque étape :
- VM1 Prospects — VM2 MQLs — VM3 SQLs / Opportunités — VM4 SALs (Sales Accepted Leads) — VM5 Wins (signés) — VM6 Onboardings — VM7 ARR départ — VM8 LTV

**Taux de conversion (CR1 → CR8)** :
- **CR1** : Awareness → Education (Leads → MQL)
- **CR2** : Education → Selection (MQL → SQL)
- **CR3** : Passation SDR → AE (acceptation de l'opportunité par l'AE)
- **CR4** : Opportunité → Won = **Win Rate**
- **CR5** : Onboarding (irréversible, = Time-to-Impact ; churn onboarding)
- **CR6** : Churn / Rétention (réversible, Impact récurrent)
- **CR7** : Expansion
- **CR8** : Ratio d'expansion

**Durées** — les 3 clés :
- Sales Cycle (à mesurer à partir de l'acceptation AE)
- Durée d'Onboarding (T5) — rarement mesurée, pourtant critique
- Durée de vie des clients (ΔT6, ΔT7)

### Analyse par couple d'indicateurs

Pour identifier la cause profonde, on n'évalue pas indicateur par indicateur mais par paires :

| Couple | Ce que cela révèle |
|---|---|
| **VM3 / CR4** | Problème de ciblage ? A-t-on assez d'opportunités ? Qualité de l'appel de découverte ? |
| **CR3 / CR4** | Qualité de la passation SDR→AE ; mauvaise acceptation / transmission |
| **CR4 / CR5** | Survente — les vendeurs promettent plus que le produit ne peut livrer |
| **CR4 / CR6** | Problème de ciblage : on signe des prospects qui churneront |
| **T5 / CR6** | Onboarding trop long/trop dur fait churner ; ou onboarding bâclé fait churner ensuite |
| **VM5 / T5** | Plus de wins que la capacité d'onboarding → durée qui explose → churn à venir |

### 4 niveaux de benchmark

| Niveau | Outil | Source | Usage |
|---|---|---|---|
| Grosse maille | Hache / Tronçonneuse | Sectoriel (VC, WbD) | Identifier le plus gros écart |
| Plus précis | Ciseaux | Pairs (étude, interview, embauche d'ex-concurrent) | Vérifier la comparabilité, fixer une cible |
| Concurrent direct | — | Écoute passive, ex-employés | Se positionner |
| Chirurgical | Bistouri / Scalpel | Vs soi-même (équipes, périodes, zones) | Déterminer causalité, plan d'action, suivi |

**Outil référence** : `benchsights.com/wbd` (Bowtie Benchmarks de Winning by Design). Gratuit, collaboratif, **filtrer obligatoirement par ACV**. Plus l'ACV est élevée, meilleurs CR4 et CR7, plus faible le churn. Avant CR3 maximiser n'est pas l'objectif (sélectivité = qualité, 30-35% de conversion amont peut être suspect).

### Principes de mesure (3 conditions de fiabilité)

1. Définition claire, partagée par tous.
2. Source de donnée unique et fiable.
3. Processus opérationnel qui garantit la fiabilité (pas de saisie manuelle tordue).

### Toujours travailler en base 100

Rétention (1 − churn) = 94% ; Expansion (1 + taux) = 108%. Permet de multiplier les taux le long de la chaîne : `ARR_{n+1} = ARR_n × Rétention × Expansion`.

## Application pratique

Un PM utilise le bowtie pour :

1. **Diagnostiquer où investir produit**. Faible CR5 = priorité onboarding (activation, first-time UX, guide intégré). Faible CR6 = priorité adoption (notifications, scores de santé, nudges). Faible CR7 = priorité expansion (cross-sell in-product, packaging modulaire).
2. **Cadrer un discovery**. Quelle étape du bowtie ? Quelle hypothèse de déplacement du taux de conversion ? Quel impact attendu sur VM7 (ARR) et VM8 (LTV) ?
3. **Calibrer un budget ou une cible**. En remontant les ratios benchmark depuis l'ACV cible, on dérive le budget par MQL (ex : ACV 15k€, LTV/CAC=3 → budget acquisition ≤ 10% → 61€/MQL).
4. **Segmenter les GTM**. Un bowtie par GTM (PLG, MidMarket, Grands Comptes) — pas un unique reporting consolidé.

### Questions à se poser face à un choix produit

- Quelle étape du bowtie cette feature fait-elle progresser ? De combien de points ?
- Sur quel couple d'indicateurs observe-t-on aujourd'hui la plus grande dérive ?
- Est-ce un problème d'acquisition (gauche) ou d'impact récurrent (droite) ?
- A-t-on les 3 conditions de mesure avant de se lancer (définition / source / process) ?

## Signaux / anti-patterns

**Bien appliqué :**
- Un unique reporting partagé Marketing + Sales + CS, avec les mêmes définitions.
- Le churn onboarding (CR5) est mesuré séparément du churn d'usage (CR6).
- Le CS est orienté vers l'Impact (pas seulement la satisfaction) et a des KPI d'expansion.
- Les décisions produit se justifient par leur effet sur un CR nommé.

**Anti-patterns :**
- Un seul KPI "churn global" qui mélange CR5 et CR6.
- Focus exclusif sur le côté gauche ("closing") ; l'ARR expansion n'est pas piloté.
- Benchmarks sectoriels utilisés sans filtre ACV → conclusions fausses.
- Les Sales ne sont pas un peu CSM, les CSM ne sont pas un peu Sales → silos.
- Balance acquisition/expansion déséquilibrée vers la gauche alors qu'on vend en SaaS annuel (devrait être 50/50) ou en usage (devrait pencher à droite).
- Pas de "gardien du playbook" — chacun réinvente le modèle à chaque trimestre, l'historique est perdu.

## Questions pour challenger une décision Galigeo

1. **Quel est le bowtie de TM vs RetailFocus vs Org** ? Sont-ils pilotés avec un modèle de données unifié (VM1-VM8, CR1-CR7) ou avec 3 reportings hétérogènes que le Board consolide manuellement ? Si on lance une feature cross-produit, sait-on sur quel CR on agit ?
2. **Pour TM côté grands comptes (retail/banque/assurance)** : quel CR est aujourd'hui le plus faible ? Si c'est CR5 (Time-to-Impact), la feature priorisée doit être sur l'onboarding (templates zones préconfigurées, import de données client, formation intégrée) — pas sur une nouvelle fonction d'analyse amont.
3. **Couple CR4 / CR5 sur RetailFocus** : nos commerciaux promettent-ils un niveau d'analyse de zone que le produit ne délivre qu'après 3 semaines de setup data ? (survente → mauvaise réputation sur un marché où les Dir Dev se connaissent).
4. **Couple T5 / CR6 pour un Dir RE** : combien de temps met-il pour obtenir son premier dashboard de portefeuille exploitable ? Si > 6 semaines sur TM, le renouvellement est déjà compromis à l'échéance N+1.
5. **Expansion côté PLG (RetailFocus self-serve si existe)** : mesure-t-on VM7 (ARR départ) vs VM8 (LTV) séparément par motion ? Les Network Managers qui adoptent un compte gratuit puis montent en gamme doivent être tracés dans un bowtie PLG distinct.
6. **Benchlight WbD filtré sur notre ACV** : quel est notre écart le plus grand vs la médiane ? (hypothèse : CR5 et CR6 chez Galigeo, car B2B SaaS français à onboarding lourd). Si personne n'a saisi les données, c'est le premier chantier Data.
7. **Le PM est-il "gardien du playbook"** sur les critères de feature (Impact New Business / Rétention / Faisabilité — cf `plg-vs-slg-decision.md`) ou chaque Dir commerciale pousse ses features prioritaires en direct ?
8. **3 conditions de fiabilité** : avant de lancer un dashboard KPIs pour le CODIR, a-t-on vraiment (a) une définition partagée d'un "client actif RetailFocus", (b) une source unique, (c) un process qui n'altère pas la donnée (ex : pas de statut déplacé manuellement dans le CRM) ?

## Citations-clés du coach

- "Historiquement on s'arrêtait au closing ce qui voulait dire quelque part on était à la fin. Alors qu'en fait c'était plutôt un début sur lequel on s'engage mutuellement."
- "Le churn onboarding, c'est assez irréversible. Si vous cochez toutes les mauvaises cases et que vous y allez, 1,5 an à remonter la pente."
- "Il faut rendre les Sales un peu CSM, et les CSM un peu Sales."
- "Parler en base 100, c'est tout bête mais juste c'est multipliable le long de la chaîne."
- "Il faut qu'il y ait un gardien du temps du playbook nommé en interne."

## Liens

- Sessions sources : [../sessions/01-business-models.md](../sessions/01-business-models.md), [../sessions/02-mesurer-analyser-performance.md](../sessions/02-mesurer-analyser-performance.md), [../sessions/03-plg-to-slg.md](../sessions/03-plg-to-slg.md)
- Frameworks connexes :
  - [business-models-saas.md](business-models-saas.md) — l'unit economics (LTV/CAC) qui se calcule sur le bowtie
  - [plg-vs-slg-decision.md](plg-vs-slg-decision.md) — un bowtie par GTM
  - [icp-segmentation-spiced.md](icp-segmentation-spiced.md) — SPICED alimente le côté gauche du bowtie
  - [growth-stages-gtm.md](growth-stages-gtm.md) — le bowtie se pilote différemment selon le stade
