# Data & Analytics Workflow

## Purpose
Enable data-driven decisions through SQL queries, analysis, and automated reporting.

## BigQuery Query Patterns

### Query Request Template

When asking for data/SQL:

```markdown
## Data Request

**Question**: [Natural language question]
**Context**: [Why you need this data]
**Output format**: [Table/Chart/Single value]
**Audience**: [Who will see this]
**Urgency**: [When needed]
```

### Common Query Patterns

**Aggregation by Time**
```sql
-- Daily/Weekly/Monthly aggregation
SELECT
  DATE_TRUNC(created_at, MONTH) AS period,
  COUNT(*) AS total_count,
  COUNT(DISTINCT user_id) AS unique_users
FROM `project.dataset.table`
WHERE created_at BETWEEN @start_date AND @end_date
GROUP BY period
ORDER BY period DESC
```

**Year-over-Year Comparison**
```sql
-- YoY comparison
WITH current_period AS (
  SELECT
    metric_name,
    SUM(value) AS current_value
  FROM `project.dataset.metrics`
  WHERE date BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 1 YEAR) AND CURRENT_DATE()
  GROUP BY metric_name
),
previous_period AS (
  SELECT
    metric_name,
    SUM(value) AS previous_value
  FROM `project.dataset.metrics`
  WHERE date BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 2 YEAR) 
                 AND DATE_SUB(CURRENT_DATE(), INTERVAL 1 YEAR)
  GROUP BY metric_name
)
SELECT
  c.metric_name,
  c.current_value,
  p.previous_value,
  ROUND((c.current_value - p.previous_value) / p.previous_value * 100, 2) AS yoy_change_pct
FROM current_period c
LEFT JOIN previous_period p ON c.metric_name = p.metric_name
```

**Cohort Analysis**
```sql
-- User cohort retention
WITH user_cohorts AS (
  SELECT
    user_id,
    DATE_TRUNC(first_activity_date, MONTH) AS cohort_month
  FROM `project.dataset.users`
),
user_activity AS (
  SELECT
    user_id,
    DATE_TRUNC(activity_date, MONTH) AS activity_month
  FROM `project.dataset.activity`
)
SELECT
  uc.cohort_month,
  DATE_DIFF(ua.activity_month, uc.cohort_month, MONTH) AS months_since_start,
  COUNT(DISTINCT ua.user_id) AS active_users,
  COUNT(DISTINCT uc.user_id) AS cohort_size
FROM user_cohorts uc
LEFT JOIN user_activity ua ON uc.user_id = ua.user_id
GROUP BY cohort_month, months_since_start
ORDER BY cohort_month, months_since_start
```

**Funnel Analysis**
```sql
-- Conversion funnel
WITH funnel_stages AS (
  SELECT
    user_id,
    MAX(CASE WHEN event = 'page_view' THEN 1 ELSE 0 END) AS visited,
    MAX(CASE WHEN event = 'signup_start' THEN 1 ELSE 0 END) AS started_signup,
    MAX(CASE WHEN event = 'signup_complete' THEN 1 ELSE 0 END) AS completed_signup,
    MAX(CASE WHEN event = 'first_action' THEN 1 ELSE 0 END) AS activated
  FROM `project.dataset.events`
  WHERE event_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
  GROUP BY user_id
)
SELECT
  'Visited' AS stage,
  SUM(visited) AS users,
  100.0 AS conversion_rate
UNION ALL
SELECT
  'Started Signup',
  SUM(started_signup),
  ROUND(SUM(started_signup) / SUM(visited) * 100, 2)
FROM funnel_stages
UNION ALL
SELECT
  'Completed Signup',
  SUM(completed_signup),
  ROUND(SUM(completed_signup) / SUM(visited) * 100, 2)
FROM funnel_stages
UNION ALL
SELECT
  'Activated',
  SUM(activated),
  ROUND(SUM(activated) / SUM(visited) * 100, 2)
FROM funnel_stages
```

**Territory Performance (Galigeo-specific)**
```sql
-- Territory Manager metrics
SELECT
  territory_id,
  territory_name,
  region,
  COUNT(DISTINCT store_id) AS store_count,
  SUM(revenue) AS total_revenue,
  AVG(performance_score) AS avg_performance,
  SUM(potential_revenue) AS market_potential,
  ROUND(SUM(revenue) / SUM(potential_revenue) * 100, 2) AS penetration_rate
FROM `project.dataset.territory_metrics`
WHERE period = @current_period
GROUP BY territory_id, territory_name, region
ORDER BY total_revenue DESC
```

**Zone Study Analysis (RetailFocus)**
```sql
-- Zone catchment analysis
SELECT
  zone_id,
  zone_name,
  isochrone_minutes,
  population,
  households,
  avg_income,
  competitor_count,
  market_size_estimate,
  ROUND(market_size_estimate / competitor_count, 2) AS market_share_opportunity
FROM `project.dataset.zone_studies`
WHERE study_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY)
  AND isochrone_minutes <= 15
ORDER BY market_share_opportunity DESC
LIMIT 20
```

### Query Best Practices

**Performance**
- Always include date filters
- Use partitioned tables when available
- Avoid `SELECT *`
- Use `LIMIT` for exploration

**Readability**
- Use CTEs for complex logic
- Meaningful aliases
- Comment non-obvious logic
- Consistent formatting

**Safety**
- Parameterize user inputs
- Include `WHERE` clauses
- Test with `LIMIT` first

## Insights Interpretation

### Analysis Framework

```markdown
# Data Analysis: [Topic]

## Question
[What are we trying to understand?]

## Methodology
- **Data source**: [Table/dataset]
- **Time period**: [Range]
- **Filters applied**: [Any exclusions]
- **Metrics used**: [Definitions]

## Findings

### Key Insight #1
**Observation**: [What the data shows]
**So what**: [Why it matters]
**Now what**: [Recommended action]

### Key Insight #2
[Same structure]

## Data Quality Notes
- [Any caveats or limitations]

## Recommended Next Analysis
- [Follow-up question]
```

### Anomaly Detection Checklist

When data looks unexpected:
- [ ] Check date range accuracy
- [ ] Verify filters are correct
- [ ] Look for data pipeline delays
- [ ] Check for definition changes
- [ ] Compare to known events (releases, holidays)
- [ ] Validate against secondary source

### Insight Communication

**For Executives**
```markdown
## [Metric] Update

**Bottom line**: [One sentence insight]

**Key number**: [X%] change in [metric] → [€ impact]

**Recommended action**: [What to do]
```

**For Technical Audience**
```markdown
## Analysis: [Topic]

**Query**: [Link or snippet]
**Data quality**: [Confidence level]
**Statistical notes**: [Significance, sample size]
**Raw data**: [Link to full output]
```

## Report Generation

### Automated Report Template

```markdown
# [Report Name]
**Generated**: [Timestamp]
**Period**: [Date range]
**Owner**: [PM Name]

## Executive Summary
[Auto-generated key metrics and trends]

## Section 1: [Metric Category]

### KPIs
| Metric | Value | vs Target | vs Previous |
|--------|-------|-----------|-------------|
| [Metric] | [Value] | [%] | [%] |

### Trend
[Chart placeholder]

### Notable Changes
- [Auto-flagged significant changes]

## Section 2: [Metric Category]
[Same structure]

## Appendix
- Data definitions
- Query references
- Methodology notes
```

### Report Types by Audience

**Daily Operations Report**
```markdown
## Daily Ops: [Date]

### Today's Numbers
- Active users: [n] ([+/-]% vs avg)
- Key action completed: [n]
- Errors: [n] ([+/-]% vs avg)

### Alerts 🚨
[Auto-flagged anomalies]

### Yesterday's Actions
- [Action taken] → [Result]
```

**Weekly Metrics Report**
```markdown
## Weekly Metrics: Week [N]

### Summary
| Metric | This Week | Last Week | WoW | MTD |
|--------|-----------|-----------|-----|-----|
| [Metric] | [Value] | [Value] | [%] | [%] |

### Highlights
1. [Best performing area]
2. [Needs attention]

### Charts
[Weekly trends]
```

**Monthly Business Review Data**
```markdown
## Monthly Data Pack: [Month]

### Performance Dashboard
[Comprehensive metrics table]

### Segment Analysis
[By customer type, region, product]

### Trend Analysis
[MoM, YoY comparisons]

### Forecast vs Actual
| Metric | Forecast | Actual | Variance |
|--------|----------|--------|----------|
| [Metric] | [Value] | [Value] | [%] |

### Data Quality Score
- Completeness: [%]
- Freshness: [Hours since update]
- Known issues: [List]
```

## Self-Service Analytics Patterns

### Dashboard Requirements

```markdown
# Dashboard Spec: [Name]

## Purpose
[Who uses this, for what decisions]

## Key Questions It Answers
1. [Question]
2. [Question]

## Metrics
| Metric | Definition | Source | Refresh |
|--------|------------|--------|---------|
| [Metric] | [Calc] | [Table] | [Frequency] |

## Filters Needed
- Date range (default: last 30 days)
- [Dimension]
- [Dimension]

## Visualizations
| Chart | Metric | Type | Drilldown |
|-------|--------|------|-----------|
| [Name] | [Metric] | Line/Bar/Table | [What clicking does] |

## Alerts
- [Metric] > [Threshold] → Notify [Channel]
```

### Query Documentation

When saving reusable queries:

```sql
/*
Query: [Name]
Purpose: [What it answers]
Author: [Name]
Last updated: [Date]
Parameters:
  - @start_date: Beginning of period (DATE)
  - @end_date: End of period (DATE)
  - @segment: Customer segment filter (STRING, optional)
Output:
  - column1: [Description]
  - column2: [Description]
Dependencies:
  - project.dataset.table1
  - project.dataset.table2
Notes:
  - [Any caveats or usage notes]
*/

SELECT ...
```

## Data Quality Checks

### Validation Queries

```sql
-- Row count trend (catch missing data)
SELECT
  DATE(created_at) AS date,
  COUNT(*) AS row_count
FROM `project.dataset.table`
WHERE created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
GROUP BY date
ORDER BY date

-- Null rate by column
SELECT
  COUNTIF(column1 IS NULL) / COUNT(*) * 100 AS null_rate_col1,
  COUNTIF(column2 IS NULL) / COUNT(*) * 100 AS null_rate_col2
FROM `project.dataset.table`
WHERE created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY)

-- Duplicate detection
SELECT
  key_column,
  COUNT(*) AS duplicate_count
FROM `project.dataset.table`
GROUP BY key_column
HAVING COUNT(*) > 1
```

### Data Issue Escalation

```markdown
## Data Issue Report

**Severity**: Critical / High / Medium / Low
**Discovered**: [Date/Time]
**Affected**: [What data/reports]

### Description
[What's wrong]

### Impact
[Who/what is affected]

### Root Cause (if known)
[Why it happened]

### Workaround (if any)
[Temporary solution]

### Fix Required
[What needs to happen]
[Owner]
[ETA]
```
