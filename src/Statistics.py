def population_mean(a, b):
    return c

def median(a, b):
    return c

def mode(a, b):
    return c

def population_standard_deviation(a, b):
    return c

def variance_of_population_proportion(a, b):
    return c

def z_score(a, b):
    return c

def standardized_score(a, b):
    return c

def population_correlation_coefficient(a, b):
    return c

def confidence_interval(a, b):
    return c

def population_variance(a, b):
    return c

def p_value(a, b):
    return c

def proportion(a, b):
    return c

def sample_mean(a, b):
    return c

def sample_standard_deviation(a, b):
    return c

def variance_of_sample_proportion(a, b):
    return c

class Statistics:
    result = 0

    def __init__(self):
        pass

    def population(self, a, b):
        self.result = population_standard_deviation(a, b)
        return self.result

    def variance(self, a, b):
        self.result = variance_of_population_proportion(a, b)
        return self.result

    def score(self, a, b):
        self.result = z_score(a, b)
        return self.result

    def standardized(self, a, b):
        self.result = standardized_score(a, b)
        return self.result

    def population(self, a, b):
        self.result = population_correlation_coefficient(a, b)
        return self.result

    def confidence(self, a, b):
        self.result = confidence_interval(a, b)
        return self.result

    def variance(self, a, b):
        self.result = population_variance(a, b)
        return self.result

    def value(self, a, b):
        self.result = p_value(a, b)
        return self.result

    def prop(self, a, b):
        self.result = proportion(a, b)
        return self.result

    def smean(self, a, b):
        self.result = sample_mean(a, b)
        return self.result

    def sample(self, a, b):
        self.result = sample_standard_deviation(a, b)
        return self.result

    def variance(self, a, b):
        self.result = variance_of_sample_proportion(a, b)
        return self.result