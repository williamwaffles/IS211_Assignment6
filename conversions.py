
class convert_temp_exception(Exception):
    pass

def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""

    kelvins = round(float((celsius) + 273.15), 2)
    return kelvins


def convertCelsiusToFahrenheit(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit"""

    fahrenheit = round(float(((1.8) * celsius) + 32), 2)
    return fahrenheit

def convertFahrenheitToKelvin(fahrenheit):

    kelvins = round(float(((fahrenheit + 459.67) * (5/9))), 2)
    return kelvins

def convertFahrenheitToCelsius(fahrenheit):

    celsius = round(float((fahrenheit - 32) * (5/9)), 2)
    return celsius

def convertKelvinToFahrenheit(kelvins):

    fahrenheit = round(float((kelvins * 1.8) - 459.67), 2)
    return fahrenheit

def convertKelvinToCelsius(kelvins):

    celsius = round(float(kelvins - 273.15), 2)
    return celsius

print(convertCelsiusToFahrenheit(45))
print(convertCelsiusToKelvin(66))
print(convertFahrenheitToKelvin(80))
print(convertFahrenheitToCelsius(212))
