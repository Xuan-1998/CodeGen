import sys

def has_ab_ba(s):
    n = len(s)
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    last_a, last_b = -1, -1
    for i in range(n):
        if s[i:i+2] == "AB":
            last_a, last_b = i + 1, last_b
            dp[i+1][n] = True
        elif s[i:i+2] == "BA" and last_a != -1:
            last_b = i + 1
            dp[n][i+1] = True
    return "YES" if dp[n][n] else "NO"

s = input()
print(has_ab_ba(s))
