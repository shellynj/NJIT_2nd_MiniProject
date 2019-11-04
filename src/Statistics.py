import math

def population_mean(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    d = (a + b) / c
    return d

def median(a, b, c, d, e):
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)
    med_n = [a, b, c, d, e]
    n = len(med_n)
    med_n.sort()
    if n % 2 == 0:
        median1 = med_n[n // 2]
        median2 = med_n[n // 2 - 1]
        f = (median1 + median2) / 2
    else:
        f = med_n[n // 2]
    return f

def mode(a, b, c, d, e, f, g):
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)
    f = int(f)
    mod_n = [a, b, c, d, e, f]
    n = len(mod_n)
    mode1 = [k for k, v in g.items() if v == max(list(mod_n.values()))]

    if len(mode1) == n:
        g = "no mode"
    else:
        g = "mode is: " + ', '.join(map(str, mode1))
    return g

def population_standard_deviation(a, b):
    a = int(a)
    b = int(b)
    c = (a ** 2) / b
    return c

def variance_of_population_proportion(a, b):
    a = int(a)
    b = int(b)
    c = (a ** 2) / b
    return c ** 2

def z_score(data, a):
    a = int(a)
    b = ((a - population_mean(data)) / population_standard_deviation(data))
    return b

def standardized_score(a, b):
    a = int(a)
    b = int(b)
    c = a + b
    return c

##TEMPORARY TESTING with PROVIDED VALUES
def correlation_coefficient(a, b, n) :
   try:
        sum_a = 0
        sum_b = 0
        sum_ab = 0
        squareSum_a = 0
        squareSum_b = 0
        i = 0
        while i < n:
            # sum of elements of array a.
            sum_a = sum_a + a[i]

            # sum of elements of array b.
            sum_b = sum_b + b[i]

            # sum of a[i] * b[i].
            sum_ab = sum_ab + a[i] * b[i]

            # sum of square of array elements.
            squareSum_a = squareSum_a + a[i] * a[i]
            squareSum_b = squareSum_b + b[i] * b[i]

            i = i + 1

        # Actual Formula for Correlation Coefficient
        # corr = (float(n * sum_ab - sum_a * sum_b)) /(float(math.sqrt((n * squareSum_a - sum_a * sum_b) * (n * squareSum_b - sum_b * sum_b))))
        # Breakdown of formula for Correlation Coefficient.
        c = float(n * squareSum_a - sum_a * sum_a)
        d = float(n * squareSum_b - sum_b * sum_b)
        e = float(math.sqrt(c * d))
        f = float(n * sum_ab - sum_a * sum_b)
        corr = float(f / e)
        return corr
    except ZeroDivisionError:
        print("Error: Dividing by Zero is not valid!!")
    except ValueError:
        print ("Error: Only Numeric Values are valid!!")

##a = [15, 18, 21, 24, 27] ( you need cvs file)
##b = [25, 25, 27, 31, 32] ( you need cvs file)

    # Find the size of array.
##n = len(b)
##print(correlationCoefficient(a, b, n))

def confidence_interval(a, b):
    c = a + b
    return c

def population_variance(a, b):
    c = a + b
    return c

def p_value(a, b):
    c = a + b
    return c

def proportion(a, b):
    c = a + b
    return c

def sample_mean(a, b):
    c = a + b
    return c

def sample_standard_deviation(a, b):
    c = a + b
    return c

def variance_of_sample_proportion(a, b):
    c = a + b
    return c

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

    def score(self, a):
        self.result = z_score(a)
        return self.result

    def standardized(self, a, b):
        self.result = standardized_score(a, b)
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
