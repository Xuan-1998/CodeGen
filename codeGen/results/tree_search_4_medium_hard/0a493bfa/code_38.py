from math import gcd
from functools import reduce

def f(x):
    p = min((p for p in range(2, int(x ** 0.5) + 1) if x % p == 0), default=None)
    return 0 if p is None or p not in bad_primes else x - (x // p)

n, m = map(int, input().split())
a = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

dp = [0] * (n + 1)
for i in range(2, n + 1):
    for j in range(i - 1, -1, -1):
        s = sum(gcd(a[k], a[i]) for k in range(j + 1, i))
        dp[i] = max(dp[i], f(s) + (dp[j - 1] if j > 0 else 0))

print(dp[n])
