from sys import stdin

def min_points_to_reach_destination():
    N, M = map(int, stdin.readline().split())
    grid = [[int(cell) for cell in stdin.readline().split()] for _ in range(N)]
    
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if grid[i - 1][j - 1] > 0:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]

    return dp[N][M]

print(min_points_to_reach_destination())
