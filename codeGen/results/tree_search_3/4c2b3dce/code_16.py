import sys
from collections import defaultdict

dp = defaultdict(bool)
s = input()

for i in range(len(s)):
    if s[i:i+2] in ['AB', 'BA']:
        dp[i] = True
    elif s[i-1] == 'A' and s[i] == 'B':
        dp[i] = not dp[i-1]
    else:
        for j in range(i):
            if s[j:j+2] in ['AB', 'BA'] or dp[j]:
                dp[i] = True
                break

print("YES" if any(dp) else "NO")
