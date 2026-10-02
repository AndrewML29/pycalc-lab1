import pytest
from toolkit.calculator import calculate

def test_basic_operations():
    assert calculate("1+1") == 2
    assert calculate("5-3") == 2
    assert calculate("4*3") == 12
    assert calculate("10/2") == 5.0

def test_integer_operations():
    assert calculate("10//3") == 3
    assert calculate("10%3") == 1

def test_unary_signs():
    assert calculate("-5+3") == -2
    assert calculate("5+-3") == 2

def test_precedence():
    assert calculate("2+3*4") == 14
    assert calculate("10-4/2") == 8
    assert calculate("2*(3+4)") == 14

def test_floats():
    assert calculate("2.5+1.5") == 4.0
    assert calculate("10.5/2") == 5.25

def test_spaces_ignored():
    assert calculate("1 + 1") == 2
    assert calculate(" 5 * 3 ") == 15
    assert calculate("10 / 2 + 3") == 8.0