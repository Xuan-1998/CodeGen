from functools import lru_cache

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

@lru_cache(None)
def f(s):
    p = next((i for i in range(2, int(s**0.5) + 1) if s % i == 0), None)
    return f(s // p) - s if p in bad_primes else f(s // p) + s

bad_primes = set(map(int, input().split()))

n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = sum(arr[:i])

@lru_cache(None)
def solve(i, j):
    if not bad_primes:
        return f(gcd(*arr[:i]))
    if j == 0:
        return dp[i][j]
    res = max(solve(k, l - 1) + f(gcd(*arr[k:i], *bad_primes[l:j])))
    for k in range(i):
        for l in range(j):
            if k >= i - l:
                break
            res = max(res, solve(k, l))
    return res

print(solve(n, m))
