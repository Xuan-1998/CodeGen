import sys
from functools import lru_cache

def solve(n, edges, m, primes):
    MOD = 10**9 + 7
    dp = [[0] * (n+1) for _ in range(m+1)]

    @lru_cache(None)
    def f(k, i):
        if k == 1:
            return 0
        res = k
        for p in primes:
            while k % p == 0:
                res += p
                k //= p
        return res

    for edge in edges:
        u, v = edge
        for k in range(1, m+1):
            dp[k][min(u, v)] += (k-1) * f(n-k+1, min(u, v))

    ans = 0
    for i in range(1, n+1):
        ans += sum(dp[j][i] for j in range(m+1))
    return int(ans % MOD)


T = int(input())
for _ in range(T):
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n-1)]
    m = int(input())
    primes = list(map(int, input().split()))
    print(solve(n, edges, m, primes))
