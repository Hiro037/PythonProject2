from typing import Union

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("string1, expected_result1", [
    (7000792289606361, '700079******6361'),
    (8567452289606361, '856745******6361')
])
def test_get_mask_card_number(string1: Union[str, int], expected_result1: str) -> None:
    assert get_mask_card_number(string1) == expected_result1


@pytest.mark.parametrize("string2, expected_result2", [
    (73654108430135874305, '**4305'),
    (73654108430135871234, '**1234')
])
def test_get_mask_account(string2: Union[str, int], expected_result2: str) -> None:
    assert get_mask_account(string2) == expected_result2
