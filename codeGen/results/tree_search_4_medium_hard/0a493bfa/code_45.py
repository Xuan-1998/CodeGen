### BEGIN CODE ###
import sys
from functools import lru_cache

@lru_cache(None)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
bad_primes = list(map(int, sys.stdin.readline().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n):
    for j in range(i):
        dp[i][j] = max(dp[i - 1][k] + min(arr[k], gcd(arr[k], arr[i])) for k in range(j))

print(max(dp[n - 1]))
