def solve():
    n = int(input())
    MOD = 998244353
    dp = [[0] * (n + 2) for _ in range(n + 2)]
    dp[0][0] = 1
    dp[n+1][n+1] = 0
    for i in range(1, n+1):
        for k in range(i + 1):
            if k == 0 or k == i:
                dp[i][k] = dp[i-1][k]
            else:
                dp[i][k] = (dp[i-1][k-1] if k > 0 else 0) % MOD
    print(dp[n+1][n])
