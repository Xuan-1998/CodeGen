def solve(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(2, n + 1):
        for j in range(1, min(i+1, k)+1):
            if j == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i-1][j-1] + (i // k) * (j <= i % k)) % 100000007

    return dp[n][k]
