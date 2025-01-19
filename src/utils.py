import json
from json import JSONDecodeError
from src.external_api import currency_conversion

def fin_transactions(fin_data_json):
    try:
        with open(f'{fin_data_json}', encoding='utf-8') as f:
            try:
                fin_data = json.load(f)
                return fin_data
            except JSONDecodeError:
                print('Ошибка декодирования')
                return []
            except Exception as e:
                print(f'Произошла ошибка: {e}')
                return []
    except FileNotFoundError:
        print('Файл не найден')
        return []


def amount_transactions(transaction):
    if transaction["operationAmount"]["currency"]["code"] == 'RUB':
        message = f'Сумма транзакции: {float(transaction["operationAmount"]["amount"])} рублей.'
        return message
    else:
        amount = currency_conversion(float(transaction["operationAmount"]["amount"]), transaction["operationAmount"]["currency"]["code"])
        message = f'Сумма транзакции: {amount} рублей.'
        return message
