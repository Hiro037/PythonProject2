from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    '''функция возвращает замаскированный номер'''
    if account_card[0:4] == 'Счет':
        return 'Счет ' + get_mask_account(account_card)

    else:
        card_number = account_card[-16:]
        return account_card[0:-16] + get_mask_card_number(card_number)


def get_date(date_data: str) -> str:
    '''функция форматирует данные о дате'''
    new_date = date_data[8:10]+'.'+date_data[5:7]+'.'+date_data[0:4]
    return new_date
