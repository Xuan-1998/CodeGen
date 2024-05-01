===BEGIN SOLUTION===
def min_squares(n, m):
    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i <= 2 and j <= 2:
                dp[i][j] = min(i, j)
            else:
                if i < j:
                    dp[i][j] = dp[i][j-1] + 1
                elif j < i:
                    dp[i][j] = dp[i-1][j] + 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + (min(i, j) - 1)**2

    return dp[n][m]

n, m = map(int, input().split())
print(min_squares(n, m))
