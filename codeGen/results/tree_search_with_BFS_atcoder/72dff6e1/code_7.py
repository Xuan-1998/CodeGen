MOD = 998244353
N = int(input())
A = list(map(int, input().split()))
A = [0] + A
dp = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0] = 1
for i in range(1, N+1):
    for j in range(i+1):
        for k in range(j+1):
            if k:
                dp[i][j][k] = dp[i-1][j-1][k-1]*min(k, A[i])%MOD
            if j != k:
                dp[i][j][k] += dp[i-1][j][k]*max(0, k-j+A[i-1])%MOD
            dp[i][j][k] %= MOD
ans = 0
for j in range(1, N+1):
    ans += dp[N][j][N]
    ans %= MOD
print(ans)

