import sys

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    p = 2
    while p**2 <= n:
        if primes[p]:
            for i in range(p*p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n+1) if primes[p]]

def is_prime(n):
    if n < 2:
        return False
    for p in range(2, int(n**0.5) + 1):
        if n % p == 0:
            return False
    return True

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

good_primes = [p for p in bad_primes if not is_prime(p)]

dp = [[0] * (n + 1) for _ in range(n + 1)]
sieve = sieve_of_eratosthenes(max(arr))

for i in range(2, n + 1):
    for j in range(i, -1, -1):
        if arr[j] % sieve[i-2] == 0:
            dp[i][j] = max(dp[i-1][k] for k in range(j) if arr[k] not in bad_primes)
        else:
            dp[i][j] = max(dp[i-1][k] for k in range(j))
    for j in range(n, i - 1, -1):
        if arr[j] % sieve[i-2] == 0 and is_prime(arr[j]):
            dp[i][j] += 1
        elif arr[j] % sieve[i-2] != 0:
            dp[i][j] = max(dp[i-1][k] for k in range(j))

print(max(dp[n]))
