import sys

n, m = map(int, input().split())
dp = [[0] * 2 for _ in range(n+1)]

for i in range(m):
    u, v = map(int, input().split())
    dp[u][1] += 1
    dp[v][1] += 1

for i in range(1, n+1):
    if dp[i][0]:
        dp[i][0] = max(dp[i-1][1] + (i-1) * dp[i][1], dp[i-1][0] + i * dp[i][1])

print(max(dp[n][0], dp[n][1]))
