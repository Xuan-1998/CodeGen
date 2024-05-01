def shortest_uncommon_subsequence(S, T):
    n = len(S)
    m = len(T)

    # Initialize DP table and hash maps
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    s_freq = {}
    t_freq = {}

    # Preprocess character frequencies
    for c in S:
        s_freq[c] = s_freq.get(c, 0) + 1
    for c in T:
        t_freq[c] = t_freq.get(c, 0) + 1

    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j], dp[i][j - 1])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Find the shortest uncommon subsequence
    for i in range(n, -1, -1):
        if dp[i][m] > 0:
            return i

    # No uncommon subsequence found
    return -1
