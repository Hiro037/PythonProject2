import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("string1, expected_result1", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2025-06-29T02:26:18.671407", "29.06.2025")
])
def test_get_date(string1: str, expected_result1: str):
    assert get_date(string1) == expected_result1
    assert get_date(string1) == expected_result1


@pytest.mark.parametrize("string2, expected_result2", [
    ('Maestro 1596837868705199', 'Maestro 159683******5199'),
    ('Visa Classic 6831982476737658', 'Visa Classic 683198******7658'),
    ('Счет 73654108430135874305', 'Счет **4305')
])
def test_mask_account_card(string2: str, expected_result2: str):
    assert mask_account_card(string2) == expected_result2
    assert mask_account_card(string2) == expected_result2
    assert mask_account_card(string2) == expected_result2
