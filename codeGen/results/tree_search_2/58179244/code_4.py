from collections import defaultdict

def min_recolors(s):
    n = len(s)
    dp = [[0] * 3 for _ in range(n + 1)]

    for i in range(1, n + 1):
        if s[i - 1] == 'R':
            dp[i][0] = dp[i - 1][1]
            dp[i][1] = dp[i - 1][2]
        elif s[i - 1] == 'G':
            dp[i][0] = dp[i - 1][2]
            dp[i][1] = dp[i - 1][0]
        else:
            dp[i][0] = dp[i - 1][1]
            dp[i][1] = dp[i - 1][0]

    return min(dp[-1])

n = int(input())
s = input()

print(min_recolors(s))
