def median(a, b, c, d, e):
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)
    med_n = [a, b, c, d, e]
    med_n.sort()
    med_s = len(med_n) // 2
    g = med_n(med_s)
    h = med_n(-med_s -1)
    f = (g + h) / 2
    return f