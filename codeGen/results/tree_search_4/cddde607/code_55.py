def num_paths_to_collect_k_coins(K, N, arr):
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                if K < arr[i][j]:
                    return 0
                elif K >= arr[i][j]:
                    dp[i][j][K] = 1
            else:
                if K < arr[i][j]:
                    dp[i][j][K] = dp[i-1][j][K] + dp[i][j-1][K]
                elif K >= arr[i][j]:
                    dp[i][j][K] = dp[i-1][j][K-arr[i][j]] + dp[i][j-1][K-arr[i][j]]

    return dp[N-1][N-1][K]
