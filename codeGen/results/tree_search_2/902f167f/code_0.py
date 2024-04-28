import sys

n, m = map(int, input().split())

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = min((i - k) * (j - k) + dp[k][j] if k <= i and k <= j else sys.maxsize
                         for k in range(min(i, j), 0, -1)) + 1

print(dp[n][m])
