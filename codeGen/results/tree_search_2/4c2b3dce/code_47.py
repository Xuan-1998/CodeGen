import sys

def has_ab_ba(s):
    n = len(s)

    # Initialize dp table with base cases for empty strings
    dp = [[True, True] for _ in range(n+1)]

    for i in range(1, n+1):
        if s[i-1] == 'A':
            dp[i][0] = dp[i-1][0]
            dp[i][1] = dp[i-1][0] and not dp[i-1][1]
        else:
            dp[i][0] = dp[i-1][0] or not dp[i-1][0]
            dp[i][1] = dp[i-1][1]

    return "YES" if any(dp[n][0] and dp[n][1]) else "NO"

s = sys.stdin.readline().strip()
print(has_ab_ba(s))
