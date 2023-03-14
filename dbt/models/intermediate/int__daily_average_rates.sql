select
  date,
  source_currency,
  target_currency,
  avg(rate) as rate
from {{ ref('stg__exchange_rates') }}
group by date, source_currency, target_currency
