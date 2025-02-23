import csv
import pandas as pd


def read_csv_transactions(file_path: str) -> list[dict]:
    """
    Считывает финансовые транзакции из CSV-файла.

    Аргументы:
        file_path (str): Путь к CSV-файлу.

    Возвращает:
        list[dict]: Список словарей, где каждый словарь представляет транзакцию.
    """
    transactions = []
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                transactions.append(row)
            return transactions
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return []

def read_excel_transactions(file_path: str) -> list[dict]:
    """
    Считывает финансовые транзакции из Excel-файла.

    Аргументы:
        file_path (str): Путь к Excel-файлу.

    Возвращает:
        list[dict]: Список словарей, где каждый словарь представляет транзакцию.
    """
    try:
        # Чтение Excel-файла с помощью pandas
        df = pd.read_excel(file_path)
        # Преобразование DataFrame в список словарей
        transactions = df.to_dict(orient='records')
        return transactions
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return []



