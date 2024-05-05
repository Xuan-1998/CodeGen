import math
from functools import lru_cache

@lru_cache(maxsize=None)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

@lru_cache(maxsize=None)
def f(s):
    p = min((p for p in range(2, int(math.sqrt(s)) + 1) if s % p == 0), default=s)
    if p not in bad_primes:
        return s
    else:
        return s - p

bad_primes = set(map(int, input().split()))
n, m = map(int, input().split())
array = list(map(int, input().split()))

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, min(i, m) + 1):
        if i == j:
            dp[i][j] = array[0]
            for k in range(1, i):
                good_primes = [p for p in bad_primes if math.gcd(array[k], p) > 1]
                dp[i][j] = max(dp[i-1][j] + f(math.gcd(*good_primes)), dp[k][j-1] + array[0])
        else:
            dp[i][j] = max(dp[i-1][j] + f(math.gcd(*bad_primes[:j]))), 
                       dp[i][j-1] + array[0])

print(max(dp))
