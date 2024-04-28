n = int(input())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

dp = [[0] * n for _ in range(n)]
for i in range(n):
    dp[i][0] = grid[i][0]
for j in range(1, n):
    for i in range(n):
        if i == 0:
            dp[i][j] = grid[i][j] + min(dp[k][j-1] for k in range(i))
        elif i == n - 1:
            dp[i][j] = grid[i][j] + min(dp[k][j-1] for k in range(n-1, i, -1))
        else:
            dp[i][j] = grid[i][j] + min(max(dp[k][j-1], dp[l][j-1]) for k in range(i) for l in range(n-1, i, -1))

print(min(dp[-1]))
