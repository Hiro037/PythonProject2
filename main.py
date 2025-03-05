from src.masks import get_mask_account
from src.masks import get_mask_card_number
from src.data_import import read_csv_transactions, read_excel_transactions
from src.utils import fin_transactions
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card
from src.regex_utils import filter_operations_by_description
#user_card_number = input('Введите номер карты:')
#print(get_mask_card_number(user_card_number))

#user_account_number = input('Введите номер счета:')
#print(get_mask_account(user_account_number))


def main():
    """
    Основная функция, объединяющая функциональности проекта.
    Реализует диалог с пользователем, выбор источника транзакций,
    фильтрацию по статусу (с учетом приведения к единому регистру),
    опциональную сортировку по дате, фильтрацию по валюте и описанию,
    а затем вывод отфильтрованного списка транзакций.
    """
    # Приветствие и выбор источника данных
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ").strip()
    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        transactions = fin_transactions('data/operations.json')
    elif choice == "2":
        print("Для обработки выбран CSV-файл.")
        transactions = read_csv_transactions('data/transactions.csv')
    elif choice == "3":
        print("Для обработки выбран XLSX-файл.")
        transactions = read_excel_transactions('data/transactions_excel.xlsx')
    else:
        print("Неверный выбор. Завершение программы.")
        return

    # Фильтрация по статусу с приведением к верхнему регистру
    allowed_statuses = {"EXECUTED", "CANCELED", "PENDING"}
    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status_input = input("Пользователь: ").strip().upper()
        if status_input in allowed_statuses:
            print(f'Операции отфильтрованы по статусу "{status_input}"')
            break
        else:
            print(f'Статус операции "{status_input}" недоступен.')

    # Отбор транзакций по выбранному статусу
    filtered_transactions = filter_by_state(transactions, status_input)

    # Сортировка транзакций по дате
    sort_choice = input("Отсортировать операции по дате? Да/Нет\nПользователь: ").strip().lower()
    if sort_choice == "да":
        sort_order = input("Отсортировать по возрастанию или по убыванию?\nПользователь: ").strip().lower()
        if "возрастанию" in sort_order:
            ascending = False
        elif "убыванию" in sort_order:
            ascending = True
        else:
            print("Неверный ввод. По умолчанию сортировка по возрастанию.")
            ascending = False


        filtered_transactions = sort_by_date(filtered_transactions, ascending)

    # Фильтрация по рублевой валюте
    ruble_choice = input("Выводить только рублевые тразакции? Да/Нет\nПользователь: ").strip().lower()
    if ruble_choice == "да":
        filtered_transactions = [
            tx for tx in filtered_transactions if "RUB" in tx["operationAmount"]["currency"]["code"]
        ]

    # Фильтрация по ключевому слову в описании
    desc_filter_choice = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: ").strip().lower()
    if desc_filter_choice == "да":
        search_word = input("Введите слово для фильтрации описания: ").strip()
        filtered_transactions = filter_operations_by_description(filtered_transactions, search_word)

    # Вывод результата
    print("Распечатываю итоговый список транзакций...")
    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}\n")
        for tx in filtered_transactions:
            date = get_date(tx.get("date"))
            description = tx.get("description", "")
            account_from = mask_account_card(tx.get('from', ""))
            account_to = mask_account_card(tx.get('to', ""))
            amount = tx["operationAmount"]["amount"]
            currency = tx["operationAmount"]["currency"]["code"]
            print(f"{date} {description}")
            print(f'{account_from} -> {account_to}')
            print(f"Сумма: {amount} {currency}\n")


if __name__ == '__main__':
    main()
