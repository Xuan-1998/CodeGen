import sys

n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = 1
for j in range(m + 1):
    dp[0][j] = 1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i == 1 and j > 0:
            dp[i][j] = min(dp[i][j-1], dp[i][j])
        elif j == 1 and i > 0:
            dp[i][j] = min(dp[i-1][j], dp[i][j])
        else:
            for k in range(1, i + 1):
                if k * k <= i and k * k <= j:
                    dp[i][j] = min(dp[i][j], dp[i-k][j-k] + 1)

print(dp[n][m])
