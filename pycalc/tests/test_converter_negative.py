import pytest
from toolkit.converter import convert
from toolkit.errors import ConversionError

def test_incompatible_groups():
    with pytest.raises(ConversionError):
        convert(100, "g", "m")

def test_unknown_unit():
    with pytest.raises(ConversionError):
        convert(100, "stone", "kg")

def test_temperature_below_absolute_zero():
    with pytest.raises(ConversionError):
        convert(-300, "c", "k")

def test_invalid_numeric_value():
    with pytest.raises(ConversionError):
        convert("abc", "m", "km")

def test_empty_value():
    with pytest.raises(ConversionError):
        convert("", "m", "km")