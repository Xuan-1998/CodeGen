import sys

n, k = map(int, input().split())
a = list(map(int, input().split()))

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = i
    for j in range(1, min(i, k) + 1):
        if a[i - 1] == a[i - 2]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 2][j - 1])
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + 1)

print(dp[n][k])
