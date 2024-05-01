def min_uncommon_subsequence_length(S, T):
    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    same = [[False] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:
                same[i][j] = True
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1])
            if not same[i][j]:
                dp[i][j] += 1

    return max(0, dp[m][n])

S, T = input().split()
print(min_uncommon_subsequence_length(S, T))
