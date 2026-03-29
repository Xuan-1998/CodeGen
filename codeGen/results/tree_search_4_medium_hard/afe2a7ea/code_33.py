n = int(input())
dp = [[0] * (n + 1) for _ in range(n + 2)]

for i in range(n + 1):
    dp[0][i] = 1

for i in range(1, n + 2):
    for j in range(1, n + 1):
        if i == 1:
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i-1][j] + dp[i-1][j+1] + dp[i-1][j-1]) % 998244353

print(sum(dp[n]))

