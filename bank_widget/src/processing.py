from datetime import datetime

def filter_by_state(data: list, state: str ='EXECUTED') -> list:
    """
    Функция принимает список словарей (данные банковских операций)
    Возвращает отфильтрованный по параметру state список словарей
    """

    filtered = []
    for dicts in data:
        if dicts['state'] == state:
            filtered.append(dicts)

    return filtered


def sort_by_date(data: list, sort=True) -> list:
    """
    Функция принимает список словарей и параметр порядка сортировки
    Возвращает отсортированный список согласно параметру sort
    """
    sorted_list = sorted(data, key=lambda item: datetime.fromisoformat(item['date']), reverse=sort)

    return sorted_list
