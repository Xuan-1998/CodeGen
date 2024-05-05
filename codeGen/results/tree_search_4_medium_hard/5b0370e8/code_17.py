import sys
from functools import lru_cache

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        dp = [[[0] * (1 << k) for _ in range(1 << k)] for _ in range(n + 1)]
        dp[-1][0][0] = 1
        @lru_cache(None)
        def dfs(i, and_, xor_):
            if i == -1:
                return and_
            res = 0
            for v in range(2 ** k):
                new_and = and_ & v
                new_xor = xor_ ^ v
                if (and_ >= new_and) & (new_xor <= xor_):
                    res += dfs(i - 1, new_and, new_xor)
            return res % (10 ** 9 + 7)
        print((dfs(n - 1, 0, 0) + 1) % (10 ** 9 + 7))

if __name__ == "__main__":
    solve()
