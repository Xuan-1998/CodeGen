from sys import stdin

def min_points_required():
    N, M = map(int, stdin.readline().split())
    grid = []
    for _ in range(N):
        row = list(map(int, stdin.readline().split()))
        grid.append(row)

    dp = [[float('inf')] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 0

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if grid[i - 1][j - 1] > 0:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]

    return dp[N][M]

print(min_points_required())
