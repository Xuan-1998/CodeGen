def minFallingPathSum(grid):
    m = len(grid)
    for i in range(1, m):
        for j in range(m):
            if j == 0:
                grid[i][j] += min(grid[i-1][0], grid[i-1][1])
            elif j == m - 1:
                grid[i][j] += min(grid[i-1][m-2], grid[i-1][m-1])
            else:
                grid[i][j] += min(grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1])

    return min(grid[m-1])
