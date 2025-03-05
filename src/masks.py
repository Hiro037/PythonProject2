import logging
import os
from typing import Union

current_dir = os.path.abspath(os.path.dirname(__file__))
base_dir = os.path.dirname(current_dir)
log_file_path = os.path.join(base_dir, 'logs', 'masks.log')

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s',
                    filename=log_file_path,
                    filemode='w',
                    encoding='utf-8')

logger = logging.getLogger(__name__)


def get_mask_card_number(card_number: Union[str, int]) -> str:
    '''принимает на вход номер карты и возвращает ее маску'''
    logger.info('Принят номер карты')
    try:
        int(card_number)
        if len(str(card_number)) == 16:
            try:
                logger.info('Функция вернула маску номера карты')
                mask_card_number = str(card_number)[0:6]+'******'+str(card_number)[-4:]
                mask_card_number = str(card_number)[0:4] + ' ' + str(card_number)[4:6] + '** **** ' + str(card_number)[-4:]
                return mask_card_number
            except Exception as e:
                logger.warning(f'Произошла ошибка: {e}')
                pass
        else:
            logger.warning('Введён неправильный формат номера')
            return 'Неверный формат номера'
    except Exception:
        logger.warning('Введён неправильный формат номера')
        return 'Неверный формат номера'


def get_mask_account(account: Union[str, int]) -> str:
    '''принимает на вход номер счета и возвращает его маску'''
    logger.info('Принят номер счёта')
    try:
        int(account)
        try:
            logger.info('Функция вернула маску номера счета')
            mask_account = '**'+str(account)[-4:]
            return mask_account
        except Exception as e:
            logger.warning(f'Произошла ошибка: {e}')
            pass
    except Exception:
        logger.warning('Введён неправильный формат номера')
        return 'Неверный формат номера'
