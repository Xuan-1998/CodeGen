import sys

n, m, h = map(int, input().split())
s = list(map(int, input().split()))

dp = [[0.0] * (n + 1) for _ in range(m + 1)]
for i in range(1, m + 1):
    if s[i - 1] > 0:
        dp[i][0] = 1.0
        for k in range(1, min(i, n) + 1):
            if h == i:
                dp[i][k] = max(dp[i - 1][k], (s[h - 1] / sum(s)) * (1.0 - dp[i - 1][k]))
            else:
                dp[i][k] = max(dp[i - 1][k], (1 - s[i - 1] / sum(s)) * dp[i - 1][k])
        if i == m and k < n:
            dp[m][n] = 1.0

print('%.6f' % dp[m][n]) if dp[m][n] > 0 else print(-1)
