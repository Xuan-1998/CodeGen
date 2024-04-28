n = int(input())
grid = [[int(x) for x in input().split()] for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for i in range(1, n):
    for j in range(n):
        if i == 1:
            dp[i][j] = grid[i][j]
        else:
            min_sum = float('inf')
            for k in range(n):
                if (j != k or i-1 != 0) and dp[i-1][k] + grid[i][j] < min_sum:
                    min_sum = dp[i-1][k] + grid[i][j]
            dp[i][j] = min_sum

print(min(dp[-1]))
