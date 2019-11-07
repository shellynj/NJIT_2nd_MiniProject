from Calculator.Calculator import Calculator
from Statistics.Mean import population_mean
from Statistics.Median import median_i
from Statistics.Mode import mode_i
from Statistics.Population_standard_deviation import deviation
from Statistics.Variance_of_population_proportion import n_proportion
from Statistics.Z_score import z_score_n
from Statistics.Standardized_score import score_n
from Statistics.Correlation_coefficient import correlation
from Statistics.Confidence_interval import interval
from Statistics.Population_variance import population_n
from Statistics.P_value import p_value_n
from Statistics.Proportion import proportion_n
from Statistics.Sample_mean import sample_mean_n
from Statistics.Sample_standard_deviation import sample_standard_deviation_n
from Statistics.Variance_of_sample_proportion import variance_of_sample_proportion_n

class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean(self, a, b, c):
        self.result = population_mean(a, b, c)
        return self.result

    def med(self, a, b, c, d, e, f):
        self.result = median_i(a, b, c, d, e, f)
        return self.result

    def mod(self, a, b):
        self.result = mode_i(a, b)
        return self.result

    def population(self, a, b):
        self.result = deviation(a, b)
        return self.result

    def variance(self, a, b):
        self.result = n_proportion(a, b)
        return self.result

    def score(self, a, b, c):
        self.result = z_score_n(a, b, c)
        return self.result

    def standardized(self, a, b, c):
        self.result = score_n(a, b, c)
        return self.result

    def population1(self, a, b):
        self.result = correlation(a, b)
        return self.result

    def confidence(self, a, b):
        self.result = interval(a, b)
        return self.result

    def variance_p(self, a, b):
        self.result = population_n(a, b)
        return self.result

    def value(self, a, b):
        self.result = p_value_n(a, b)
        return self.result

    def prop(self, a, b):
        self.result = proportion_n(a, b)
        return self.result

    def s_mean(self, a, b):
        self.result = sample_mean_n(a, b)
        return self.result

    def sample(self, a, b):
        self.result = sample_standard_deviation_n(a, b)
        return self.result

    def variance_1(self, a, b):
        self.result = variance_of_sample_proportion_n(a, b)
        return self.result