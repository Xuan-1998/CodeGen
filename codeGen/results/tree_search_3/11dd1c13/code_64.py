def minFallingPathSum(grid):
    n = len(grid)
    memo = [[0] * (n + 1) for _ in range(n)]
    
    for j in range(n):
        memo[0][j] = grid[0][j]
        
    for i in range(1, n):
        for j in range(n):
            min_sum = float('inf')
            for k in range(n):
                if abs(k - j) == 1:  # ignore adjacent columns
                    continue
                min_sum = min(min_sum, memo[i-1][k] + grid[i][j])
            memo[i][j] = min_sum
            
    return min(memo[-1])

