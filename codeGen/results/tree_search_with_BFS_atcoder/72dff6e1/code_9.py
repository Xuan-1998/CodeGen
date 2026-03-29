MOD = 998244353
N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)

dp = [[0]*(N+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(1, N+1):
    for j in range(i+1):
        if j > 0:
            dp[i][j] = (dp[i][j] + dp[i-1][j-1] * (A[i] - j + 1)) % MOD
        if j <= i-1:
            dp[i][j] = (dp[i][j] + dp[i-1][j] * (j - A[i] + 1)) % MOD

answer = sum(dp[N][j] for j in range(N+1)) % MOD
print(answer)

