def findPaths(arr, K, N):
    dp = [[0]*N for _ in range(N)]
    dp[N-1][N-1] = 1 if arr[N-1][N-1] <= K else 0

    for i in range(N-2, -1, -1):
        for j in range(N-1, -1, -1):
            if arr[i][j] > K:
                dp[i][j] = 0
            elif i == N-1 and j < N-1:
                dp[i][j] = dp[i][j+1]
            elif j == N-1 and i < N-1:
                dp[i][j] = dp[i+1][j]
            else:
                dp[i][j] = dp[i+1][j] + dp[i][j+1]

    return dp[0][0]

