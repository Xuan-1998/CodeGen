import sys

n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

for i in range(1, n):
    for j in range(n):
        min_sum = sys.maxsize
        for k in range(n):
            if k != j:
                min_sum = min(min_sum, dp[i-1][k]) + grid[i][j]
        dp[i][j] = min_sum

print(min(dp[-1]))
