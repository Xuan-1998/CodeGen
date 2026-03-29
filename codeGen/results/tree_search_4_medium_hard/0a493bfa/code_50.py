from math import gcd

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = set(map(int, input().split()))

dp = {(i, set(), 0) for i in range(n+1)}

def beauty(i, bad_primes, max_beauty):
    if i > n:
        return 0
    pivot = a[i-1]
    new_bad_primes = bad_primes - {p for p in bad_primes if p*gcd(p, pivot) == gcd(p, pivot)}
    gcd_func = lambda x: x if x == 1 else min(x, beauty(i-1, new_bad_primes, max_beauty) // x)
    next_beauty = max(max_beauty, pivot + sum(gcd_func(x) for x in a[:i] if x not in bad_primes))
    return dp[(i, new_bad_primes, next_beauty)]

print(beauty(n, set(b), 0))
