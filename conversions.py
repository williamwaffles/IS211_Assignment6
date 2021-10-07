
def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""

    kelvins = float((celsius) + 273.15)
    return kelvins


def convertCelsiusToFahrenheit(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit"""
    fahrenheit = float(((9/5) * celsius) + 32)
    
    return fahrenheit

print(convertCelsiusToFahrenheit(45))
print(convertCelsiusToKelvin(66))