n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[float('inf')] * n for _ in range(n)]
dp[0][j] = grid[0][j] for j in range(n)

for i in range(1, n):
    for j in range((i+1)//2, (i-1)//2, -1):
        for k in range(j-1, -1, -1):
            dp[i][j] = min(dp[i][j], dp[i-1][k] + grid[i][j])

print(min(dp[-1]))
