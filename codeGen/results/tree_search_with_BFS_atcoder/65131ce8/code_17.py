N = int(input().strip())
d = list(map(int, input().split()))
mod = 998244353

dp = [[0]*(N+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(1, N+1):
    for j in range(i+1):
        dp[i][j] = dp[i-1][j]
        if j:
            dp[i][j] += dp[i-1][j-1]
        dp[i][j] %= mod

cnt = [0]*(N+1)
cnt[0] = 1
for i in range(1, N+1):
    for j in range(i, -1, -1):
        cnt[j] = cnt[j-1]*dp[i][d[i-1]]%mod
    cnt[0] = 0

ans = sum(cnt[i]*dp[N][i]%mod for i in range(N+1))%mod
print(ans)

