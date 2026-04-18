import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

@pytest.fixture
def transactions():
    return [
        {"operationAmount": {"currency": {"code": "USD"}}, "description": "Перевод организации"},
        {"operationAmount": {"currency": {"code": "FRA"}}, "description": "Перевод со счета на счет"},
        {"operationAmount": {"currency": {"code": "USD"}}, "description": ""},
    ]


@pytest.mark.parametrize(
    "code, expected_len",
    [
        ("USD", 2),
        ("FRA", 1),
        ("EUR", 0),
    ],
)
def test_filter_by_currency(transactions, code, expected_len):
    result = list(filter_by_currency(transactions, code))
    assert len(result) == expected_len


@pytest.mark.parametrize(
    "expected",
    [
        ["Перевод организации", "Перевод со счета на счет", ""],
    ],
)
def test_transaction_descriptions(transactions, expected):
    result = list(transaction_descriptions(transactions))
    assert result == expected


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 3, [
            "0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003",
        ]),
    ],
)
def test_card_number_generator(start, end, expected):
    result = list(card_number_generator(start, end))
    assert result == expected