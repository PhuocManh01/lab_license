# Usage

## Calculator

- `add(a, b)`
- `subtract(a, b)`
- `multiply(a, b)`
- `divide(a, b)`

## Converter

- `celsius_to_fahrenheit(celsius)`
- `kelvin_to_celsius(kelvin)`

`kelvin_to_celsius(kelvin)` raises `ValueError` when `kelvin` is negative,
because Kelvin temperatures cannot be below absolute zero.
### Celsius to Fahrenheit

Use `celsius_to_fahrenheit(celsius)` to convert a numeric Celsius value to
Fahrenheit.

Formula:

```text
fahrenheit = (celsius * 9 / 5) + 32
```

Example:

```python
from src.converter import celsius_to_fahrenheit

result = celsius_to_fahrenheit(25)
print(result)  # 77.0
```

The input must be a numeric Celsius value. The function returns the equivalent
temperature in Fahrenheit as a number.

### Fahrenheit to Celsius

To convert a numeric Fahrenheit value to Celsius, use the reverse formula:

```text
celsius = (fahrenheit - 32) * 5 / 9
```

Example:

```python
fahrenheit = 77
celsius = (fahrenheit - 32) * 5 / 9
print(celsius)  # 25.0
```

The input is a numeric Fahrenheit value, and the output is the equivalent
temperature in Celsius as a number.

- `km_to_miles(km)`

## Validator

- `is_positive_number(value)`
- `is_non_empty_text(value)`
