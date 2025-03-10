from src.session_6.challenge import factorial
import pytest

def test_factorial():
    assert factorial(10) == 3628800
    assert factorial(1) == 1

    with pytest.raises(Exception, match="Sorry, no numbers below zero"):
        factorial(-5)