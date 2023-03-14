# Exchange rates simple pipeline

A simple pipeline example

## Scope

This repo is intended to provide a simple pipeline example for extracting, loading and transforming exchange rate data.
It is not meant for full production as it is only a technical test showcasing various pieces

## Setup

- Add a .env file at the root with:
  - Your own Postgres connection string as `PG_CONNECTION_STRING`
  - Extract your Postgres password from the above string and store as `PG_PASSWORD` (this is for DBT to connect)
  - An API key for exchange rates data from [here]('https://apilayer.com/marketplace/exchangerates_data-api') as `EXCHANGE_API_KEY`

- Create environment
    - `python3 -m venv venv`<br>
    - `source venv/bin/activate`<br>
    - `python3 -m pip install --upgrade pip -r requirements.txt`<br>

- Run alembic migrations to get the database into the desired state
  - `alembic upgrade head`

- Run `dbt deps` to install dbt dependencies

## Non boilerplate content
- dbt
  - models
    - staging
      - stg__exchange_rates.sql # Creates a staging table switching from JSON source data to columnar data
      - schema.yml # Includes definitions and standard tests
    - intermediate
      - int__daily_average_rates.sql # Averages separate response data for a given day
      - schema.yml # Includes definitions and standard tests
    - marts
      - monthly_average_rates.sql # Gets data into required format for a monthly average shown for each day
      - six_month_fixed_rates.sql # Gets data into required format for a six month fixed rate
      - schema.yml # Includes definitions and standard tests
  - tests
    - rate_is_an_outlier.sql # Simple test for if a rate is an outlier compared to the previous 30 rate readings

- exchange_rates
    - main.py # command line script for ELT jobs
    - extract.py # Handles extraction of data from the exchange rates API
    - load.py # Loads data from the response into Postgres
    - models.py # Holds SQLAlchemy table definitions for the project
- README.md
- requirements.txt

