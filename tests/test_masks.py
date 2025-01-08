from src.masks import get_mask_account, get_mask_card_number

def test_get_mask_card_number():
    assert get_mask_card_number(7000792289606361) == '700079******6361'
    assert get_mask_card_number(8567452289606361) == '856745******6361'

def test_get_mask_account():
    assert get_mask_account(73654108430135874305) == '**4305'
    assert get_mask_account(73654108430135871234) == '**1234'