from math import sqrt
from functools import lru_cache

@lru_cache(maxsize=None)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

@lru_cache(maxsize=None)
def min_prime_divisor(n):
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            return i

@lru_cache(maxsize=None)
def beauty(arr, good):
    return sum(min_prime_divisor(x) if x > 1 else 0 for x in arr) if good else -sum(min_prime_divisor(x) if x > 1 else 0 for x in arr)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

dp = [[-float('inf')] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if bad_primes[j - 1] not in arr[:i]:
            dp[i][j] = max(dp[i-1][j], beauty(arr[:i], bad_primes[j-1] in [x for x in arr[:i]]))
        else:
            dp[i][j] = beauty(arr[:i], False)

print(max(dp[-1]))
