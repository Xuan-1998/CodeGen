import sys
from math import gcd

def f(s):
    p = min((i for i in range(2, int(s ** 0.5) + 1) if s % i == 0), default=None)
    return 0 if p is None or p not in bad_primes else f(s // p) - s

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
bad_primes = set(map(int, sys.stdin.readline().split()))

dp = [0] * (n + 1)
for i in range(n):
    dp[i + 1] = max(dp[i], a[i] if a[i] not in bad_primes else f(a[i]))

print(max(dp))
