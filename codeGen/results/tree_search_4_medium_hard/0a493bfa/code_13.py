import sys
from functools import lru_cache

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

@lru_cache(maxsize=None)
def f(s):
    p = next((p for p in range(2, s+1) if all(p > i for i in range(2, int(s**0.5)+1))) or (s == 1)
    return -s if p in bad_primes else 0

bad_primes = set(map(int, input().split()))
n, m = map(int, input().split())
a = list(map(int, input().split()))

dp = [[-float('inf')] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(i, -1, -1):
        if i == 1:
            dp[i][j] = f(a[0])
        else:
            for k in range(j+1, i):
                dp[i][j] = max(dp[k-1][j-1] * gcd(*a[k:j+1]) + f(sum(a[k:i])), dp[i][j])

print(dp[n][m])
