import sys

def minFallingPathSum(grid):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(n)]
    
    # Initialize dp with grid[0]
    for j, val in enumerate(grid[0]):
        dp[0][j] = val
    
    for i in range(1, n):
        for j in range(n):
            min_val = float('inf')
            for k in range(n):
                if abs(j - k) != 1:  # This ensures no matching column
                    min_val = min(min_val, dp[i-1][k])
            dp[i][j] = min_val + grid[i][j]
    
    return min(dp[-1])

grid = []
for _ in range(int(input())):
    row = list(map(int, input().split()))
    grid.append(row)

print(minFallingPathSum(grid))
