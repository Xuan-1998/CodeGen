def f(n):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if (mid * (high - low + 1)) % 2 == 0:  # even number of comparisons
            low = mid + 1
        else:  # odd number of comparisons
            high = mid
    return high

t, l, r = map(int, input().split())
result = t * f(l) + t * (f(l + 1) - f(l)) + ... + t * (f(r) - f(r-1))
print(result % (10**9 + 7))
