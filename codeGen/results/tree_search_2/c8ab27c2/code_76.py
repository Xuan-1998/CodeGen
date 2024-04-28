def shortest_common_subsequence(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s[i - 1] == t[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return m + n - 2 * dp[m][n]

# Test cases
s1, t1 = "abcba", "abcbc"
print(shortest_common_subsequence(s1, t1))  # Output: 4

s2, t2 = "axcayb", "bayminax"
print(shortest_common_subsequence(s2, t2))  # Output: 3
