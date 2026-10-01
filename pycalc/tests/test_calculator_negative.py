import pytest
from toolkit.calculator import calculate
from toolkit.errors import ValidationError, DivisionByZeroError

def test_empty_expression():
    with pytest.raises(ValidationError):
        calculate("")

def test_invalid_characters():
    with pytest.raises(ValidationError):
        calculate("5 & 3")

def test_missing_operand():
    with pytest.raises(ValidationError):
        calculate("5 + * 3")

def test_two_binary_operators():
    with pytest.raises(ValidationError):
        calculate("5 ++ 3")

def test_division_by_zero():
    with pytest.raises(DivisionByZeroError):
        calculate("5 / 0")

def test_invalid_numeric_value():
    with pytest.raises(ValidationError):
        calculate("a + b")

def test_starts_with_binary_operator():
    with pytest.raises(ValidationError):
        calculate("*5+3")
    with pytest.raises(ValidationError):
        calculate("/2+1")
