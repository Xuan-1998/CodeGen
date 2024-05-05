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

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
bad_primes = list(map(int, sys.stdin.readline().split()))

good_primes = [p for p in sieve_of_eratosthenes(max(arr)) if p not in bad_primes]

beauty = sum(min(p for p in good_primes if p > 1 and p % a == 0) if a > 1 else 0 for a in arr)

print(beauty)
