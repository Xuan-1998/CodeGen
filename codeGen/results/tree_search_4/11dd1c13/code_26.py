def min_falling_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # Base case: When we reach the last row or column, there are no more choices.
    for i in range(1, m):
        dp[i][0] = grid[i][0]
    for j in range(1, n):
        dp[0][j] = grid[0][j]

    # State transition: For each cell, find the minimum sum of a falling path with non-zero shifts.
    for i in range(1, m):
        for j in range(n):
            if i == 1:
                # First row: Choose the smallest element from the previous column.
                dp[i][j] = min(grid[i-1][:j+1])
            else:
                # Other rows: Find the minimum sum of a falling path with non-zero shifts.
                dp[i][j] = grid[i][j] + min(dp[max(0, i-1)-1][k] for k in range(max(0, j-grid[i-1][k-1])))

    return min(dp[-1])
