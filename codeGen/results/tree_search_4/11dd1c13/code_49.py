def min_falling_path_sum(grid):
    n = len(grid)
    dp = [[0] * (n + 1) for _ in range(n)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1:
                # base case: first row
                dp[i][j] = grid[i - 1][j]
            else:
                min_sum = float('inf')
                for k in range(i - 1):
                    min_sum = min(min_sum, dp[k][min(j, 2 * n - j)] + grid[i - 1][j])
                dp[i][j] = min_sum

    return dp[n][0]
