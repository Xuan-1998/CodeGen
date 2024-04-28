import sys

n, m = map(int, input().split())

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = float('inf')
        for k in range(1, i + 1):
            for l in range(1, j + 1):
                if k * k <= i and l * l <= j:
                    dp[i][j] = min(dp[i][j], 1 + dp[max(0, i - k)][max(0, j - l)])

print(dp[n][m])
