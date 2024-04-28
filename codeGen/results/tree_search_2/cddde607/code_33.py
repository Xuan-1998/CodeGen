def num_paths_with_k_coins(K, N, arr):
    dp = [[0] * N for _ in range(N)]

    # Base case: bottom-right corner
    if arr[N-1][N-1] == K:
        dp[N-1][N-1] = 1

    for i in range(N):
        for j in range(N):
            # Come from above
            if i > 0 and (arr[i][j] + K - arr[i-1][j]) >= 0:
                dp[i][j] += dp[i-1][j]
            # Come from the left
            if j > 0 and (arr[i][j] + K - arr[i][j-1]) >= 0:
                dp[i][j] += dp[i][j-1]

    return dp[0][0]
