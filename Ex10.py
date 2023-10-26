def bacteria(n):
    if n == 1:
        return 50000
    else:
        return bacteria(n-1) * 3

print(bacteria(3))