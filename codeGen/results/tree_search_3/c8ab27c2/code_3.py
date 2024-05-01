def shortest_uncommon_subsequence(S, T):
    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                continue
            prefix = S[:i]
            if prefix not in T[:j]:
                dp[i][j] = min(i, j)
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j])

    return dp[m][n]

# Example usage
S = input().strip()
T = input().strip()
print(shortest_uncommon_subsequence(S, T))
