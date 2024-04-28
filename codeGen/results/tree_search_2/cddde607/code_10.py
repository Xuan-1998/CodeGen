def coinPaths(arr, N, K):
    # Create a 2D DP table
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]

    def dfs(i, j, k):
        if i == N - 1 and j == N - 1:
            return arr[N-1][N-1] == k
        if dp[i][j][k]:
            return dp[i][j][k]
        result = 0
        for ni, nj in [(i+1, j), (i, j+1)]:
            if 0 <= ni < N and 0 <= nj < N:
                result += dfs(ni, nj, k + arr[ni][nj])
        dp[i][j][k] = result
        return result

    # Initialize the DP table
    for i in range(N):
        for j in range(N):
            dp[i][j][0] = 1 if all(arr[m][n] == 0 for m in range(i+1) for n in range(j+1)) else 0

    return dfs(0, 0, 0)
