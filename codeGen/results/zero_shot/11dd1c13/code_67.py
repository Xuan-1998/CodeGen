import sys
n = int(sys.stdin.readline())
grid = []
for _ in range(n):
    grid.append(list(map(int, sys.stdin.readline().split())))
dp = [[0]*n for _ in range(n)]
dp[0][0] = grid[0][0]
for i in range(1,n):
    dp[i][0] = max(dp[i-1][0],grid[i][0])
for j in range(1,n):
    dp[0][j] = max(dp[0][j-1],grid[0][j])
for i in range(1,n):
    for j in range(1,n):
        dp[i][j] = max(min(dp[i-1][j-1],dp[i-1][j]),min(dp[i][j-1],dp[i][j])) + grid[i][j]
print(max(min(row[-1],row[0]) for row in dp))
