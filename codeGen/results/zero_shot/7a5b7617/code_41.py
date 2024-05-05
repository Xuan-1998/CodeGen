dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[i][0] = 1

for j in range(1, M + 1):
    dp[0][j] = 1

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if j <= M:
            dp[i][j] = (dp[i - 1][j - 1] + dp[i][M]) % (10 ** 9 + 7)

print(sum(dp[N][1:]))
