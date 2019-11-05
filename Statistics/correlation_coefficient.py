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

a = [15, 18, 21, 24, 27] 
b = [25, 25, 27, 31, 32]

    # Find the size of array.
n = len(b)
##print(correlationCoefficient(a, b, n))
