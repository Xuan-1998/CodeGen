def minFallingPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    
    dp = [[float('inf')] * n for _ in range(m)]
    dp[0] = grid[0]
    
    for i in range(1, m):
        for j in range(n):
            for k in range(j):  # consider all columns up to j
                dp[i][j] = min(dp[i][j], dp[i-1][k] + grid[i][j])
    
    return min(dp[-1])  # return the minimum sum of a falling path

grid = []
while (row := list(map(int, input().split()))):
    if not row:
        break
    grid.append(row)
print(minFallingPathSum(grid))
