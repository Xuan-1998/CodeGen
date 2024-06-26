from sys import stdin

m, n = map(int, stdin.readline().split())
grid = [list(map(int, stdin.readline().split())) for _ in range(m)]

dp = [[0] * n for _ in range(m)]
dp[0][j] = grid[0][j] for j in range(n)
dp[i][0] = grid[i][0] for i in range(m)

for i in range(1, m):
    for j in range(1, n):
        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

print(dp[m-1][n-1])
