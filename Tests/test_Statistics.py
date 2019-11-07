import unittest
from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CsvReader
from pprint import pprint

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_population_mean(self):
        test_data = CsvReader("Tests/Data/mean.csv").data
        pprint(test_data)
        for row in test_data:
           result = int(row['Result'])
           self.assertEqual(self.statistics.mean(row['Value 1'], row['Value 2'], row['Value 3']), result)
           self.assertEqual(self.statistics.result, result)

    def test_median(self):
        test_data = CsvReader("Tests/Data/median.csv").data
        pprint(test_data)
        for row in test_data:
           result = float(row['Result'])
           self.assertEqual(self.statistics.med(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4'], row['Value 5'], row['Value 6']), result)
           self.assertEqual(self.statistics.result, result)

    ##def test_mode(self):
      ##  test_data = CsvReader("Tests/Data/mode.csv").data
        ##pprint(test_data)
        ##for row in test_data:
          ## result = float(row['Result'])
           ##self.assertEqual(self.statistics.mod(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4'], row['Value 5'], row['Value 6']), result)
           ##self.assertEqual(self.statistics.result, result)

    def test_correlation_coefficient(self):
        test_data = CsvReader("Tests/Data/mode1.csv").data
        pprint(test_data)
        for row in test_data:
           result = int(row['Result'])
           self.assertEqual(self.statistics.mod(row['Value 1'], row['Value 2']), result)
           self.assertEqual(self.statistics.result, result)

    def test_population_standard_deviation(self):
        test_data = CsvReader("Tests/Data/devi.csv").data
        pprint(test_data)
        for row in test_data:
            result = int(row['Result'])
            self.assertEqual(self.statistics.population(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.statistics.result, result)

    def test_variance_of_population_proportion(self):
        test_data = CsvReader("Tests/Data/variance.csv").data
        pprint(test_data)
        for row in test_data:
           result = int(row['Result'])
           self.assertEqual(self.statistics.variance(row['Value 1'], row['Value 2']), result)
           self.assertEqual(self.statistics.result, result)

    def test_z_score(self):
        test_data = CsvReader("Tests/Data/score.csv").data
        pprint(test_data)
        for row in test_data:
           result = float(row['Result'])
           self.assertEqual(self.statistics.score(row['Value 1'], row['Value 2'], row['Value 3']), result)
           self.assertEqual(self.statistics.result, result)

    def test_standardized_score(self):
        test_data = CsvReader("Tests/Data/score_1.csv").data
        pprint(test_data)
        for row in test_data:
           result = float(row['Result'])
           self.assertEqual(self.statistics.standardized(row['Value 1'], row['Value 2'], row['Value 3']), result)
           self.assertEqual(self.statistics.result, result)

    def test_correlation_coefficient(self):
        test_data = CsvReader("Tests/Data/1.csv").data
        pprint(test_data)
        for row in test_data:
           result = int(row['Result'])
           self.assertEqual(self.statistics.population1(row['Value 1'], row['Value 2']), result)
           self.assertEqual(self.statistics.result, result)

    def test_confidence_interval(self):
        test_data = CsvReader("Tests/Data/2.csv").data
        pprint(test_data)
        for row in test_data:
           result = int(row['Result'])
           self.assertEqual(self.statistics.confidence(row['Value 1'], row['Value 2']), result)
           self.assertEqual(self.statistics.result, result)

    def test_population_variance(self):
        test_data = CsvReader("Tests/Data/3.csv").data
        pprint(test_data)
        for row in test_data:
           result = int(row['Result'])
           self.assertEqual(self.statistics.variance_p(row['Value 1'], row['Value 2']), result)
           self.assertEqual(self.statistics.result, result)

    def test_p_value(self):
        test_data = CsvReader("Tests/Data/4.csv").data
        pprint(test_data)
        for row in test_data:
           result = int(row['Result'])
           self.assertEqual(self.statistics.value(row['Value 1'], row['Value 2']), result)
           self.assertEqual(self.statistics.result, result)

    def test_proportion(self):
        test_data = CsvReader("Tests/Data/5.csv").data
        pprint(test_data)
        for row in test_data:
           result = int(row['Result'])
           self.assertEqual(self.statistics.prop(row['Value 1'], row['Value 2']), result)
           self.assertEqual(self.statistics.result, result)

    def test_sample_mean(self):
        test_data = CsvReader("Tests/Data/6.csv").data
        pprint(test_data)
        for row in test_data:
           result = int(row['Result'])
           self.assertEqual(self.statistics.s_mean(row['Value 1'], row['Value 2']), result)
           self.assertEqual(self.statistics.result, result)

    def test_sample_standard_deviation(self):
        test_data = CsvReader("Tests/Data/7.csv").data
        pprint(test_data)
        for row in test_data:
           result = int(row['Result'])
           self.assertEqual(self.statistics.sample(row['Value 1'], row['Value 2']), result)
           self.assertEqual(self.statistics.result, result)

    def test_variance_of_sample_proportion(self):
        test_data = CsvReader("Tests/Data/8.csv").data
        pprint(test_data)
        for row in test_data:
           result = int(row['Result'])
           self.assertEqual(self.statistics.variance_1(row['Value 1'], row['Value 2']), result)
           self.assertEqual(self.statistics.result, result)

    def test_results_property(self):
        self.assertEqual(self.statistics.result, 0)


if __name__ == '__main__':
    unittest.main()
