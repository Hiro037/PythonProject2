def get_mask_card_number(card_number: str):
    '''принимает на вход номер карты и возвращает ее маску'''
    mask_card_number = card_number[0:7]+'******'+card_number[-4:]
    return mask_card_number: str


def get_mask_account(account: str):
    '''принимает на вход номер счета и возвращает его маску'''
    mask_account = '**'+account[-4:]
    return mask_account: str
