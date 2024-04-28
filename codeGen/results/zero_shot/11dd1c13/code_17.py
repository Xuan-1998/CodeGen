import sys
n = int(sys.stdin.readline())
grid = []
for _ in range(n):
    grid.append(list(map(int, sys.stdin.readline().split())))
dp = [[0]*n for _ in range(n)]
dp[0][0] = grid[0][0]
for i in range(1, n):
    dp[i][0] = min(dp[i-1][0], grid[i][0]) + grid[i][0]
for j in range(1, n):
    dp[0][j] = min(dp[0][j-1], grid[0][j]) + grid[0][j]
for i in range(1, n):
    for j in range(1, n):
        if i==j:
            dp[i][j] = max(min(grid[i-1][k] for k in range(n) if k!=i), min(grid[k][j-1] for k in range(n) if k!=i)) + grid[i][j]
        else:
            dp[i][j] = min(max(dp[i-1][k] for k in range(n) if k!=i)+grid[i][j], max(dp[k][j-1] for k in range(n) if k!=i)+grid[i][j])
print(min(dp[n-1]))
