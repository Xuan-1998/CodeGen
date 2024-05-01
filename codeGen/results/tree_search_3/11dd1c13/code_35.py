def min_falling_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # Base case: topmost row
    dp[0][j] = grid[0][j] for j in range(n)

    for i in range(1, m):
        for j in range(n):
            min_sum = float('inf')
            for k in range(n):
                if abs(j - k) == 1:  # non-zero shift
                    continue
                min_sum = min(min_sum, dp[i-1][k] + grid[i][j])
            dp[i][j] = min_sum

    return min(dp[m-1])  # minimum sum of the last row
