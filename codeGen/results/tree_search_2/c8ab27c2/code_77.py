def shortest_uncommon_subsequence(S, T):
    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Find the maximum length of uncommon subsequences
    max_length = 0
    for i in range(m + 1):
        for j in range(n + 1):
            if S[i:] and T[j:]:
                max_length = max(max_length, dp[i][j])

    return -1 if max_length == 0 else max_length
