def isScramble(s1, s2):
    n = len(s1)
    m = len(s2)

    dp = [[False] * (m + 1) for _ in range(n + 1)]

    def scramble(i, j):
        if i == 0:
            return s2[:j] == s1
        for k in range(1, i+1):
            if ((dp[k-1][j] and s1[:k] + s1[i-k:] == s2[:j]) or 
                (dp[i][j-k] and s1[:i-k] + s1[k:i] == s2[:j])):
                return True
        return False

    for i in range(1, n+1):
        dp[i][0] = scramble(i, 0)
    for j in range(1, m+1):
        dp[0][j] = scramble(0, j)

    for i in range(1, n+1):
        for j in range(1, m+1):
            if (dp[i-1][j] and s1[:i] + s1[i:] == s2[:j] + s2[j:]):
                dp[i][j] = True
            else:
                for k in range(1, i+1):
                    if ((dp[k-1][j] and s1[:k] + s1[i-k:] == s2[:j]) or 
                        (dp[i][j-k] and s1[:i-k] + s1[k:i] == s2[:j])):
                        dp[i][j] = True
                        break

    return dp[n][m]

# test the function
s1, s2 = input().split()
print(isScramble(s1, s2))
