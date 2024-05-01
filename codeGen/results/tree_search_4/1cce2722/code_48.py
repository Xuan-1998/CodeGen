def max_points(sequence):
    n = len(sequence)
    dp = [[0] * (2*n) for _ in range(n)]

    for i in range(n):
        if i == 0:
            dp[i][n-1] = 0
        elif i == n-1:
            dp[i][i] = 0
        else:
            for j in range(2*n-1, 0, -1):
                if sequence[i] == j:
                    if i > 0 and i < n-1 and (sequence[i-1] == j-1 or sequence[i+1] == j+1):
                        dp[i][j] = max(dp[i-2][i+2], dp[i-1][j], dp[i-1][j-1] + 1)
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + 1)
                else:
                    dp[i][j] = dp[i-1][j]

    return dp[n-1][2*n-1]
