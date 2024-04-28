n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][0] = grid[i][0]
for j in range(1, n):
    for i in range(j+1):
        dp[i][j] = max(dp[(i+1)%n][j-1], dp[i][j-1]) + grid[i][j]

print(max(dp[0]))
