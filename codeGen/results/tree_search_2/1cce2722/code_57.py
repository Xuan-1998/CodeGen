def max_points(seq):
    n = len(seq)
    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(2, n+1):
        for j in range(i-2, -1, -1):
            if seq[i-1] == seq[j]+1 or seq[i-1] == seq[j]-1:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j+1])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j+1]) + 1

    return dp[n][0]
