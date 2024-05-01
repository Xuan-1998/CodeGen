def has_AB_BA(s):
    n = len(s)
    dp = [False] * (n + 1)

    for i in range(n - 1):
        if s[i:i+2] == 'AB' or s[i:i+2] == 'BA':
            dp[i+2] = True

    return "YES" if dp[-1] else "NO"

import sys
input = sys.stdin.readline

s = input().strip()
print(has_AB_BA(s))
