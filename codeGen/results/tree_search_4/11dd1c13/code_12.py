def minFallingPathSum(grid):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(n)]
    
    # Base case: the minimum sum of a falling path with non-zero shifts from the top cell to any cell in the first row is equal to the value of that cell
    for j in range(n):
        dp[0][j] = grid[0][j]
        
    for i in range(1, n):
        for j in range(n):
            # Update each dp[i][j] using the minimum sum of a falling path with non-zero shifts from the top cell to the (i-1, k)th cell
            for k in range(n):
                if abs(i - k) > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + grid[i][j])
                    
    # Return the minimum sum of a falling path with non-zero shifts from the top cell to any cell in the last row
    return min(dp[-1])

grid = []
for _ in range(int(input())):
    row = list(map(int, input().split()))
    if not grid:
        grid = [row]
    else:
        grid.append(row)

print(minFallingPathSum(grid))
