n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for i in range(1, n):
    for j in range(n):
        dp[i][j] = max(grid[i-1][k] + (i == j or i-j) * dp[j][min(max(k, 0), j-1)] for k in range(n))

print(min(dp[-1]))
