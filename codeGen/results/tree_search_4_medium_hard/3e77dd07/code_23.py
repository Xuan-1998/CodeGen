def is_scrambled(s1, s2):
    if len(s1) != len(s2):
        return False

    dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = True
            elif i > 0 and j > 0:
                dp[i][j] = (dp[i - 1][j - 1] or dp[i - 1][j] or dp[i][j - 1])

    return dp[-1][-1]
