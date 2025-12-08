# BigQuery Schemas Reference

## Overview
This file contains data schemas for Galigeo's BigQuery environment. Update with actual schemas from your data warehouse.

> **Note**: This is a template. Replace with your actual table schemas, relationships, and business logic definitions.

## Core Tables

### Territory Manager (TM)

```sql
-- Table: territories
-- Description: Territory definitions and hierarchy
CREATE TABLE `project.dataset.territories` (
  territory_id STRING NOT NULL,
  territory_name STRING,
  parent_territory_id STRING,
  territory_level INT64,  -- 1=national, 2=regional, 3=local
  geometry GEOGRAPHY,
  created_at TIMESTAMP,
  updated_at TIMESTAMP
);

-- Table: territory_assignments
-- Description: Store-to-territory assignments
CREATE TABLE `project.dataset.territory_assignments` (
  assignment_id STRING NOT NULL,
  store_id STRING NOT NULL,
  territory_id STRING NOT NULL,
  assigned_from DATE,
  assigned_to DATE,
  assignment_type STRING  -- 'primary', 'secondary'
);

-- Table: territory_metrics
-- Description: Aggregated territory performance
CREATE TABLE `project.dataset.territory_metrics` (
  territory_id STRING NOT NULL,
  period DATE NOT NULL,  -- Partitioned by this
  revenue FLOAT64,
  target_revenue FLOAT64,
  store_count INT64,
  active_store_count INT64,
  performance_score FLOAT64,
  market_potential FLOAT64,
  penetration_rate FLOAT64
);
```

### RetailFocus (Zone Studies)

```sql
-- Table: zone_studies
-- Description: Zone study requests and results
CREATE TABLE `project.dataset.zone_studies` (
  study_id STRING NOT NULL,
  study_name STRING,
  study_type STRING,  -- 'new_location', 'cannibalization', 'market_analysis'
  created_by STRING,
  created_at TIMESTAMP,
  status STRING,  -- 'draft', 'in_progress', 'completed'
  center_point GEOGRAPHY,
  isochrone_minutes INT64,
  isochrone_type STRING  -- 'drive', 'walk', 'transit'
);

-- Table: zone_demographics
-- Description: Demographic data for study zones
CREATE TABLE `project.dataset.zone_demographics` (
  zone_id STRING NOT NULL,
  study_id STRING NOT NULL,
  population INT64,
  households INT64,
  avg_household_size FLOAT64,
  avg_income FLOAT64,
  median_age FLOAT64,
  population_density FLOAT64,
  -- Socio-professional categories
  csp_plus_pct FLOAT64,
  csp_minus_pct FLOAT64,
  data_year INT64
);

-- Table: zone_competition
-- Description: Competitor presence in zones
CREATE TABLE `project.dataset.zone_competition` (
  zone_id STRING NOT NULL,
  competitor_id STRING,
  competitor_name STRING,
  competitor_type STRING,  -- 'direct', 'indirect'
  store_count INT64,
  estimated_market_share FLOAT64,
  distance_to_center_m FLOAT64
);
```

### Organizations (Org)

```sql
-- Table: organizations
-- Description: Client organizations
CREATE TABLE `project.dataset.organizations` (
  org_id STRING NOT NULL,
  org_name STRING,
  org_type STRING,  -- 'retail', 'banking', 'insurance', 'services'
  subscription_tier STRING,
  modules_enabled ARRAY<STRING>,
  created_at TIMESTAMP,
  contract_start DATE,
  contract_end DATE
);

-- Table: org_users
-- Description: Users within organizations
CREATE TABLE `project.dataset.org_users` (
  user_id STRING NOT NULL,
  org_id STRING NOT NULL,
  email STRING,
  role STRING,  -- 'admin', 'analyst', 'viewer'
  last_login TIMESTAMP,
  created_at TIMESTAMP
);
```

### Stores & Points of Sale

```sql
-- Table: stores
-- Description: Store/point of sale master data
CREATE TABLE `project.dataset.stores` (
  store_id STRING NOT NULL,
  org_id STRING NOT NULL,
  store_name STRING,
  store_type STRING,
  address STRING,
  city STRING,
  postal_code STRING,
  country STRING,
  latitude FLOAT64,
  longitude FLOAT64,
  location GEOGRAPHY,
  opening_date DATE,
  closing_date DATE,
  surface_sqm INT64,
  status STRING  -- 'active', 'closed', 'planned'
);

-- Table: store_performance
-- Description: Store-level metrics (partitioned by date)
CREATE TABLE `project.dataset.store_performance` (
  store_id STRING NOT NULL,
  date DATE NOT NULL,  -- Partition key
  revenue FLOAT64,
  transactions INT64,
  avg_basket FLOAT64,
  footfall INT64,
  conversion_rate FLOAT64
)
PARTITION BY date;
```

### Usage & Activity

```sql
-- Table: user_events
-- Description: Product usage events
CREATE TABLE `project.dataset.user_events` (
  event_id STRING NOT NULL,
  user_id STRING NOT NULL,
  org_id STRING NOT NULL,
  event_type STRING,
  event_name STRING,
  module STRING,  -- 'tm', 'retailfocus', 'mapping'
  event_properties JSON,
  session_id STRING,
  timestamp TIMESTAMP
)
PARTITION BY DATE(timestamp);

-- Table: feature_usage
-- Description: Aggregated feature usage
CREATE TABLE `project.dataset.feature_usage` (
  org_id STRING NOT NULL,
  feature_name STRING NOT NULL,
  period DATE NOT NULL,
  usage_count INT64,
  unique_users INT64,
  avg_duration_sec FLOAT64
);
```

## Key Relationships

```
organizations (1) ──────< (N) org_users
      │
      │ (1)
      │
      └──────< (N) stores
                    │
                    │ (1)
                    │
                    └──────< (N) store_performance
                    │
                    │ (1)
                    │
                    └──────< (N) territory_assignments ────> (N) territories
```

## Common Joins

```sql
-- Store with organization and territory
SELECT
  s.store_id,
  s.store_name,
  o.org_name,
  t.territory_name
FROM stores s
JOIN organizations o ON s.org_id = o.org_id
LEFT JOIN territory_assignments ta ON s.store_id = ta.store_id
  AND CURRENT_DATE() BETWEEN ta.assigned_from AND COALESCE(ta.assigned_to, '9999-12-31')
LEFT JOIN territories t ON ta.territory_id = t.territory_id

-- Zone study with demographics and competition
SELECT
  zs.study_id,
  zs.study_name,
  zd.population,
  zd.avg_income,
  COUNT(DISTINCT zc.competitor_id) AS competitor_count
FROM zone_studies zs
JOIN zone_demographics zd ON zs.study_id = zd.study_id
LEFT JOIN zone_competition zc ON zd.zone_id = zc.zone_id
GROUP BY 1, 2, 3, 4
```

## Metric Definitions

| Metric | Definition | Calculation |
|--------|------------|-------------|
| **Penetration Rate** | Market share captured | `revenue / market_potential * 100` |
| **Performance Score** | Composite store rating | `(revenue_index * 0.4) + (growth_index * 0.3) + (efficiency_index * 0.3)` |
| **Conversion Rate** | Visitors who purchase | `transactions / footfall * 100` |
| **Avg Basket** | Revenue per transaction | `revenue / transactions` |
| **Cannibalization Rate** | Revenue overlap % | `shared_customers_revenue / total_revenue * 100` |

## Notes for PM

### When Requesting Data
1. Specify the time period needed
2. Clarify if you need store-level or aggregated data
3. Mention any filters (org, region, store type)
4. Indicate the output format preference

### Data Freshness
- `user_events`: Near real-time (15 min delay)
- `store_performance`: Daily (updated overnight)
- `zone_demographics`: Quarterly
- `territory_metrics`: Weekly

### Access Levels
- Some tables require elevated permissions
- PII data requires explicit approval
- Raw event data may need anonymization
