def count_paths(K, N, arr):
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]
    dp[0][0][0] = 1
    for i in range(1, N):
        for j in range(i + 1):
            if arr[i][j] <= K:
                dp[i][j][K - arr[i][j]] += dp[i - 1][j][K - arr[i][j]]
            if arr[i][j] > 0:
                dp[i][j][arr[i][j] - 1] += dp[i - 1][j][arr[i][j] - 1]
    return dp[N - 1][N - 1][K]
