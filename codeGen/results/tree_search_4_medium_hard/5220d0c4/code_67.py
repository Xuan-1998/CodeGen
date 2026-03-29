import sys

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    p = 2
    while p ** 2 <= n:
        if primes[p]:
            for i in range(p ** 2, n + 1, p):
                primes[i] = False
        p += 1
    bad_primes = [i for i in range(2, n + 1) if primes[i]]
    return bad_primes

def max_beauty(n, bad_primes):
    dp = [[0, 0]] * (n + 1)
    min_divisors = {}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            j = n // i
            if i not in bad_primes and j not in bad_primes:
                dp[i].append([i, False])
            if i in bad_primes and j not in bad_primes:
                dp[i].append([j, True])
            if i not in bad_primes and j in bad_primes:
                dp[i].append([i, True])
    for p in range(2, n + 1):
        if p not in min_divisors:
            min_divisors[p] = [p, None]
        for d, is_bad in dp[p]:
            if d not in min_divisors:
                min_divisors[d] = [d, is_bad]
            else:
                dp[p].append([min_divisors[d][0], min_divisors[d][1]])
    return max(dp[n])

n, m = map(int, input().split())
bad_primes = list(map(int, input().split()))
print(max_beauty(n, bad_primes))
