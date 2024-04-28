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
                if k != j and (dp[i-1][k] < min_val or not any(dp[i-1][x] == dp[i-1][k] for x in range(k, n))):
                    min_val = dp[i-1][k]
            dp[i][j] = grid[i][j] + min_val

print(min(max(row) for row in zip(*dp)))
