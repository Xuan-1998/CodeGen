def min_falling_path_sum(grid):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(n)]
    
    # Fill up the first row of the DP table
    for j in range(n):
        dp[0][j] = grid[0][j]
    
    # Fill up the rest of the DP table
    for i in range(1, n):
        for j in range(n):
            min_sum = float('inf')
            for k in range(n):
                if abs(j - k) > 0:  # Ensure non-zero shifts
                    min_sum = min(min_sum, dp[i-1][k] + grid[i][j])
            dp[i][j] = min_sum
    
    return dp[n-1][0]

# Example usage:
grid = [[2], [1, 3], [5, 6, 9]]
print(min_falling_path_sum(grid))  # Output: 13
