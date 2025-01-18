import pytest
from decorators import log

@log()
def add(a, b):
    return a + b

@log()
def divide(a, b):
    return a / b

def test_log_successful_function_execution(capsys):
    """Тест успешного выполнения функции с выводом в консоль."""
    result = add(3, 7)
    assert result == 10

    captured = capsys.readouterr()
    assert "add ok" in captured.out


def test_log_function_exception(capsys):
    """Тест обработки исключения с выводом в консоль."""
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError." in captured.out
    assert "Inputs: (10, 0), {}" in captured.out

