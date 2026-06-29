import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def mask_test_cases():
    return [
        ("4444444444444444", "4444 44** **** 4444"),
        ("1212 3434 5656 7878", "1212 34** **** 7878"),
        ("", ValueError),
        ("1212 34br 5656 7878", ValueError),
        ("qwertyuiopasdfgh", ValueError),
        ("12123434", ValueError),
    ]


@pytest.mark.parametrize("index", range(6))
def test_get_mask_card_number(mask_test_cases, index):
    card_number, expected = mask_test_cases[index]
    if expected is ValueError:
        with pytest.raises(ValueError):
            get_mask_card_number(card_number)
    else:
        assert get_mask_card_number(card_number) == expected


@pytest.fixture
def mask_account_test_cases():
    return [
        ("4444444444444444", "**4444"),
        ("1212 3434 5656 7878", "**7878"),
        ("", ValueError),
        ("1212 34br 5656 7878", "**7878"),
        ("qwertyuiopasdfgh", "**dfgh"),
        ("12123434", "**3434"),
    ]


@pytest.mark.parametrize("index", range(6))
def test_get_mask_account(mask_account_test_cases, index):
    account_number, expected = mask_account_test_cases[index]
    if expected is ValueError:
        with pytest.raises(ValueError):
            get_mask_account(account_number)
    else:
        assert get_mask_account(account_number) == expected
