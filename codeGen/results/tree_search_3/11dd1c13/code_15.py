code
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]
for i in range(n):
    dp[i][0] = grid[i][0]
for j in range(1, n):
    for i in range(n):
        dp[i][j] = min(dp[max(0, i-1)][k] + grid[i][j]) for k in range(max(0, j-1), min(n, j+1))]
print(min(dp[n-1]))
