import sys

def min_points_to_reach_bottom_right(grid):
    N, M = len(grid), len(grid[0])
    dp = [[sys.maxsize] * (M + 1) for _ in range(N + 1)]
    
    for i in range(N + 1):
        dp[i][0] = grid[i-1][0]
    for j in range(M + 1):
        dp[0][j] = grid[0][j]
        
    for i in range(1, N+1):
        for j in range(1, M+1):
            if grid[i-1][j-1] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
    return dp[N][M]

def main():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    print(min_points_to_reach_bottom_right(grid))

if __name__ == "__main__":
    main()
