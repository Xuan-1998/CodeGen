from functools import lru_cache

@lru_cache(None)
def max_beauty(i, j, f, p):
    if i < 0:
        return 0
    if f and j <= m:
        for bad_prime in range(2, min(p + 1, j) + 1):
            for good_prime in range(2, bad_prime):
                max_beauty(i - 1, j, not(f), good_prime)
    elif not f:
        for prime in range(2, min(p + 1, m) + 1):
            max_beauty(i - 1, m, False, prime)
    return max(max_beauty(i - 1, j, f and p > 0, 0), 
               max_beauty(i - 1, j, not f, p) + (p in bad_primes))

n, m = map(int, input().split())
array = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(max_beauty(n, m, True, max(array)))
