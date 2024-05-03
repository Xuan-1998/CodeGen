python
n = int(input())
dp = [[-float('inf')] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = 0

for i in range(1, n + 1):
    for k in range(min(i, n) + 1):
        if commands[i - 1] == 'F':
            dp[i][k] = max(dp[i - 1][k], 1 + dp[i - 1][k])
        else:
            dp[i][k] = max(dp[i - 1][k - 1], 0 + dp[i - 1][k])

print(max(0, dp[n][n]))
