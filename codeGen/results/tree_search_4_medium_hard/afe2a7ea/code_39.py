p = 998244353
n = int(input())
dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    dp[0][i] = 1

for i in range(1, n+1):
    for j in range(i):
        if j == 0:
            dp[i][j] = (i-1 choose j) * p
        else:
            dp[i][j] = (dp[i-1][j-1] * (n-i+2)) % p

print(sum(dp[n][k] for k in range(n+1)) % p)
