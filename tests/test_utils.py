import json

import pytest

from src.utils import amount_transactions, fin_transactions


@pytest.fixture
def valid_json_file(tmp_path):
    file = tmp_path / "valid.json"
    file.write_text(json.dumps([{"id": 1, "operation": "Payment"}, {"id": 2, "operation": "Transfer"}]))
    return str(file)


@pytest.fixture
def empty_file(tmp_path):
    file = tmp_path / "empty.json"
    file.write_text("")
    return str(file)


@pytest.fixture
def invalid_json_file(tmp_path):
    file = tmp_path / "invalid.json"
    file.write_text("{invalid_json: true")
    return str(file)


def test_fin_transactions_valid_json(valid_json_file):
    """Тест для файла с валидным JSON."""
    result = fin_transactions(valid_json_file)
    assert result == [{"id": 1, "operation": "Payment"}, {"id": 2, "operation": "Transfer"}]


def test_fin_transactions_empty_file(empty_file, capsys):
    """Тест для пустого файла."""
    result = fin_transactions(empty_file)
    captured = capsys.readouterr()
    assert result == []
    assert "Ошибка декодирования" in captured.out


def test_fin_transactions_invalid_json(invalid_json_file, capsys):
    """Тест для файла с некорректным JSON."""
    result = fin_transactions(invalid_json_file)
    captured = capsys.readouterr()
    assert result == []
    assert "Ошибка декодирования" in captured.out


def test_fin_transactions_file_not_found(capsys):
    """Тест для отсутствующего файла."""
    result = fin_transactions("nonexistent.json")
    captured = capsys.readouterr()
    assert result == []
    assert "Файл не найден" in captured.out


def test_amount_transactions_RUB():
    transaction = {
        "operationAmount": {
            "currency": {"code": "RUB"},
            "amount": "50"
        }
    }
    result = amount_transactions(transaction)
    assert result == 'Сумма транзакции: 50.0 рублей.'
