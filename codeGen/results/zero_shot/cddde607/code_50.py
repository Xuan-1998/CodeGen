def count_paths(K, N, arr):
    dp = [[[0] * (K+1) for _ in range(N)] for _ in range(N)]

    dp[0][0][0] = 1
    for i in range(1, N):
        dp[i][0][0] = 0
    for j in range(1, N):
        dp[0][j][0] = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] > K:
                continue
            if i == 0 and j == 0:
                dp[i][j][arr[i][j]] = 1
            elif i == 0:
                dp[i][j][arr[i][j]] += dp[i][j-1][arr[i][j]-1]
            elif j == 0:
                dp[i][j][arr[i][j]] += dp[i-1][j][arr[i][j]-1]
            else:
                dp[i][j][arr[i][j]] += dp[i-1][j][arr[i][j]-1] + dp[i][j-1][arr[i][j]-1]

    return dp[N-1][N-1][K]
