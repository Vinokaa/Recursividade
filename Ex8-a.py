def A(n):
    if n == 1:
        return 1
    else:
        return A(n-1) * 3


print(A(4))