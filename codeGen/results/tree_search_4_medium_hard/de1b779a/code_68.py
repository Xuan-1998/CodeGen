for i in range(1, n+1):
    dp[i][0] = max(dp[i-1][0], d0)
    for j in range(1, m+1):
        if c0 > i:
            dp[i][j] = dp[c0][0]
        elif j == 0:  # No stuffing
            dp[i][j] = dp[i-1][0]
        else:
            dp[i][j] = max(dp[i-ci[j]][j-1], dp[i][j-1])
