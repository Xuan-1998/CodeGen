import sys

N, M = map(int, input().split())
grid = [[int(i) for i in j.split()] for j in [sys.stdin.readline() for _ in range(N)]]

dp = [[0]*M for _ in range(N)]

for i in range(N):
    dp[i][0] = grid[i][0]
for j in range(M):
    dp[0][j] = grid[0][j]

for i in range(1, N):
    for j in range(1, M):
        if grid[i][j] > 0:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        else:
            if i == 0 and j == 0: 
                min_points = 0
            elif i > 0: 
                min_points = min(min_points, dp[i-1][j])
            elif j > 0: 
                min_points = min(min_points, dp[i][j-1])

print(min_points)
