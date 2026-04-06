import pytest

from src.widget import get_date, mask_account_card


@pytest.fixture
def test_cases():
    return [
        ("Счет 1212343456567878", "Счет **7878"),
        ("Visa 1212343456567878", "Visa 1212 34** **** 7878"),
        ("СЧЕТ", pytest.raises(ValueError)),
        ("СЧЕТ 1212343456567878", "СЧЕТ **7878"),
        ("", pytest.raises(ValueError)),
        ("Visa1212343456567878", pytest.raises(ValueError)),
        ("qwertyuiopasdfghj", pytest.raises(ValueError)),
    ]


@pytest.mark.parametrize("index", range(7))
def test_mask_account_card(test_cases, index):
    card_or_bill, expected = test_cases[index]
    if isinstance(expected, str):
        assert mask_account_card(card_or_bill) == expected
    else:
        with expected:
            mask_account_card(card_or_bill)


@pytest.fixture
def test_date_cases():
    return [
        ("20240606", "06.06.2024"),
        ("2024.06.06", pytest.raises(ValueError)),
        ("шестое июня две тысячи двадцать четвертого года", pytest.raises(ValueError)),
        ("", pytest.raises(ValueError)),
        ("06062024", pytest.raises(ValueError)),
        ("8-900-000-00-00", pytest.raises(ValueError)),
    ]


@pytest.mark.parametrize("index", range(5))
def test_get_date(test_date_cases, index):
    data_time, expected = test_date_cases[index]
    if isinstance(expected, str):
        assert get_date(data_time) == expected
    else:
        with expected:
            get_date(data_time)
