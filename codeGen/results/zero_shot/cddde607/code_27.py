def count_paths(K, N, arr):
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(N):
            if i > 0:
                dp[i][j][0] += dp[i-1][j][0]
            if j > 0:
                dp[i][j][0] += dp[i][j-1][0]
            if arr[i][j] <= K:
                for k in range(1, min(K+1, arr[i][j]+1)):
                    dp[i][j][k] = dp[i][j][k-1] + (dp[i-1][j][k-1] if i > 0 else 0) + (dp[i][j-1][k-1] if j > 0 else 0)
    return dp[N-1][N-1][K]
