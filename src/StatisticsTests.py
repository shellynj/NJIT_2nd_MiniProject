import unittest
from Statistics import Statistics
from CsvReader import CsvReader
from pprint import pprint

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Statistics)

    def test_population_mean(self):
        test_data = CsvReader('/src/mean.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.calculator.mean(row['Value 1'], row['Value 2'], row['Value 3']), int(row['Result']))
           self.assertEqual(self.calculator.result, int(row['Result']))

    def test_median(self):
        test_data = CsvReader('/src/median.csv').data
        for row in test_data:
           self.assertEqual(self.calculator.med(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4'], row['Value 5']), int(row['Result']))
           self.assertEqual(self.calculator.result, int(row['Result']))

    def test_mode(self):
        test_data = CsvReader('/src/mode.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.calculator.mod(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4'], row['Value 5'], row['Value 6']), int(row['Result']))
           self.assertEqual(self.calculator.result, int(row['Result']))

    def test_population_standard_deviation(self):
        test_data = CsvReader('/src/devi.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.population(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_variance_of_population_proportion(self):
        test_data = CsvReader('').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.calculator.variance(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.calculator.result, int(row['Result']))

    def test_z_score(self):
        test_data = CsvReader('').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.calculator.score(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.calculator.result, int(row['Result']))

    def test_standardized_score(self):
        test_data = CsvReader('').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.calculator.standardized(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.calculator.result, int(row['Result']))

    def test_correlation_coefficient(self):
        test_data = CsvReader('').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.calculator.population1(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.calculator.result, int(row['Result']))

    def test_confidence_interval(self):
        test_data = CsvReader('').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.calculator.confidence(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.calculator.result, int(row['Result']))

    def test_population_variance(self):
        test_data = CsvReader('1').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.calculator.variance_p(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.calculator.result, int(row['Result']))

    def test_p_value(self):
        test_data = CsvReader('2').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.calculator.value(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.calculator.result, int(row['Result']))

    def test_proportion(self):
        test_data = CsvReader('3').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.calculator.prop(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.calculator.result, int(row['Result']))

    def test_sample_mean(self):
        test_data = CsvReader('4').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.calculator.s_mean(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.calculator.result, int(row['Result']))

    def test_sample_standard_deviation(self):
        test_data = CsvReader('5').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.calculator.sample(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.calculator.result, int(row['Result']))

    def test_variance_of_sample_proportion(self):
        test_data = CsvReader('6').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.calculator.variance_1(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.calculator.result, int(row['Result']))

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

if __name__ == '__main__':
    unittest.main()
