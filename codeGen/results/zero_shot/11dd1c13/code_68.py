n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
for i in range(1, n):
    for j in range(n):
        if j == 0:
            dp[i][j] = grid[i][j] + min(dp[i-1][:])
        elif j == n-1:
            dp[i][j] = grid[i][j] + min(dp[i-1][-1:])
        else:
            dp[i][j] = grid[i][j] + min(max(dp[i-1][:j]), max(dp[i-1][j:]))
print(min(sum(row) for row in zip(*dp)))
