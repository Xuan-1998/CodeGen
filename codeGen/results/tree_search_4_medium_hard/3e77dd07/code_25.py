def isScrambled(s1, s2):
    if len(s1) != len(s2):
        return False

    n = len(s1)
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True
        dp[0][i] = True

    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = (dp[i-1][j] or dp[i][j-1])

    return dp[n][n]

s1, s2 = input().split()
print(isScrambled(s1, s2))
