dp = [[0] * (m + 1) for _ in range(N + 1)]

for i in range(N + 1):
    for j in range(m + 1):
        if i == 0:
            dp[i][j] = 1
        elif j == 1:
            dp[i][j] = 1
        else:
            dp[i][j] = sum(dp[i - 1][k] for k in range(1, j)) + dp[i - 1][j - 1]

print((dp[N][m] % (10**9 + 7)))
