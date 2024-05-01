from typing import List

def min_falling_path_sum(grid: List[List[int]]) -> int:
    n = len(grid)
    dp = [[0] * n for _ in range(n)]

    # Initialize the first row with zeros
    dp[0] = grid[0]

    for i in range(1, n):
        for j in range(n):
            dp[i][j] = max(0, dp[i-1][k]) + grid[i][j]
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1])
            if j < n - 1:
                dp[i][j] = min(dp[i][j], dp[i][j+1])

    return min(dp[-1])
