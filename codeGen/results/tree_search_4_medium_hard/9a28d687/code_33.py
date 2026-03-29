import sys
from functools import lru_cache

n = int(input())
dp = [[float('inf')] * (n+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][i] = 0

@lru_cache(None)
def rev_cost(j, k):
    return min(dp[k-1][j-1] if j > 0 else 0 + cost[j], 
               dp[k-1][j+1] if j < n else 0 + cost[j])

cost = [int(input()) for _ in range(n)]
strings = [input() for _ in range(n)]

for k in range(2, n+1):
    for j in range(k-1, -1, -1):
        dp[k][j] = min(dp[k][j], rev_cost(j, k))

print(-1) if dp[n][0] == float('inf') else print(dp[n][0])
