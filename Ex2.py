def PG(n, a1, r):
    if n == 1:
        return a1
    else:
        return PG(n-1, a1, r) * r


print(PG(5, 1, 2))