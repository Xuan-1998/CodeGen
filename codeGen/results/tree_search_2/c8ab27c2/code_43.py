def shortest_uncommon_subsequence():
    S = input().strip()
    T = input().strip()

    n, m = len(S), len(T)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + 1

    return n + m - 2 * dp[n][m]

print(shortest_uncommon_subsequence())
