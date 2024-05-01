import sys

n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = 1
    for j in range(1, m + 1):
        if i > 1:
            min_val = float('inf')
            for k in range(i):
                min_val = min(min_val, dp[k][j - 1] + (n - i) // (k + 1))
            dp[i][j] = min_val
        else:
            dp[i][j] = j

print(dp[n][m])
