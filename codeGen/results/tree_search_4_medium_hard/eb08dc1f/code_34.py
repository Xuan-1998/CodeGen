def solve():
    n = int(input())
    dp = [[0]*(n+1) for _ in range(n+1)]

    for i in range(n+1):
        dp[i][1] = 1

    for j in range(2, n+1):
        for i in range(j-1, -1, -1):
            if (i == 0 or dp[i][j-1] != 0) and (i > 0 or dp[i][j] == 0):
                dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 998244353
            elif i > 0 and dp[i][j] == 0:
                dp[i][j] = dp[i-1][j]

    for j in range(1, n+1):
        print(dp[n][j], end=' ')
