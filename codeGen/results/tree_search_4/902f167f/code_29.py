import sys

def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 and j == 0:
                dp[i][j] = 0
            elif i == 0 or j == 0:
                dp[i][j] = max(i, j)
            else:
                min_val = sys.maxsize
                for k in range(1, min(i, j) + 1):
                    if i - k >= 0 and j - k >= 0:
                        val = dp[i-k][j] + dp[k][k]
                        if val < min_val:
                            min_val = val
                dp[i][j] = min_val
    
    return dp[n][m]

# Receive input from stdin
n, m = map(int, sys.stdin.readline().split())

print(min_squares(n, m))
