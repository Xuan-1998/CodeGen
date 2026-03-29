def count_good_subsequences(n, a):
    MOD = 10**9 + 7

    # Initialize dp table with zeros
    dp = [[0] * (n+1) for _ in range(n+1)]

    # Base case: when the length of subsequence is 1
    for i in range(1, n+1):
        dp[i][i] = 1

    # Dynamic programming transition state
    for i in range(2, n+1):
        for j in range(i):
            if a[j] % (j+1) == 0:
                dp[i][j+1] += dp[j][j]
                dp[i][j+1] %= MOD

    # Calculate the total number of good subsequences
    ans = sum(dp[n][i] for i in range(1, n+1))
    return ans % MOD
