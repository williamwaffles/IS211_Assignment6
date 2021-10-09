from conversions import convertCelsiusToKelvin, convertCelsiusToFahrenheit, convertFahrenheitToKelvin, convertFahrenheitToCelsius, convertKelvinToFahrenheit, convertKelvinToCelsius
from conversions import convertMilesToMeters, convertMilesToYards, convertYardsToMeters, convertYardsToMiles, convertMetersToMiles, convertMetersToYards
import unittest

class conversion_tester(unittest.TestCase):

    c_to_k = ((54, 327.15), (0, 273.15), (32, 305.15), (100, 373.15), (66, 339.15))
    c_to_f = ((54, 129.2), (0, 32.0), (32, 89.6), (100, 212.0), (66, 150.8))
    f_to_k = ((36,275.37), (85, 302.59), (10, 260.93), (1, 255.93), (53, 284.82))
    f_to_c = ((36, 2.22), (255, 123.89), (69, 20.56), (87.5, 30.83), (55.34, 12.97))
    k_to_c = ((0, -273.15), (23.34, -249.81), (289, 15.85), (333.33, 60.18), (430.45, 157.3))
    k_to_f = ((777, 938.93), (656.56, 722.14), (300, 80.33), (9887, 17336.93), (225.67, -53.46))
    miles_to_yards = ((2, 3520), (1, 1760), (6, 10560), (76, 133760), (23, 40480))
    miles_to_meters = ((3, 4828.02), (13, 20921.42), (1, 1609.34), (5.5, 8851.37), (.25, 402.33))
    meters_to_miles = ((44, .03), (5023, 3.12), (192.24, .12), (55232, 34.33), (12345, 7.67))
    meters_to_yards = ((77, 84.24), (3429, 3751.33), (1000.4, 1094.44), (69333, 75850.3), (15, 16.41) )
    yards_to_miles = ((4252, 2.42), (100, 0.06), (1425.3, 0.81), (235235, 133.66), (5555.55, 3.16))
    yards_to_meters = ((324, 296.16), (122, 111.52), (12, 10.97), (12414, 11347.35), (9984, 9126.14))

    # test cases for Celsius to Kelvin conversions
    def test_convertCelsiusToKelvin(self):
        print('--------------------------------------')
        print('Testing Celsius to Kelvin conversions:')
        for c, k, in self.c_to_k:
            result = convertCelsiusToKelvin(c)
            self.assertEqual(result, k)
            print(f'The temperature {c} in Celsius is equal to {k} in Kelvin.')

    # test cases for Celsius to Fahrenheit
    def test_convertCelsiusToFarenheit(self):
        print('--------------------------------------')
        print('Testing Celsius to Fahrenheit conversions:')
        for c, f, in self.c_to_f:
            result = convertCelsiusToFahrenheit(c)
            self.assertEqual(result, f)
            print(f'The temperature {c} in Celsius is equal to {f} in Fahrenheit.')


    # test cases for Fahrenheit to Kelvin
    def test_convertFahrenheitToKelvin(self):
        print('--------------------------------------')
        print('Testing Fahrenheit to Kelvin conversions:')
        for f, k, in self.f_to_k:
            result = convertFahrenheitToKelvin(f)
            self.assertEqual(result, k)
            print(f'The temperature {f} in Fahrenheit is equal to {k} in Kelvin.')

    # test cases for Fahrenheit to Celsius
    def test_convertFahrenheitToCelsius(self):
        print('--------------------------------------')
        print('Testing Fahrenheit to Celsius conversions:')
        for f, c, in self.f_to_c:
            result = convertFahrenheitToCelsius(f)
            self.assertEqual(result, c)
            print(f'The temperature {f} in Fahrenheit is equal to {c} in Kelvin.')

    # test cases for Kelvin to Fahrenheit
    def test_convertKelvinToFahrenheit(self):
        print('--------------------------------------')
        print('Testing Kelvin to Fahrenheit conversions:')
        for k, f, in self. k_to_f:
            result = convertKelvinToFahrenheit(k)
            self.assertEqual(result, f)
            print(f'The temperature {k} in Kelvin is equal to {f} in Fahrenheit.')


    # test cases for Kelvin to Celsius
    def test_convertKelvinToCelsius(self):
        print('--------------------------------------')
        print('Testing Kelvin to Celsius conversions.')
        for k, c, in self.k_to_c:
            result = convertKelvinToCelsius(k)
            self.assertEqual(result, c)
            print(f'The temperature {k} in Kelvin is equal to {c} in Fahrenheit.')

    # test cases for Miles to Yards
    def test_convertMilesToYards(self):
        print('--------------------------------------')
        print('Testing Miles to Yards conversions.')
        for m, y, in self.miles_to_yards:
            result = convertMilesToYards(m)
            self.assertEqual(result, y)
            print(f'The distance {m} in Miles is equal to {y} Yards.')

    # test cases for Miles to Meters
    def test_convertMilesToMeters(self):
        print('--------------------------------------')
        print('Testing Miles to Meters conversions.')
        for m, met, in self.miles_to_meters:
            result = convertMilesToMeters(m)
            self.assertEqual(result, met)
            print(f'The distance {m} in Miles is equal to {met} Meters.')

    # test cases for Meters to Miles
    def test_convertMetersToMiles(self):
        print('--------------------------------------')
        print('Testing Meters to Miles conversions.')
        for met, m, in self.meters_to_miles:
            result = convertMetersToMiles(met)
            self.assertEqual(result, m)
            print(f'The distance {met} in Meters is equal to {m} Miles.')

    # test cases for Meters to Yards
    def test_convertMetersToYards(self):
        print('--------------------------------------')
        print('Testing Meters to Yards conversions.')
        for met, y, in self.meters_to_yards:
            result = convertMetersToYards(met)
            self.assertEqual(result, y)
            print(f'The distance {met} in Meters is equal to {y} Yards.')

    # test cases for Yards to Meters
    def test_convertYardsToMeters(self):
        print('--------------------------------------')
        print('Testing Yards to Meters conversions.')
        for y, met, in self.yards_to_meters:
            result = convertYardsToMeters(y)
            self.assertEqual(result, met)
            print(f'The distance {y} in Yards is equal to {met} Meters.')

    # test cases for Yards to Miles
    def test_convertYardsToMiles(self):
        print('--------------------------------------')
        print('Testing Yards to Miles conversions.')
        for y, m, in self.yards_to_miles:
            result = convertYardsToMiles(y)
            self.assertEqual(result, m)
            print(f'The distance {y} in Yards is equal to {m} Miles.')


if __name__ == '__main__':
    unittest.main()