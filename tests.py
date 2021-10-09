from conversions import convertCelsiusToKelvin, convertCelsiusToFahrenheit, convertFahrenheitToKelvin, convertFahrenheitToCelsius, convertKelvinToFahrenheit, convertKelvinToCelsius
import unittest

class conversion_tester(unittest.TestCase):

    c_to_k = ((54, 327.15), (0, 273.15), (32, 305.15), (100, 373.15), (66, 339.15))
    c_to_f = ((54, 129.2), (0, 32.0), (32, 89.6), (100, 212.0), (66, 150.8))
    f_to_k = ((36,275.37), (85, 302.59), (10, 260.93), (1, 255.93), (53, 284.82))
    f_to_c = ((36, 2.22), (255, 123.89), (69, 20.56), (87.5, 30.83), (55.34, 12.97))
    k_to_c = ((0, -273.15), (23.34, -249.81), (289, 15.85), (333.33, 60.18), (430.45, 157.3))
    k_to_f = ((777, 938.93), (656.56, 722.14), (300, 80.33), (9887, 17336.93), (225.67, -53.46))

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


if __name__ == '__main__':
    unittest.main()