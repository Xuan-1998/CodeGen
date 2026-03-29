def min_function_value(n, s, a):
    F = 0
    for i in range(1, n-1):
        x = max(s, a[i] - s)
        y = min(s, a[i] - s)
        F += (y * x) + (a[n-1] if i == n-2 else 0)
    return F
