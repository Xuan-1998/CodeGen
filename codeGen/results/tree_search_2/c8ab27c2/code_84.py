def shortest_uncommon_subsequence(s1, s2):
    m = len(s1)
    n = len(s2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    ans = m + n
    for i in range(m + 1):
        for j in range(n + 1):
            if s1[i:] and s2[j:]:
                ans = min(ans, (m - i) + (n - j))

    return ans

s1, s2 = input().split()
print(shortest_uncommon_subsequence(s1, s2))
