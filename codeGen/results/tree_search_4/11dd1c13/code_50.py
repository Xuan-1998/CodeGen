import sys

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

for i in range(n):
    if i == 0:
        dp[i][j] = grid[0][j]
    else:
        for j in range(n):
            min_sum = sys.maxsize
            for k in range(n):
                if j != k and (i - 1, k) not in [(x, y) for x in range(i) for y in range(n)]:
                    min_sum = min(min_sum, dp[i-1][k] + grid[i][j])
            dp[i][j] = min_sum

print(min(dp[-1]))
