def min_squares(n, m):
    for i in range(n, -1, -1):
        for j in range(m, -1, -1):
            if i <= 1 or j <= 1:
                dp[i][j] = 0
            else:
                min_val = float('inf')
                for k in range(1, min(i, j) + 1):
                    if i % k == 0 and j % k == 0:
                        min_val = min(min_val, dp[(i-k)][(j-k)]) + 1
                dp[i][j] = min_val
    return dp[0][0]

n, m = map(int, input().split())
dp = [[float('inf')] * (m+1) for _ in range(n+1)]
print(min_squares(n, m))
