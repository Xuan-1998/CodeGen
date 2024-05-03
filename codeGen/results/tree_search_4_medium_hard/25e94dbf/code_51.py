def max_distance(commands, n):
    m = len(commands)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(n + 1):
            if commands[i - 1] == 'T':
                dp[i][j] = max(dp[i-1][k] for k in range(j)) if j > 0 else 0
            elif commands[i - 1] == 'F':
                dp[i][j] = 1 + (dp[i-1][j-1] if j > 0 else 0)

    return max(dp[m])
