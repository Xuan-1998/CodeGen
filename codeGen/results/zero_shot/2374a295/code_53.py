n, k = map(int, input().split())
dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(1, n+1):
    dp[i][1] = 1
for j in range(2, k+1):
        for i in range(j, n+1):
            dp[i][j] = (dp[i-1][j-1]*(i-1) if i>1 else 0)
print((dp[n][k]%1000000007))
