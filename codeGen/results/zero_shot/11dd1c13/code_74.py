n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for i in range(1,n):
    for j in range(n):
        if j == 0:
            dp[i][j] = dp[i-1][j] + grid[i][j]
        elif j == n-1:
            dp[i][j] = min([dp[i-1][k]+grid[i][j] for k in range(n)]) 
        else: 
            dp[i][j] = min([dp[i-1][k]+grid[i][j] for k in range(j)] + [dp[i-1][k]+grid[i][j] for k in range(j+1,n)])
print(min(dp[-1]))
