def shortest_uncommon_subsequence(S, T):
    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1])
            else:
                dp[i][j] = i + (S[:i].find(T[:j]) != j)

    return max(0, m - dp[m][n])

# Read input from stdin
S = input()
T = input()

print(shortest_uncommon_subsequence(S, T))
