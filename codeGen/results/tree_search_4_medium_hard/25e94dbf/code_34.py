def maximum_distance(commands, n):
    m = len(commands)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        if commands[i-1] == 'T':
            dp[i][0] = 0
        else:
            dp[i][0] = 1

    for k in range(1, n+1):
        for i in range(k+1):
            if i < k:
                dp[m][i] = max(dp[m-1][i-1] + 1, dp[m-1][i])
            else:
                dp[m][k] = 1

    return dp[m][n]
