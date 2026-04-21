---
name: Glossaire revenue
type: glossary
---

# Glossaire — Leadership du revenu

Termes utilisés par Collective Impact et le modèle Winning by Design. À charger quand on rencontre un sigle inconnu dans une session ou un framework.

## Modèle de données Winning by Design (Bowtie)

### Volume metrics (VM)
| Code | Nom | Définition |
|------|-----|------------|
| VM1 | Prospects | Volume d'identifiés en haut de funnel |
| VM2 | MQLs | Marketing Qualified Leads |
| VM3 | Opportunités | Nombre d'opportunités ouvertes (après qualification SDR/AE) |
| VM4 | Engagés | Opportunités passées en phase Commit |
| VM5 | # Wins | Nouveaux clients signés sur la période |
| VM6 | Clients actifs | Base renouvelée |
| VM7 | ARR départ | Revenu récurrent annualisé en début de période |
| VM8 | LTV | Lifetime Value d'un client |

### Conversion rates (CR)
| Code | Nom | Étape du funnel |
|------|-----|-----------------|
| CR1 | Awareness → Education | Trafic → lead |
| CR2 | Education → Selection (MQL) | Lead → MQL |
| CR3 | Passation SDR → AE | MQL → SQL (Sales Accepted) |
| CR4 | Win Rate | Opportunité → client (Commit) |
| CR5 | Onb churn | % de clients qui quittent pendant l'onboarding |
| CR6 | Churn | % de clients qui ne renouvellent pas |
| CR7 | Expansion | Taux d'expansion (upsell / crossell / resell) |
| CR8 | Ratio d'expansion | Multiplicateur ARR par client existant |

### Durées-clés (T)
- **T1** : Durée phase Awareness/Education
- **T2** : Durée phase Selection
- **T3** : Durée phase Commit (négociation)
- **T4** : Durée cycle de vente total (T1+T2+T3)
- **T5** : Durée d'onboarding
- **T6** : Temps avant première expansion

## Revenu récurrent

- **MRR** : Monthly Recurring Revenue
- **ARR** : Annual Recurring Revenue (= MRR × 12)
- **NRR** (Net Revenue Retention) = (MRR début + Expansion − Contraction − Churn) / MRR début. > 100 % = expansion couvre le churn. Seuil scale-up : viser 110–130 %.
- **GRR** (Gross Revenue Retention) = (MRR début − Contraction − Churn) / MRR début. Ne compte pas l'expansion. Mesure la « santé pure » de la base.
- **Contraction** : Downgrade d'un client existant
- **Churn** : Perte complète d'un client
- **Expansion** : Upsell, Crossell, Resell

## Économie unit

- **ACV** (Annual Contract Value) : Valeur annuelle d'un contrat
- **TCV** (Total Contract Value) : Valeur totale (engagement pluriannuel inclus)
- **CAC** (Customer Acquisition Cost) : Coût d'acquisition d'un client
- **CAC Payback** : Nombre de mois pour rembourser le CAC avec la marge brute du client. Benchmarks Bessemer : ≤12 mois (excellent), 12–24 (bon), >24 (attention).
- **LTV** (Lifetime Value) : Revenu total attendu d'un client sur sa durée de vie. Formule = `-FV((Rétention × Expansion) − 1, durée, ACV)`
- **Ratio LTV/CAC** : Cible = 3. En dessous, le modèle ne finance pas son propre marketing.
- **Rule of 40** : Croissance ARR (%) + Marge EBITDA (%) ≥ 40. Indicateur santé financière SaaS.
- **T2D3** : Triple Triple Double Double Double. Trajectoire idéale ARR post-Série A : ×3, ×3, ×2, ×2, ×2 sur 5 ans → ×72.

## Motions Go-To-Market

| Motion | Sigle | Axe No-touch → Dedicated |
|--------|-------|--------------------------|
| **PLG** | Product-Led Growth | Le produit fait le marketing et la vente (self-serve) |
| **PLS** | Product-Led Sales | PLG + détection des 3 % top users pour sales touch |
| **MLS** | Marketing-Led Sales | Marketing génère des leads pour les sales |
| **SLG** | Sales-Led Growth | Sales assisté, cycle long, multi-décideurs |
| **ISR 1-Stage** | Inside Sales Rep | 1 vendeur gère tout le cycle |
| **2-Stages SDR+AE** | SDR puis AE | SDR prospecte, AE ferme |
| **Field Sales** | Vente terrain | Expert secteur/zone, ~50 comptes |
| **Named Accounts** | Grands Comptes nommés | Liste fermée de ~8 comptes stratégiques |

## Rôles commerciaux

- **SDR** : Sales Development Rep — prospecte, qualifie, passe au closer
- **BDR** : Business Development Rep — équivalent SDR orienté outbound
- **AE** : Account Executive — ferme les deals
- **ISR** : Inside Sales Rep — gère le cycle complet (inbound, courts cycles)
- **AM** : Account Manager — gère les comptes existants (expansion)
- **CSM** : Customer Success Manager — adoption, rétention, expansion
- **SE** : Sales Engineer — expertise technique en appui de l'AE
- **SDR/AE 2-stages** : Modèle le plus répandu en B2B MidMarket

## Marketing

- **Inbound** : Attirer via contenu à valeur (SEO, content, nurturing)
- **Outbound** : Contact proactif
  - **Prospection** : 1-to-many
  - **ABM** (Account Based Marketing) : 1-to-few
  - **Target** : 1-to-1

## ICP & qualification

- **ICP** (Ideal Customer Profile) : Profil client idéal (segment entreprise)
- **Persona** : Profil humain au sein de l'ICP (décideur, utilisateur, gate-keeper)
- **Tier 1 / 2 / 3** : Priorisation des prospects dans l'ICP
- **Champion** : Personne interne chez le prospect qui vend le produit en interne
- **Critical Event** : Déclencheur dans le temps qui force la décision d'achat
- **Salle de décision** : 7 rôles type dans un achat B2B complexe (utilisateur, acheteur, décideur, influenceur, ratificateur, gate-keeper, saboteur)

## Framework SPICED (Winning by Design)

Langage commun de qualification Marketing/Sales/CS :
- **S**ituation : contexte actuel du prospect
- **P**ain : douleur ressentie
- **I**mpact : ce que la douleur coûte (rationnel + émotionnel)
- **C**ritical Event : moment où il faut agir
- **D**ecision : processus de décision + décideurs

## Autres frameworks mémo

- **RESA** : Résultat = f(Efforts, Savoirs, Aptitudes). Grille de diagnostic performance individuelle.
- **RACE** : Raisonnez GTM, Adoptez long terme, Contrôlez efficience, Engagez-vous. Conclusion Session 3.
- **ECR** : Engagement, Création de valeur, Requête. Structure de prospection.
- **RESULTAT** : Structure de closing de meeting (acronyme non listé ici en détail — voir Session 5).
- **Parcours du héros** : Le client est le héros, pas le vendeur (Winning by Design).
- **Pyramide Deming** : 85 % des problèmes sont dans les systèmes (Process > Tech > Enablement > Skills > Org), 15 % chez les personnes.
- **Pyramide Superstar** : Pyramide inversée instable — dépendance à quelques top performers.
- **Matrice d'expansion 2×2** : Même acheteur / autre acheteur × même impact / autre impact = Renouvellement / Upsell / Crossell / **Resell** (le grand oublié).

## Business Models

- **Arc des BM** : Propriété ↔ Abonnement ↔ Consommation. Chaque position implique une logique cohérente (cycle vente, win rate, risque/remise).
- **Features paillettes** : 5–10 % de la roadmap dédiée à des features qui ne seront pas utilisées mais déclenchent l'achat sur les Grands Comptes.

## Stades de croissance

| Stade | ARR indicatif | Obsession |
|-------|---------------|-----------|
| **Startup** | 0 → 1 M€ | Product-Market Fit (PMF) |
| **Scale-Up** | 1 → 10 M€ | GTM Fit + NRR |
| **Grown-Up** | 10 → 50 M€ | Efficience + multi-GTM |
| **Enterprise** | 50 M€+ | Marque + expansion géographique |

- **PMF** : Product-Market Fit
- **GTM Fit** : Go-To-Market Fit (premier GTM qui marche de manière répétable)
- **Founder Sales Led** : Les fondateurs font la vente eux-mêmes tant que le GTM Fit n'est pas atteint.
- **Camp de base** : 4 fondamentaux avant ascension (BM aligné valeur, Founder Sales Led, Modèle de données, Organisation GTM).

## Benchmarks

- **benchsights.com/wbd** : Outil Winning by Design pour benchmark CR/VM
- **4 niveaux de benchmark** :
  1. Sectoriel (grosse maille)
  2. Pairs (plus précis)
  3. Concurrent direct
  4. Soi-même (chirurgical : équipe/période/zone)
