def C(n, a, b):
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        return C(n-2, a, b) + C(n-1, a, b)


print(C(5, 1, 2))