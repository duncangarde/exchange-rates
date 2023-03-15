import sys
import traceback
import logging
import os
from dotenv import load_dotenv

import extract
import load
from models import SourceExchangeRateResponses


logging.basicConfig(
    format="%(asctime)s %(name)s %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

if not os.getenv("EXCHANGE_API_KEY"):
    load_dotenv()
EXCHANGE_API_KEY = os.getenv("EXCHANGE_API_KEY")
PG_CONNECTION_STRING = os.getenv("PG_CONNECTION_STRING")


def main():
    try:
        logger.info("Starting extract...")
        data = extract.get(
            "https://api.apilayer.com/exchangerates_data/latest?base=GBP",
            EXCHANGE_API_KEY,
        )
        del data["success"]
        logger.info("Extract completed.")
        logger.info("Inserting data...")
        load.insert(data, SourceExchangeRateResponses, PG_CONNECTION_STRING)
        logger.info("Data inserted.")
        sys.exit(0)
    except Exception:
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
