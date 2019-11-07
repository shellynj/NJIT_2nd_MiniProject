def score(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    ## a is value
    ## b is mean
    ## c is standard deviation
    d = (a - b) / c
    return d
