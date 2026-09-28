import pytest

from src.converter import celsius_to_fahrenheit, kelvin_to_celsius, km_to_miles


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32


def test_km_to_miles():
    assert round(km_to_miles(1), 6) == 0.621371


def test_kelvin_to_celsius():
    assert kelvin_to_celsius(273.15) == 0
    assert kelvin_to_celsius(300) == 26.85


def test_kelvin_to_celsius_rejects_negative_temperature():
    with pytest.raises(ValueError, match="cannot be negative"):
        kelvin_to_celsius(-1)
def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212

def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    
def main():
    test_celsius_to_fahrenheit()
    test_fahrenheit_to_celsius()
