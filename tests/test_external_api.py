from src.external_api import currency_conversion
from unittest.mock import patch

@patch('requests.get')
def test_currency_conversion(mock_get):
    mock_get.return_value.json.return_value = {'result': 1}
    assert currency_conversion(1000, 'RUB') == 1