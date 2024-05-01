def minFallingPathSum(grid):
    n = len(grid)
    m = len(grid[0])
    
    # Initialize dp array
    dp = [[float('inf')] * m for _ in range(n)]
    dp[0] = grid[0]
    
    for i in range(1, n):
        for j in range(m):
            min_val = float('inf')
            for k in range(m):
                if k != j:
                    min_val = min(min_val, dp[i-1][k] + grid[i][j])
            dp[i][j] = min_val
    
    # Find the minimum sum of a falling path
    return min(dp[-1])

# Read input from stdin
grid = []
for _ in range(int(input())):
    grid.append(list(map(int, input().split())))

print(minFallingPathSum(grid))
