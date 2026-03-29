from sys import stdin

N, M = map(int, stdin.readline().split())
grid = []
for _ in range(N):
    row = list(map(int, stdin.readline().split()))
    grid.append(row)

dp = [[0] * M for _ in range(N)]

# Initialize the top-left cell with its value
dp[0][0] = grid[0][0]

# Fill up the DP table row by row
for i in range(1, N):
    for j in range(M):
        if j == 0:
            dp[i][j] = dp[i-1][j] + grid[i][j]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

# The minimum initial points required to reach the destination cell is stored in the bottom-right cell
min_points = dp[-1][-1]

print(min_points)
