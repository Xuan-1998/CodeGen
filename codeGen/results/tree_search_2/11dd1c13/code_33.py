def minFallingPathSum(grid):
    n = len(grid)
    memo = {}

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        res = float('inf')
        for k in range(i):
            for col in range(n):
                if grid[k][col] == grid[i-1][j]:
                    continue
                res = min(res, dfs(k, col-1) + grid[i-1][j])
        memo[(i, j)] = res
        return res

    return min(dfs(i, j) for i in range(n) for j in range(n))
