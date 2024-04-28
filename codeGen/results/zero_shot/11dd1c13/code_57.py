n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for i in range(1, n):
    for j in range(n):
        if j == 0:
            dp[i][j] = grid[i][j] + min(dp[i-1][:])
        elif j == n - 1:
            dp[i][j] = grid[i][j] + min(dp[i-1][-1:])
        else:
            dp[i][j] = grid[i][j] + min([dp[i-1][k] for k in range(n) if k != j])

print(min(dp[-1]))
