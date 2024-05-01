def count_paths(arr, N, K):
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    def dfs(i, j):
        if i == N - 1 and j == N - 1:  # base case: we've reached the bottom right corner
            return 1 if arr[i][j] <= K else 0

        if dp[i][j]:  # memoization
            return dp[i][j]

        total_paths = 0
        if i < N - 1 and arr[i][j] <= K:  # move down
            total_paths += dfs(i + 1, j)
        if j < N - 1 and arr[i][j] <= K:  # move right
            total_paths += dfs(i, j + 1)

        dp[i][j] = total_paths

        return total_paths

    return dfs(0, 0)
