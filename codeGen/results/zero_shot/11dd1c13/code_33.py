n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for i in range(1, n):
    for j in range(n):
        if i == 1:
            dp[i][j] = grid[i][j]
        else:
            min_val = float('inf')
            for k in range(n):
                if abs(j-k) != i-1: 
                    min_val = min(min_val, dp[i-1][k])
            dp[i][j] = grid[i][j] + min_val

print(min(dp[-1]))
