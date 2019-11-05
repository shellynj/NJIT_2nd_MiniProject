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
        f = round(f, 9)
    else:
        f = med_n[n // 2]
        f = round(f, 9)
    return f