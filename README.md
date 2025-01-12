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

## Тестирование

В папке tests присутствуют тесты всех реализованных в проекте функций. Тесты релизованы при помощи фреймворка pytest.
