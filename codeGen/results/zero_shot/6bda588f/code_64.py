def min_f(a, s):
    n = len(a)
    f = 0

    for i in range(n - 1):
        x = a[i] // 2
        y = a[i] - x
        if (x <= s and y >= s) or (x >= s and y <= s):
            f += a[i] * s
        else:
            f += x * y

    return f
