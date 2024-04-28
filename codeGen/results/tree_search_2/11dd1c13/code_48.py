def minFallingPathSum(grid):
    n = len(grid)
    memo = [[float('inf')] * n for _ in range(n)]
    
    def dfs(i, j):
        if i == n - 1:
            return grid[i][j]
        
        res = float('inf')
        for dx in [-1, 0, 1]:
            ni, nj = i + dx, j
            if 0 <= ni < n and 0 <= nj < n:
                res = min(res, dfs(ni, nj))
        memo[i][j] = grid[i][j] + (res - grid[i][j])
        return memo[i][j]
    
    ans = float('inf')
    for j in range(n):
        ans = min(ans, dfs(0, j))
    return min(ans, 0)

grid = [[-19,15,6,8],[18,3,-7,12],[-5,9,1,20]]
print(minFallingPathSum(grid)) 
