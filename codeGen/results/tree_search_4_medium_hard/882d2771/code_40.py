def f(n):
    if n == 1:
        return 0
    res = float('inf')
    for l in range(2, n+1):
        r = n - l + 1
        if l > 1 or r > 1:  # make sure it's not the base case
            res = min(res, f(l-1) + f(r-l))
    return (n-1) + res

t, l, r = map(int, input().split())
print(f(t) % (10**9 + 7))
