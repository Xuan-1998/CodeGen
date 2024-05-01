import sys

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
m = n - 1

for j in range(m):
    for i in range(n):
        dp[j][i] = min((grid[j][i] + grid[k][i]) for k in range(j+1, m) if i != k) + grid[j][i]

print(min(dp[0]))
