import sys

n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    dp[u][i] += 1
max_j = 0

for j in range(1, m + 1):
    for i in range(1, n + 1):
        if i == p[j]:
            dp[i][j] = min(dp[i][j-1], max_j)
        else:
            dp[i][j] = 1 + max(dp[v][0])
        max_j = max(max_j, j)

print(min(dp[t]), max_j)
