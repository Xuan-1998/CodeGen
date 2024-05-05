def expected_carries(N):
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(i + 1):
            if j == 0:  # A is a single digit
                dp[i][j] = sum(dp[k][k-1] * (dp[i-k-1][i-j-1] or 0.5) for k in range(j))
            elif j == i:  # B is a single digit
                dp[i][j] = sum(dp[k][i-k-1] * (dp[i-k-1][0] or 0.5) for k in range(i-j))
            else:
                dp[i][j] = sum(dp[k][k-1] * dp[i-k-1][j-k-1] for k in range(min(j, i-j)))

    return sum(dp[N][j] / (N ** j) for j in range(N + 1)) / N
