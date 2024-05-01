def solve():
    m, N = map(int, input().split())
    nums = list(map(int, input().split()))
    MOD = 10**9 + 7

    dp = [[0] * (m + 1) for _ in range(N + 1)]

    for i in range(m + 1):
        dp[0][i] = 1

    for i in range(1, N + 1):
        for j in range(1, min(i, m) + 1):
            dp[i][j] = sum(dp[k][j-1] for k in range(min(i, j), i+1)) % MOD

    return dp[N][m]

print(solve())
