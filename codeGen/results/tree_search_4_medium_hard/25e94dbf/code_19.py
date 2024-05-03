def max_distance(commands, n):
    m = len(commands)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = 0
            elif i % 2 == 0 and j > 0:
                dp[i][j] = max(dp[i-1][j-1], dp[i-2][j]) + (commands[i-1] == 'F')
            else:
                dp[i][j] = dp[i-1][j] + (commands[i-1] == 'F')

    return dp[m][n]
