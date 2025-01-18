# PythonProject2

Разработка кода для банковского приложения.

## Установка

1. Клонируйте репозиторий:
   ```
   git clone https://github.com/Hiro037/PythonProject2.git
   ```
2. Перейдите в директорию проекта:
   ```
   cd PythonProject2
   ```
3. Установите необходимые зависимости:
   ```
   pip install -r requirements.txt
   ```

## Использование

Примеры использования функций:

```python
from src.processing import filter_by_state, sort_by_date

## Пример использования filter_by_state
transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 59402872, 'state': 'CANCELLED', 'date': '2018-09-17T21:27:25.241241'}
]
executed_transactions = filter_by_state(transactions)

# Пример использования sort_by_date
sorted_transactions = sort_by_date(transactions)
```


## Функции для работы с транзакциями и номерами карт

### 1. `filter_by_currency(transactions: List[Dict], currency: str) -> Generator[Dict, None, None]`

Фильтрует транзакции по указанной валюте.

**Пример использования:**
```python
gen = filter_by_currency(transactions, "USD")
for transaction in gen:
    print(transaction)
```

### transaction_descriptions(transactions: List[Dict]) -> Generator[str, None, None]

Возвращает описание каждой транзакции.

**Пример использования:**
```python
gen = transaction_descriptions(transactions)
for description in gen:
    print(description)
```

### card_number_generator(start: int, end: int) -> Generator[str, None, None]

Генерирует номера карт в формате XXXX XXXX XXXX XXXX.

**Пример использования:**
```python
gen = card_number_generator(1, 4)
for card in gen:
    print(card)
```

## Декоратор `log`

Декоратор `log` предназначен для логирования информации о работе функции, включая:
- Начало и успешное завершение выполнения функции.
- Возникшие ошибки с указанием их типа и входных параметров.

## Особенности
1. **Вывод логов**:
   - Если передан параметр `filename`, логи записываются в указанный файл.
   - Если `filename` не указан, логи выводятся в консоль.

2. **Логируемая информация**:
   - Успешное выполнение функции (`имя_функции ok`).
   - Ошибки: `имя_функции error: тип_ошибки. Inputs: (args, kwargs)`.

### Пример использования
```python
@log(filename="log.txt")
def divide(a, b):
    return a / b

divide(10, 2)  # Запишет "divide ok" в log.txt
divide(10, 0)  # Запишет "divide error: ZeroDivisionError. Inputs: (10, 0), {}" в log.txt
```

## Тестирование

В папке tests присутствуют тесты всех реализованных в проекте функций. Тесты релизованы при помощи фреймворка pytest.
