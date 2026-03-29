import sys

def min_points_to_reach_bottom_right(grid):
    M, N = len(grid) - 1, len(grid[0]) - 1
    
    dp = [[0] * (N + 1) for _ in range(M + 1)]
    
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if grid[i][j] > 0:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[M][N]

if __name__ == "__main__":
    M, N = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(M)]
    
    print(min_points_to_reach_bottom_right(grid))
