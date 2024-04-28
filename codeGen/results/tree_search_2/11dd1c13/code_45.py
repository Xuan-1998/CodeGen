from sys import stdin
n = int(stdin.readline())
m = int(stdin.readline())
dp = [[0] * m for _ in range(n)]
for i in range(1, n):
    for j in range(m):
        if j == 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j+1]) + grid[i][j]
        elif j == m-1:
            dp[i][j] = dp[i-1][j-1] + grid[i][j]
        else:
            dp[i][j] = min(max(dp[i-1][j-1], dp[i-1][j]), dp[i-1][j+1]) + grid[i][j]

print(min(dp[-1]))
