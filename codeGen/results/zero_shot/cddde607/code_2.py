def count_paths(arr, K, N):
    dp = [[[0]*(K+1) for _ in range(N)] for _ in range(N)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(N):
            for k in range(K+1):
                if i == 0 and j == 0:
                    continue
                elif i > 0:
                    dp[i][j][k] += dp[i-1][j][min(k, arr[i-1][j-1])]
                elif j > 0:
                    dp[i][j][k] += dp[i][j-1][min(k, arr[i][j-1])]
    return dp[N-1][N-1][K]
