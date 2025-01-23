from typing import Dict, Generator, List


def filter_by_currency(transactions: List[Dict], currency: str) -> Generator[Dict, None, None]:
    '''Функция принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD).'''
    result = (
        transaction
        for transaction in transactions
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency
    )
    yield from result


def transaction_descriptions(transactions: List[Dict]) -> Generator[str, None, None]:
    '''Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.'''
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    '''Функция выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.'''
    for i in range(start, end + 1):
        formatted_card = f'{i:016d}'
        yield f"{formatted_card[:4]} {formatted_card[4:8]} {formatted_card[8:12]} {formatted_card[12:]}"
