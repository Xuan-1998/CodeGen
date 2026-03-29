def is_scrambled(s1, s2):
    n = len(s1)
    m = len(s2)

    dp = [[False] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = False
    for j in range(m + 1):
        dp[0][j] = False

    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                k = 0
                while i > k and j > k:
                    if s1[i - 1 - k] != s2[j - 1 - k]:
                        break
                    k += 1
                dp[i][j] = dp[i - k][j - k]

    return dp[n][m]
