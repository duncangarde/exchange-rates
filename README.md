# Exchange rates simple pipeline

A simple pipeline

## Scope

This repo is intended to provide a simple pipeline for extracting, loading and transforming exchange rate data.
It is not meant for full production as it is only a technical test showcasing various pieces

## Setup

- Add a .env file at the root with values as shown in `.env.example`

- Create environment
    - `python3 -m venv venv`<br>
    - `source venv/bin/activate`<br>
    - `python3 -m pip install --upgrade pip -r requirements.txt`<br>

- Run alembic migrations to get the database into the desired state
  - `alembic upgrade head`

- Run `dbt deps` to install dbt dependencies

## Non boilerplate content
- alembic
  - versions
    - migration file to create exchange rate responses table in postgres
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
    - main.py # command line script for ELT job
    - extract.py # Handles extraction of data from the exchange rates API
    - load.py # Loads data from the response into Postgres
    - models.py # Holds SQLAlchemy table definitions for the project
- README.md
- requirements.txt

## Usage

The best example of using the various code parts is to look at the github action `.github/workflows/elt.yml` where we bring it all together

## Known omissions

As this is a technical test showcase, not everything has been implemented to make this production ready:
- it does not take into account any backfilling of the rates which could be done through the history section of the API
- main.py and load.py probably need test coverage (although they are very simple)
- monitoring:
  - although github actions will output logs for this service nothing else has been implemented. It is possible from the web interface to check these logs
- alerting:
  - this has not been implemented but it can be configured as notifications from github or actions can be added to the workflows
- dbt:
  - overall folder structure is very simple and would need to be iterated on in a bigger project
  - the outlier test could be a bit more sophisticated using standard deviations from the mean or similar
