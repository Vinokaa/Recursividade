def B(n):
    if n == 1:
        return 2
    else:
        return B(n-1) / 2


print(B(4))