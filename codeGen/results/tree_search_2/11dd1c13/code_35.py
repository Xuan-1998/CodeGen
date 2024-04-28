import sys

def minFallingPathSum(grid):
    n = len(grid)
    
    # Initialize memoized table
    dp = [[0] * n for _ in range(n)]
    
    # Fill up memoized table
    for i in range(1, n):
        for j in range(n):
            if j == 0:
                dp[i][j] = min(dp[k][j+1] + grid[i][k] for k in range(i))
            elif j == n-1:
                dp[i][j] = min(dp[k][j-1] + grid[i][k] for k in range(i))
            else:
                dp[i][j] = min(min(dp[k][j+1] + grid[i][k] for k in range(i)) if j+1 != n else float('inf'), 
                                min(dp[k][j-1] + grid[i][k] for k in range(i)) if j-1 >= 0 else float('inf'))
    
    # Perform final tabulation step
    return min(dp[-1])

grid = []
n = int(input())

for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

print(minFallingPathSum(grid))
