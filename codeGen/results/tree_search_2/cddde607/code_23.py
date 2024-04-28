def findPaths(N, K, arr):
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]

    # Base case: number of ways to collect exactly K coins from cells (0, 0) to (N-1, N-1)
    dp[0][0][arr[0][0]] = 1

    for i in range(N):
        for j in range(N):
            for k in range(K + 1):
                if i < N - 1 and arr[i][j] <= k:
                    dp[i + 1][j][k] += dp[i][j][k]
                if j < N - 1 and arr[i][j] <= k:
                    dp[i][j + 1][k] += dp[i][j][k - arr[i][j]]

    return dp[N-1][N-1][K]
