n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][0] = grid[i][0]
for j in range(1, n):
    for i in range(n):
        dp[i][j] = max(dp[k][j-1] + grid[i][j] if k != i else float('-inf') for k in range(n))

print(min(dp[-1]))
