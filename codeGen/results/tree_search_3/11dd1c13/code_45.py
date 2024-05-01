import sys

def min_falling_path(grid):
    R, C = len(grid), len(grid[0])
    dp = [[-sys.maxsize] * C for _ in range(R)]
    
    # Base case: initialize the first row
    for j in range(C):
        dp[0][j] = grid[0][j]
        
    # Fill up the table using memoization
    for i in range(1, R):
        for j in range(C):
            min_val = -sys.maxsize
            for k in range(j+1):  # Try all possible non-zero shifts
                min_val = max(min_val, dp[i-1][k])
            dp[i][j] = grid[i][j] + min_val
            
    return min(dp[-1])  # Return the minimum sum of a falling path

# Example usage:
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(min_falling_path(grid))  # Output: 12
