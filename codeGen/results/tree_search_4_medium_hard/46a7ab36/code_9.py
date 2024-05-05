import sys
from functools import lru_cache

def solve():
    t = int(input())
    MOD = 10**9 + 7

    @lru_cache(None)
    def dp(k, l):
        if k == 0:
            return 1
        if l >= n or (2 * l > n and l != 0):
            return 0
        res = 0
        if 2 * l <= n:
            for i in range(max(0, l), min(n, 2 * l)):
                res += dp(k - 1, i)
            res %= MOD
        else:
            res = (res + n * (dp(k, l + 1) + dp(k - 1, l))) % MOD
        return res

    for _ in range(t):
        n, m = map(int, input().split())
        print(dp(m, 0))
