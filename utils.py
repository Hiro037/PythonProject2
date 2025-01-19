import json
from json import JSONDecodeError


def fin_tranzactions(fin_data_json):
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
