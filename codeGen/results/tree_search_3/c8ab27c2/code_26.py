def shortest_uncommon_subsequence(S, T):
    n = len(S)
    m = len(T)

    # Initialize memoization table
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    # Fill the table using dynamic programming and memoization
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = not dp[i - 1][j]

    # Find the maximum length of uncommon subsequences
    max_len = 0
    for i in range(n + 1):
        if not any(dp[i][j] for j in range(m + 1)):
            max_len = i

    return n - max_len if max_len > 0 else -1
