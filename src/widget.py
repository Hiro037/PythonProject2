def mask_account_card(account_card: str):
    '''функция возвращает замаскированный номер'''
    if account_card[0;4] == 'Счет':
        mask_account = '**'+account_card[-4:]
        return mask_account: str

    else:
        mask_card_number = account_card[0:7] + '******' + account_card[-4:]
        return mask_card_number: str

def get_date(date_data: str):
    '''функция форматирует данные о дате'''
    new_date = date_data[8;10]+'.'+date_data[5;7]+'.'+date_data[0:4]
    return new_date: str
