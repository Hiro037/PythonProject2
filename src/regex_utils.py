import re


def filter_operations_by_description(operations, search_pattern):
    """
    Фильтрует список операций, оставляя только те, в описании которых
    найдено совпадение с регулярным выражением search_pattern.

    :param operations: Список словарей с данными операций.
    :param search_pattern: Строка с регулярным выражением для поиска.
    :return: Отфильтрованный список операций.
    """
    filtered_operations = []
    try:
        pattern = re.compile(search_pattern, re.IGNORECASE)
    except re.error as e:
        raise ValueError(f"Некорректное регулярное выражение: {e}") from e

    for operation in operations:
        description = operation.get("description", "")
        if pattern.search(description):
            filtered_operations.append(operation)

    return filtered_operations


def count_operations_by_category(transactions, categories):
    """
    Подсчитывает количество операций для каждой категории.

    Параметры:
    transactions (list): Список словарей с данными о банковских операциях. Каждая операция имеет поле 'description'.
    categories (list): Список категорий операций, по которым нужно вести подсчет.

    Возвращает:
    dict: Словарь, где ключи — названия категорий, а значения — количество операций,
     в описании которых встречается соответствующая категория.
    """
    category_counts = {}

    # Для каждой категории создаём регулярное выражение с учетом игнорирования регистра
    for category in categories:
        pattern = re.compile(re.escape(category), re.IGNORECASE)
        count = 0
        for transaction in transactions:
            description = transaction.get('description', '')
            if pattern.search(description):
                count += 1
        category_counts[category] = count

    return category_counts
