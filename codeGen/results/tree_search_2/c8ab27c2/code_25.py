def shortest_common_subsequence(S, T):
    m = len(S)
    n = len(T)

    # Initialize the dp table with all 1s. This is because an empty string is always a subsequence of another empty string.
    dp = [[1] * (n + 1) for _ in range(m + 1)]

    # Fill up the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] != T[j - 1]:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
            else:
                dp[i][j] = dp[i - 1][j - 1]

    # The length of the shortest uncommon subsequence is just the difference between the lengths of S and T minus the length of the longest common subsequence.
    return m + n - 2 * dp[m][n]
