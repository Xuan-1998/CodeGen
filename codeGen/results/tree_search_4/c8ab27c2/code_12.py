def shortest_uncommon_subsequence(S, T):
    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = min(dp[i - 1][j - 1] + 1, max(dp[i - 1][j], dp[i][j - 1]))
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return min(dp[-1]) if any(dp[-1]) else -1

S = input().strip()
T = input().strip()

print(shortest_uncommon_subsequence(S, T))
