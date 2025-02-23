import pytest
import pandas as pd
from io import StringIO
from unittest.mock import mock_open, patch

# Импорт тестируемых функций (замените 'transactions' на актуальное имя модуля)
from src.data_import import read_csv_transactions, read_excel_transactions


def test_read_csv_transactions_success():
    # Тестовые данные CSV
    csv_data = (
        "date,amount,description\n"
        "2022-01-01,100,Test transaction\n"
        "2022-01-02,200,Another transaction"
    )
    # Настраиваем mock для встроенной функции open
    m = mock_open(read_data=csv_data)
    with patch("builtins.open", m):
        transactions = read_csv_transactions("dummy.csv")

    expected = [
        {"date": "2022-01-01", "amount": "100", "description": "Test transaction"},
        {"date": "2022-01-02", "amount": "200", "description": "Another transaction"},
    ]

    assert transactions == expected
    m.assert_called_with("dummy.csv", mode="r", newline="", encoding="utf-8")


def test_read_csv_transactions_file_not_found():
    # Проверяем, что функция корректно обрабатывает отсутствие файла
    with patch("builtins.open", side_effect=FileNotFoundError):
        transactions = read_csv_transactions("nonexistent.csv")
    assert transactions == []


def test_read_excel_transactions_success():
    # Тестовые данные в виде DataFrame
    test_data = {
        "date": ["2022-01-01", "2022-01-02"],
        "amount": [100, 200],
        "description": ["Test transaction", "Another transaction"],
    }
    df = pd.DataFrame(test_data)

    with patch("pandas.read_excel", return_value=df) as mock_read_excel:
        transactions = read_excel_transactions("dummy.xlsx")

    expected = df.to_dict(orient="records")
    assert transactions == expected
    mock_read_excel.assert_called_with("dummy.xlsx")


def test_read_excel_transactions_file_not_found():
    # Проверяем обработку ошибки при отсутствии Excel файла
    with patch("pandas.read_excel", side_effect=FileNotFoundError):
        transactions = read_excel_transactions("nonexistent.xlsx")
    assert transactions == []
