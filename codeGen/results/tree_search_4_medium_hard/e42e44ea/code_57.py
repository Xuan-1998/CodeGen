from sys import maxsize as INF

def minInitialPoints(grid):
    m, n = len(grid), len(grid[0])
    
    dp = [[INF] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = grid[0][0]
    
    for i in range(1, m + 1):
        if grid[i - 1][0] > 0:
            dp[i][0] = min(dp[i - 1][0], dp[0][0]) + grid[i - 1][0]
        else:
            break
    
    for j in range(1, n + 1):
        if grid[0][j - 1] > 0:
            dp[0][j] = min(dp[0][j - 1], dp[0][0]) + grid[0][j - 1]
        else:
            break
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if grid[i - 1][j - 1] > 0:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]
    
    return dp[m][n]

if __name__ == "__main__":
    m, n = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(m)]
    print(minInitialPoints(grid))
