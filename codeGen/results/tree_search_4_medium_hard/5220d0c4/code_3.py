import sys
from math import sqrt

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    p = 2
    while p**2 <= n:
        if primes[p]:
            for i in range(p**2, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]

def get_min_prime_divisor(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return i

def max_beauty(n, bad_primes):
    dp = [[[-float('inf') for _ in range(2)] for _ in range(m + 1)] for _ in range(n + 1)]
    good_primes = [p for p in range(2, n + 1) if get_min_prime_divisor(p) == p]
    for i in range(n + 1):
        dp[i][0][0] = 0
        dp[i][0][1] = -i
    for j in range(m + 1):
        dp[0][j][0] = 0
        dp[0][j][1] = -n
    for i in range(1, n + 1):
        for j in range(min(i, m) + 1):
            if bad_primes[j] not in good_primes:
                for k in range(2):
                    if k == 0 and dp[i-1][j][k] != -i:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j][1-k] + (i-j))
                    elif k == 1 and dp[i-1][j][k] != -n:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j][0] - i)
    return max(max(dp[n]))

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))
    print(max_beauty(n, bad_primes))
