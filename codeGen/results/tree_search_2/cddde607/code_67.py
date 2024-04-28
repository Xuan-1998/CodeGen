def numPaths(arr, N, K):
    dp = [[[False for _ in range(K+1)] for _ in range(N)] for _ in range(N)]
    dp[0][0][0] = True

    for i in range(N):
        for j in range(N):
            if arr[i][j] <= K:
                if i < N-1 and dp[i+1][j][K-arr[i][j]]:
                    dp[i+1][j][K-arr[i][j]] = True
                if j < N-1 and dp[i][j+1][K-arr[i][j]]:
                    dp[i][j+1][K-arr[i][j]] = True

    return sum(1 for i in range(N) for j in range(N) if dp[N-1][N-1][K])
