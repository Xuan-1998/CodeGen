def maximum_distance(commands, n):
    m = len(commands)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif commands[i - 1] == "F":
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + 1)
            else:  # Turn around
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1])

    return dp[m][n]
