import sys
from collections import defaultdict

dp = defaultdict(bool)

def solve(s):
    n = len(s)
    for i in range(n):
        dp[i] = False

    for i in range(1, n):
        if s[i-1] == 'A' and s[i] == 'B':
            dp[i] = True
        elif s[i-1] == 'B' and s[i] == 'A':
            dp[i] = any(dp[j] for j in range(i-2, -1, -1))

    return "YES" if dp[-1] else "NO"

s = input().strip()
print(solve(s))
