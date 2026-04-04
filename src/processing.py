from datetime import datetime
from typing import Any


def filter_by_state(data: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """
    args:
        data: список словарей с операциями
        state: статус операции
    return:
        отфильтрованный список операций
    """

    filtered = []
    for dicts in data:
        if dicts["state"] == state:
            filtered.append(dicts)

    return filtered


def sort_by_date(data: list[dict[str, Any]], sort: bool = True) -> list[dict[str, Any]]:
    """
    args:
        data: список словарей с операциями
        sort: параметр сортировки
    return:
        отсортированный по дате список операций
    """
    sorted_list = sorted(data, key=lambda item: datetime.fromisoformat(item["date"]), reverse=sort)

    return sorted_list
