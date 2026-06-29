from src.pd_operations import get_transactions_csv

# Bank Widget

## Описание
Проект содержит функции для обработки банковских операций:
- фильтрация операций по статусу, валюте
- сортировка операций по дате
- маскировка номера карт
- маскировка личного счета
- получение описания каждой транзакции
- получение нового номера карты

## Установка

Клонировать репозиторий:

git clone https://github.com/Goodessb0y/Bank_Project.git

Перейти в папку проекта


## Пример использования функций:
### Фильтрация по статусу и сортировка по дате

```python
from src.processing import filter_by_state, sort_by_date

data = [...]
filtered = filter_by_state(data)
sorted_data = sort_by_date(filtered)
```

### Фильтрация транзакций по валютному коду
```python
from src.generators import filter_by_currency

data = [...]
code = 'USD'

filter_by_currency(data, code)
```

### Получение описания транзакции
```python
from src.generators import transaction_descriptions

data = [...]
transaction_descriptions(data)
```

### Получение нового номера карты
```python
from src.generators import card_number_generator

start = 0
end = 10000
card_number_generator(start, end)
```

## Log decorator

Декоратор `log` используется для логирования выполнения функций:
- успешное завершение
- ошибки с типом исключения и входными параметрами


- При успешном выполнении функции записывает:
  `имя_функции ok`

- При ошибке записывает:
  `имя_функции error: <тип ошибки>. Inputs: (<args>, <kwargs>)`

- Логи могут писаться:
  - в файл, если указан `filename`
  - в консоль, если `filename` не задан

### Пример:

```python
@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)
```

---

### Логи:

```md
## Examples

Success:
    my_function ok

Error:
    my_function error: ZeroDivisionError. Inputs: (1, 0), {}
```
## Работа с  CVS/EXCEL
Функции get_transactions_csv, get_transactions_excel
- Получение данных о транзакциях по пути файла в формате список словарей

## Тестирование
Для проекта используются:

- pytest - запуск тестов
- pytest-cov - измерение покрытия кода тестами

### Генерация HTML-отчета покрытия 

pytest --cov=src --cov-report=html

После выполнения команды будет создана папка htmlcov/.
Откройте файл htmlcov/index.html в браузере, чтобы посмотреть подробный отчёт покрытия.

### Покрытие тестами

Общее покрытие проекта: 100%