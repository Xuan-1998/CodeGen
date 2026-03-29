n, m = map(int, input().split())
a = input()
b = input()

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 4)
        else:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1])
        dp[i][0] = 0
        dp[0][j] = 0

print(max(0, dp[n][m]))
