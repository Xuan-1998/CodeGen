def min_falling_path_sum(grid):
    m = len(grid)
    dp = [[0] * (m + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        dp[i][1] = grid[i - 1][0]
        for j in range(2, m + 1):
            if i > 1:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j + 1]) + grid[i - 1][j - 1]
            else:
                dp[i][j] = grid[i - 1][j - 1]

    return min(dp[m])

grid = [[-10,9,20],[35,3,-2]]
print(min_falling_path_sum(grid))
