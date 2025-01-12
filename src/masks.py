from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    '''принимает на вход номер карты и возвращает ее маску'''
    mask_card_number = str(card_number)[0:6]+'******'+str(card_number)[-4:]
    return mask_card_number


def get_mask_account(account: Union[str, int]) -> str:
    '''принимает на вход номер счета и возвращает его маску'''
    mask_account = '**'+str(account)[-4:]
    return mask_account
