N = int(input())
d = list(map(int, input().split()))
MOD = 998244353

dp = [[0]*N for _ in range(N+1)]
sums = [0]*(N+1)
dp[0][0] = sums[0] = 1

for i in range(1, N+1):
    for j in range(i+1):
        if j > 0:
            dp[i][j] = dp[i-1][j-1]*d[j-1]
        if j < i:
            dp[i][j] += sums[i-1]*d[j] - (dp[i-1][j]*d[j] if j > 0 else 0)
        dp[i][j] %= MOD
    sums[i] = sums[i-1]*d[i] % MOD

answer = sum(dp[N]) % MOD
print(answer)

