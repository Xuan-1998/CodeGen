def solve():
    n = int(input())
    MOD = 998244353

    dp = [[0] * (n + 3) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(i - 1, n + 2):
            if i == j:
                continue
            dp[i][j] = (dp[i-1][i-1] * (n+1-j) // i) % MOD

    print(dp[n][n+2])

solve()
