def find_paths_with_k_coins(K, N, arr):
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: bottom right corner
    dp[N-1][N-1] = 1 if arr[N-1][N-1] <= K else 0

    for i in range(N - 2, -1, -1):
        for j in range(N - 2, -1, -1):
            if arr[i][j] > K:
                dp[i][j] = 0
            else:
                if i < N - 1 and j < N - 1:
                    dp[i][j] = (dp[i+1][j] + dp[i][j+1]) if arr[i][j] <= K else 0

    return dp[0][0]
