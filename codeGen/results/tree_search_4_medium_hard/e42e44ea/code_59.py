def min_initial_points(grid):
    # Get dimensions of the grid
    N, M = len(grid), len(grid[0])
    
    # Initialize minimum positive points required to reach each cell
    dp = [[0] * M for _ in range(N)]
    
    # Fill in the first row (top-left edge)
    for j in range(M):
        if grid[0][j] > 0:
            dp[0][j] = grid[0][j]
        else:
            dp[0][j] = float('inf')  # If points are negative, set to infinity
    
    # Fill in the first column (top-left edge)
    for i in range(N):
        if grid[i][0] > 0:
            dp[i][0] = grid[i][0]
        else:
            dp[i][0] = float('inf')  # If points are negative, set to infinity
    
    # Fill in the rest of the grid
    for i in range(1, N):
        for j in range(1, M):
            if grid[i][j] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            else:
                dp[i][j] = float('inf')  # If points are negative, set to infinity
    
    # Return the minimum positive points required to reach the bottom-right cell
    return dp[-1][-1]

# Example usage
grid = [[3, -2], [1, 4]]
print(min_initial_points(grid))  # Output: 5

