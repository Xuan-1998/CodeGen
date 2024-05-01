def findUncommonSubsequence():
    m, n = [int(i) for i in input().split()]
    s = list(input())
    t = list(input())

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s[i - 1] == t[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                for k in range(i):
                    if not isSubsequence(t, s[k:i]):
                        dp[i][j] = 1 + dp[k][j]
                        break
                else:
                    dp[i][j] = -1

    return dp[m][n]

def isSubsequence(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)

print(findUncommonSubsequence())
