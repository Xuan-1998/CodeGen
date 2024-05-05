def solve():
    n = int(input())  # input variable
    MOD = 998244353

    dp = [[0] * (n + 2) for _ in range(n + 2)]

    dp[0][n] = 1  # base case

    for j in range(1, n + 1):
        for i in range(j - 1, n + 1):
            dp[i][j] = (dp[i][j - 1] * (1 << (i - 1))) % MOD

    result = dp[n][n]
    print(result)
