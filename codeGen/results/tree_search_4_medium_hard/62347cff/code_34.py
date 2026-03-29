### BEGIN SOLUTION
m, n = map(int, input().split())
grid = [[int(x) for x in input().split()] for _ in range(m)]
dp = [[0] * (n+1) for _ in range(m+1)]

for i in range(1, m+1):
    for j in range(1, n+1):
        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]

print(dp[m][n])
### END SOLUTION
