import sys

def min_squares(n, m):
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                dp[i][j] = 1
            elif i > 0 and j > 0:
                min_val = float('inf')
                for k in range(i, 0, -1):
                    for sq_j in range(j, 0, -1):
                        if k*k >= i and sq_j*sq_j >= j:
                            min_val = min(min_val, dp[k-1][j] + dp[i-k][sq_j])
                dp[i][j] = min_val
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n][m]

n, m = map(int, input().split())
print(min_squares(n, m))
