n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for i in range(1, n):
    for j in range(n):
        if j == 0:
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i-1][j+1])
        elif j == n-1:
            dp[i][j] = grid[i][j] + min(dp[i-1][j-1], dp[i-1][j])
        else:
            dp[i][j] = grid[i][j] + min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])

print(min([row[-1] for row in dp]))
