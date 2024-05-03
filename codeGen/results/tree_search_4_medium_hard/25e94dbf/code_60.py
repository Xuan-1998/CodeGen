def max_distance(commands, n):
    m = len(commands)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        if commands[i - 1] == 'F':
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]) + 1
        else:
            dp[i][1] = min(dp[i-1][0], dp[i-1][1])
            dp[i][0] = max(0, dp[i-1][1] - 1)

    return dp[m][n]
