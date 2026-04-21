---
name: PLG vs SLG — Choix et coexistence des motions GTM
type: framework
sources:
  - Session 1 (Business Models) — slides 106-108
  - Session 3 (PLG to SLG) — slides 12-63
  - Session 4 (Stades de croissance) — slides 3-7, 45, 48
---

# PLG vs SLG — Choix et coexistence des motions GTM

## Definition

Le choix PLG (Product-Led Growth) vs SLG (Sales-Led Growth) n'est pas binaire mais s'inscrit sur un **axe No touch → Dedicated touch** à 5 positions : **PLG → ISR 1-Stage → 2-Stages (SDR+AE) → Field Sales → Named Accounts**. Le choix se fait sur l'**ACV cible × nombre de deals/an**, et doit être **aligné horizontalement** sur Marketing, Sales et Customer Success (un GTM = une chaîne, pas 3 départements). Les erreurs de GTM sont la cause n°1 des contre-performances commerciales (observée dans 95% des diagnostics du coach).

## Pourquoi c'est important

Pour un PM, ce framework répond à :
- **Quel produit/packaging pour quel segment ?** Un PLG exige une expérience utilisateur irréprochable ; un SLG Grands Comptes exige sécurité, archi, RSE — pas les mêmes features.
- **À qui parler dans la roadmap ?** En PLG l'utilisateur est le décideur ; en Grands Comptes c'est un processus multi-décideurs où l'utilisateur est souvent le moins influent.
- **Combien de motions maintenir en parallèle ?** Seuils empiriques : 5M€ ARR minimum avant d'ouvrir une 2e, 20M€ pour en tenir 2.
- **Combien de "features paillettes" allouer ?** 5-10% de la roadmap à des features qui ne seront pas utilisées mais qui déclenchent la décision d'achat.
- **Comment évaluer une feature ?** Matrice 3D : Impact New Business / Impact Rétention / Faisabilité technique.

## Le framework en détail

### Les 5 motions Sales

| Motion | Principe | ACV typique | Adapté à |
|---|---|---|---|
| **PLG** | Le produit fait son propre marketing, intègre la découverte, orchestre vente et paiement ; les utilisateurs en parlent autour d'eux | Très bas | Produits intuitifs avec potentiel viral (Slack, Notion, Zoom, Calendly) |
| **ISR 1-Stage** | 1 Inside Sales Rep gère tout (prospection → closing) | Bas | Processus simples, produits standardisés |
| **2-Stages SDR+AE** | SDR prospecte, AE ferme ; Inbound/Outbound séparés | Moyen | Circuits complexes, vente consultative, qualité de passation cruciale |
| **Field Sales** | Expert sectoriel/zone/type d'acteur, ~50 comptes, appui Sales Engineer | Élevé | Produits forte valeur ajoutée, expertise nécessaire |
| **Named Accounts** | Liste de ~8 grands comptes clés, ultra-personnalisée | Très élevé | Très grands comptes stratégiques, dépendance CA |

**Variante PLS (Product-Led Sales)** : même self-serve en amont, mais détection des 3% meilleurs utilisateurs + intervention commerciale pour les convertir. Prérequis : que le PLG fonctionne déjà très bien.

### Le GTM = chaîne horizontale

Ce n'est pas un département, c'est **Marketing → Sales → Customer Success**, avec le **Produit en soutien**. Les 3 équipes doivent être alignées sur :
- Langage commun (voir `icp-segmentation-spiced.md`)
- Niveau d'expertise/séniorité cohérent entre les 3 équipes pour un même client
- Mêmes objectifs (OKR partagés)
- Ateliers mixtes, PODs

### Ce que les clients achètent n'est pas la même chose

| Critère | Petit client (ACV faible) | Grands comptes (ACV élevé) |
|---|---|---|
| Ce qu'ils achètent | **Le produit** | **Le service** |
| Curiosité produit | Forte | Faible (commodité) |
| Autonomie | Élevée | Faible |
| Interactions attendues | Minimales | Fréquentes (service premium) |
| Critères d'achat | Fonctionnalités et coût | Résultats et accompagnement |

Corollaire coach : *"Pour les grands comptes, le produit devrait être gratuit. Ce qu'ils achètent c'est le service."*

### Seuils empiriques (ARR) pour ouvrir un nouveau GTM

- **5 M€ d'ARR** (US : 10 M$) minimum sur un 1er GTM avant d'en lancer un 2nd
- **20 M€ d'ARR** (US : 50 M$) minimum pour tenir 2 GTM avant d'en envisager un 3ème

Sans ces seuils, la dispersion des ressources tue les deux motions.

### 3 logiques de croissance différentes selon la motion

1. **PLG** : produit incroyable, expérience utilisateur irréprochable → **utilisateurs = moteur** (bouche-à-oreille, viralité)
2. **MidMarket** : stratégie de contenu + événements → **Thought Leadership** (HubSpot = référence sur le CRM)
3. **Grands Comptes** : marque + réputation individuelle des collaborateurs → **pattern McKinsey** (le CEO CAC40 achète la marque + le pedigree)

### Les 5 erreurs classiques de GTM

1. **Décalage ACV ↔ organisation GTM** — *Slide montré en premier de 95% des diagnostics.*
2. **Oublier que les clients n'achètent pas la même chose** (produit vs service).
3. **Ne regarder que l'ACV de départ**, pas la valeur cible (land & expand : Crédit Agricole Picardie signé 20k€ mais l'enjeu = toutes les caisses).
4. **Incohérence entre départements** (Marketing ABM + Sales 2-stages + CS Helpdesk = incohérent). Souvent effet du turnover : managers qui importent leurs recettes passées sans cohérence.
5. **Instabilité** : promouvoir un top performer PLG/MidMarket vers Grands Comptes ou Management sans accompagnement = triple perte (nouveau rôle raté + ancien affaibli + démission probable).

### 5 organisations Customer Success (mêmes axes)

Self-Serve/Communauté → Helpdesk → Volume → Segment → Comptes dédiés.

4 critères de distinction : effort du client, canaux accessibles, expertise CSM, dédicace au compte.

### Intégrer le Produit au GTM — 3 leviers

1. **Mettre du liant** : bureaux partagés, Product Marketing au centre, accès roadmap temps réel via IA.
2. **Revoir la culture** : customer-centric, PMM qui fait des cold calls/démos chaque mois, empathie au recrutement.
3. **Évaluer les features sur 3 critères** :
   - **Impact New Business**
   - **Impact Rétention**
   - **Faisabilité technique**

**Règle des "features paillettes"** : allouer **5-10% de la roadmap** à des features non utilisées mais déclencheuses d'achat (ex : Time Slider, visualisations 3D). Ce n'est pas un dévoiement, c'est une allocation consciente.

### 4 rôles de partenaires

| Rôle | Contribution | Étape bowtie |
|---|---|---|
| Revendeurs | Vendent pour vous | Selection → Onboard + Expansion |
| Partenaires stratégiques | Améliorent la valeur (complémentarité) | Awareness-Selection + Adoption-Expansion |
| Intégrateurs | Mettent en place dans systèmes complexes | Selection → Adoption |
| Apporteurs d'affaires | Affiliation, font connaître | Awareness / Education |

Marathon de 6-12 mois, risque de réputation, moins de contrôle, équilibre économique différent. **Pas adapté en Product-Market Fit** : gardez le lien direct.

### RACE — synthèse stratégique

- **R**aisonnez en GTM (pas en silos fonctionnels)
- **A**doptez une organisation pour le long terme
- **C**ontrôlez l'efficience dans la durée (trimestre par trimestre)
- **E**ngagez-vous sur les batailles clés du succès

## Application pratique

Un PM utilise ce framework pour :

1. **Trancher un débat packaging** : faut-il un tier self-serve "light" ? Dépend du seuil ARR et de la maturité du GTM principal.
2. **Filtrer les demandes features** : matrice 3D Impact New Business × Impact Rétention × Faisabilité. Une feature qui maximise New Business mais dégrade Rétention = arbitrage explicite.
3. **Orienter la découverte** : en PLG on parle à l'utilisateur ; en Grands Comptes on parle à un Champion + un Décideur + un Gatekeeper (cf. `icp-segmentation-spiced.md`).
4. **Prévenir un pivot dangereux** : si l'investisseur pousse à ouvrir PLG alors qu'on n'a pas 5M€ sur SLG, il faut dire non (ou ralentir).
5. **Évaluer les exigences enterprise** : quand un Grand Compte demande cert RSE / archi cloud souveraine / hébergement dédié, ces exigences tuent-elles la rentabilité d'une motion MidMarket ? Si oui, il faut un GTM Grands Comptes séparé (avec son P&L).

### Questions à se poser

- Quelle est l'ACV cible (pas de départ) du segment ?
- Les 3 couches (Marketing + Sales + CS) sont-elles cohérentes sur ce segment ?
- Sommes-nous au seuil ARR pour lancer/tenir cette motion ?
- Les exigences enterprise (sécurité, archi, RSE) sont-elles financées par le tarif du segment ?
- Cette feature passe-t-elle les 3 critères (New Business / Rétention / Faisabilité) ?

## Signaux / anti-patterns

**Bien appliqué :**
- Un GTM par P&L, chacun avec ses propres KPIs et playbook.
- La roadmap est catégorisée en % par segment (PLG / MidMarket / Grands Comptes).
- 5-10% de "features paillettes" assumées et pilotées consciemment.
- Les Sales Grands Comptes savent qu'ils vendent un service, pas un produit.
- Les partenaires (intégrateurs, revendeurs) ont un QBR, KPIs partagés, sponsor exécutif.

**Anti-patterns :**
- Un unique reporting commercial qui mélange PLG et Grands Comptes.
- Un commercial "full-cycle" SDR+AE+CSM qui gère tout (ne tient que sur deals très simples).
- Marketing en ABM alors que Sales est en 2-stages et CS en Helpdesk (incohérence = slide 43 erreur 4).
- Promotion d'un AE MidMarket → AE Grands Comptes sans coaching. Triple perte en vue.
- "On a 3 utilisateurs chez Total donc on a une stratégie Enterprise" — non, c'est de l'acquisition opportuniste PLG.
- Partenaires signés "et on verra" — pas de sponsor exécutif, pas de KPI, pas de QBR.
- Produit Frankensteinisé par l'accumulation de demandes Sales, sans grille New Business / Rétention / Faisabilité.

## Questions pour challenger une décision Galigeo

1. **Où est Galigeo sur l'axe des motions ?** TM Grand Compte retail/banque/assurance/foncière = probablement Field Sales ou Named Accounts. RetailFocus = plus léger, peut être 2-stages voire PLS. Org = SaaS pur, probablement 2-stages. Cette cartographie est-elle explicitée dans l'organisation, ou traite-t-on tous les deals avec la même motion ?
2. **Décalage ACV vs GTM (erreur n°1)** : quel est l'ACV moyen réel par segment et par produit ? Cohérent avec l'équipe Sales qui le couvre ? Si un Network Manager achète RetailFocus à 5k€/an mais est suivi par un AE sénior dédié, il y a décalage (coût ressource > rentabilité).
3. **ACV de départ vs cible** : un contrat signé avec une caisse régionale banque à 20k€, l'enjeu c'est **toutes les caisses** (land & expand). Qui, chez Galigeo, dimensionne l'effort commercial et CS sur la valeur cible 115k€+ plutôt que les 20k€ signés ?
4. **Cohérence des 3 couches sur TM retail** : Marketing fait-il du contenu Thought Leadership (Dir Dev retail) ou de la prospection quantitative ? Sales est en Field Sales ? CS est en segment ou comptes dédiés ? Si les 3 ne s'empilent pas proprement (slide 33 WbD), c'est un signal rouge.
5. **Seuils ARR** : Galigeo a-t-il passé 5M€ ARR stables sur un premier GTM avant de lancer RetailFocus et Org comme GTM parallèles ? 20M€ pour en tenir 2 ? Si non, on disperse.
6. **Exigences enterprise qui tuent la rentabilité** : quand un Grand Compte banque demande archi cloud souveraine + cert ISO + audit RSE annuel, ces exigences sont-elles prises en compte dans le tarif, ou absorbées comme surcoût sur le P&L MidMarket ? Faut-il un GTM Grands Comptes séparé ?
7. **Features paillettes chez Galigeo** : le "Time Slider" cité par le coach, ou les visualisations 3D, heatmaps — combien de % de la roadmap y est alloué consciemment ? Ou sont-elles développées en mode "les Sales demandent, on fait" sans arbitrage ?
8. **Matrice 3 critères (New Business / Rétention / Faisabilité)** : appliquée systématiquement aux demandes features ? Par qui ? Gardien du playbook nommé ? Les arbitrages sont-ils tracés ou la roadmap est-elle un puits sans fond ?
9. **Lancement PLG de RetailFocus** : si on le fait, comment éviter de cannibaliser la motion SLG ? Quelle segmentation fonctionnelle ? Règles d'engagement (qui "possède" un compte qui arrive via PLG et monte en gamme) ? Le coach prévient : "les Sales SLG perdent en motivation si PLG prend les deals faciles".
10. **Promotion d'un AE retail vers banque ou assurance** : la séniorité technique/sectorielle est-elle vraiment interchangeable, ou importe-t-on des réflexes retail qui fonctionneront mal en banque (cycle plus long, Decision multi-têtes, exigences réglementaires) ? Plan de coaching prévu ?
11. **PMM chez Galigeo** : existe-t-il, et fait-il des cold calls/démos régulières ? Est-il au centre entre Product et Sales ? Ou y a-t-il un "doc roadmap de 200 pages" illisible (cas cité par le coach) ?
12. **Partenaires** (Esri, intégrateurs Geo, intégrateurs retail) : ont-ils un sponsor exécutif Galigeo, des KPIs partagés, un QBR ? Ou sont-ce des accords commerciaux dormants ? Le coach : "Ne partenarisez pas trop tôt, gardez le lien direct en PMF."

## Citations-clés du coach

- "Ce qui fait votre succès c'est pas votre produit, c'est comment vous ciblez, éduquez, vendez, accompagnez : c'est votre GoToMarket."
- "Les grands comptes, les utilisateurs sont les plus mauvais. Ce qu'ils achètent c'est un partenaire qui va les prendre par la main. Le produit devrait être gratuit — ce qu'ils paient c'est le service."
- "J'ai des responsables produits qui allouent 5 ou 10% de la roadmap à des features qu'on sait qui ne seront utilisées par personne, mais qui font vendre."
- "Pour se permettre d'avoir 2 GTM en parallèle : en moyenne 20 M€ d'ARR. Pour un seul bien stabilisé avant d'en ouvrir un autre : 5 M€ minimum."
- "C'est le slide que je montre en premier de 95% de mes diagnostics : décalage entre l'ACV et l'organisation GTM."
- "Il faut faire accepter le deuil, notamment aux fondateurs qui viennent du produit : à un moment donné, la clé du succès long terme c'est pas que ça."

## Liens

- Sessions sources : [../sessions/01-business-models.md](../sessions/01-business-models.md), [../sessions/03-plg-to-slg.md](../sessions/03-plg-to-slg.md), [../sessions/04-stades-de-croissance.md](../sessions/04-stades-de-croissance.md)
- Frameworks connexes :
  - [bowtie-winning-by-design.md](bowtie-winning-by-design.md) — un bowtie par GTM
  - [business-models-saas.md](business-models-saas.md) — le BM conditionne le GTM
  - [icp-segmentation-spiced.md](icp-segmentation-spiced.md) — le cadre commun aux 3 couches du GTM
  - [growth-stages-gtm.md](growth-stages-gtm.md) — quand ouvrir un nouveau GTM selon le stade
