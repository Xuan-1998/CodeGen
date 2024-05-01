import sys

n, m = map(int, input().split())

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i == 1 and j == 1:
            dp[i][j] = 1
        else:
            min_val = sys.maxsize
            for k in range(1, min(i, j) + 1):
                min_val = min(min_val, dp[k-1][j-1] + (i - k) * (j - k))
            dp[i][j] = min_val

print(dp[n][m])
