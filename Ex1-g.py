def T(n):
    if n <= 3:
        return n
    else:
        return T(n-1) + 2 * T(n-2) + 3 * T(n-3)


print(T(5))