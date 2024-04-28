def minFallingPathSum(grid):
    dp = [[0] * len(grid[0]) for _ in range(len(grid))]

    def dfs(i, j):
        if i == 0:
            return grid[i][j]
        res = float('inf')
        for k in range(len(grid[0])):
            res = min(res, dfs(i-1, k) + grid[i][j])
        return res

    res = float('inf')
    for j in range(len(grid[0])):
        res = min(res, dfs(0, j))
    return res
