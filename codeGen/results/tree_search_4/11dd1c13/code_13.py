from collections import Counter

def minFallingPathSum(grid):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(n)]
    
    # Base case: The minimum sum of a falling path starting from the first row is the value itself.
    dp[0] = grid[0]
    
    for i in range(1, n):
        for j in range(n):
            # Calculate the minimum sum of a falling path starting from this cell.
            for k in range(n):
                if j != k:
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + grid[i][j])
    
    # The minimum sum of a falling path is the minimum value in the last row.
    return min(dp[-1])

grid = [[-1]]
print(minFallingPathSum(grid))
