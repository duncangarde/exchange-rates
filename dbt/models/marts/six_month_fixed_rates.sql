{{ config(
  materialized='table',
  indexes=[
    {'columns': ['date', 'source_currency', 'target_currency'], 'unique': True},
  ]
) }}

with expanded_daily_rates as (
  select
    dar.*,
    case when date_part('month',date) <= 6 then 1 else 2 end as year_half,
    date_trunc('year', date) as year
  from {{ ref('int__daily_average_rates') }} dar
)

select
  date,
  source_currency,
  target_currency,
  avg(rate) over (partition by year, year_half, source_currency, target_currency) as fixed_rate
from expanded_daily_rates
