MOD = 998244353
N = int(input())
A = list(map(int, input().split()))
A = [0] + A
dp = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0] = 1
for i in range(1, N+1):
    for j in range(i+1):
        for k in range(j+1):
            if j < i:
                dp[i][j][k] = dp[i-1][j][k] * max(A[i]-j, 0) % MOD
                if k < j:
                    dp[i][j][k] += dp[i-1][j-1][k] * max(j-k+1, 0) % MOD
            elif j == i and k < j:
                dp[i][j][k] = dp[i-1][j-1][k] * max(j-k+1, 0) % MOD
            dp[i][j][k] %= MOD
res = 0
for j in range(N+1):
    for k in range(j+1):
        res = (res + dp[N][j][k]) % MOD
print(res)

