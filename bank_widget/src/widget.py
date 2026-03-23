from datetime import datetime
from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_bill: str) -> str:
    """Маскировка данных (номер счета или карты)"""
    parts = card_or_bill.rsplit(" ", 1)

    name, number = parts

    if name.lower().startswith("счет"):
        return f"{name} {get_mask_account(number)}"
    else:
        return f"{name} {get_mask_card_number(number)}"


def get_date(data_time: str) -> str:
    """Смена формата даты"""
    dt = datetime.fromisoformat(data_time)
    return dt.strftime("%d.%m.%Y")
