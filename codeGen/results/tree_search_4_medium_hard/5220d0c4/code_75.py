import sys
from collections import defaultdict

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def min_prime_divisor(n):
    for p in range(2, int(n ** 0.5) + 1):
        if n % p == 0:
            return p

def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = set(map(int, input().split()))

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        if arr[i - 1] not in bad_primes:
            min_divisor = min_prime_divisor(arr[i - 1])
            for j in range(m + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + (arr[i - 1] // min_divisor))
        else:
            dp[i][0] = dp[i - 1][0]
            for j in range(1, m + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] - arr[i - 1])

    return dp[n][m]

print(solve())
