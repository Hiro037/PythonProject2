from datetime import datetime
from src.widget import get_date

def filter_by_state(list_of_dictionaries, state = 'EXECUTED'):
    final_list = []
    for list_ in list_of_dictionaries:
        if list_['state'] == state:
            final_list.append(list_)
    return final_list

def sort_by_date(list_of_dictionaries, sort_descending = True ):
    sorted_list = sorted(list_of_dictionaries, key = lambda x: datetime.strptime(get_date(x['date']), '%d.%m.%Y'),  reverse=(sort_descending == True))
    return sorted_list
