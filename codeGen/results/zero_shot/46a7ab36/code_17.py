import sys
from functools import lru_cache

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        @lru_cache(None)
        def dp(i):
            if i > n:
                return 1
            res = 0
            for j in range(n, -1, -1):
                if j >= 2 * i and j < 2 * (i + 1):
                    res += dp(j)
                elif 2 * i <= n and j == 2 * i:
                    res += dp(2 * i) - 1
            return res

        print((dp(m) % (10**8+7)) if m > 0 else 0)

if __name__ == "__main__":
    solve()
