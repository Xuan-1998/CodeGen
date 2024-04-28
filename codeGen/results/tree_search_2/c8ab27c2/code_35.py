def minUncommonLength(S, T):
    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

    uncommon_length = float('inf')
    for i in range(m):
        for j in range(n):
            if S[i] != T[j]:
                uncommon_length = min(uncommon_length, dp[i][j])

    return -1 if uncommon_length == float('inf') else m - uncommon_length
