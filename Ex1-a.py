def S(n):
    if n == 1:
        return 10
    else:
        return S(n-1) + 10


print(S(2))