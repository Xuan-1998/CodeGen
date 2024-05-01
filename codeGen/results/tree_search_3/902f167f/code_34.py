import math

def min_squares(n, m):
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                for k in range(1, min(i, j) + 1):
                    if (i - k) * (j - k) % (k ** 2) == 0:
                        dp[i][j] = min(dp[i][j], dp[k - 1][j - k] + 1)
    
    return dp[n][m]

n, m = map(int, input().split())
print(min_squares(n, m))
