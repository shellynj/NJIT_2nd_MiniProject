import unittest
from Statistics import Statistics
from CsvReader import CsvReader
from pprint import pprint

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.Statistics = Statistics()

    def test_instantiate_Statistics(self):
        self.assertIsInstance(self.Statistics, Statistics)

    def test_population_mean(self):
        test_data = CsvReader('/src/test.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.mean(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result']))

    def test_median(self):
        test_data = CsvReader('/src/test.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.med(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result']))

    def test_mode(self):
        test_data = CsvReader('/src/test.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.mod(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result']))

    def test_population_standard_deviation(self):
        test_data = CsvReader('/src/test.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.population(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result'])

    def test_variance_of_population_proportion(self):
        test_data = CsvReader('/src/test.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.variance(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result'])

    def test_variance_of_population_proportion(self):
        test_data = CsvReader('/src/test.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.variance(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result'])

    def test_zscore(self):
        test_data = CsvReader('/src/test.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.score(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result'])

    def test_standardized_score(self):
        test_data = CsvReader('/src/test.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.standardized(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result'])

    def test_population_correlation_coefficient(self):
        test_data = CsvReader('/src/test.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.population(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result'])

    def test_confidence_interval(self):
        test_data = CsvReader('/src/test.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.confidence(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result'])

    def test_population_variance(self):
        test_data = CsvReader('/src/test.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.variance(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result'])

    def test_pvalue(self):
        test_data = CsvReader('/src/test.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.value(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result'])

    def test_proportion(self):
        test_data = CsvReader('/src/test.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.prop(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result'])

    def test_sample_mean(self):
        test_data = CsvReader('/src/test.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.smean(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result'])

    def test_sample_standard_deviation(self):
        test_data = CsvReader('/src/test.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.sample(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result'])

    def test_variance_of_sample_proportion(self):
        test_data = CsvReader('/src/test.csv').data
        pprint(test_data)
        for row in test_data:
           self.assertEqual(self.Statistics.variance(row['Value 1'], row['Value 2']), int(row['Result']))
           self.assertEqual(self.Statistics.result, int(row['Result'])

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

if __name__ == '__main__':
    unittest.main()
