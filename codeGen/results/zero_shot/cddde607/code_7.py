def count_paths(K, N, arr):
    dp = [[[0] * (K+1) for _ in range(N)] for _ in range(N)]

    dp[0][0][0] = 1
    for i in range(N):
        for j in range(N):
            if i < N-1:
                dp[i+1][j][0] += dp[i][j][0]
            if j < N-1:
                dp[i][j+1][0] += dp[i][j][0]
            if arr[i][j] <= K and i < N-1 and j < N-1:
                dp[i+1][j][arr[i][j]] += dp[i][j][arr[i][j]-1]
                dp[i][j+1][arr[i][j]] += dp[i][j][arr[i][j]-1]

    return dp[N-1][N-1][K]
