import sys

def min_squares(n, m):
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif i == 1 and j == 1:
                dp[i][j] = 1
            else:
                min_val = sys.maxsize
                for k in range(1, min(i, j)+1):
                    if (i-k) >= 0 and (j-k) >= 0:
                        min_val = min(min_val, dp[i-k][j-k] + 1)
                dp[i][j] = min_val
    
    return dp[n][m]

n, m = map(int, input().split())
print(min_squares(n, m))
