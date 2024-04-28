def find_pathways(K, N, arr):
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]

    # Base case: The bottom right cell has exactly K coins.
    dp[-1][-1][K] = arr[-1][-1]

    for i in range(N - 2, -1, -1):
        for j in range(N - 2, -1, -1):
            if i < N - 1:
                dp[i][j][K] += dp[i + 1][j][min(K, arr[i][j])]
            if j < N - 1:
                dp[i][j][K] += dp[i][j + 1][min(K, arr[i][j])]

    return dp[0][0][K]
