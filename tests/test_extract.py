from requests import Session
from unittest.mock import Mock, patch

from nose.tools import assert_dict_equal

from exchange_rates.extract import get


@patch.object(Session, "get")
def test_getting_rates_when_response_is_ok(mock_get):
    rates = {
        "timestamp": 123456789,
        "success": True,
        "base": "GBP",
        "date": "2023-01-01",
        "rates": {"USD": 1.44, "EUR": 1.56},
    }

    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = rates

    response = get("https://foo.bar", "F00")

    assert_dict_equal(response, rates)
