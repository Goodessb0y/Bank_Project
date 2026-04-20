from typing import Any, Iterator


def filter_by_currency(transactions: list[dict[str, Any]], code: str) -> Iterator[dict]:
    """Генератор yielding транзакции отфильтрованные по коду.

    Args:
        transactions: список с словарем транзакций
        code: валютная аббревиатура (e.g. 'USD')

    Yields:
        dict: транзакция, соответствующая указанной валюте"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == code:
            yield transaction


def transaction_descriptions(transaction_data: list[dict[str, Any]]) -> Iterator[dict]:
    """Генератор yielding описание транзакций.

    Args:
        transaction_data: список с словарем транзакций

    Yields:
        str: описание транзакции"""
    for transaction in transaction_data:
        yield transaction["description"]


def card_number_generator(start: int, end: int):
    """Генератор yielding отформатированный номер карты в заданном диапазоне.

    Args:
        start: начало диапазона
        end: конец диапазона

    Yields:
        str: отформатированный номер карты"""
    for number in range(start, end + 1):
        s = str(number).zfill(16)
        parts = [s[i : i + 4] for i in range(0, 16, 4)]
        yield " ".join(parts)
