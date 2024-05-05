def mergeSortV(M):
    MOD = 10**9 + 7

    N = len(M)
    dp = [[0] * (N+1) for _ in range(N+1)]

    # base cases
    dp[0][0] = 1
    for i in range(1, N+1):
        dp[i][0] = 1

    for i in range(1, N+1):
        for j in range(i+1):
            if M[j-1] <= i:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % MOD
            else:
                dp[i][j] = dp[i-1][j]

    return dp[N][N]
