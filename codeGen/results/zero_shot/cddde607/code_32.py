def countPaths(K, N, arr):
    dp = [[[0] * (K+1) for _ in range(N)] for _ in range(N)]

    dp[0][0][0] = 1
    for i in range(1, N):
        dp[i][0][0] = 0

    for j in range(1, N):
        dp[0][j][0] = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                if i < N-1:
                    dp[i+1][j][arr[i][j]] += dp[i][j][arr[i][j]]
                if j < N-1:
                    dp[i][j+1][arr[i][j]] += dp[i][j][arr[i][j]]

    return dp[N-1][N-1][K]
