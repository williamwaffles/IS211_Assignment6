
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

def convertMilesToYards(miles):

    yards = round(float(miles * 1760), 2)
    return yards

def convertMilesToMeters(miles):

    meters = round(float(miles * 1609.34), 2)
    return meters

def convertYardsToMiles(yards):

    miles = round(float(yards / 1760), 2)
    return miles

def convertYardsToMeters(yards):

    meters = round(float(yards / 1.094), 2)
    return meters

def convertMetersToMiles(meters):

    miles = round(float(meters / 1609), 2)
    return miles

def convertMetersToYards(meters):

    yards = round(float(meters * 1.094), 2)
    return yards