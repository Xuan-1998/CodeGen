from math import sqrt

def min_prime_divisor(n):
    for p in range(2, int(sqrt(n)) + 1):
        if n % p == 0:
            return p

def beauty(i, j, f, g, memo):
    if (i, j, f, g) in memo:
        return memo[(i, j, f, g)]
    
    if i > j or g and f:
        return 0
    
    if not f:
        good = beauty(i + 1, j, False, True, memo)
        bad = beauty(i + 1, j, False, False, memo)
        return max(good, bad) if g else max(0, good, bad)
    
    good = beauty(i + 1, j, False, True, memo)
    bad = beauty(i + 1, j, False, False, memo)
    return max(good, bad)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

memo = {}
print(beauty(0, n - 1, True, True, memo))
