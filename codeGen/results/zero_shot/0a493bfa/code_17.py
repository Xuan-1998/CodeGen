import sys
from math import sqrt

def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(sqrt(n)) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [p for p in range(2, n) if sieve[p]]

n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
bad_primes = list(map(int, sys.stdin.readline().split()))

sieve = sieve_of_eratosthenes(max(array) + 1)
good_primes = [p for p in sieve if p not in bad_primes]

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(i, n + 1):
        dp[i][j] = max(dp[i - 1][k] + array[k] for k in range(j))
        if sieve[array[j - 1]]:
            dp[i][j] -= array[j - 1]

max_beaauty = max(max(row) for row in dp)
print(max_beauty)
