from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.Population_standard_deviation import population_standard_deviation
from Statistics.Variance_of_population_proportion import variance_of_population_proportion
from Statistics.Z_score import z_score
from Statistics.Standardized_score import score
from Statistics.Correlation_coefficient import correlation_coefficient
from Statistics.Confidence_interval import confidence_interval
from Statistics.Population_variance import population_variance
from Statistics.P_value import p_value
from Statistics.Proportion import proportion
from Statistics.Sample_mean import sample_mean
from Statistics.Sample_standard_deviation import sample_standard_deviation
from Statistics.Variance_of_sample_proportion import variance_of_sample_proportion

class Statistics(Calculator):
    result = 0

    def __init__(self):
        super().__init__()

    def mean(self, a, b, c):
        self.result = mean(a, b, c)
        return self.result

    def med(self, a, b, c, d, e, f):
        self.result = median(a, b, c, d, e, f)
        return self.result

    def mod(self, a, b):
        self.result = mode(a, b)
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
        self.result = score(a, b, c)
        return self.result

    def population1(self, a, b):
        self.result = correlation_coefficient(a, b)
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

    # original Mykola
    #def sample(self, a, b):
     #   self.result = sample_standard_deviation(a, b)
      #  return self.result

        # original Michelle
  #  def stan_dev(self, a, b, c, d, e, f, g, h, j, k):
  #      self.result = standard_deviation(a, b, c, d, e, f, g, h, j, k)
  #      return self.result

     def stan_dev(self, a, b, c, d, e, f, g, h, j, k):
         self.result = sample_standard_deviation(a, b, c, d, e, f, g, h, j, k)
         return self.result

    def variance_1(self, a, b):
        self.result = variance_of_sample_proportion(a, b)
        return self.result
