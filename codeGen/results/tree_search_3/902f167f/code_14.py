import sys

def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 or j == 1:
                dp[i][j] = 0
            else:
                min_val = float('inf')
                for k in range(max(1, i - j), i + 1):
                    for l in range(max(1, j - i + 1), j + 1):
                        if (k * l) <= (i * j):
                            min_val = min(min_val, dp[k][l] + 1)
                dp[i][j] = min_val
    
    return dp[n][m]

n, m = map(int, input().split())
print(min_squares(n, m))
