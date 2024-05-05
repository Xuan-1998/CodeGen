import sys
from functools import lru_cache

@lru_cache(None)
def sieve(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int((limit ** 0.5)) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return [p for p in range(2, limit + 1) if primes[p]]

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

primes = sieve(max(arr))

def beauty(arr):
    bad_beauty = sum(-1 for x in arr if x in bad_primes)
    good_beauty = 0
    for p in primes:
        count = sum(1 for x in arr if x == p)
        if count > 1 and p not in bad_primes:
            good_beauty -= count - 1
        elif count == 1:
            good_beauty += 1
    return max(0, good_beauty + bad_beauty)

print(beauty(arr))
