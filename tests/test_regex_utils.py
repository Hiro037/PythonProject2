import pytest

from src.regex_utils import count_operations_by_category, filter_operations_by_description

# Тестирование filter_operations_by_description


@pytest.fixture
def sample_operations():
    return [
        {"description": "Перевод организации", "amount": "100"},
        {"description": "Открытие вклада", "amount": "200"},
        {"description": "Перевод с карты на карту", "amount": "300"},
        {"description": "Покупка в магазине", "amount": "400"},
        {"amount": "500"},  # Операция без описания
        {"description": "Перевод СО СЧЕТА", "amount": "600"},  # Проверка регистра
    ]


# Тест 1: Корректный поиск по шаблону
def test_basic_search(sample_operations):
    result = filter_operations_by_description(sample_operations, r"перевод")
    assert len(result) == 3, "Должно найти 3 операции с 'перевод'"
    assert all("перевод" in op["description"].lower() for op in result if "description" in op)


# Тест 2: Чувствительность к регистру (игнорируется)
def test_case_insensitive(sample_operations):
    result = filter_operations_by_description(sample_operations, r"СЧЕТА")
    assert len(result) == 1, "Должна найти операцию 'Перевод СО СЧЕТА'"
    assert "СО СЧЕТА" in result[0]["description"]


# Тест 3: Отсутствие совпадений
def test_no_matches(sample_operations):
    result = filter_operations_by_description(sample_operations, r"авиабилет")
    assert len(result) == 0, "Не должно быть совпадений"


# Тест 4: Некорректное регулярное выражение
def test_invalid_regex(sample_operations):
    with pytest.raises(ValueError) as exc_info:
        filter_operations_by_description(sample_operations, r"[invalid(regex")
    assert "Некорректное регулярное выражение" in str(exc_info.value)


# Тест 5: Обработка операций без описания
def test_missing_description(sample_operations):
    result = filter_operations_by_description(sample_operations, r".+")
    # Операция без описания не должна попасть в результат
    assert len(result) == 5, "Должно быть 5 операций с описанием"


# Тест 6: Пустой список операций
def test_empty_input():
    result = filter_operations_by_description([], r"перевод")
    assert len(result) == 0, "Результат должен быть пустым"


# Тест 7: Специальные символы в регулярном выражении
def test_special_characters(sample_operations):
    result = filter_operations_by_description(sample_operations, r"вклад$")
    assert len(result) == 1, "Должна найти операцию 'Открытие вклада'"
    assert result[0]["description"] == "Открытие вклада"


# Тестирование count_operations_by_category


@pytest.fixture
def sample_transactions():
    return [
        {"description": "Покупка в магазине", "amount": 100},
        {"description": "Оплата услуг ЖКХ", "amount": 200},
        {"description": "Покупка в МАГАЗИНЕ", "amount": 300},  # Проверка регистра
        {"description": "Кинотеатр 'Звезда'", "amount": 400},
        {"description": "Перевод в банк", "amount": 500},
        {"amount": 600},  # Транзакция без описания
        {"description": "Кафе 'Кофейня' и магазин", "amount": 700},  # Множественные совпадения
        {"description": "Оплата интернета", "amount": 800},
    ]


# Тест 1: Базовый подсчёт категорий
def test_basic_count(sample_transactions):
    categories = ["магазин", "оплата", "кино"]
    result = count_operations_by_category(sample_transactions, categories)
    assert result == {
        "магазин": 3,  # 1 прямой + 1 регистронезависимый + 1 в составе строки
        "оплата": 2,    # "Оплата услуг" и "Оплата интернета"
        "кино": 1       # "Кинотеатр"
    }, "Некорректный базовый подсчёт"


# Тест 2: Регистронезависимость
def test_case_insensitivity(sample_transactions):
    categories = ["МАГАЗИН"]
    result = count_operations_by_category(sample_transactions, categories)
    assert result["МАГАЗИН"] == 3, "Не игнорируется регистр"


# Тест 3: Частичное совпадение
def test_partial_match(sample_transactions):
    categories = ["кофе"]
    result = count_operations_by_category(sample_transactions, categories)
    assert result["кофе"] == 1, "Не найдено частичное совпадение (Кафе -> кофе)"


# Тест 4: Транзакции без описания
def test_missing_description_by_category(sample_transactions):
    categories = ["магазин"]
    result = count_operations_by_category(sample_transactions, categories)
    assert result["магазин"] == 3, "Транзакции без описания не должны влиять"


# Тест 5: Пустые входные данные
def test_empty_input_by_category():
    assert count_operations_by_category([], ["категория"]) == {"категория": 0}, "Пустой список транзакций"
    assert count_operations_by_category([{"description": "test"}], []) == {}, "Пустой список категорий"


# Тест 6: Специальные символы в категориях
def test_special_characters_by_category(sample_transactions):
    categories = ["магазин.", "оплата+"]  # Проверка экранирования
    result = count_operations_by_category(sample_transactions, categories)
    assert result["магазин."] == 0, "Спецсимволы не экранированы"
    assert result["оплата+"] == 0, "Спецсимволы не экранированы"


# Тест 7: Множественные совпадения в одной транзакции
def test_multiple_matches(sample_transactions):
    categories = ["магазин", "кофе"]
    result = count_operations_by_category(sample_transactions, categories)
    assert result["магазин"] == 3 and result["кофе"] == 1, "Не учтены множественные совпадения"
