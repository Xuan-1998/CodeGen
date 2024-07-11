N = int(input())
D = list(map(int, input().split()))

MOD = 998244353
dp = [[0]*(N+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    for j in range(i+1):
        for k in range(min(j, D[i-1])+1):
            dp[i][j] = (dp[i][j] + dp[i-1][j-k] * dp[k][D[i-1]-k]) % MOD

print(sum(dp[N][j] for j in range(1, N+1)) % MOD)

