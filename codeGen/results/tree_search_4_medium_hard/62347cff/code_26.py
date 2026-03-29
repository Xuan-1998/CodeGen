def minPathSum(grid):
    m, n = len(grid), len(grid[0])
    
    dp = [[0] * n for _ in range(m)]
    
    # base cases
    dp[0][j] = grid[0][j] for j in range(n)
    dp[i][0] = grid[i][0] for i in range(m)
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            
    return dp[m-1][n-1]

if __name__ == "__main__":
    # Read input from stdin
    m, n = map(int, input().split())
    grid = [[int(x) for x in input().split()] for _ in range(m)]
    
    print(minPathSum(grid))
