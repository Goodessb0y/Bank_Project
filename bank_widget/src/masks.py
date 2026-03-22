def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера карты"""
    start = card_number[:6]
    end = card_number[-4:]
    masked_middle = "*" * (len(card_number) - 10)

    masked_number = start + masked_middle + end
    result_mask = " ".join([masked_number[i : i + 4] for i in range(0, len(masked_number), 4)])

    return result_mask


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера аккаунта"""

    return "*" * 2 + account_number[-4:]
