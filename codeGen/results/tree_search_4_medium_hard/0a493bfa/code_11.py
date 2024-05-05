def max_beauty(n, bad_primes):
    def f(s):
        p = min((p for p in range(2, int(s**0.5) + 1) if s % p == 0), default=s)
        return f(s // p) - (s % p) * (p in bad_primes)

    @lru_cache(None)
    def dp(i, j):
        if i < 0 or j < 0:
            return 0
        g = functools.reduce(gcd, a[i:j+1])
        return max(dp(k, j-1) + f(g) for k in range(i, j))

    a = [int(x) for x in input().split()]
    bad_primes = [int(x) for x in input().split()]
    print(max_beauty(len(a), set(bad_primes)))
