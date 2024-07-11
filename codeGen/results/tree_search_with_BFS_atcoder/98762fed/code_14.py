def solve():
    MOD = 998244353
    N, M = map(int, input().split())
    dp = [[[0]*M for _ in range(M)] for _ in range(N)]
    pow2 = [1]
    for _ in range(N*M+1):
        pow2.append(pow2[-1]*2%MOD)
    for i in range(M):
        dp[0][i][i] = 2
    for n in range(1, N):
        for l in range(M):
            for r in range(l, M):
                dp[n][l][r] = dp[n-1][l][r]*pow2[r-l+1]%MOD
                for k in range(l, r):
                    dp[n][l][r] += dp[n-1][l][k]*dp[0][k+1][r]%MOD
                    dp[n][l][r] %= MOD
    print(dp[N-1][0][M-1])

solve()

