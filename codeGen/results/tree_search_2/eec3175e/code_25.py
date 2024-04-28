code
n, m = map(int, input().split())
dp = [[False] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if j >= i:
            dp[i][j] = dp[i - 1][j]
        elif i <= j and not dp[i - 1][j % (i - 1)]:
            dp[i][j] = True

print(int(dp[n][m]))
