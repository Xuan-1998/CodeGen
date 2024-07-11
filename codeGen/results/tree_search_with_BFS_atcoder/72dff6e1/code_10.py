MOD = 998244353
N = int(input())
A = list(map(int, input().split()))

dp = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0] = 1

for i in range(N):
    dp[i+1] = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
    for j in range(i+1):
        for k in range(j+1):
            dp[i+1][j+1][k+1] += dp[i][j][k] * (N-j)
            dp[i+1][j+1][k+1] %= MOD
            dp[i+1][j+1][k] += dp[i][j][k] * (j-k+1)
            dp[i+1][j+1][k] %= MOD
            dp[i+1][j][k] += dp[i][j][k] * (j*2-k)
            dp[i+1][j][k] %= MOD
            dp[i+1][j][k+1] += dp[i][j][k] * (k+1)
            dp[i+1][j][k+1] %= MOD

ans = 0
for j in range(N+1):
    for k in range(j+1):
        if k <= A[N-1]:
            ans += dp[N][j][k]
            ans %= MOD

print(ans)

