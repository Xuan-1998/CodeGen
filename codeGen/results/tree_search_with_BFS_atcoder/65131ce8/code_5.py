MOD = 998244353
N = int(input().strip())
d = list(map(int,input().strip().split()))
d = [0] + d
dp = [[0]*(N+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(1,N+1):
    for j in range(i+1):
        dp[i][j] = dp[i-1][j]
        if j >= 1:
            dp[i][j] += dp[i-1][j-1]
        dp[i][j] %= MOD
ans = [0]*(N+1)
for i in range(1,N+1):
    for j in range(i,N+1):
        ans[i] += dp[j][i]*dp[N-j][d[i]] % MOD
        ans[i] %= MOD
print(sum(ans)%MOD)

