import sys

def check_AB_BA(s):
    n = len(s)
    dp = [[False] * 2 for _ in range(n + 1)]

    for i in range(2):
        if s[i] == 'A':
            dp[i][0] = False
            dp[i][1] = True
        else:
            dp[i][0] = True
            dp[i][1] = False

    for i in range(2, n + 1):
        for j in range(2):
            if s[i - 1] == 'A':
                if j == 0:
                    dp[i][j] = dp[i - 1][1]
                else:
                    dp[i][j] = dp[i - 1][0] and True
            else:
                if j == 0:
                    dp[i][j] = True and (dp[i - 1][1] or False)
                else:
                    dp[i][j] = dp[i - 1][0]

    return "YES" if dp[n][1] and any("AB" in s[:i] for i in range(n)) else "NO"

s = input()
print(check_AB_BA(s))
