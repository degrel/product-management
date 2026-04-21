# CLAUDE.md — knowledge/revenue

Règles de chargement pour le skill `pm-revenue` et pour tout assistant qui exploite cette base.

## Ne charge jamais tout

Cette base pèse ~300 KB. Ne la charge pas dans une conversation sauf demande explicite. Utilise la stratégie ci-dessous.

## Règle de chargement

### Étape 1 — Identifier la question

Lis ce que demande le PM. Classe la question :

| Type de question | Exemple | Fichier à charger |
|------------------|---------|-------------------|
| Funnel, conversion, rétention, churn | "Mon CR4 est à 18 %, c'est bon ?" | `frameworks/bowtie-winning-by-design.md` |
| Pricing, unit economics, NRR | "Mon LTV/CAC de 2.4 est-il acceptable ?" | `frameworks/business-models-saas.md` |
| PLG, SLG, motions, self-serve, sales-led | "Faut-il lancer une version self-serve de TM ?" | `frameworks/plg-vs-slg-decision.md` |
| ICP, persona, ciblage, expansion, champion | "Mon ICP mélange 3 personas, est-ce un problème ?" | `frameworks/icp-segmentation-spiced.md` |
| Croissance, tours de table, PMF, GTM Fit | "On est à 3 M€ ARR, faut-il déjà ouvrir un 2e GTM ?" | `frameworks/growth-stages-gtm.md` |
| Recrutement, coaching, performance équipe | "Mon CSM lead sous-performe, que faire ?" | `frameworks/coaching-performance-culture.md` |

### Étape 2 — Besoin d'aller plus loin ?

Si la réponse standard d'un framework ne suffit pas :
- Charge la session complète correspondante depuis `sessions/0N-*.md` pour avoir la parole du coach.
- Charge les frameworks connexes (liens en bas de chaque fichier framework).
- Ajoute `glossaire.md` si des sigles inconnus apparaissent.

### Étape 3 — Question vague / transverse

Si la question porte sur plusieurs frameworks (ex : "Challenge ma stratégie revenue 2026"), alors :
- Propose au PM d'utiliser `challenge-prompts.md` (prompts structurés prêts à l'emploi).
- Ou charge `README.md` + les 3 frameworks pertinents parmi les 6.

## Règles de style

- **Fidélité au coach** : quand tu cites un concept, reste fidèle au vocabulaire du coach (Winning by Design, Collective Impact). Pas de re-traduction en jargon anglo-saxon si le coach utilise le terme français.
- **Chiffres précis** : les seuils (5 M€, 20 M€, LTV/CAC=3, CAC payback <24 mois, NRR 110-130 %, etc.) sont calibrés — ne les arrondis pas.
- **Contexte Galigeo** : quand tu challenges, contextualise avec TM, RetailFocus, Org, personas Galigeo (C-Level, Dir Dev, Dir RE, Data Leaders, Network Managers), clients retail/banque/assurance/real-estate.
- **Français** : même si le PM passe à l'anglais, ce contenu reste en français. Réponds en français.

## Ce que tu ne dois pas faire

- **Ne mélange pas** avec tes connaissances SaaS générales si ça contredit le coach. Ex : le coach distingue "Crossell" (autre acheteur, même impact) et "Upsell" (même acheteur, autre impact) — ne pas confondre avec l'usage vague habituel.
- **Ne sur-interprète pas** : le coach propose des seuils empiriques, pas des lois. Si le PM est dans un cas limite, pose la question "ton contexte est-il typique ?" avant d'appliquer.
- **Ne remplace pas** la discovery : ces frameworks servent à structurer la pensée, pas à donner la réponse. Challenge le PM à aller sur le terrain.

## Déclencheurs d'alerte

Si le PM :
- Mentionne une décision irréversible (lancement produit, restructuration équipe, pricing change) → charge **2 frameworks** et force 5 questions minimum avant de valider.
- Te montre un dashboard de KPIs → vérifier qu'il couvre CR1-CR8 au moins partiellement. Signaler les CR manquants.
- Parle de "scale" sans parler de GTM Fit → charger `growth-stages-gtm.md` et vérifier le camp de base.
