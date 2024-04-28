import sys

def min_falling_path(grid):
    n = len(grid)
    m = len(grid[0])
    
    dp = [[sys.maxsize] * m for _ in range(n)]
    
    # Base case: when i == n - 1, the minimum sum is just the value of the current cell
    for j in range(m):
        dp[n-1][j] = grid[n-1][j]
        
    for i in range(n-2, -1, -1):
        for j in range(m):
            # Calculate the minimum sum by considering all possible previous cells with non-zero shifts
            for k in range(i+1):
                dp[i][j] = min(dp[i][j], dp[k][max(0, j-1)] + grid[i][j])
    
    return min(dp[0])

grid = [list(map(int, input().split())) for _ in range(int(input()))]
print(min_falling_path(grid))
