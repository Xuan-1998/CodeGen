import sys

n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    s_i, x_i = map(int, input().split())
    for j in range(1, m + 1):
        if s_i == j:
            dp[i][j] = min(dp[i - 1][k] + 1 for k in range(m)) if i > 1 else 1
        else:
            dp[i][j] = dp[i - 1][j]

print(min(dp[-1]))
