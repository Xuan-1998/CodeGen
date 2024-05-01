def shortest_uncommon_subsequence(S, T):
    m, n = len(S), len(T)
    dp = [[-1] * (n + 1) for _ in range(m + 1)]

    i, j = 0, 0
    while i <= m and j <= n:
        if S[i] == T[j]:
            i += 1
            j += 1
        else:
            dp[i][j] = 0 if i == 0 or j == 0 else min(dp[i - 1][j], dp[i][j - 1]) + 1
            if i < m and S[i] != T[j]:
                i += 1
            elif j < n:
                j += 1

    return max(max(row) for row in dp) if any(val > 0 for row in dp for val in row) else -1
