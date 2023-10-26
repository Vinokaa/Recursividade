def T(n):
    if n == 2:
        return True
    elif n > 2:
        if n % 2 == 0:
            return T(n / 2)
        else:
            return T(n - 3)
    else:
        return False

for i in [6, 7, 19, 12]:
    print(f"{i}: {T(i)}")