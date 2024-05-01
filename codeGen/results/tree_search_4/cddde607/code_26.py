def numPathsWithKCoins(K, N, arr):
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                if arr[i][j] == K:
                    return 1
                else:
                    dp[i][j] = 0
            elif i > 0 and j > 0:
                if arr[i][j] <= K:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0
            elif i == 0:
                if arr[i][j] <= K:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = 0
            elif j == 0:
                if arr[i][j] <= K:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = 0

    return dp[N-1][N-1]
