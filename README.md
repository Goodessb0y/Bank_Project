# Bank Widget

## Описание
Проект содержит функции для обработки банковских операций:
- фильтрация операций по статусу
- сортировка операций по дате
- маскировка номера карт
- маскировка личного счета

## Установка

Клонировать репозиторий:

git clone https://github.com/Goodessb0y/Bank_Project.git

Перейти в папку проекта:

cd bank_widget

## Пример использования функций фильтрации и сортировки

```python
from src.processing import filter_by_state, sort_by_date

data = [...]
filtered = filter_by_state(data)
sorted_data = sort_by_date(filtered)