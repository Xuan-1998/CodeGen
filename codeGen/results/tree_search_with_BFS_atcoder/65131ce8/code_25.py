N = int(input())
d = list(map(int,input().split()))
MOD = 998244353
dp = [[[0]*2 for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0] = 1
for i in range(N):
    for j in range(i+1):
        for k in range(2):
            if dp[i][j][k] > 0:
                dp[i+1][j+1][k or d[i]>j] += dp[i][j][k]
                dp[i+1][j+1][k or d[i]>j] %= MOD
                dp[i+1][j][k or d[i]>=j] += dp[i][j][k]*(d[i]-(k and d[i]==j))
                dp[i+1][j][k or d[i]>=j] %= MOD
                dp[i+1][j-1][k or d[i]>j-1] += dp[i][j][k]*(j-(d[i]-(k and d[i]==j)))
                dp[i+1][j-1][k or d[i]>j-1] %= MOD
res = 0
for j in range(N+1):
    res += dp[N][j][1]
    res %= MOD
print(res)

