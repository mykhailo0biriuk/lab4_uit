import unittest
from main import add_numbers, subtract_numbers, multiply_numbers, divide_numbers
import xmlrunner

if __name__ == '__main__':
    with open('test-reports/results.xml', 'w') as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output))


class TestCalculatorFunctions(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(3, 5), 8)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertAlmostEqual(add_numbers(2.5, 3.1), 5.6)

    def test_subtract_numbers(self):
        self.assertEqual(subtract_numbers(10, 5), 5)
        self.assertEqual(subtract_numbers(0, 0), 0)
        self.assertAlmostEqual(subtract_numbers(5.5, 2.2), 3.3)

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(3, 5), 15)
        self.assertEqual(multiply_numbers(0, 5), 0)
        self.assertAlmostEqual(multiply_numbers(1.5, 2), 3.0)

    def test_divide_numbers(self):
        self.assertEqual(divide_numbers(10, 2), 5)
        self.assertAlmostEqual(divide_numbers(5.5, 2.2), 2.5)
        with self.assertRaises(ValueError):
            divide_numbers(10, 0)

if __name__ == "__main__":
    unittest.main()
