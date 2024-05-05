def possible_words(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base case: no words are possible with an empty alphabet or word.
    for i in range(n + 1):
        dp[i][0] = 1

    # Fill up the DP table.
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Place a letter from the i-th character of the alphabet.
            dp[i][j] += dp[i - 1][j - 1]
            # Don't place anything at position j.
            if 2 * (i - 1) > n:
                dp[i][j] += sum(dp[k][m - 1] for k in range(i))
            else:
                dp[i][j] += dp[min(i, (n + 1) // 2)][m - 1]

    # The answer is the value of dp[n][m].
    return dp[n][m] % (10**8 + 7)
