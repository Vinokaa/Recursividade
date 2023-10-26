def A(n):
    if n == 1:
        return 2
    else:
        return 1 / A(n-1)


print(A(3))