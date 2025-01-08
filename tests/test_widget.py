from src.widget import get_date, mask_account_card

def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2025-06-29T02:26:18.671407") == "29.06.2025"

def test_mask_account_card():
    assert mask_account_card('Maestro 1596837868705199') == 'Maestro 159683******5199'
    assert mask_account_card('Visa Classic 6831982476737658') == 'Visa Classic 683198******7658'
    assert mask_account_card('Счет 73654108430135874305') == 'Счет **4305'