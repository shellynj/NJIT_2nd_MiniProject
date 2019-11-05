from Statistics.population_mean import population_mean
from Statistics.median import median
from Statistics.mode import mode
from Statistics.population_standard_deviation import population_standard_deviation
from Statistics.variance_of_population_proportion import variance_of_population_proportion
from Statistics.z_score import z_score
from Statistics.standardized_score import standardized_score
from Statistics.correlation_coefficient import correlation_coefficient
from Statistics.confidence_interval import confidence_interval
from Statistics.population_variance import population_variance
from Statistics.p_value import p_value
from Statistics.proportion import proportion
from Statistics.sample_mean import sample_mean
from Statistics.sample_standard_deviation import sample_standard_deviation
from Statistics.variance_of_sample_proportion import variance_of_sample_proportion

class Statistics:
    result = 0

    def __init__(self):
        pass

    def mean(self, a, b, c):
        self.result = population_mean(a, b, c)
        return self.result

    def med(self, a, b, c, d, e):
        self.result = median(a, b, c, d, e)
        return self.result

    def mod(self, a, b, c, d, e, f, g):
        self.result = mode(a, b, c, d, e, f, g)
        return self.result

    def population(self, a, b):
        self.result = population_standard_deviation(a, b)
        return self.result

    def variance(self, a, b):
        self.result = variance_of_population_proportion(a, b)
        return self.result

    def score(self, a, b, c):
        self.result = z_score(a, b, c)
        return self.result

    def standardized(self, a, b, c):
        self.result = standardized_score(a, b, c)
        return self.result

    def population1(self, a, b, n):
        self.result = correlation_coefficient(a, b, n)
        return self.result

    def confidence(self, a, b):
        self.result = confidence_interval(a, b)
        return self.result

    def variance_p(self, a, b):
        self.result = population_variance(a, b)
        return self.result

    def value(self, a, b):
        self.result = p_value(a, b)
        return self.result

    def prop(self, a, b):
        self.result = proportion(a, b)
        return self.result

    def s_mean(self, a, b):
        self.result = sample_mean(a, b)
        return self.result

    def sample(self, a, b):
        self.result = sample_standard_deviation(a, b)
        return self.result

    def variance_1(self, a, b):
        self.result = variance_of_sample_proportion(a, b)
        return self.result
