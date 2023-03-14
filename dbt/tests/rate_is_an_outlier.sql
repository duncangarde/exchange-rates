{% set threshold = 0.5 %}

with rolling_stats as (
  select
    rate,
    avg(rate) over (
        partition by source_currency, target_currency
        order by extracted_at asc
        rows between 31 preceding and 1 preceding
  ) as last_30_rates_avg
  from {{ ref('stg__exchange_rates') }}
)

select * from rolling_stats
where not rate / last_30_rates_avg between last_30_rates_avg * {{ threshold }} and last_30_rates_avg / {{ threshold }}
and last_30_rates_avg is not null
