import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint

class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_results_property_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.result, 0)

    def test_add_method_calculator(self):
        calculator = Calculator()

        test_data = CsvReader('/src/Addition.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(calculator.add(row['Value 1'], row['Value 2']), row('Result'))
            self.assertEqual(calculator.result, row['Result'])

    def test_subtract_method_calculator(self):
        calculator = Calculator()

        test_data = CsvReader('/src/Subtraction.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(calculator.subtract(row['Value 1'], row['Value 2']), row('Result'))
            self.assertEqual(calculator.result, row['Result'])


    def test_multiply_method_calculator(self):
        calculator = Calculator()

        test_data = CsvReader('/src/Multiplication.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(calculator.multiply(row['Value 1'], row['Value 2']), row('Result'))
            self.assertEqual(calculator.result, row['Result'])



    def test_divide_method_calculator(self):
        calculator = Calculator()

        test_data = CsvReader('/src/Division.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(calculator.divide(row['Value 1'], row['Value 2']), row('Result'))
            self.assertEqual(calculator.result, row['Result'])

    def test_square_method_calculator(self):
        calculator = Calculator()


    def test_square_root_method_calculator(self):
        calculator = Calculator()



if __name__ == '__main__':
    unittest.main()
