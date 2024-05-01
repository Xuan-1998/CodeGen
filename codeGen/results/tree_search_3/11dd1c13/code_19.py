def min_falling_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[-float('inf')] * (n+1) for _ in range(m+1)]
    
    for j in range(n+1):
        dp[0][j] = -99

    for i in range(1, m+1):
        for j in range(1, n+1):
            for k in range(i):
                if (i-k) % 2 == 1: # consider the case of shifting elements up and down
                    dp[i][j] = min(dp[i][j], sum(grid[k][min(j, n)] for _ in range(m)))
    
    return max(min(row) for row in dp[1:])
