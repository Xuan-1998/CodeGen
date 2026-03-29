def solve():
    n = int(input())
    MOD = 998244353

    dp = [[0] * (n + 2) for _ in range(n + 1)]
    dp[0][1] = 1

    for i in range(1, n + 1):
        for j in range(min(i + 2, n + 2)):
            if j == 0:
                continue
            for k in range(max(1, i - j + 1), min(i + 2, j + 1) + 1):
                dp[i][j] = (dp[i][j] + dp[k - 1][j - 1] * (n - k + 1)) % MOD
    return dp[n][n]

print(solve())
