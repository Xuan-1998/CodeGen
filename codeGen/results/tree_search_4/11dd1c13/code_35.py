def minFallingPathSum(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]

    # Base case: first row
    for j in range(n):
        dp[0][j] = grid[0][j]

    for i in range(1, n):
        for j in range(n):
            min_sum = float('inf')
            for k in range(n):
                if k != j:
                    min_sum = min(min_sum, dp[i-1][k])
            dp[i][j] = grid[i][j] + min_sum

    # Find the minimum sum at the bottom row
    return min(dp[-1])

# Example usage:
grid = [[2,1,3], [4,5,6], [7,8,9]]
print(minFallingPathSum(grid))  # Output: 12
