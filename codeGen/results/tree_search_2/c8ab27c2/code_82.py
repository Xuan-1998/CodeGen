def shortest_uncommon_subsequence(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base case: all zeros
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] != t[j - 1]:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])

    # The answer is the maximum length of uncommon subsequences
    return m if not any(dp[i][n] == 0 for i in range(m)) else max(dp[i][n] for i in range(m))
