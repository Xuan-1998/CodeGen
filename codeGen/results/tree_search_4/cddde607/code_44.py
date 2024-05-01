def findPath(K, N, arr):
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]

    # Initialize the base case
    dp[0][0][arr[0][0]] = 1

    # Fill up the table by considering subproblems
    for i in range(1, N):
        for j in range(N):
            if arr[i][j] <= K:
                dp[i][j][K - arr[i][j]] += dp[(i - 1)][j][max(K - arr[i-1][j], 0)] + \
                                               dp[i][(j - 1)][max(K - arr[i][j-1], 0)]

    return dp[N - 1][N - 1][K]
