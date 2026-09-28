def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def kelvin_to_celsius(kelvin):
    if kelvin < 0:
        raise ValueError("Kelvin temperature cannot be negative")
    return kelvin - 273.15


"""Creates conflict with the test file, so I will comment it out for now."""
# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5 / 9
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
