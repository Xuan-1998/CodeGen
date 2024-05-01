def numPathsWithKCoins(K, N, arr):
    memo = [[[0 for _ in range(K+1)] for _ in range(N)] for _ in range(N)]

    def dfs(i, j, k):
        if i == N-1 and j == N-1:
            return 1
        if i < N-1 and j < N-1:
            return memo[i][j][k] = (memo[i+1][j][k-arr[i][j]] or 0) + (memo[i][j+1][k-arr[i][j]] or 0)
        return 0

    dp = [[0 for _ in range(K+1)] for _ in range(N)]
    dp[0][0] = 1
    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = dfs(i, j, K-arr[i-1][j-1])
    return dp[N-1][K]
