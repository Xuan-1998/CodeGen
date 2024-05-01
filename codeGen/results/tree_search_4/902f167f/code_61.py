from math import sqrt

n, m = map(int, input().split())
dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = 0
for j in range(m + 1):
    dp[0][j] = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        for k in range(1, min(i, j) + 1):
            if (i - k) * (j - k) > 0:
                dp[i][j] = min(dp[i][j], dp[k-1][j-k+1] + ((i-k+1)*(j-k+1)) / (k**2))
