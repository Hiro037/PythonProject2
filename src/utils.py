import json
import logging
import os
from json import JSONDecodeError

from src.external_api import currency_conversion

current_dir = os.path.abspath(os.path.dirname(__file__))
base_dir = os.path.dirname(current_dir)
log_file_path = os.path.join(base_dir, 'logs', 'utils.log')

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s',
                    filename=log_file_path,
                    filemode='w',
                    encoding='utf-8')

logger = logging.getLogger(__name__)


def fin_transactions(fin_data_json: str):
    '''Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.'''
    ''' Если файл пустой, содержит не список или не найден, функция возвращает пустой список.'''
    logger.info('Функция начала своё выполнение')
    try:
        with open(fin_data_json, encoding='utf-8') as f:
            try:
                logger.info('Функция завершила своё выполнение без ошибок')
                fin_data = json.load(f)
                return fin_data
            except JSONDecodeError:
                logger.warning('Передан неверный формат данных')
                print('Ошибка декодирования')
                return []
            except Exception as e:
                logger.warning(f'Произошла ошибка: {e}')
                print(f'Произошла ошибка: {e}')
                return []
    except FileNotFoundError:
        logger.warning('Файл не найден')
        print('Файл не найден')
        return []


def amount_transactions(transaction: list):
    '''Функция  принимает на вход транзакцию и возвращает сумму транзакции в рублях'''
    '''В случае, если транзакция проведена не в рублях,
    функция обращается к функции currency_conversion из src.external_api'''
    logger.info('Функция начала своё выполнение')
    try:
        if transaction["operationAmount"]["currency"]["code"] == 'RUB':
            logger.info('Транзакция в рублях. Функция выполнена')
            message = f'Сумма транзакции: {float(transaction["operationAmount"]["amount"])} рублей.'
            return message
        else:
            logger.info('Транзакция не в рублях. Функция выполнена')
            amount = currency_conversion(float(transaction["operationAmount"]["amount"]),
                                         transaction["operationAmount"]["currency"]["code"])
            message = f'Сумма транзакции: {amount} рублей.'
            return message
    except Exception as e:
        logger.warning(f'Произошла ошибка: {e}')
