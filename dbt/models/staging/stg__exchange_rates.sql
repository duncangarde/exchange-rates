
{{ config(materialized='view') }}

{%- set currencies = ["EUR", "USD"] -%}

with source_data as (
    select * from {{ source('platform','source__exchange_rate_responses') }}
)

{% for currency in currencies %}
    select
        date,
        base as source_currency,
        '{{currency}}' as target_currency,
        (rates ->> '{{currency}}')::float as rate,
        to_timestamp(timestamp) as extracted_at
    from source_data
{% if not loop.last %} union all {% endif %}
{% endfor %}
