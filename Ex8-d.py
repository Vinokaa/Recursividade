def D(n, p, q):
    if n == 1:
        return p
    elif n == 2:
        return p - q
    else:
        if n % 2 == 1:
            return D(n-2, p, q) + q
        else:
            return D(n-2, p, q) - q


print(D(4, 2, 1))