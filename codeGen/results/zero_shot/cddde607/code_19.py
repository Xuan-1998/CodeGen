def solve(K, N, arr):
    dp = [[[0 for _ in range(K+1)] for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                if arr[0][0] <= K:
                    dp[i][j][K] = 1
            elif i > 0:
                if j > 0:
                    dp[i][j][K] += dp[i-1][j][min(K, arr[i-1][j])] + dp[i][j-1][min(K, arr[i][j-1])]
                else:
                    dp[i][j][K] = dp[i-1][j][min(K, arr[i-1][j])]
            elif j > 0:
                dp[i][j][K] = dp[i][j-1][min(K, arr[i][j-1])]

    return dp[N-1][N-1][K]
