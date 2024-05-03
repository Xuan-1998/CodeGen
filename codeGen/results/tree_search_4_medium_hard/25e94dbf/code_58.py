def max_distance(commands, n):
    m = len(commands)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        t_count = sum(1 for c in commands[:i] if c == 'T')
        for j in range(min(i, n), -1, -1):
            if t_count <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + 1)
            else:
                dp[i][j] = dp[i-1][j]

    return dp[m][n]
