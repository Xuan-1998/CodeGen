n = int(input())
grid = [[int(x) for x in input().split()] for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for i in range(1, n):
    dp[i][0] = grid[i][0] + min(dp[i-1][0], dp[i-1][1])
    for j in range(1, i):
        dp[i][j] = grid[i][j] + min(max(dp[i-1][k-1]+dp[i-1][k], k==0) for k in range(j))
    dp[i][-1] = grid[i][-1] + min(dp[i-1][-2], dp[i-1][-1])

print(min(dp[-1]))
