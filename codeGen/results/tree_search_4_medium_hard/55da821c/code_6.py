import sys

n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    s, x = map(int, input().split())
    dp[i][min(s, m)] = 1
    for j in range(m - 1, min(s, m) - 1, -1):
        if dp[i - 1][j] > dp[i][j]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] += 1

print(dp[-1][-1])
