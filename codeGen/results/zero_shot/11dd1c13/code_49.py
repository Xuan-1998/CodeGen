import sys
n = int(sys.stdin.readline().strip())
grid = [[int(x) for x in line.strip().split()] for line in sys.stdin.readlines()]
dp = [[0]*n for _ in range(n)]
for i in range(1, n):
    dp[i][0] = min(dp[i-1][0], grid[i-1][i-1]) + grid[i][0]
for j in range(1, n):
    dp[0][j] = min(dp[0][j-1], grid[0][j-1]) + grid[0][j]
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(min(dp[i-1][j], grid[i-1][j]), min(dp[i][j-1], grid[i][j])) + grid[i][j]
print(min(dp[n-1]))
