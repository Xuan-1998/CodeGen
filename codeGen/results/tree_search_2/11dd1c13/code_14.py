def min_falling_path(grid):
    n = len(grid)
    dp = [[0] * len(grid[0]) for _ in range(n)]

    for i in range(n):
        if i == 0:
            dp[i] = grid[i]
        else:
            new_dp = [float('inf')] * n
            for j in range(n):
                if j > 0 and j < n - 1:
                    new_dp[j] = min(new_dp[j-1], new_dp[j+1]) + grid[i][j]
                elif j == 0:
                    new_dp[0] = dp[i-1][n-1] + grid[i][0]
                elif j == n - 1:
                    new_dp[n-1] = dp[i-1][0] + grid[i][n-1]
            dp = new_dp

    return min(dp)
