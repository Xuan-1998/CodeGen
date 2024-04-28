def numberOfPaths(arr, K):
    N = len(arr)
    dp = [[0]*N for _ in range(N)]

    # Base case: only one way to reach the last cell
    dp[N-1][N-1] = 1 if arr[N-1][N-1] <= K else 0

    for i in range(N):
        for j in range(N):
            if i == N-1 and j == N-1:
                continue
            if (i > 0 or j > 0) and arr[i][j] <= K:
                if i < N-1:
                    dp[i][j] += dp[i+1][j]
                if j < N-1:
                    dp[i][j] += dp[i][j+1]

    return dp[0][0]
