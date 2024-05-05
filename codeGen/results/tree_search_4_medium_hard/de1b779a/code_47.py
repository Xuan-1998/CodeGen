import sys
from functools import lru_cache

def max_profit(n, m, c0, d0, ai, bi, ci, di):
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    @lru_cache(None)
    def dfs(i, j):
        if i > m or j < 0:
            return 0
        if j >= c0:
            return max(dfs(i - 1, j), dfs(i - 1, j - ci[i]) + di[i] - bi[i])
        else:
            return 0

    return dfs(m, n)

n, m, c0, d0 = map(int, input().split())
ai = [int() for _ in range(m)]
bi = [int() for _ in range(m)]
ci = [int() for _ in range(m)]
di = [int() for _ in range(m)]

for i in range(m):
    ai[i], bi[i], ci[i], di[i] = map(int, input().split())

print(max_profit(n, m, c0, d0, ai, bi, ci, di))
