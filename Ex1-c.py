def B(n):
    if n == 1:
        return 1
    else:
        return B(n-1) + (n*n)


print(B(2))