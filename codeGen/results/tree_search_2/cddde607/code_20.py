def count_paths(K, N, arr):
    dp = [[0]*N for _ in range(N)]

    dp[0][0] = 1 if arr[0][0] == K else 0

    for i in range(1, N):
        for j in range(N):
            if j > 0:
                dp[i][j] += dp[i-1][j-1] if arr[i][j] + dp[i-1][j-1] <= K else 0
            if i > 0:
                dp[i][j] += dp[i-1][j] if arr[i][j] + dp[i-1][j] <= K else 0

    return dp[N-1][N-1]
