def min_falling_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    for j in range(n):
        dp[0][j] = grid[0][j]

    for i in range(1, m):
        for j in range(n):
            prev_min = float('inf')
            for k in range(n):
                if abs(k - j) == 1:
                    continue
                prev_min = min(prev_min, dp[i-1][k])
            dp[i][j] = grid[i][j] + prev_min

    return min(dp[-1])

grid = [[2],[3,4]]
print(min_falling_path_sum(grid))  # Output: 5
