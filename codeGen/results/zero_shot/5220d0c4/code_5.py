import sys

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

def beauty(arr):
    max_beauty = 0
    bad_primes = set(int(x) for x in sys.stdin.readline().split())
    sieve = sieve_of_eratosthenes(max(arr))
    for x in arr:
        min_prime_divisor = None
        for p in range(2, int(x**0.5) + 1):
            if p in bad_primes or not sieve[p]:
                continue
            if x % p == 0 and (min_prime_divisor is None or p < min_prime_divisor):
                min_prime_divisor = p
        beauty_value = 1 if min_prime_divisor is None else -1
        max_beauty = max(max_beauty, beauty_value)
    return max_beauty

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
print(beauty(arr))
