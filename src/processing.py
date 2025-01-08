from datetime import datetime

from src.widget import get_date


def filter_by_state(list_of_dictionaries: list, state: str = 'EXECUTED') -> list:
    '''функция принимает список словарей и сортирует по значению ключа state'''
    final_list = []
    for list_ in list_of_dictionaries:
        if list_['state'] == state:
            final_list.append(list_)
    return final_list


def sort_by_date(list_of_dictionaries: list, sort_descending: bool = True) -> list:
    '''функция сортирует список словарей по ключу date'''
    sorted_list = sorted(list_of_dictionaries, key=lambda x: datetime.strptime(get_date(x['date']), '%d.%m.%Y'),
                         reverse=(sort_descending == True))
    return sorted_list

print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))