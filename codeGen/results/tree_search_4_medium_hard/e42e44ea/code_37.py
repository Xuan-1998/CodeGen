from functools import lru_cache

def minInitialPoints(grid):
    M, N = len(grid), len(grid[0])
    dp = [[0] * N for _ in range(M)]
    
    @lru_cache(None)
    def dfs(i, j):
        if i == M - 1 and j == N - 1:
            return grid[i][j]
        
        if i < M - 1 and j < N - 1:
            return min(dfs(i + 1, j), dfs(i, j + 1)) + grid[i][j]
        elif i < M - 1:
            return dfs(i + 1, j) + grid[i][j]
        else:
            return dfs(i, j + 1) + grid[i][j]

    return dfs(0, 0)
