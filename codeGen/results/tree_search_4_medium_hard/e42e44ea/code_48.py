import sys

def min_points_to_reach(grid):
    N, M = len(grid), len(grid[0])
    dp = [[sys.maxsize] * (M + 1) for _ in range(N + 1)]
    
    # base case: initialize the top-left cell
    dp[0][0] = grid[0][0]
    
    # fill up the DP table
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if i > 0 and j > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            elif i > 0:
                dp[i][j] = dp[i-1][j] + grid[i][j]
            else:  # j > 0
                dp[i][j] = dp[i][j-1] + grid[i][j]
    
    return dp[N][M]

# Example usage:
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
print(min_points_to_reach(grid))
