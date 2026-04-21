# Knowledge — Revenue Architecture

Base de connaissance dérivée de la formation **"Leadership du revenu"** (Collective Impact, formateur : coach certifié Winning by Design). 5 sessions, 363 slides, ~70 000 lignes de transcript.

Cette base sert à challenger les décisions produit/roadmap/UX d'un PM chez Galigeo qui gère des produits **PLG + SLG simultanés** (Territory Manager, RetailFocus, Org management).

## Quand utiliser cette base

- Tu prends une décision produit qui touche au revenu (pricing, packaging, onboarding, expansion, churn)
- Tu arbitres entre deux motions (PLG vs SLG, self-serve vs sales-assisted)
- Tu challenges ta roadmap, ton ICP, ton modèle de données
- Tu prépares un pitch C-Level sur la stratégie de croissance
- Tu rédiges un PRD, une OKR, un business case

Déclenche le skill **`/pm-revenue`** ou charge manuellement les fichiers ci-dessous.

## Structure

### `sessions/` — Notes de session
Contenu slide-par-slide + citations du coach, 1 fichier par session.

| Fichier | Thème | Slides |
|---------|-------|--------|
| [01-business-models.md](sessions/01-business-models.md) | Fondations Leadership Revenu, Business Models, Bowtie | 110 |
| [02-mesurer-analyser-performance.md](sessions/02-mesurer-analyser-performance.md) | Modèle de données, bow-tie, gains marginaux, benchmarks | 83 |
| [03-plg-to-slg.md](sessions/03-plg-to-slg.md) | **GTM horizontal, 5 motions sales, PLG ↔ SLG** | 65 |
| [04-stades-de-croissance.md](sessions/04-stades-de-croissance.md) | Courbe en S, camp de base, 14 points de passage | 53 |
| [05-deploiement-go-to-market-spiced-icp-coaching.md](sessions/05-deploiement-go-to-market-spiced-icp-coaching.md) | Déploiement GTM, SPICED, ICP, coaching | 52 |

### `frameworks/` — Frameworks transversaux
Auto-suffisants : chaque fichier peut être chargé seul pour challenger un angle précis.

| Framework | Usage |
|-----------|-------|
| [bowtie-winning-by-design.md](frameworks/bowtie-winning-by-design.md) | Funnel CR1-CR8, VM1-VM8, analyse couple d'indicateurs, benchmarks |
| [business-models-saas.md](frameworks/business-models-saas.md) | Arc Propriété/Abo/Conso, LTV/CAC, NRR, Rule of 40, T2D3 |
| [plg-vs-slg-decision.md](frameworks/plg-vs-slg-decision.md) | **5 motions Sales, seuils 5/20 M€, features paillettes** |
| [icp-segmentation-spiced.md](frameworks/icp-segmentation-spiced.md) | SPICED, Tiers 1/2/3, Impact rationnel/émotionnel, matrice expansion |
| [growth-stages-gtm.md](frameworks/growth-stages-gtm.md) | 4 stades, camp de base, 14 points de passage, tours de table |
| [coaching-performance-culture.md](frameworks/coaching-performance-culture.md) | RESA, Deming 85/15, scorecards, gains marginaux |

### `glossaire.md`
Tous les sigles (VM, CR, T, NRR, GRR, SPICED, ICP, Tier, PLG, SLG, PLS, Named Accounts, etc.). Charger en complément quand un sigle inconnu apparaît.

### `challenge-prompts.md`
10 prompts prêts à l'emploi pour challenger ton ICP, ta roadmap, tes KPIs, ton onboarding, ton pricing, ta stratégie GTM, etc. Contextualisés Galigeo.

## Stratégie de chargement

**Claude ne charge PAS tout**. Pour une conversation donnée :

1. Si la question est vague : charge ce `README.md` et laisse Claude décider.
2. Si la question touche un concept précis : charge le ou les 1-2 `frameworks/*.md` pertinents.
3. Si la question demande la parole exacte du coach : charge le `sessions/*.md` correspondant.
4. Si un sigle bloque : ajouter `glossaire.md`.

Voir `CLAUDE.md` pour les règles de chargement détaillées du skill `pm-revenue`.

## Sources

Matériel source extrait depuis la formation "Leadership du revenu" de **Collective Impact France** (5 sessions × ~2h, 363 slides, ~70 000 lignes de transcript VTT). Les fichiers originaux (PDFs + VTTs) ne sont pas conservés dans ce dépôt — les frontmatter des fichiers `sessions/*.md` en gardent trace (`source_pdf:`, `source_vtt:`). Pour récupérer les originaux : contacter Collective Impact.
