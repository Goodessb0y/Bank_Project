from unittest.mock import patch

import pytest

from src.external_api import currency_amount


def test_rub():
    tx = {"operationAmount": {"amount": "100", "currency": {"code": "RUB"}}}

    assert currency_amount(tx) == 100.0


@patch("src.external_api.convert_currency")
def test_usd(mock_convert):
    mock_convert.return_value = 87.5

    tx = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}

    result = currency_amount(tx)

    assert result == 87.5
    mock_convert.assert_called_once_with("USD", "RUB", 100.0)


@patch("src.external_api.convert_currency")
def test_eur(mock_convert):
    mock_convert.return_value = 90.0

    tx = {"operationAmount": {"amount": "100", "currency": {"code": "EUR"}}}

    result = currency_amount(tx)

    assert result == 90.0
    mock_convert.assert_called_once_with("EUR", "RUB", 100.0)


def test_invalid_currency():
    tx = {"operationAmount": {"amount": "100", "currency": {"code": "GBP"}}}

    with pytest.raises(ValueError):
        currency_amount(tx)


@patch("src.external_api.convert_currency")
def test_rub_without_conversion(mock_convert):
    tx = {"operationAmount": {"amount": "100", "currency": {"code": "RUB"}}}

    result = currency_amount(tx)

    assert result == 100.0
    mock_convert.assert_not_called()
