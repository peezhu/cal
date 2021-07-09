import unittest
from Calculator import Calculator
from CsvReader import CsvReader


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
        for row in test_data:
            self.assertEqual(calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(calculator.result, int(row['Result']))

    def test_subtract_method_calculator(self):
        calculator = Calculator()

        test_data = CsvReader('/src/Subtraction.csv').data
        for row in test_data:
            self.assertEqual(calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(calculator.result, int(row['Result']))

    def test_multiply_method_calculator(self):
        calculator = Calculator()

        test_data = CsvReader('/src/Multiplication.csv').data
        for row in test_data:
            self.assertEqual(calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(calculator.result, int(row['Result']))

    def test_divide_method_calculator(self):
        calculator = Calculator()

        test_data = CsvReader('/src/Division.csv').data
        for row in test_data:
            self.assertEqual(calculator.divide(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(calculator.result, int(row['Result']))

    def test_square_method_calculator(self):
        calculator = Calculator()

        test_data = CsvReader('/src/Square.csv').data
        for row in test_data:
            self.assertEqual(calculator.square(row['Value 1']), int(row['Result']))
            self.assertEqual(calculator.result, row['Result'])

    def test_square_root_method_calculator(self):
        calculator = Calculator()

        test_data = CsvReader('/src/Root.csv').data
        for row in test_data:
            self.assertEqual(calculator.root(row['Value 1']), int(row['Result']))
            self.assertEqual(calculator.result, int(row['Result']))


if __name__ == '__main__':
    unittest.main()
