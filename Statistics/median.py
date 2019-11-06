def median(a, b, c, d, e):
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)
    med = [a, b, c, d, e]
    med.sort()
    med_s = len(med) // 2
    g = med(med_s)
    h = med(-med_s -1)
    f = (g + h) / 2
    return f