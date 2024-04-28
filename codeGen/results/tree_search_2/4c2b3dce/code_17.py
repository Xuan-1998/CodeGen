import sys
from collections import defaultdict

dp = defaultdict(bool)

def f(i):
    if i < 3:
        return True
    if dp[i]:
        return True
    if s[i-2:i] == 'BA':
        if i >= 6 and s[i-5:i-2] == 'AB':
            dp[i] = True
            return True
    return f(i-1)

s = input()
print("YES" if f(len(s)) else "NO")
