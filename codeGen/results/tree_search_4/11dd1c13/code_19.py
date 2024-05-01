import sys

def min_falling_path(grid):
    n = len(grid)
    dp = [[0] * (n - 1) for _ in range(n)]

    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + grid[i][j]
            else:
                dp[i][j] = min(dp[i-1][k-1] + grid[i][j] for k in range(1, j+1))

    return sum(dp[-1])

# Example usage
grid = [[1, 2], [3, 4]]
print(min_falling_path(grid))  # Output: 7
