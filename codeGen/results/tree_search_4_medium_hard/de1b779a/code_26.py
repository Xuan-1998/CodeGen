import sys

n, m, c0, d0 = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(m + 1):
        # No stuffing
        dp[i][j] = max(dp[i-1][j], c0)
        
        if j > 0 and i >= bi[j]:
            # Use stuffing j
            dp[i][j] = max(dp[i][j], di[j] + dp[max(0, i-bi[j])][max(0, j-1)])

print(max(dp[-1]))
