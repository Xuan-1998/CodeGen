python
import sys

n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = -i
for j in range(m + 1):
    dp[0][j] = -j

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if input().strip()[:i] == input().strip()[:j]:
            dp[i][j] = max(dp[i-1][j-1], 4) + dp[i-1][j-1]
        else:
            dp[i][j] = max(4, dp[i-1][j], dp[i][j-1])

print(max(max(row) for row in dp))
