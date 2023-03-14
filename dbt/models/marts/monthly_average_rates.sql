{{ config(
  materialized='table',
  indexes=[
    {'columns': ['date', 'source_currency', 'target_currency'], 'unique': True},
  ]
) }}

select
  date,
  source_currency,
  target_currency,
  avg(rate) over (partition by date_trunc('month', date), source_currency, target_currency) as month_rate
from {{ ref('int__daily_average_rates') }}
