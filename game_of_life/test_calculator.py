import pytest
from .calculator import evaluate

def test_expression():
    # When the expression is evaluated
    result = evaluate("asd")
    # Then the result is as expected
    assert result == 0