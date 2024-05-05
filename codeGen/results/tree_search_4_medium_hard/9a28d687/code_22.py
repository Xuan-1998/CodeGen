===BEGIN CODE===
import sys
n = int(input())
dp = [[0 for _ in range(100000)] for _ in range(n + 1)]
m = cost.reverse_count

for i in range(1, n + 1):
    for j in range(min(i, m) + 1):
        if j == 0:
            dp[i][j] = sum(cost[:i])
        else:
            dp[i][j] = min(dp[i-1][j-1] + cost[i-1], dp[i-1][j])

if dp[n][m] != -1 and dp[n][m] > sum(cost):
    print(-1)
else:
    print(dp[n][m])
