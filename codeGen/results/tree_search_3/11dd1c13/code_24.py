def minFallingPathSum(grid):
    n = len(grid)
    dp_dict = {(0, j): grid[0][j] for j in range(n)}
    
    for i in range(1, n):
        temp_dict = {}
        for j in range(n):
            if i == 1:
                min_val = float('inf')
                for k in range(j-1, -1, -1):
                    min_val = min(min_val, dp_dict[(i-1, k)])
                temp_dict[(i, j)] = min_val + grid[i][j]
            else:
                min_val = float('inf')
                for k in range(max(0, j-1), n):
                    min_val = min(min_val, dp_dict[(i-1, k)])
                temp_dict[(i, j)] = min_val + grid[i][j]
        
        dp_dict.update(temp_dict)
    
    return min(dp_dict.values())
