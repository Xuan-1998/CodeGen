def isScramble(s1, s2):
    n = len(s1)
    m = len(s2)

    dp = [[False] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 and j == 0:
                continue
            elif i == 0 or j == 0:
                dp[i][j] = (i == 0) != (j == 0)
            else:
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    for k in range(i):
                        if dp[k][j - 1] and dp[i - 1 - k][j - 1]:
                            dp[i][j] = True
                            break

    return dp[n][m]

# Test cases
s1, s2 = input().split()
print(isScramble(s1, s2))
