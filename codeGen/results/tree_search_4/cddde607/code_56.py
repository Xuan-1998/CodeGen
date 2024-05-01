def numPaths(arr, K):
    N = len(arr)
    k_max = K
    dp = [[[0 for _ in range(k_max+1)] for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == N-1 and j == N-1:
                dp[i][j][k_max] = 1
            elif i == N-1:
                dp[i][j][k_max] = dp[i][j+1][k_max - arr[i][j]]
            elif j == N-1:
                dp[i][j][k_max] = dp[i+1][j][k_max - arr[i][j]]

    for i in range(N):
        for j in range(N):
            if k_max > 0:
                dp[i][j][k_max] = max(dp[i+1][j][k_max-arr[i][j]], dp[i][j+1][k_max-arr[i][j]])
            else:
                dp[i][j][k_max] = 1

    return dp[0][0][K]
