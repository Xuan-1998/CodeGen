def min_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = {}
    
    def dfs(i, j):
        if (i, j) in dp:
            return dp[(i, j)]
        
        if i == 0 and j == 0:
            return grid[i][j]
        
        min_sum = float('inf')
        if i > 0:
            min_sum = min(min_sum, dfs(i-1, j))
        if j > 0:
            min_sum = min(min_sum, dfs(i, j-1))
        
        dp[(i, j)] = grid[i][j] + min_sum
        return dp[(i, j)]
    
    return dfs(m-1, n-1)
