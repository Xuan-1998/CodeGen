n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for i in range(1, n):
    for j in range(n):
        if i == 1:
            dp[i][j] = grid[i][j]
        else:
            dp[i][j] = max(dp[i-1][:j] + [grid[i][j]])[0] + grid[i][j]

print(min([row[-1] for row in dp]))
