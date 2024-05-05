import sys
from math import gcd
from functools import lru_cache

@lru_cache(None)
def f(s, bad_primes):
    if s == 1:
        return 0
    p = next((p for p in range(2, int(sys.maxsize)) if all(p % i != 0 for i in range(2, int(sys.maxsize)))) or (None,))
    while p and p not in bad_primes:
        p = gcd(s, p)
        s //= p
    return f(s, bad_primes) + s if p is None else f(s, bad_primes) - s

def max_beauty(n, m, a, bad_primes):
    dp_bit = [[0] * (m + 1) for _ in range(2**n + 1)]
    for i in range(2**n + 1):
        mask = bin(i)[2:].zfill(n)
        for j in range(m + 1):
            k = sum(int(mask[m - j]) for m in range(j))
            if k == 0:
                dp_bit[i][j] = f(a[0], bad_primes) * (1 - all(int(mask[m]) for m in range(n)))
            else:
                for l in range(k, -1, -1):
                    if all(a[m] % l == 0 for m in range(k)):
                        dp_bit[i][j] = max(dp_bit[i][j], dp_bit[i ^ (1 << k)][l - 1] * f(gcd(a[k:l+1], bad_primes), bad_primes))
            if j > 0:
                dp_bit[i][j] = max(dp_bit[i][j], dp_bit[i][j - 1] * (1 - all(int(mask[m]) for m in range(n))))
    return dp_bit[2**n - 1][m]

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))
    print(max_beauty(n, m, a, bad_primes))
