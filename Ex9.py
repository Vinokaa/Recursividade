def triangular(n):
    if n == 1:
        return 1
    else:
        return triangular(n-1) + n


print(triangular(4))