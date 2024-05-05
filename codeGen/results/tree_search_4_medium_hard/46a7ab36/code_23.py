code
from functools import lru_cache

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        @lru_cache(None)
        def dp(i, j):
            if i > n or j < 0:
                return 0
            if j == 0:
                return 1
            if i <= n // 2:
                res = dp(1, j - 1) + (n % 2 and 1)
            else:
                res = dp(n // 2 + 1, j - 1) + (j > 1 and 1)
            return res
        print((dp(1, m) % (10**8 + 7)) or 0)

solve()
