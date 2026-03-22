import datetime
import  re

from bank_widget.src.masks import get_mask_account, get_mask_card_number


def is_cyrrilic(bank_data):
    """Проверка на вхождение кириллицы в строку"""
    return bool(re.search("[а-яА-Я]", bank_data))


def mask_account_card(card_or_bill: str) -> str:
    """Маскировка данных (номер карты или счета)"""
    mask_data = ''
    if is_cyrrilic(card_or_bill):
        mask_data = get_mask_account(card_or_bill[5:])
        return f'Счет {mask_data}'
    else:
        mask_data = get_mask_card_number(card_or_bill[-16:])
        return f'{card_or_bill[:-16]}{mask_data}'


def get_date(data_time: str) -> str:
    """Смена формата даты"""
    time_list = data_time[:10].split('-')
    correct_time = '.'.join(time_list[::-1])
    return correct_time
