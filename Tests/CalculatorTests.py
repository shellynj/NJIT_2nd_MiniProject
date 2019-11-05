import unittest
from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        test_data = CsvReader("Tests/Data/Addition.csv").data
        for row in test_data:
           result = int(row['Result'])
           self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
           self.assertEqual(self.calculator.result, result)

    def test_subtraction(self):
        test_data = CsvReader("Tests/Data/Subtraction.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiplication(self):
        test_data = CsvReader("Tests/Data/Multiplication.csv").data
        for row in test_data:
             result = int(row['Result'])
             self.assertEqual(self.calculator.multiple(row['Value 1'], row['Value 2']), result)
             self.assertEqual(self.calculator.result, result)

    def test_division(self):
        test_data = CsvReader("Tests/Data/Division.csv").data
        for row in test_data:
             result = float(row['Result'])
             self.assertEqual(self.calculator.div(row['Value 1'], row['Value 2']), result)
             self.assertEqual(self.calculator.result, result)

    def test_square(self):
        test_data = CsvReader("Tests/Data/Square.csv").data
        for row in test_data:
             result = int(row['Result'])
             self.assertEqual(self.calculator.squaring(row['Value 1']), result)
             self.assertEqual(self.calculator.result, result)

    def test_square_root(self):
        test_data = CsvReader("Tests/Data/Square_root.csv").data
        for row in test_data:
             result = float(row['Result'])
             self.assertEqual(self.calculator.square_rooting(row['Value 1']), result)
             self.assertEqual(self.calculator.result, result)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

if __name__ == '__main__':
    unittest.main()
