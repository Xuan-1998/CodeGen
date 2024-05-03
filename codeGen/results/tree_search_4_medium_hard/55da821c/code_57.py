import sys
from collections import defaultdict

n, m = map(int, input().split())
plants = defaultdict(list)
for _ in range(n):
    s, x = map(int, input().split())
    plants[s].append(x)

dp = [[0] * (m-1) for _ in range(n+1)]
for i in range(1, n+1):
    for k in range(min(i-1, m-1)):
        if plants[k % m][k] < x:
            dp[i][k] = min(dp[i-1][k], 1 + dp[i-1][k])
        else:
            dp[i][k] = dp[i-1][k]
print(dp[n][m-2])  # subtract one because we don't need to replant the last plant
