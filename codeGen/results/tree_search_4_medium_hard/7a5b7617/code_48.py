dp = [[0]*(2002) for _ in range(2002)]

for j in range(M+1):
    dp[0][j] = 1

for i in range(N):
    for j in range(M+1):
        if j == 0:
            dp[i][j] = dp[i-1][j]
        elif j > i:
            dp[i][j] = 0
        else:
            dp[i][j] = (dp[i-1][j-k] + dp[i-1][j]) % 1000000000

print(dp[N-1][M-1])
