def min_squares(n, m):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 or j == 1:
                dp[i][j] = 1
            elif (i >= 2 and j >= 2) and ((i-1)//j)*j + j <= i and ((j-1)//i)*i + i <= j:
                dp[i][j] = min(dp[(i-1)//j]*j + 1, dp[(j-1)//i]*i + 1)
            else:
                dp[i][j] = 1

    return dp[n][m]

n, m = map(int, input().split())
print(min_squares(n, m))
