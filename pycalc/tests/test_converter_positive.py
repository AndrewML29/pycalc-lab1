import pytest
from toolkit.converter import convert

def test_length_conversions():
    assert convert(1000, "m", "km") == 1.0
    assert convert(500, "mm", "m") == 0.5
    assert convert(100, "cm", "mm") == 1000.0
    assert convert(1, "km", "cm") == 100000.0

def test_mass_conversions():
    assert convert(1000, "g", "kg") == 1.0
    assert convert(1, "kg", "mg") == 1000000.0
    assert convert(500, "mg", "g") == 0.5

def test_temperature_conversions():
    assert convert(0, "c", "f") == 32.0
    assert convert(100, "c", "k") == 373.15
    assert convert(32, "f", "k") == 273.15
    assert convert(273.15, "k", "c") == 0.0

def test_case_insensitivity():
    assert convert(100, "KG", "g") == 100000.0
    assert convert(100, "m", "KM") == 0.1