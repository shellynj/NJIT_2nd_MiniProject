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