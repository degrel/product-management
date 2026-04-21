---
name: Business Models SaaS — Arc Propriété ↔ Abonnement ↔ Consommation
type: framework
sources:
  - Session 1 (Business Models) — slides 38-78, 92-100
  - Session 2 (Mesurer et analyser la performance) — slides 3-4, 10-11, 60-65
  - Session 4 (Stades de croissance) — slides 14, 35, 41
---

# Business Models SaaS — Arc Propriété ↔ Abonnement ↔ Consommation

## Definition

Le Business Model d'une entreprise SaaS se lit sur un **arc à 3 zones** : **Propriété** (engagement à l'avance, perpétuel), **Abonnement** (engagement récurrent, pluriannuel → mensuel), **Consommation** (engagement à l'impact/usage, freemium). Chaque zone impose une **cohérence sur 3 dimensions de vente** (cycle, taux de réussite, politique de remise) et son propre modèle d'unit economics (CAC payback, LTV/CAC, NRR, Rule of 40). Un Business Model est **adapté à un segment de marché** — une entreprise peut en avoir plusieurs, mais ils doivent être pilotés séparément.

## Pourquoi c'est important

Pour un PM, le Business Model détermine :
- **Ce que le client achète** (propriété d'une IP, accès récurrent, résultats/usage) → détermine le packaging produit.
- **La durée d'engagement possible** → détermine la granularité des cycles de release (annuel ≠ mensuel).
- **Où est le risque** (acheteur côté propriété, vendeur côté usage/freemium) → détermine la politique de remise et l'effort de CS/produit post-closing.
- **La valorisation par les investisseurs** : revenus **récurrents** vs **ré-récurrents** vs **one-shot** ne se valorisent pas pareil. Un contrat pluriannuel ≠ ARR pur.
- **Le chemin de croissance** : Rule of 40, T2D3, NRR, Règles de franchissement (Seed→A = 1/2, A→B = 1/2, B→C = 1/3, IPO = 1%).

Mal aligner ces éléments = piloter à l'aveugle (ex : traiter un deal abonnement comme une propriété, remiser comme si le risque était côté acheteur).

## Le framework en détail

### L'arc des Business Models

```
Engagement à l'avance ◄──────────────── Engagement récurrent ────────────────► Engagement à la consommation

   PROPRIÉTÉ                              ABONNEMENT                           CONSOMMATION
┌────────────────┐     ┌──────────────────────────────────────────┐     ┌──────────────────────────┐
│ Matériel       │     │ Pluriannuel │ Annuel │ Trimestriel │ Mensuel │     │ Usage │ Impact │ Freemium│
│ Matériel+Suppt │     │             │        │             │        │     │       │        │         │
│ Logiciel perp. │     │                                             │     │                          │
└────────────────┘     └──────────────────────────────────────────┘     └──────────────────────────┘
```

- **Propriété** : l'acheteur paie d'avance, responsable de tirer la valeur.
- **Abonnement** : l'acheteur paie une redevance récurrente pendant la période contractuelle, n'en devient jamais propriétaire.
- **Consommation** : l'acheteur paie pour son usage — plus il utilise, plus il paie.

### Cohérence des 3 dimensions de vente (à ne jamais casser)

| Zone BM | Durée cycle de vente | Taux de réussite | Qui porte le risque |
|---|---|---|---|
| **Propriété** | 9-18 mois (jusqu'à 3 ans) | 1 sur 3 | **Acheteur** → remise possible |
| **Abonnement** | 10 jours à 6 mois | 1 sur 5 | Mixte, bascule vers vendeur | 
| **Usage** | Heures à secondes | 1 sur 10 | **Vendeur** → remise restrictive |
| **Impact / Freemium** | Heures à secondes | 1 sur 8 | Vendeur (maximal) | 

**Conséquence pricing** : plus le risque est côté vendeur, plus la politique de remise doit être restrictive. On ne remise pas un abonnement mensuel comme un deal propriétaire.

### Distinguer 3 types de revenus

| Type | Définition | Valorisation |
|---|---|---|
| **Récurrent (ARR/MRR)** | Engagement contractuel sur une période définie, re-facturé automatiquement | Forte, multiples élevés |
| **Ré-récurrent** | À échéance variable (déploiement d'un nouveau site, formation de nouvelles équipes) | Moyenne |
| **One-shot (ponctuel)** | Setup, développements spécifiques, audits uniques | Faible |

**Critère pour distinguer ARR vs one-shot** : la propriété intellectuelle.
- Spécifique au client → plutôt one-off
- Liée à l'expertise du fournisseur, réutilisable → plutôt récurrent

### Professional Services hybrides (4 types)

1. **Implémentation** (plan projet)
2. **Onboarding** (utilisateurs)
3. **Expertise post-implémentation** : fonctionnel paramétrique / métier / technique (interconnexion)
4. **Développements spécifiques**

Certains PS sont variabilisables en ARR (maintenance, support, audit annuel), d'autres restent du ré-récurrent (déploiement nouveau site), d'autres ponctuels. **Attention** : variabiliser un projet complexe peut être contre-productif — le client peut penser que vous avez sous-estimé l'ampleur.

### Unit economics : les 4 repères

**CAC payback** (Bessemer, "Scaling to $100M" 2021) — temps pour récupérer le CAC par tranche d'ARR :

| Tranche ARR | CAC payback |
|---|---|
| $1-10M | 15 mois |
| $10-25M | 24 mois |
| $25-50M | 20 mois |
| $50-100M | 21 mois |
| $100M+ | 30 mois |

**LTV/CAC** (repère Bessemer) :

| Ratio | Appréciation |
|---|---|
| 3 | Standard |
| 4 | Excellent |
| > 5 | On pourrait investir plus (on laisse du revenu sur la table) |

**Formule LTV** (tableur) : `LTV = -FV((Rétention × Expansion) − 1, Nb_périodes, ACV_départ)`
- Avec augmentation tarifaire contractuelle : `-FV((Rétention × Augmentation × Expansion) − 1, N, ACV)`
- Rétention et Expansion sont les leviers CS ; ACV_départ est le levier Sales+Marketing.
- **Tout le GTM contribue à la LTV.**

**Conséquence** : si CAC payback = 24 mois et attente LTV/CAC = 3, il faut garder le client **3 × 24 = 6 ans** pour justifier l'acquisition.

### GRR vs NRR

- **GRR (Gross Revenue Retention)** : mesure uniquement ce qui reste du revenu initial (churn seul). Jamais > 100%.
- **NRR (Net Revenue Retention)** : GRR + Expansion − Contraction. Peut dépasser 100%.
- Formule : **NRR = (MRR_début + Expansion − Contraction − Churn) / MRR_début**
- **Les investisseurs regardent le NRR**. Mais ne jamais regarder qu'au global : un NRR élevé peut cacher un churn caché sur un périmètre fonctionnel, compensé par un upsell ailleurs.

### Rule of 40 et T2D3

- **Rule of 40** : Taux de croissance (%) + Taux de rentabilité (%) ≥ 40% = santé financière. Ex : 30% croissance + 10% marge = 40%.
- **T2D3** (Triple, Triple, Double, Double, Double) : loi d'hypercroissance Tech. Tripler 2 ans, puis doubler 3 ans. Exemple Datadog : 1,2 → 4 → 12 → 24 → 52 → 89 M$.

### Transformations de Business Model : prennent du temps

- Perpétuel → Abonnement (ex : lancement produit SaaS depuis un existant licence).
- Annuel → Pluriannuel (sécuriser le revenu, grands comptes et public).
- Abonnement → Usage (gagner scalabilité et vélocité ; 1 à 2 ans pour monter en puissance).

Repère coach : **Microsoft et Adobe ont mis ~9 ans** pour transitionner. Ne pas sous-estimer le coût de maintenir plusieurs BM en parallèle (double des moyens et efforts).

## Application pratique

Un PM utilise ce framework pour :

1. **Cadrer le positionnement d'un produit** : où est-il sur l'arc ? Est-ce cohérent avec le cycle de vente observé et la politique de remise ?
2. **Challenger un pricing** : un contrat pluriannuel remisé lourdement ne gagne pas en valeur (la valorisation investisseur diminue car on "mange" la growth future).
3. **Trancher "récurrent vs one-off"** en packaging : l'IP Galigeo doit-elle être vendue comme un livrable ponctuel ou comme un abonnement ?
4. **Estimer un effort produit** : si le BM exige de garder le client 6 ans, la roadmap doit allouer autant d'effort à l'adoption/expansion qu'à l'acquisition.
5. **Évaluer une décision CS** : avant de sur-investir en CSM, vérifier le CAC payback et la LTV attendue.

### Questions à se poser

- Sur quelle zone de l'arc est ce produit ? Et sa politique tarifaire ?
- Les 3 dimensions (cycle, win rate, remise) sont-elles cohérentes ?
- La LTV observée (sur données réelles 3 ans) permet-elle un LTV/CAC ≥ 3 ?
- Le NRR est-il > 100% et bien segmenté ? Cache-t-il un churn caché ?
- Si on ajoute un nouveau BM, a-t-on les moyens de le doubler pendant 2-3 ans ?

## Signaux / anti-patterns

**Bien appliqué :**
- Chaque BM a son propre P&L, son propre playbook, son propre dashboard.
- La politique de remise est claire, graduée par zone.
- Le NRR est lu par segment et par module, pas seulement global.
- L'ARR déclaré aux investisseurs exclut explicitement le ré-récurrent et le one-shot.

**Anti-patterns :**
- "Nous avons 3M€ d'ARR" alors qu'il y a 1M€ de services ré-récurrents dedans.
- Remise de 30% sur un deal abonnement mensuel (risque vendeur maximal, remise doit être minimale).
- Migration "on lance un self-serve" sans alignement du cycle de vente ni de la politique de remise ni du niveau de support.
- Un Business Model hybride (SaaS + PS lourds) piloté avec des KPIs uniformes.
- Sur-estimer sa capacité à tenir 2 BM en parallèle sans doubler les équipes.

## Questions pour challenger une décision Galigeo

1. **Galigeo opère-t-il un seul Business Model ou plusieurs ?** TM (abonnement annuel/pluriannuel grand compte), RetailFocus (zone study — one-shot projet ou abonnement ?), Org management (SaaS pur). Chaque produit a-t-il sa propre politique de pricing, son propre cycle, son propre win rate ? Sont-ils pilotés séparément ou consolidés dans un unique reporting qui ment ?
2. **Où est RetailFocus sur l'arc ?** Si le produit ressemble à une étude de zone ponctuelle (one-shot), le cycle 9-18 mois et un win rate 1/3 doivent être la norme. Si on veut le migrer vers abonnement ("zone studies illimitées"), le cycle doit passer à 10j-6 mois, le win rate à 1/5, et la politique de remise devenir plus restrictive. Avez-vous modélisé ces 3 dimensions avant de lancer la migration ?
3. **CAC payback par produit** : à notre tranche d'ARR, on devrait viser 15-24 mois. TM grand compte (cycle long, sales heavy) peut avoir un CAC énorme ; le LTV/CAC tient-il la route sur retail/banque/assurance séparément ?
4. **Revenus récurrents vs ré-récurrents** : l'ARR Galigeo contient-il du MRR contractuel, ou des renouvellements annuels négociés (ré-récurrents déguisés) ? Un investisseur valoriserait très différemment. La méthodologie RetailFocus (IP Galigeo, réutilisable chez plusieurs clients) devrait-elle migrer vers le récurrent plutôt que rester one-off ?
5. **NRR par module et par persona** : TM a-t-il un NRR > 100% ? Cache-t-il un churn sur RetailFocus ou Org compensé par upsell TM ? Comment évolue le NRR par segment (retail vs banque vs assurance) ?
6. **Clauses d'augmentation tarifaire** : les contrats pluriannuels Galigeo incluent-ils +5%/an automatique ? Si oui, c'est justifié par la R&D (nouvelles features) ou juste l'inflation ? Votre LTV modélisée intègre-t-elle ce levier ?
7. **Cohérence remise/risque sur un deal banque** : un Dir Dev banque s'engage pluriannuel → risque bascule vers vendeur → remise doit être restrictive. Si la politique de remise uniforme Galigeo autorise -20% sur un deal banque pluriannuel, il y a incohérence.
8. **Transformation BM** : si on veut migrer RetailFocus vers un pur SaaS abonnement, est-on prêt à doubler les moyens (Sales équipés pour cycle court + CS équipés pour onboarding rapide + Produit pour self-serve) pendant ~2-3 ans ? Microsoft/Adobe = 9 ans.
9. **Hybride PS lourds** : quelle part de la facturation Galigeo est de l'implémentation / onboarding / expertise / dev spécifique ? Les 4 types sont-ils identifiés et tarifés séparément ? La variabilisation en récurrent est-elle systématique ou au cas par cas ?
10. **Rule of 40 et stade** : où est Galigeo aujourd'hui (croissance % + rentabilité %) ? Si < 40%, c'est le signal d'un arbitrage stratégique (soit +croissance, soit +rentabilité).

## Citations-clés du coach

- "Il convient de distinguer les revenus récurrents et les revenus ré-récurrents : le ré-récurrent est à échéance variable, vous ne pourrez pas le valoriser de la même manière."
- "Microsoft et Adobe ont mis environ 9 ans pour transitionner vers le SaaS. Il ne faut pas surestimer sa capacité à avoir plusieurs Business Models."
- "Si ça vous prend 24 mois pour récupérer votre CAC et que vos investisseurs attendent un LTV/CAC = 3, il faut que vous gardiez le client 6 ans."
- "Un bon Business Model s'aligne sur la valeur perçue par le client — pas sur les moyens (gigaoctets, licences)."
- "Vous ne pouvez faire de l'upsell et du cross-sell que sur des clients que vous gardez. Donc la base de votre calcul pour l'expansion c'est pas les 100 000, c'est ce qui vous reste en résidu après le churn."

## Liens

- Sessions sources : [../sessions/01-business-models.md](../sessions/01-business-models.md), [../sessions/02-mesurer-analyser-performance.md](../sessions/02-mesurer-analyser-performance.md), [../sessions/04-stades-de-croissance.md](../sessions/04-stades-de-croissance.md)
- Frameworks connexes :
  - [bowtie-winning-by-design.md](bowtie-winning-by-design.md) — le funnel sur lequel se calcule LTV/CAC
  - [plg-vs-slg-decision.md](plg-vs-slg-decision.md) — le choix de motion dépend du BM
  - [growth-stages-gtm.md](growth-stages-gtm.md) — CAC payback, T2D3, Rule of 40 détaillés
