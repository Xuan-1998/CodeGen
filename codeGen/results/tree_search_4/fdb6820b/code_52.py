def solve(m, N, arr):
    MOD = 10**9 + 7

    dp = [[[0] * (N+1) for _ in range(N+1)] for _ in range(m+1)]
    res = 0

    for k in range(1, m+1):
        for i in range(k, N+1):
            for j in range(i, N+1):
                if i == j:
                    dp[k][i][k] = 1
                elif k > 1 and i > 0:
                    dp[k][j][k] += sum(dp[prev_k][i-prev_k-1][k-1] for prev_k in range(1, k))
                res += dp[k][N][k]
        res %= MOD

    return res
