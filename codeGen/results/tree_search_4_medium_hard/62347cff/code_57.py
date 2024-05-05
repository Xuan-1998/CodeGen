from sys import stdin

m, n = map(int, stdin.readline().split())
grid = [[int(x) for x in stdin.readline().split()] for _ in range(m)]

dp = [[0] * n for _ in range(m)]

for i in range(m):
    dp[i][0] = grid[i][0]
for j in range(n):
    dp[0][j] = grid[0][j]

for i in range(1, m):
    for j in range(1, n):
        dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

print(dp[m-1][n-1])
