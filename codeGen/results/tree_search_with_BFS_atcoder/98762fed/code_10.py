def solve(N, M):
    MOD = 998244353
    dp = [[[0]*(M+1) for _ in range(M+1)] for _ in range(N+1)]
    pow2 = [1]*(N*M+1)
    for i in range(1, N*M+1):
        pow2[i] = pow2[i-1] * 2 % MOD

    for i in range(1, M+1):
        dp[1][i][i] = 2

    for i in range(2, N+1):
        for j in range(1, M+1):
            dp[i][j][j] = dp[i-1][j][j] * 2 % MOD
            for k in range(j+1, M+1):
                dp[i][j][k] = (dp[i-1][j][k] * pow2[k-j+1] + dp[i][j][k-1] * pow2[i] - dp[i-1][j][k-1] * pow2[k-j+i-1] + 2 * MOD) % MOD

    return dp[N][1][M]

N, M = map(int, input().split())
print(solve(N, M))

