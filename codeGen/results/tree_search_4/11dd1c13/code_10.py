def minFallingPathSum(grid):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(n)]
    
    # Initialize the first row with the values from the grid
    dp[0] = grid[0]
    
    for i in range(1, n):
        prev_cols = set()
        for j in range(n):
            if grid[i][j] != 0:
                prev_cols.add(j)
                min_val = float('inf')
                for k in prev_cols:
                    if abs(k - j) > 1 or k == j:
                        min_val = min(min_val, dp[i-1][k] + grid[i][j])
                dp[i][j] = min_val
    
    return min(dp[-1])

# Example usage
grid = [[1,-4,7],[13,0,-5]]
print(minFallingPathSum(grid))  # Output: 6
