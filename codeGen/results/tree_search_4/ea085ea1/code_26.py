def solve(str1, str2):
    N = len(str1)
    dp = [[0] * (N+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(i+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][k] for k in range(j))

    return dp[N][N]

str1, str2 = input().split()
print(solve(str1, str2))
