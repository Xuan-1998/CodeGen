def f(n):
    if n % 2 == 0:
        return 0
    else:
        min_value = float('inf')
        for i in range(l, r+1):
            min_value = min(min_value, f(i) + f(n-i-1))
        return min_value + 1

t0, l, r = map(int, input().split())
print((t0*f(l) + sum(t[i]*f(l+i) for i in range(1, r-l+2)) - l*f(r)) % (10**9 + 7))
