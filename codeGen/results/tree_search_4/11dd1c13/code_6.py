import sys

def min_falling_path_sum(grid):
    n = len(grid)
    m = len(grid[0])
    
    # Initialize dp array with infinity values
    dp = [[float('inf')] * m for _ in range(n)]
    
    # Base case: first row, no previous rows to consider
    dp[0] = grid[0]
    
    for i in range(1, n):
        for j in range(m):
            # Consider left and right shifts
            min_shift = float('inf')
            for k in range(max(0, j-1), min(m, j+2)):
                min_shift = min(min_shift, dp[i-1][k] + grid[i][j])
            
            # Update dp array with minimum sum
            dp[i][j] = min_shift
    
    return min(dp[-1])

# Read input from stdin
grid = []
for _ in range(int(input())):
    row = list(map(int, input().split()))
    grid.append(row)

print(min_falling_path_sum(grid))
