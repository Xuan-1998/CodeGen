def max_distance(commands, n):
    m = len(commands)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(min(i, n) + 1):
            if commands[i - 1] == 'F':
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + (commands[i - 1] == 'T')
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[m][n]
