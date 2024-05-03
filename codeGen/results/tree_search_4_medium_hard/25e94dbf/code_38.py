def max_distance(commands, n):
    m = len(commands)
    dp = [[[0] * 51 for _ in range(2)] for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0][0] = 0

    for i in range(1, m + 1):
        for j in range(min(i, n) + 1):
            if commands[i - 1] == 'T':
                dp[i][j][0] = max(dp[i - 1][j - 1][1] + 1, dp[i - 1][j][0])
                dp[i][j][1] = max(dp[i - 1][j - 1][0], dp[i - 1][j][1] - 1)
            else:
                dp[i][j][0] = max(dp[i - 1][j - 1][0] + 1, dp[i - 1][j][0])
                dp[i][j][1] = max(dp[i - 1][j - 1][1], dp[i - 1][j][1] - 1)

    return dp[m][n][0]
