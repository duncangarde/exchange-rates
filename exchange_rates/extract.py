import requests
from requests.adapters import HTTPAdapter, Retry


def get(url: str, api_key: str) -> dict:
    """
    Returns the data from the exchange rates API for the requested URL.
    Internally implements retries on timeouts, server errors,
    and too many requests
    """
    session = requests.Session()
    retries = Retry(
        total=5, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504]
    )
    adapter = HTTPAdapter(max_retries=retries)
    session.mount("https://", adapter)

    response = session.get(url, headers={"apikey": api_key}, timeout=10)
    response.raise_for_status()

    data = response.json()
    return data
