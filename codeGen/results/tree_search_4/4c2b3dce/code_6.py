import sys

def check_AB(s):
    n = len(s)
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    # Initialize base case
    dp[0][0] = False

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if s[j - 1] == 'A' and s[j - 2] == 'B':
                dp[i - 1][j] = True
                break
            elif s[j - 1] == 'B' and s[j - 2] == 'A':
                dp[i - 1][j] = True
                break

    for i in range(1, n + 1):
        if dp[0][i]:
            return "YES"

    return "NO"

s = input()
print(check_AB(s))
