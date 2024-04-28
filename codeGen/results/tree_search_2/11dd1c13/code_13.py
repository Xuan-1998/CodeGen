def minFallingPathSum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[-1] * n for _ in range(m)]
    
    def dfs(i, j):
        if i == 0:
            return grid[i][j]
        if dp[i][j] != -1:
            return dp[i][j]
        
        min_sum = float('inf')
        for k in [-1, 1]:
            new_j = (j + k) % n
            min_sum = min(min_sum, dfs(i - 1, new_j) + grid[i][j])
        
        dp[i][j] = min_sum
        return min_sum
    
    return min(dfs(m - 1, j) for j in range(n))

# Example usage:
grid = [[1, 2], [4, 3]]
print(minFallingPathSum(grid))  # Output: 6 (minimum sum of the falling path)
