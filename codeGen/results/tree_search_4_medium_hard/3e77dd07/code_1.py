def isScramble(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                dp[i][j] = j == 0
            elif j == 0:
                dp[i][j] = i == 0
            elif s1[i - 1] != s2[j - 1]:
                dp[i][j] = True
            else:
                dp[i][j] = isScramble(s1[:i-1], s2[:j-1])

    return dp[n][m]

# Receive input from stdin and print the answer to stdout
s1, s2 = input().split()
print(isScramble(s1, s2))
