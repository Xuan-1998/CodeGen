code
import sys

def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 or j == 1:
                dp[i][j] = 0
            elif i < j:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + 1
            else:
                for k in range(1, i + 1):
                    if k * k <= i and k * k <= j:
                        dp[i][j] = min(dp[i][j], dp[max(0, i - k)][max(0, j - k)] + 1)
    
    return dp[n][m]

n, m = map(int, sys.stdin.readline().split())
print(min_squares(n, m))
