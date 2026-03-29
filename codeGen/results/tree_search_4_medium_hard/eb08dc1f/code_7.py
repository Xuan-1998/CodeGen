import sys
from functools import lru_cache

n = int(sys.stdin.readline())
mod = 998244353

@lru_cache(None)
def choose(i, j):
    if j > i:
        return 0
    if j == 1:
        return 1
    res = 1
    for k in range(2, j + 1):
        res = (res * (i - k + 1)) % mod
    return res

dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][1] = 1
    if i > 0:
        for j in range(2, n + 1):
            for k in range(i - j + 1, i):
                dp[i][j] += dp[k][1] * choose(i - k, j - 1)
            dp[i][j] %= mod

ans = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        ans[i] += dp[i][j]
    ans[i] %= mod

print(*ans, sep=' ')
