from functools import lru_cache

c0, d0, n, m = map(int, input().split())
dp = [[[0 for _ in range(11)] for _ in range(m+1)] for _ in range(n+1)]

@lru_cache(None)
def max_profit(i, j):
    if i < c[j]:
        return dp[i][j-1][0]  # no dough left
    else:
        return dp[i-c[j]][j-1][1] + d[j]

for i in range(1, n+1):
    for j in range(m+1):
        if i >= c[j]:
            dp[i][j] = max((dp[i-c[j]][j-1][0] if j > 0 else 0) +
                            max_profit(i-c[j], j-1) + d[j],
                           dp[i][0])
        else:
            dp[i][j] = dp[i][0]

print(max(dp[n]))
