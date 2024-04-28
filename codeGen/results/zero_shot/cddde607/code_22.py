def countPaths(K, N, arr):
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                if arr[i][j] <= K:
                    dp[i][j][arr[i][j]] = 1
            elif i > 0:
                dp[i][j][K] += dp[i-1][j][K-arr[i][j]]
            elif j > 0:
                dp[i][j][K] += dp[i][j-1][K-arr[i][j]]

    return dp[N-1][N-1][K]
