def solve(n):
    MOD = 998244353
    dp = [[False] * (n+2) for _ in range(n+2)]

    # Base case: when i = 0 or j = 0, it's always possible to set signal powers
    for i in range(n+2):
        dp[i][0] = True
    for j in range(n+2):
        dp[0][j] = True

    # Fill up the DP table
    for i in range(1, n+1):
        for j in range(1, min(i, n)+1):
            if j == 0:  # no radio towers built
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = (dp[i-1][j-1] or dp[i-1][j]) and True

    return int(dp[n][n]) % MOD

n = int(input())
print(solve(n))
